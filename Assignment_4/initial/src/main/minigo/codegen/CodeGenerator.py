#2212019
from Utils import *

from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from typing import Tuple, List
from Visitor import *
from AST import *

class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None
        self.arrayCellType = None
        self.list_type = {}
        self.struct: StructType = None

    def init(self):
        mem = [
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),

            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),

            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),

            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),

            Symbol("putLn", MType([], VoidType()), CName("io", True)),
        ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
        
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", Id(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def emitObjectCInit(self, ast: Program, env):
        frame = Frame("<cinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame
        global_inits = [Assign(Id(item.varName), item.varInit) for item in ast.decl if isinstance(item, VarDecl) and item.varInit] + [Assign(Id(item.conName), item.iniExpr) for item in ast.decl if isinstance(item, ConstDecl) and item.iniExpr]
        self.visit(Block(global_inits), env)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()
        
        

    
    def visitProgram(self, ast: Program, c):
        self.list_type = {x.name: x for x in ast.decl if isinstance(x, Type)}
        
        self.list_function = c + [
            Symbol(item.name, MType([param.parType for param in item.params], item.retType), CName(self.className))
            for item in ast.decl if isinstance(item, FuncDecl)
        ]
        
        for item in ast.decl:
            if isinstance(item, MethodDecl):
                struct_type  = self.list_type.get(item.recType.name)
                if struct_type:
                    struct_type.methods.append(item)
                    
        env = {'env': [c]}
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for decl in ast.decl:
            if isinstance(decl, (VarDecl, ConstDecl)):
                self.visit(decl, env)
        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                self.visit(decl, env)
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)
        # self.emit.printout(self.emit.emitEPILOG())
        epilog = self.emit.emitEPILOG()
        self.emit.printout(epilog)
        
        for item in self.list_type.values():
            self.struct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, {
                'env': env['env']
            })
            
        return env

    def visitFuncDecl(self, ast: FuncCall, o: dict) :

        self.function = ast

        frame = Frame(ast.name, ast.retType)

        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
            ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        

        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']

        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)

        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 

        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()
        return o

    def visitParamDecl(self, ast: ParamDecl, o: dict) :
        frame = o['frame']
        index = frame.getNewIndex()
        param_symbol = Symbol(ast.parName, ast.parType, Index(index))
        o['env'][0].append(param_symbol)
        self.emit.printout(self.emit.emitVAR(index, param_symbol.name, param_symbol.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
        return o

    def create_init(self, varType: Type, o: dict):
        if isinstance(varType, IntType):
            return IntLiteral(0)
        elif isinstance(varType, FloatType):
            return FloatLiteral(0.0)
        elif isinstance(varType, StringType):
            return StringLiteral("\"\"")
        elif isinstance(varType, BoolType):
            return BooleanLiteral("false")
        elif isinstance(varType, ArrayType):
            def create_array_default(dimensions, eleType):
                if not dimensions:
                    return self.create_init(eleType, o)

                current_dim = dimensions[0]
                if isinstance(current_dim, IntLiteral):
                    size = current_dim.value
                else:
                    return None  

                return [create_array_default(dimensions[1:], eleType) for _ in range(size)]

            return create_array_default(varType.dimens, varType.eleType)
        elif isinstance(varType, Id):
            struct_type = self.list_type.get(varType.name)
            if isinstance(struct_type, StructType):
                return StructLiteral(varType.name, [])
        return None  

    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:
        varInit = ast.varInit 
        varType = ast.varType 
        
        if not varInit:
            if type(varType) is ArrayType:
                varInit = ArrayLiteral(varType.dimens, varType.dimens, varType)
            else:
                varInit = self.create_init(varType, o)
            ast.varInit = varInit

        env = o.copy()
        env['frame'] = Frame("<template_VT>", VoidType()) 

        rhsCode, rhsType = self.visit(varInit, env)

        if not varType:
            varType = rhsType
            
        if 'frame' not in o: 
            self.declareGlobalVar(ast.varName, varType, o)
        else:
            self.declareLocalVar(ast.varName, varType, varInit, o)
        
        return o
    
    def declareGlobalVar(self, varName: str, varType: Type, o: dict) :
        o['env'][0].append(Symbol(varName, varType, CName(self.className)))
        
        attr_code = self.emit.emitATTRIBUTE(varName, varType, True, False, None)
        if attr_code is None:
            attr_code = ""
        self.emit.printout(attr_code)

    def declareLocalVar(self, varName: str, varType: Type, varInit, o: dict) :
        frame = o['frame']
        start_label = frame.getStartLabel()
        end_label = frame.getEndLabel()
        index = frame.getNewIndex()
        
        o['env'][0].append(Symbol(varName, varType, Index(index)))
        
        var_code = self.emit.emitVAR(index, varName, varType, start_label, end_label, frame)
        if var_code is None:
            var_code = ""
        self.emit.printout(var_code)
        
        rhsCode, rhsType = self.visit(varInit, o)
        if rhsCode is None:
            rhsCode = ""
        
        if isinstance(varType, FloatType) and isinstance(rhsType, IntType):
            i2f_code = self.emit.emitI2F(frame)
            if i2f_code is None:
                i2f_code = ""
            rhsCode += i2f_code
        
        self.emit.printout(rhsCode)
        self.emit.printout(self.emit.emitWRITEVAR(varName, varType, index, frame))

    
    def visitBlock(self, ast: Block, o: dict) :
        env = o.copy()
        env['env'] = [[]] + env['env'] 
        frame = env['frame']
        frame.enterScope(False)  
        
        start_label = frame.getStartLabel()
        end_label = frame.getEndLabel()
        
        self.emit.printout(self.emit.emitLABEL(start_label,frame))
        
        
        for item in ast.member:
            if type(item) is FuncCall or type(item) is MethCall:
                env["stmt"] = True
            env = self.visit(item, env)

        self.emit.printout(self.emit.emitLABEL(end_label,frame))
        frame.exitScope()
        return o
    
    def visitFuncCall(self, ast: FuncCall, o: dict) :
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function), None)
        env = o.copy()
        if o.get('stmt'):
            o["stmt"] = False
            output = "".join([str(self.visit(x, o)[0]) for x in ast.args])
            self.emit.printout(output)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
            return o
        
        output = "".join([str(self.visit(x, env)[0]) for x in ast.args])
        output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])
        return output, sym.mtype.rettype

   
    def visitId(self, ast: Id, o: dict) :
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]), None)
        if sym is None:
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR("this", Id(""), 0, o['frame']), Id("")
            return self.emit.emitREADVAR("this", Id(""), 0, o['frame']), Id("")
        if o.get('isLeft'): 
            if type(sym.value) is Index:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:         
                return self.emit.emitPUTSTATIC(f"{sym.value.value}/{sym.name}", sym.mtype, o['frame']), sym.mtype        
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value , o['frame']), sym.mtype
        else:         
            return self.emit.emitGETSTATIC(f"{sym.value.value}/{sym.name}", sym.mtype, o['frame']), sym.mtype

    def visitAssign(self, ast: Assign, o: dict) :
        if type(ast.lhs) is Id and not next(filter(lambda x: x.name == ast.lhs.name, [j for i in o['env'] for j in i]),None):
            return self.visitVarDecl(VarDecl(ast.lhs.name, None, ast.rhs), o)
        
        if type(ast.lhs) is FieldAccess:
            fieldAccess = ast.lhs
            if type(fieldAccess.receiver) is Id and fieldAccess.receiver.name == "this":
                self.emit.printout(self.emit.emitREADVAR("this", Id(self.struct.name), 0, o['frame']))
                field = self.lookup(fieldAccess.field, self.struct.elements, lambda x: x[0])
                rhsCode, rhsType = self.visit(ast.rhs, o) 
                self.emit.printout(rhsCode)
                self.emit.printout(self.emit.emitPUTFIELD(f"{self.struct.name}/{field[0]}", field[1], o['frame']))
                return o
            elif type(fieldAccess.receiver) is Id:
                code,typ = self.visit(fieldAccess.receiver, o)
                structFound = self.list_type.get(typ.name)
                field = self.lookup(fieldAccess.field, structFound.elements, lambda x: x[0])
                rhsCode, rhsType = self.visit(ast.rhs, o)
                o['isLeft'] = False
                self.emit.printout(code)       
                self.emit.printout(rhsCode)
                self.emit.printout(self.emit.emitPUTFIELD(f"{structFound.name}/{field[0]}", field[1], o['frame']))
                return o
            elif type(fieldAccess.receiver) is FieldAccess:
                innerFieldAccess = fieldAccess.receiver
                outerCode, outerType = self.visit(innerFieldAccess.receiver, o)              
                outerStructType = self.list_type.get(outerType.name)           
                innerField = self.lookup(innerFieldAccess.field, outerStructType.elements, lambda x: x[0])            
                innerStructType = self.list_type.get(innerField[1].name)         
                targetField = self.lookup(fieldAccess.field, innerStructType.elements, lambda x: x[0])
                rhsCode, rhsType = self.visit(ast.rhs, o)                
                self.emit.printout(outerCode)           
                self.emit.printout(self.emit.emitGETFIELD(f"{outerStructType.name}/{innerFieldAccess.field}", innerField[1], o['frame']))         
                self.emit.printout(rhsCode)  
                self.emit.printout(self.emit.emitPUTFIELD(f"{innerStructType.name}/{fieldAccess.field}", targetField[1], o['frame']))
                return o
            
        if type(ast.lhs) is ArrayCell:
            o['frame'].push()
            o['frame'].push()

        rhsCode, rhsType = self.visit(ast.rhs, o)
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False

        if type(ast.lhs) is ArrayCell:
            o['frame'].pop()
            o['frame'].pop()

        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhsCode += self.emit.emitI2F(o['frame'])

        o['frame'].push()

        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitASTORE(lhsType, o['frame'])) 
        else:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)
        return o

    def visitReturn(self, ast: Return, o: dict) :
        if ast.expr:
            expr, _ = self.visit(ast.expr, o)
            self.emit.printout(expr)
        self.emit.printout(self.emit.emitRETURN(self.function.retType, o['frame']))
        return o

    def visitBinaryOp(self, ast: BinaryOp, o: dict) :
        op = ast.op
        frame = o['frame']
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)

        if op in ['+', '-'] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                elif type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)

            return codeLeft + codeRight + self.emit.emitADDOP(op, typeReturn, frame), typeReturn
        if op in ['*', '/']:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame) 
                elif type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitMULOP(op, typeReturn, frame), typeReturn
        if op in ['%']:
            return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:
            return codeLeft + codeRight + self.emit.emitREOP(op, typeLeft, frame), BoolType() 
        if op in ['||']:
            return codeLeft + codeRight + self.emit.emitOROP(frame), BoolType()
        if op in ['&&']:
            return codeLeft + codeRight + self.emit.emitANDOP(frame), BoolType()  

              
        if op in ['+', '-'] and type(typeLeft) in [StringType]:
            return codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), frame), StringType() 
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [StringType]:
            code = codeLeft + codeRight + self.emit.emitREOP(op, typeLeft, frame)
            return code, BoolType()    
              
    def visitUnaryOp(self, ast: UnaryOp, o: dict) :
        if ast.op == '!':
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()
        elif ast.op == '-':
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNEGOP(type_return, o['frame']), type_return
    
    def visitIntLiteral(self, ast: IntLiteral, o: dict) :
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) :
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) :
        return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, o: dict) :
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()
    
    def visitArrayCell(self, ast: ArrayCell, o: dict) :
        newO = o.copy()
        newO['isLeft'] = False
        codeGen, arrType = self.visit(ast.arr, newO)  

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType 
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                self.arrayCell = ast  
        else:
            retType = ArrayType(arrType.dimens[len(ast.idx):], arrType.eleType)
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                self.arrayCell = ast  
        
        return codeGen, retType
    

    def visitArrayLiteral(self, ast: ArrayLiteral, context: dict) :
        if isinstance(ast.value, ArrayType):
            return self.visit(ast.value, context)
        return self.generateArrayData(ast.value, context)
    
    def generateArrayData(self, data: Union[Literal, list], context: dict) :
        frame = context['frame']
        if not isinstance(data, list):
            return self.visit(data, context)

        arrayLength = len(data)
        code = self.emit.emitPUSHICONST(arrayLength, frame)

        # mảng 1 chiều 
        if not isinstance(data[0], list):
            _, elementType = self.visit(data[0], context)

            if isinstance(elementType, (IntType, FloatType, BoolType)):
                code += self.emit.emitNEWARRAY(elementType, frame)
            else:
                code += self.emit.emitANEWARRAY(elementType, frame)

            for index, item in enumerate(data):
                code += (
                    self.emit.emitDUP(frame) +
                    self.emit.emitPUSHCONST(index, IntType(), frame) +
                    self.visit(item, context)[0] +
                    self.emit.emitASTORE(elementType, frame)
                )

            return code, ArrayType([arrayLength], elementType)

        # mảng lồng nhau
        _, subArrayType = self.generateArrayData(data[0], context)
        code += self.emit.emitANEWARRAY(subArrayType, frame)

        for index, subArray in enumerate(data):
            subCode, _ = self.generateArrayData(subArray, context)
            code += (
                self.emit.emitDUP(frame) +
                self.emit.emitPUSHCONST(index, IntType(), frame) +
                subCode +
                self.emit.emitASTORE(subArrayType, frame)
            )

        if isinstance(subArrayType, ArrayType):
            return code, ArrayType([arrayLength] + subArrayType.dimens, subArrayType.eleType)
        else:
            return code, ArrayType([arrayLength], subArrayType)
        
    def visitConstDecl(self, ast:ConstDecl, o: dict) :
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)
    
    def visitArrayType(self, ast: ArrayType, o):
        frame = o['frame']
        codeGen = ""

        for dim in ast.dimens:
            dimCode, _ = self.visit(dim, o)
            codeGen += dimCode

        if len(ast.dimens) > 1:
            codeGen += self.emit.emitMULTIANEWARRAY(ast, len(ast.dimens), frame)
        else:
            codeGen += self.emit.emitNEWARRAY(ast.eleType, frame)

        return codeGen, ast
    
    def visitIf(self, ast: If, o: dict) :
        frame = o['frame']
        if ast.elseStmt:
            fL = frame.getNewLabel()
            tL = frame.getNewLabel()
            condCode, _ = self.visit(ast.expr, o)
            self.emit.printout(condCode)
            
            code = self.emit.emitIFFALSE(fL, frame)
            self.emit.printout(code)
            
            self.visit(ast.thenStmt, o)
            
            code = self.emit.emitGOTO(tL, frame)
            self.emit.printout(code)
            code = self.emit.emitLABEL(fL, frame)
            self.emit.printout(code)
            self.visit(ast.elseStmt, o)
            code = self.emit.emitLABEL(tL, frame)
            self.emit.printout(code)
        else:
            fL = frame.getNewLabel()
            condCode, _ = self.visit(ast.expr, o)
            self.emit.printout(condCode)
            code = self.emit.emitIFFALSE(fL, frame)
            self.emit.printout(code)
            self.visit(ast.thenStmt, o)
            code = self.emit.emitLABEL(fL, frame)
            self.emit.printout(code)
        return o
            

    def visitForBasic(self, ast: ForBasic, o: dict):
        frame = o['frame']
        frame.enterLoop()
        start_label = frame.getNewLabel()
        break_label = frame.getBreakLabel() 
        continute_label = frame.getContinueLabel()
        self.emit.printout(self.emit.emitLABEL(start_label,frame))
        cond_code, _ = self.visit(ast.cond, o)
        self.emit.printout(cond_code)
        code = self.emit.emitIFFALSE(break_label,frame)
        self.emit.printout(code)
        
        self.visit(ast.loop, o)
        
        self.emit.printout(self.emit.emitLABEL(continute_label, frame))
        self.emit.printout(self.emit.emitGOTO(start_label, frame))
        self.emit.printout(self.emit.emitLABEL(break_label, frame))
        frame.exitLoop()
        return o
    
    def visitForStep(self, ast: ForStep, o: dict) :
        frame = o['frame']
        frame.enterLoop()
        
        
        startLabel = frame.getNewLabel()
        breakLabel = frame.getBreakLabel()
        continueLabel = frame.getContinueLabel()
        
        env = o.copy()
        env['env'] = [[]] + env['env']

        self.visit(ast.init, env)
        
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))
        
        condCode, _ = self.visit(ast.cond, env)
        self.emit.printout(condCode)

        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        
        self.visit(ast.loop, env)
        
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        
        self.visit(ast.upda, env)
      
        
        self.emit.printout(self.emit.emitGOTO(startLabel, frame))
        
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        
        frame.exitLoop()
        return o

    def visitForEach(self, ast, o: dict) :
        frame = o['frame']
        return o

    def visitContinue(self, ast, o: dict) :
        frame = o['frame']
        continueLabel = frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        return o

    def visitBreak(self, ast, o: dict) :
        frame = o['frame']
        breakLabel = frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(breakLabel, frame))
        return o
    
    def visitFieldAccess(self, ast:FieldAccess, o: dict) :
        code, typ = self.visit(ast.receiver, o)
    
        if code is None:
            code = ""
  
        struct_type = None
        if hasattr(self, 'struct') and self.struct:
            struct_type = self.struct
        elif isinstance(typ, Id) and typ.name in self.list_type:
            struct_type = self.list_type[typ.name]
        else:
            struct_type = typ
        
      
        field = next((f for f in struct_type.elements if f[0] == ast.field), None)
        
        field_code = ""
        if o.get('isLeft'):
            field_code = self.emit.emitGETFIELD(f"{struct_type.name}/{ast.field}", field[1], o['frame'])
        else:
            field_code = self.emit.emitGETFIELD(f"{struct_type.name}/{ast.field}", field[1], o['frame'])

        if field_code is None:
            field_code = ""
        
        return code + field_code, field[1]
        
    def visitMethCall(self, ast: MethCall, o: dict) :
        code, typ = self.visit(ast.receiver, o)
        if isinstance(typ, Id):
            typ = self.list_type.get(typ.name)

        is_stmt = o.pop("stmt", False)

        for arg in ast.args:
            arg_code, _ = self.visit(arg, o)
            code += arg_code

        returnType = None

        if isinstance(typ, StructType):

            method = next(filter(lambda x: x.fun.name == ast.metName, typ.methods), None)
            if method:
                mtype = MType(list(map(lambda x: x.parType, method.fun.params)), method.fun.retType)
                returnType = method.fun.retType

                code += self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.metName}", mtype, o['frame'])
                
                
        elif isinstance(typ, InterfaceType):
            method = next((m for m in typ.methods if m.name == ast.metName), None)
            if method:
                mtype = MType(method.params, method.retType)
                returnType = method.retType
                count = len(method.params) + 1
                code += self.emit.emitINVOKEINTERFACE(f"{typ.name}/{ast.metName}", mtype, o['frame'],count)
            
        if is_stmt:
            self.emit.printout(code)
            return o

        return code, returnType
    
    def visitStructLiteral(self, ast: StructLiteral, o: dict) :
        
        frame = o['frame']
        code = self.emit.emitNEW(ast.name, frame)
        if code is None:
            code = ""
        dupCode  = self.emit.emitDUP(frame)
        if dupCode is None:
            dupCode = ""
        code += dupCode
        list_type = []
        for item in ast.elements:
            c, t = self.visit(item[1], o)
            if c is None:
                c = ""
            code += c
            list_type.append(t)
        
        invokeCode = ""
        if len(ast.elements) > 0:
            invokeCode += self.emit.emitINVOKESPECIAL(frame, f"{ast.name}/<init>", MType(list_type, VoidType()))
        else:
            invokeCode += self.emit.emitINVOKESPECIAL(frame, f"{ast.name}/<init>", MType([], VoidType()))
        if invokeCode is None:
            invokeCode = ""
        code += invokeCode
        return code, Id(ast.name)
    
    def visitNilLiteral(self, ast: NilLiteral, o: dict) :
        frame =o['frame']
        code = self.emit.emitPUSHNULL(frame)
        return code, Id("")
    
    def visitStructType(self, ast: StructType, o):
        implemented_interfaces = []
        for item in self.list_type.values():
            if isinstance(item, InterfaceType) and self.checkType(item, ast, [(InterfaceType, StructType)]):
                implemented_interfaces.append(item.name)
        
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java/lang/Object"))
        
        for interface in implemented_interfaces:
            self.emit.printout(self.emit.emitIMPLEMENTS(interface))

        for item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(item[0], item[1], False, False, None))  

        paramList = [ParamDecl(item[0], item[1]) for item in ast.elements]
        blockConstructor = Block([
                                Assign(
                                    FieldAccess(Id("this"), item[0]), 
                                    Id(item[0])
                                )
                                for item in ast.elements
                            ])
        param_constructor = MethodDecl(
            None,  
            None,  
            FuncDecl(
                "<init>",
                paramList,  
                VoidType(),
                blockConstructor
            )
        )
        self.visit(param_constructor, o)

        default_constructor = MethodDecl(
            None, None,
            FuncDecl("<init>", [], VoidType(), Block([]))
        )
        self.visit(default_constructor, o)

        for item in ast.methods:
            self.visit(item, o)

        self.emit.printout(self.emit.emitEPILOG())
        
    def visitMethodDecl(self, ast: MethodDecl, o):
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        
        mtype = MType([param.parType for param in ast.fun.params], ast.fun.retType)
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype,False, frame))
        frame.enterScope(True) 
       
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(self.struct.name), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id(""), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))    

        env['env'] = [[]] + env['env']
        
        env = reduce(lambda acc, param: self.visit(param, acc), ast.fun.params, env)

        self.visit(ast.fun.body, env)


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitInterfaceType(self, ast: InterfaceType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object", True))
        for item in ast.methods:
            frame = Frame(item.name, item.retType) 
            mtype = MType(item.params, item.retType)
            self.emit.printout(self.emit.emitMETHOD(item.name, mtype, False, frame, isAbstract=True))
            self.emit.printout(self.emit.emitENDMETHOD(frame, True))
        self.emit.printout(self.emit.emitEPILOG())
        
    def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []):
        if type(RHS_type) == StructType and RHS_type.name == "":
            return isinstance(LSH_type, (InterfaceType, StructType, Id))

        if isinstance(LSH_type, Id):
            LSH_type = self.lookup(LSH_type.name, self.list_type.values(), lambda x: x.name)
        if isinstance(RHS_type, Id):
            RHS_type = self.lookup(RHS_type.name, self.list_type.values(), lambda x: x.name)

        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                return self.matchInterfaceWithStruct(LSH_type, RHS_type)
            
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, InterfaceType):
                return LSH_type.name == RHS_type.name
            
            if isinstance(LSH_type, StructType) and isinstance(RHS_type, StructType):
                return LSH_type.name == RHS_type.name
            
        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            return (len(LSH_type.dimens) == len(RHS_type.dimens)
                    and all(
                        l.value == r.value  for l, r in zip(LSH_type.dimens, RHS_type.dimens)
                    )
                    and self.checkType(LSH_type.eleType, RHS_type.eleType, [list_type_permission[0]] if len(list_type_permission) != 0 else []))

        return type(LSH_type) == type(RHS_type)
    def matchInterfaceWithStruct(self, interface: InterfaceType, struct: StructType) :
        for interface_method in interface.methods:
            matched = False
            for struct_method in struct.methods:
                func1 = struct_method.fun
                func2 = interface_method

                if func1.name != func2.name:
                    continue
                if not self.checkType(func1.retType, func2.retType):
                    continue
                if len(func1.params) != len(func2.params):
                    continue
                if not all(
                    self.checkType(func1.params[i].parType, func2.params[i])
                    for i in range(len(func1.params))
                ):
                    continue

                matched = True
                break

            if not matched:
                return False
        return True