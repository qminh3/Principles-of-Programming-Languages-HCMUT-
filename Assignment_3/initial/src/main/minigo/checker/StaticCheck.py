#2212019
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List, Tuple, Union, Callable, Optional, Any

from StaticError import Type as StaticErrorType
from AST import Type
class FuntionType(Type):
    def __str__(self):
        return "FuntionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, v, param)


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
        
    
    def __init__(self,ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.function_current: Optional[FuncDecl] = None
        self.struct_current: Optional[StructType] = None
        self.list_function: List[FuncDecl] = self.initialize_builtin_functions()
        
    def initialize_builtin_functions(self):
        return [
            FuncDecl("getInt", [], IntType(), Block([])),
            FuncDecl("putInt", [ParamDecl("", IntType())], VoidType(), Block([])),
            FuncDecl("putIntLn", [ParamDecl("", IntType())], VoidType(), Block([])),
            
            FuncDecl("getFloat", [], FloatType(), Block([])),
            FuncDecl("putFloat", [ParamDecl("", FloatType())], VoidType(), Block([])),
            FuncDecl("putFloatLn", [ParamDecl("", FloatType())], VoidType(), Block([])),
            
            FuncDecl("getBool", [], BoolType(), Block([])),
            FuncDecl("putBool", [ParamDecl("", BoolType())], VoidType(), Block([])),
            FuncDecl("putBoolLn", [ParamDecl("", BoolType())], VoidType(), Block([])),
            
            FuncDecl("getString", [], IntType(), Block([])),
            FuncDecl("putString", [ParamDecl("", IntType())], VoidType(), Block([])),
            FuncDecl("putStringLn", [ParamDecl("", StringType())], VoidType(), Block([])),
            FuncDecl("putLn", [ParamDecl("", VoidType())], VoidType(), Block([]))
        ]
    def check(self):
        self.visit(self.ast, None)
    def lookupInScopes(self, name: str, scopes: List[List[Symbol]]) -> Union[Symbol, None]:
        for scope in scopes:
            symbol = self.lookup(name, scope, lambda x: x.name)
            if symbol:
                return symbol
        return None
    def evalConstExpr(self, node: AST, c : List[List[Symbol]]) :
        if isinstance(node, IntLiteral):
            return node.value
        elif isinstance(node, FloatLiteral):
            return node.value
        elif isinstance(node, BooleanLiteral):
            return node.value
        elif isinstance(node, StringLiteral):
            return node.value
        elif isinstance(node, Id):
            for scope in c:
                for sym in scope:
                    if sym.name == node.name:
                        if isinstance(sym.value, int):
                            return sym.value
                        elif isinstance(sym.value, AST):
                            return self.evalConstExpr(sym.value, c)
            raise TypeMismatch(node)
        elif isinstance(node, BinaryOp):
            left = self.evalConstExpr(node.left, c)
            right = self.evalConstExpr(node.right, c)
            op = node.op
            try:
                if op == '+': return left + right
                elif op == '-': return left - right
                elif op == '*': return left * right
                elif op == '/': return left // right
                elif op == '%': return left % right
                
            except:
                raise TypeMismatch(node)
        elif isinstance(node, UnaryOp):
            val = self.evalConstExpr(node.body, c)
            if node.op == '-': return -val
        raise TypeMismatch(node)
        
    def struct_implement_all_prototype_of_interface(self, interface: InterfaceType, struct: StructType) :
        if self.function_current and any(isinstance(p.parType, InterfaceType) for p in self.function_current.params):
            return False
        for prototype in interface.methods:
            found = False
            for method in struct.methods:
                if method.fun.name == prototype.name:
                    found = True
                    if not self.struct_prototype_compatible(prototype, method.fun):
                        return False
                    break
            if not found:
                return False
        return True
    
    def struct_prototype_compatible(self, prototype: Prototype, method: FuncDecl) :
        if len(prototype.params) != len(method.params):
            return False
        
        proto_ret_type = prototype.retType
        method_ret_type = method.retType
        
        if isinstance(proto_ret_type, Id):
            proto_ret_type = self.lookup(proto_ret_type.name, self.list_type, lambda x: x.name)
        if isinstance(method_ret_type, Id):
            method_ret_type = self.lookup(method_ret_type.name, self.list_type, lambda x: x.name)
        if type(proto_ret_type) != type(method_ret_type):
            return False
        if isinstance(proto_ret_type, StructType) and isinstance(method_ret_type, StructType):
            if proto_ret_type.name != method_ret_type.name:
                return False
            
        for i in range(len(prototype.params)):
            proto_param = prototype.params[i]
            meth_param = method.params[i].parType
            if isinstance(proto_param, Id) and isinstance(meth_param, Id):
                if proto_param.name != meth_param.name:
                    return False
            if type(meth_param) != type(proto_param):
                return False        
        return True
    
    def check_type_compatible(self, left_type: Type, right_type: Type, context: List[List[Symbol]] = None, permission: List[Tuple[Type, Type]] = []) :
        
        if type(right_type) == StructType and right_type.name == "":
            return True
       
        left_type  = self.lookup(left_type .name, self.list_type, lambda x: x.name) if isinstance(left_type , Id) else left_type 
        right_type = self.lookup(right_type.name, self.list_type, lambda x: x.name) if isinstance(right_type, Id) else right_type

        if (type(left_type ), type(left_type )) in permission or isinstance(left_type , InterfaceType) and isinstance(right_type, StructType):
            if isinstance(left_type , InterfaceType) and isinstance(right_type, StructType):               
                return self.struct_implement_all_prototype_of_interface(left_type , right_type)
                   
        if isinstance(left_type , FloatType) and isinstance(right_type, IntType):
            return (FloatType, IntType) in permission
            
        if isinstance(left_type , StructType) and isinstance(right_type, StructType):
            return left_type .name == right_type.name
        
        if isinstance(left_type , InterfaceType) and isinstance(right_type, InterfaceType):
            return left_type .name == right_type.name
        
        
        if isinstance(left_type , ArrayType) and isinstance(right_type, ArrayType):
            return self.check_array_compatibility(left_type, right_type, context)
       
        return type(left_type ) == type(right_type)
    
    def check_array_compatibility(self, left_array: ArrayType, right_array: ArrayType, env: List[List[Symbol]]) :
        
        if len(left_array.dimens) != len(right_array.dimens):
            return False
        
        if env:
            for left_dimension, right_dimension in zip(left_array.dimens, right_array.dimens):
                if self.evalConstExpr(left_dimension, env) != self.evalConstExpr(right_dimension, env):
                    return False
            
        
        if isinstance(left_array.eleType, FloatType) and isinstance(right_array.eleType, IntType):
            return True

        if isinstance(left_array.eleType, Id) and isinstance(right_array.eleType, Id):
            return left_array.eleType.name == right_array.eleType.name
        
        return self.check_type_compatible(left_array.eleType, right_array.eleType, env, [])
    
    def check_name_redeclaration(self, name: str, predefined_names: List[str], declared_names: List[str], error_type) :
        if name in predefined_names or name in declared_names:
            raise Redeclared(error_type, name)
        return True
    
    def collect_declarations(self, declarations: List[Decl]) -> Tuple[List[str], List[Any]]:
        
        predefined_methods = ["getInt", "putLn", "putInt", "putIntLn", "getFloat", "putFloat", 
                             "putFloatLn", "putBool", "putBoolLn", "putString", "putStringLn"]
        declared_names = []
        errors = []
        
        for item in declarations:
            try:
                if isinstance(item, (StructType, InterfaceType)):
                    self.check_name_redeclaration(item.name, predefined_methods, declared_names, StaticErrorType())
                    declared_names.append(item.name)
                elif isinstance(item, VarDecl): 
                    self.check_name_redeclaration(item.varName, predefined_methods, declared_names, Variable())
                    declared_names.append(item.varName)
                elif isinstance(item, ConstDecl): 
                    self.check_name_redeclaration(item.conName, predefined_methods, declared_names, Constant())
                    declared_names.append(item.conName)
                elif isinstance(item, FuncDecl):                
                    self.check_name_redeclaration(item.name, predefined_methods, declared_names, Function())
                    declared_names.append(item.name)
            except Exception as e:
                errors.append(e)
                
        return declared_names, errors
    
    
    

    
    def resolve_type_reference(self, type_ref: Type) :
       
        if isinstance(type_ref, Id):
            return self.lookup(type_ref.name, self.list_type, lambda x: x.name) or type_ref
        return type_ref
    
    def is_valid_nil_assignment(self, target_type: Type) :
        
        if isinstance(target_type, (StructType, InterfaceType)):
            return True
        if isinstance(target_type, Id):
            resolved_type = self.lookup(target_type.name, self.list_type, lambda x: x.name)
            return isinstance(resolved_type, (StructType, InterfaceType))
        return False

    def visitProgram(self, ast: Program, c : None):
        
        declared_names, errors = self.collect_declarations(ast.decl)
        if errors:
            raise errors[0]  

        def add_method_to_struct(method_decl: MethodDecl, struct: StructType) :
            for field_name, _ in struct.elements:
                if field_name == method_decl.fun.name:
                    raise Redeclared(Method(), method_decl.fun.name)

            existing_method = self.lookup(method_decl.fun.name, struct.methods, lambda x: x.fun.name)
            if existing_method is not None:
                raise Redeclared(Method(), method_decl.fun.name) 

            struct.methods.append(method_decl)

        self.list_type = reduce(
            lambda acc, ele: [self.visit(ele, acc)] + acc if isinstance(ele, Type) else acc,
            ast.decl,
            []
        )
                 
        self.list_function += list(filter(lambda d: isinstance(d, FuncDecl), ast.decl))
        
        method_decls = list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        for method in method_decls:
            struct = self.lookup(method.recType.name, self.list_type, lambda x: x.name)
            add_method_to_struct(method, struct)
        
        initial_symbols = [
            Symbol("getInt", FuntionType()),
            Symbol("putInt", FuntionType()),
            Symbol("putIntLn", FuntionType()),
            Symbol("getFloat", FuntionType()),
            Symbol("putFloat", FuntionType()),
            Symbol("putFloatLn", FuntionType()),
            Symbol("getBool", FuntionType()),
            Symbol("putBool", FuntionType()),
            Symbol("putBoolLn", FuntionType()),
            Symbol("getString", FuntionType()),
            Symbol("putString", FuntionType()),
            Symbol("putStringLn", FuntionType()),
            Symbol("putLn", FuntionType())
        ]
        
        reduce(
            lambda acc, prev: [
                ([result] + acc[0]) if isinstance(result := self.visit(prev, acc), Symbol) else acc[0]
            ] + acc[1:], 
            filter(lambda acc: isinstance(acc, Decl), ast.decl), 
            [initial_symbols]
        )

    
    def visitStructType(self, ast: StructType, c : List[Union[StructType, InterfaceType]]) :
        if self.lookup(ast.name, c, lambda x: x.name):
            raise Redeclared(StaticErrorType(), ast.name)

        seen_fields = set()
        validated_elements = []
        for field_name, field_type in ast.elements:
            if field_name in seen_fields:
                raise Redeclared(Field(), field_name)
            seen_fields.add(field_name)
            validated_elements.append((field_name, field_type))

        ast.elements = validated_elements
        return ast



    def visitInterfaceType(self, ast: InterfaceType, c : List[Union[StructType, InterfaceType]]) :
        if not (self.lookup(ast.name, c, lambda x: x.name)) is None:
            raise Redeclared(StaticErrorType(), ast.name)  
        ast.methods = reduce(lambda acc,prev: [self.visit(prev,acc)] + acc , ast.methods , [])
        return ast
    
    def visitPrototype(self, ast: Prototype, c: List[Prototype]) :
        if (self.lookup(ast.name, c, lambda x: x.name)) is not None:
            raise Redeclared(Prototype(), ast.name)
        c.append(ast)
        return ast
    
    # khai bao ham
    def visitFuncDecl(self, func_decl: FuncDecl, scopes : List[List[Symbol]]) :
        if self.lookup(func_decl.name, scopes[0], lambda x: x.name):
            raise Redeclared(Function(), func_decl.name)
        
        previous_function = self.function_current
        self.function_current = func_decl
        
        param_scope = []
        for param in func_decl.params:
            param_sym = self.visit(param, param_scope)
            param_scope.append(param_sym)
        self.visit(func_decl.body, [param_scope] + scopes)
        self.function_current = previous_function
        return Symbol(func_decl.name, FuntionType(), None)

    def visitParamDecl(self, ast: ParamDecl, c: List[Symbol]) :
        if self.lookup(ast.parName, c, lambda x: x.name):
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c : List[List[Symbol]]) :
        
        self.function_current, prev_function = ast.fun, self.function_current

        receiver_symbol = Symbol(ast.receiver, ast.recType, None)

        struct_def = self.lookup(ast.recType.name, self.list_type, lambda x: x.name)
        if isinstance(struct_def, StructType):
            if any(field_name == ast.fun.name for field_name, _ in struct_def.elements):
                raise Redeclared(Method(), ast.fun.name)
                
        param_scope = reduce( lambda acc, param: acc + [self.visit(param, acc)],ast.fun.params,[] )

        self.visit(ast.fun.body, [param_scope, [receiver_symbol]] + c)

        self.function_current = prev_function
            

    def visitVarDecl(self, var_decl: VarDecl, scopes : List[List[Symbol]]) :
        if self.lookup(var_decl.varName, scopes[0], lambda x: x.name):
            raise Redeclared(Variable(), var_decl.varName) 
        
        declared_type  = var_decl.varType if var_decl.varType else None
        inferred_type  = self.visit(var_decl.varInit, scopes) if var_decl.varInit else None
        if isinstance(inferred_type, NilLiteral):
            
            if not self.is_valid_nil_assignment(declared_type):
                raise TypeMismatch(var_decl)
            return Symbol(var_decl.varName, declared_type, None)

        if inferred_type is None:
            return Symbol(var_decl.varName, declared_type, None)
        elif declared_type is None:
            return Symbol(var_decl.varName, inferred_type, None)
        else:
            if isinstance(var_decl.varInit, NilLiteral):
                if isinstance(declared_type, (IntType, FloatType, BoolType, StringType)):
                    raise TypeMismatch(var_decl)
            if self.check_type_compatible(declared_type, inferred_type, scopes, [(FloatType, IntType)]):
                return Symbol(var_decl.varName, declared_type, None)
        raise TypeMismatch(var_decl)
        

    def visitConstDecl(self, ast: ConstDecl, c : List[List[Symbol]]) :
        if self.lookup(ast.conName, c[0], lambda x: x.name):
            raise Redeclared(Constant(), ast.conName)
        
        expr_typ = self.visit(ast.iniExpr, c)
        
        if ast.conType:
            if not self.check_type_compatible(ast.conType, expr_typ, [(FloatType, IntType)]):
                raise TypeMismatch(ast)
            const_type = ast.conType
        else:
            const_type = expr_typ
        if isinstance(const_type, IntType):
            try:
                value = self.evalConstExpr(ast.iniExpr, c)
                return Symbol(ast.conName, const_type, value)
            except:
                return Symbol(ast.conName, const_type, ast.iniExpr)
        else:
            return Symbol(ast.conName, const_type, None)
    
    
    # Statement 
    def visitBlock(self, ast: Block, c: List[List[Symbol]]) :
        local_scope = []
        new_env = [local_scope] + c
        for stmt in ast.member:
            if isinstance(stmt, (FuncCall, MethCall)):
                result = self.visit(stmt, (new_env, True))
            else:
                result = self.visit(stmt, new_env)
            if isinstance(result, Symbol):
                new_env[0] = [result] + new_env[0]
            
    def visitForBasic(self, ast: ForBasic, c : List[List[Symbol]]): 
        cond_type = self.visit(ast.cond, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)
       
    def visitForStep(self, ast: ForStep, env: List[List[Symbol]]) -> None: 
        init_scope = [[]] + env
        init_result = self.visit(ast.init, init_scope)
        if isinstance(ast.init, VarDecl):
            init_scope[0].append(init_result)

        cond_type = self.visit(ast.cond, init_scope)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        if isinstance(ast.upda, Assign) and isinstance(ast.upda.lhs, Id):
            update_var = ast.upda.lhs.name
            rhs = ast.upda.rhs

            is_self_increment = ( 
                                 isinstance(rhs, BinaryOp) and 
                                 isinstance(rhs.left, Id) and 
                                 rhs.left.name == update_var)

            is_declared = any(any(sym.name == update_var for sym in scope) for scope in init_scope )

            if is_self_increment and not is_declared:
                raise Undeclared(Identifier(), update_var)

            if not is_self_increment:
                init_scope[0].append(Symbol(update_var, None))
                
        loop_scope = [[]] + init_scope
        redeclared_decls = filter(
            lambda stmt: (
                isinstance(ast.upda, Assign) and isinstance(ast.upda.lhs, Id) and (
                    (isinstance(stmt, VarDecl) and stmt.varName == ast.upda.lhs.name) or
                    (isinstance(stmt, ConstDecl) and stmt.conName == ast.upda.lhs.name)
                )
            ),
            ast.loop.member
        )
        for decl in redeclared_decls:
            raise Redeclared(Variable() if isinstance(decl, VarDecl) else Constant(), ast.upda.lhs.name)
        
        list(map(lambda stmt: self.visit(stmt, loop_scope), ast.loop.member))

        self.visit(ast.upda, init_scope)
        

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]): 
        type_array = self.visit(ast.arr, c)
        if not isinstance(type_array, ArrayType):
            raise TypeMismatch(ast)
        type_idx = self.visit(ast.idx, c)
        if not isinstance(type_idx, IntType):
            raise TypeMismatch(ast)
        
        if len(type_array.dimens) > 1:
            expected_type = ArrayType(type_array.dimens[1:], type_array.eleType)
        else:
            expected_type = type_array.eleType
        
        type_value = self.visit(ast.value, c)
        if not self.check_type_compatible(expected_type, type_value, c, [(FloatType, IntType)]):
            raise TypeMismatch(ast)

        self.visit(Block(ast.loop.member), c)

    
    def visitId(self, ast: Id, c: List[List[Symbol]]):
        scopes = c[0] if isinstance(c, tuple) else c
        symbol = self.lookupInScopes(ast.name, scopes)
        if symbol:
            return symbol.mtype
        raise Undeclared(Identifier(), ast.name)
        
    
    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]):
        is_statement  = False
        if isinstance(c, tuple):
            c, is_statement  = c
            
        shadowed = self.lookupInScopes(ast.funName, c)
        if shadowed and not isinstance(shadowed.mtype, FuntionType):
            raise Undeclared(Function(), ast.funName)
        
        function  = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if function  is None:
            raise Undeclared(Function(), ast.funName)
        
        if len(function.params) != len(ast.args):
            raise TypeMismatch(ast)

        for param, arg in zip(function.params, ast.args):
            if isinstance(arg, NilLiteral):
                if not (isinstance(param.parType, InterfaceType) or
                        (isinstance(param.parType, Id) and isinstance(
                            self.lookup(param.parType.name, self.list_type, lambda x: x.name),
                            InterfaceType))):
                    raise TypeMismatch(ast)
                continue

            arg_type = self.visit(arg, c)
            param_type = param.parType
            if isinstance(param_type, Id):
                param_type = self.lookup(param_type.name, self.list_type, lambda x: x.name) or param_type
            
            if isinstance(param_type, InterfaceType) and isinstance(arg_type, StructType):
                raise TypeMismatch(ast)
            
            if isinstance(param_type, ArrayType) and isinstance(arg_type, ArrayType): 
                if isinstance(param_type.eleType, FloatType) and isinstance(arg_type.eleType, IntType):
                    raise TypeMismatch(ast)
            
            if not self.check_type_compatible(param_type, arg_type, c, []):
                raise TypeMismatch(ast)

        if is_statement and not isinstance(function.retType, VoidType):
            raise TypeMismatch(ast)
        if not is_statement and isinstance(function.retType, VoidType):
            raise TypeMismatch(ast)

        return function.retType
    
    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]):
        receiver_type = self.visit(ast.receiver, c)

        receiver_actual_type = self.resolve_type_reference(receiver_type)

        if not isinstance(receiver_actual_type, StructType):
            raise TypeMismatch(ast)
        
        field  = self.lookup(ast.field, receiver_actual_type.elements, lambda x: x[0])
        if field  is None:
            raise Undeclared(Field(), ast.field)
            
        return field[1]
    
    def check_struct_method_call(self, struct: StructType, ast: MethCall, c, is_stmt: bool) :
        method = self.lookup(ast.metName, struct.methods, lambda x: x.fun.name)
        if not method:
            raise Undeclared(Method(), ast.metName)
        if len(ast.args) != len(method.fun.params):
            raise TypeMismatch(ast)
            
        if is_stmt and not isinstance(method.fun.retType, VoidType):
            raise TypeMismatch(ast)
        if not is_stmt and isinstance(method.fun.retType, VoidType):
            raise TypeMismatch(ast)
        

        for i in range(len(ast.args)):
            arg_type = self.visit(ast.args[i], c)
            param_type = method.fun.params[i].parType
            if not self.check_type_compatible(param_type, arg_type, c):
                raise TypeMismatch(ast)
        
 
        return method.fun.retType
        
    def check_interface_method_call(self, interface: InterfaceType, ast: MethCall, c, is_stmt: bool) :
        
        proto = self.lookup(ast.metName, interface.methods, lambda x: x.name)
        if not proto:
            raise Undeclared(Method(), ast.metName)
            
      
        if len(ast.args) != len(proto.params):
            raise TypeMismatch(ast)
        
    
        for i in range(len(ast.args)):
            arg_type = self.visit(ast.args[i], c)
            param_type = proto.params[i]
            if not self.check_type_compatible(param_type, arg_type, c):
                raise TypeMismatch(ast)
            
    
        if is_stmt and not isinstance(proto.retType, VoidType):
            raise TypeMismatch(ast)
        if not is_stmt and isinstance(proto.retType, VoidType):
            raise TypeMismatch(ast)               
        
 
        return proto.retType   
    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]):
        is_stmt = False
        if isinstance(c, tuple):
            c, is_stmt = c
        type_receiver = self.visit(ast.receiver, c)

        if not isinstance(type_receiver, (StructType, InterfaceType, Id)):
            raise TypeMismatch(ast)

        type_def = self.resolve_type_reference(type_receiver)
            
        if not isinstance(type_def, (StructType, InterfaceType)):
            raise TypeMismatch(ast)

        if isinstance(type_def, StructType):
            return self.check_struct_method_call(type_def, ast, c, is_stmt)
        elif isinstance(type_def, InterfaceType):
            return self.check_interface_method_call(type_def, ast, c, is_stmt)

        raise Undeclared(Method(), ast.metName)

    def visitIntType(self, ast, c: List[List[Symbol]]) : 
        return ast
    def visitFloatType(self, ast, c: List[List[Symbol]]): 
        return ast
    def visitBoolType(self, ast, c: List[List[Symbol]]): 
        return ast
    def visitStringType(self, ast, c: List[List[Symbol]]) : 
        return ast
    def visitVoidType(self, ast, c: List[List[Symbol]]) : 
        return ast
    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
 
        dimensions = [self.visit(dim, c) for dim in ast.dimens]
        for dim in dimensions:
            if not isinstance(dim, IntType):
                raise TypeMismatch(ast)
        self.evalConstExpr(dim, c)
        element_type = self.visit(ast.eleType, c)
        return ArrayType(dimensions, element_type)
    
    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) :
        if isinstance(ast.lhs, Id):
            lhs_name = ast.lhs.name
            lhs_found = False
            
            for scope in c:
                for sym in scope:
                    if sym.name == lhs_name:
                        lhs_found = True
                        break
                if lhs_found:
                    break
            
            if not lhs_found:
                rhs_type = self.visit(ast.rhs, c)
                c[0].append(Symbol(lhs_name, rhs_type, None))
                return None
        
        lhs_type = self.visit(ast.lhs, c)
        rhs_type = self.visit(ast.rhs, c)

        if isinstance(lhs_type, FloatType) and isinstance(rhs_type, IntType):
            return None

        if isinstance(ast.lhs, ArrayCell):
            if isinstance(lhs_type, (IntType, FloatType, BoolType, StringType)):
                if isinstance(lhs_type, IntType) and isinstance(rhs_type, FloatType):
                    raise TypeMismatch(ast)
                elif isinstance(lhs_type, FloatType) and isinstance(rhs_type, IntType):
                    return None  
        
        if not self.check_type_compatible(lhs_type, rhs_type, c, [(FloatType, IntType)]):
            raise TypeMismatch(ast)
            
    def visitReturn(self, ast, c: List[List[Symbol]]) :        
        if isinstance(c, tuple):
            c = c[0]
    
        func_return_type = self.function_current.retType  
    
        if isinstance(func_return_type, VoidType):
            if ast.expr is not None:
                expr_type = self.visit(ast.expr, (c, False))
                raise TypeMismatch(ast)
        elif ast.expr is None:
            raise TypeMismatch(ast)
        else:
            expr_type = self.visit(ast.expr, (c, False))
            if isinstance(func_return_type, Id):
                func_return_type = self.lookup(func_return_type.name, self.list_type, lambda x: x.name) or func_return_type            
            if isinstance(expr_type, Id):
                expr_type = self.lookup(expr_type.name, self.list_type, lambda x: x.name) or expr_type
            if isinstance(func_return_type, StructType) and isinstance(expr_type, InterfaceType):
                raise TypeMismatch(ast)
            if isinstance(func_return_type, ArrayType) and isinstance(expr_type, ArrayType):
                if len(func_return_type.dimens) != len(expr_type.dimens):
                    raise TypeMismatch(ast)
                if isinstance(ast.expr, ArrayLiteral):
                    if type(func_return_type.eleType) != type(expr_type.eleType):
                        raise TypeMismatch(ast)
            if type(func_return_type) != type(expr_type):
                raise TypeMismatch(ast)
            elif not self.check_type_compatible(func_return_type, expr_type, c, []):
                raise TypeMismatch(ast)   
    
    def visitIf(self, ast: If, c: List[List[Symbol]]) : 
        if not isinstance(self.visit(ast.expr, c), BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, c) if isinstance(ast.thenStmt, If) else self.visit(ast.thenStmt, [[]] + c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, [[]] + c)
        return c

    def visitContinue(self, ast, c: List[List[Symbol]]) :
        return None
    def visitBreak(self, ast, c: List[List[Symbol]]): 
        return None
    
    
                
    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        left_type = self.visit(ast.left, c)
        right_type = self.visit(ast.right, c)

        def is_numeric(t):
            return isinstance(t, (IntType, FloatType))

        if ast.op == "+":
            if isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return StringType()
            elif is_numeric(left_type) and is_numeric(right_type):
                return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

        elif ast.op in ["-", "*", "/"]:
            if is_numeric(left_type) and is_numeric(right_type):
                return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

        elif ast.op == "%":
            if isinstance(left_type, IntType) and isinstance(right_type, IntType):
                return IntType()

        elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
            if isinstance(left_type, (IntType, FloatType, StringType)) and \
            isinstance(right_type, (IntType, FloatType, StringType)) and \
            type(left_type) is type(right_type):
                return BoolType()

        elif ast.op in ["&&", "||"]:
            if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
                return BoolType()
            
        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        exp_type = self.visit(ast.body, c)

        if ast.op == "-":
            if isinstance(exp_type, IntType):
                return IntType()
            elif isinstance(exp_type, FloatType):
                return FloatType()
        elif ast.op == "!":
            if isinstance(exp_type, BoolType):
                return BoolType()

        raise TypeMismatch(ast)
    
    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]):
        array_type = self.visit(ast.arr, c) 
        
        for index_expr in ast.idx:
            index_type = self.visit(index_expr, c)
            if not isinstance(index_type, IntType):
                raise TypeMismatch(ast)
            
        if len(ast.idx) < len(array_type.dimens):
            return ArrayType(array_type.dimens[len(ast.idx):], array_type.eleType)
        else:
            return array_type.eleType

    def visitIntLiteral(self, ast, c: List[List[Symbol]]) : 
        return IntType()
    def visitFloatLiteral(self, ast, c: List[List[Symbol]]) : 
        return FloatType()
    def visitBooleanLiteral(self, ast, c: List[List[Symbol]]) : 
        return BoolType()
    def visitStringLiteral(self, ast, c: List[List[Symbol]]) : 
        return StringType()
    def visitArrayLiteral(self, ast:ArrayLiteral , c: List[List[Symbol]]):  
        def validate_nested_array(lst, expected_type, depth, ast):
            if depth==1 :  
                for item in lst:
                    item_type = self.visit(item,c)  
                    if isinstance(expected_type, FloatType) and isinstance(item_type, IntType):
                        continue
                    if not self.check_type_compatible(expected_type, item_type, c, [(FloatType, IntType)]):
                        raise TypeMismatch(ast)   
            else:               
                if not isinstance(lst, list):
                    raise TypeMismatch(ast) 
                for sublist in lst:
                    if not isinstance(sublist, list):                      
                        raise TypeMismatch(ast)                     
                    validate_nested_array(sublist, expected_type, depth - 1, ast)

        depth = len(ast.dimens)  
        validate_nested_array(ast.value, ast.eleType, depth, ast)
        return ArrayType(ast.dimens, ast.eleType)
    
    def visitStructLiteral(self, ast:StructLiteral, c: List[List[Symbol]]): 
        struct_def = self.lookup(ast.name, self.list_type, lambda x: x.name)
    
        if struct_def is None:
            raise Undeclared(Type(), ast.name)

        struct_fields = {name: ftype for name, ftype in struct_def.elements}
        
        for field_name, field_expr in ast.elements:
            if field_name not in struct_fields:
                raise TypeMismatch(ast)
            
            field_type = struct_fields[field_name]
            expr_type = self.visit(field_expr, c)
            
            if not self.check_type_compatible(field_type, expr_type):
                raise TypeMismatch(ast)
        return struct_def
    def visitNilLiteral(self, ast:NilLiteral, c: List[List[Symbol]]) -> Type: 
        return StructType("", [], [])