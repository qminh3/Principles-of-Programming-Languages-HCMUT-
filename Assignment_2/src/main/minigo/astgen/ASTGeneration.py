# 2212019
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

class ASTGeneration(MiniGoVisitor):
   # program: list_declaration EOF;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        test = self.visit(ctx.list_declaration())
        return Program(test)


    # list_declaration: declaration list_declaration | declaration;
    def visitList_declaration(self, ctx:MiniGoParser.List_declarationContext):
        if ctx.list_declaration():
            return [self.visit(ctx.declaration())] + self.visit(ctx.list_declaration())
        return [self.visit(ctx.declaration())]


    # declaration: var_declaration| const_declaration| func_declaration| struct_declaration | interface_declaration ;
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        if ctx.var_declaration():
            return self.visit(ctx.var_declaration())
        elif ctx.const_declaration():
            return self.visit(ctx.const_declaration())
        elif ctx.func_declaration():
            return self.visit(ctx.func_declaration())
        elif ctx.struct_declaration():
            return self.visit(ctx.struct_declaration())
        elif ctx.interface_declaration():
            return self.visit(ctx.interface_declaration())


    # list_statement_primary: list_statement | ;
    def visitList_statement_primary(self, ctx:MiniGoParser.List_statement_primaryContext):
        if ctx.list_statement():
            return self.visit(ctx.list_statement())
        return []


    # list_statement: (statement list_statement) | statement;
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.list_statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())
        return [self.visit(ctx.statement())]


    # statement: (const_declaration | var_declaration | assign_statement | if_statement | for_statement | break_statement| continue_statement| func_call| call_statement| return_statement) ;
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        if ctx.const_declaration():
            return self.visit(ctx.const_declaration())
        elif ctx.var_declaration():
            return self.visit(ctx.var_declaration())
        elif ctx.assign_statement():
            return self.visit(ctx.assign_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        

    # const_declaration : CONST ID ASSIGN expression SEMICOLON ;
    def visitConst_declaration(self, ctx:MiniGoParser.Const_declarationContext):
        conName = ctx.ID().getText()
        iniExpr = self.visit(ctx.expression())
        return ConstDecl(conName,None,iniExpr)

    # var_declaration: VAR ID ((data_type ((ASSIGN (expression)) | )) | (ASSIGN (expression))) SEMICOLON;
    def visitVar_declaration(self, ctx:MiniGoParser.Var_declarationContext):
        variable_name = ctx.getChild(1).getText()
        if ctx.data_type():
            varType = self.visit(ctx.data_type())
            if ctx.expression():
                return VarDecl(variable_name, varType, self.visit(ctx.expression()))
            else:
                return VarDecl(variable_name, varType, None)
        else:
            return VarDecl(variable_name, None, self.visit(ctx.expression()))


    # struct_declaration: TYPE ID STRUCT LBRACE data_struct RBRACE (SEMICOLON);
    def visitStruct_declaration(self, ctx:MiniGoParser.Struct_declarationContext):
        struct_name = ctx.ID().getText()
        fields = self.visit(ctx.data_struct())
        return StructType(name=struct_name, elements=fields , methods=[])


    # data_struct: (ID data_type (SEMICOLON)) data_struct | (ID data_type (SEMICOLON));
    def visitData_struct(self, ctx:MiniGoParser.Data_structContext):
        data_type_tuple = list(map(lambda child: (child.getChild(0).getText(), self.visit(child.data_type())), [ctx] if ctx.data_type() else []))
        # Dùng map để xử lý data_struct
        data_struct_tuples = list(map(lambda item: item, self.visit(ctx.data_struct()) if ctx.data_struct() else []))
        
        # Kết hợp cả hai kết quả
        return (data_type_tuple + data_struct_tuples)
        
    # method_declaration: LPAREN list_method_element RPAREN;
    def visitMethod_declaration(self, ctx:MiniGoParser.Method_declarationContext):
        return self.visit(ctx.list_method_element())


    # list_method_element: method_element COMMA list_method_element | method_element;
    def visitList_method_element(self, ctx:MiniGoParser.List_method_elementContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.method_element())]
        else:
            return [self.visit(ctx.method_element())] + self.visit(ctx.getChild(2))

    # method_element: ID ID;
    def visitMethod_element(self, ctx:MiniGoParser.Method_elementContext):
        return (ctx.getChild(0).getText(), Id(ctx.getChild(1).getText()))


    # func_declaration: FUNC (method_declaration | ) ID LPAREN list_func_arguments RPAREN (data_type | ) LBRACE list_statement_primary RBRACE SEMICOLON;
    def visitFunc_declaration(self, ctx:MiniGoParser.Func_declarationContext):
        return_type = self.visit(ctx.data_type()) if ctx.data_type() else VoidType()
        params= self.visit(ctx.list_func_arguments())
        body = Block(self.visit(ctx.list_statement_primary()))
        func_decl = FuncDecl(ctx.ID().getText(), params, return_type, body)
        
        if ctx.method_declaration():
            receiver,recType = self.visit(ctx.method_declaration())[0]
            return MethodDecl(receiver,recType,func_decl)
        
        return func_decl
            
    # list_func_arguments: list_agruments | ;
    def visitList_func_arguments(self, ctx:MiniGoParser.List_func_argumentsContext):
        if ctx.list_agruments():
            return self.visit(ctx.list_agruments())
        return []


    # list_agruments: func_agrument COMMA list_agruments | func_agrument;
    def visitList_agruments(self, ctx:MiniGoParser.List_agrumentsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.func_agrument())
        else:
            return self.visit(ctx.func_agrument()) + self.visit(ctx.list_agruments())
        


    # func_agrument: data_element data_type;
    def visitFunc_agrument(self, ctx:MiniGoParser.Func_agrumentContext):
        parType=self.visit(ctx.data_type())
        return list(map( lambda parName : ParamDecl(parName,parType),self.visit(ctx.data_element())))


    # data_element: ID COMMA data_element | ID;
    def visitData_element(self, ctx:MiniGoParser.Data_elementContext):
        if ctx.data_element():
            return [ctx.ID().getText()] + self.visit(ctx.data_element())
        return [ctx.ID().getText()]
            
        
    # interface_declaration: TYPE ID INTERFACE LBRACE list_method_interface RBRACE (SEMICOLON) ;
    def visitInterface_declaration(self, ctx:MiniGoParser.Interface_declarationContext):
        name=ctx.ID().getText()
        methods = self.visit(ctx.list_method_interface())
        return InterfaceType(name, methods)

    #list_method_interface: inter_method list_method_interface | inter_method;
    def visitList_method_interface(self, ctx:MiniGoParser.List_method_interfaceContext):
        return [self.visit(ctx.inter_method())] if ctx.getChildCount() == 1 else [self.visit(ctx.inter_method())] + self.visit(ctx.list_method_interface())
            


    # inter_method: ID LPAREN list_interface_element? RPAREN (data_type |) SEMICOLON;
    def visitInter_method(self, ctx:MiniGoParser.Inter_methodContext):
        
        return_type = self.visit(ctx.data_type()) if ctx.data_type() else VoidType()
        
        params = [] if ctx.list_interface_element() is None else self.visit(ctx.list_interface_element())
        
        return Prototype(ctx.ID().getText(), params, return_type)
    
    # list_interface_element: inter_param COMMA list_interface_element | inter_param;
    def visitList_interface_element(self, ctx:MiniGoParser.List_interface_elementContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.inter_param())
        else:
            return self.visit(ctx.inter_param()) + self.visit(ctx.list_interface_element())
        
        
    # inter_param: data_element data_type;
    def visitInter_param(self, ctx:MiniGoParser.Inter_paramContext):
        data_element = self.visit(ctx.data_element())
        return list(map(lambda _: self.visit(ctx.data_type()), data_element))
   
    
    # assign_oprator: ASS_DECLARE| ADD_ASSIGN| SUB_ASSIGN| MUL_ASSIGN| DIV_ASSIGN| MOD_ASSIGN;
    def visitAssign_oprator(self, ctx:MiniGoParser.Assign_opratorContext):
        if ctx.ASS_DECLARE():
            return "="
        elif ctx.ADD_ASSIGN():
            return "+"
        elif ctx.SUB_ASSIGN():
            return "-"
        elif ctx.MUL_ASSIGN():
            return "*"
        elif ctx.DIV_ASSIGN():
            return "/"
        elif ctx.MOD_ASSIGN():
            return "%"
        
    # assign_statement: (assignment_lhs) (assign_oprator expression) SEMICOLON;
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        assign_oprator = self.visit(ctx.assign_oprator())
        assignment_lhs = self.visit(ctx.assignment_lhs())
        rhs = self.visit(ctx.expression())
        if assign_oprator == "=":
            return Assign(assignment_lhs, rhs)
        return Assign(assignment_lhs,BinaryOp(assign_oprator,assignment_lhs,rhs))
        
    # assignment_lhs: assignment_lhs (DOT ID | LBRACKET expression RBRACKET) | ID;    
    def visitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            if ctx.LBRACKET() and ctx.RBRACKET():
                assign_lhs = self.visit(ctx.assignment_lhs())
                if type(assign_lhs) == ArrayCell:
                    return ArrayCell(assign_lhs.arr, assign_lhs.idx + [self.visit(ctx.expression())])
                return ArrayCell(assign_lhs,[self.visit(ctx.expression())])
            else:
                return FieldAccess(self.visit(ctx.assignment_lhs()), ctx.ID().getText())

            
    # if_statement: if_stmt (elseif_list| ) (ELSE  block_statement | ) SEMICOLON;
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        condition, statement_if = self.visit(ctx.if_stmt())
        elseif_list = self.visit(ctx.elseif_list()) if ctx.elseif_list() else []
        else_stmt = Block(self.visit(ctx.block_statement())) if ctx.ELSE() else None
        
        if len(elseif_list) == 0:
                return If(
                    condition,
                    Block(statement_if),
                    else_stmt
                )
        def process(elseif_list, else_stmt):
            if len(elseif_list) == 0: return else_stmt
            exp, block = elseif_list[0]
            return If(exp, block, process(elseif_list[1:], else_stmt))

        return If(condition, Block(statement_if), process(elseif_list, else_stmt) ) 
        
    # if_stmt: IF LPAREN expression RPAREN block_statement;
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return (self.visit(ctx.expression()),self.visit(ctx.block_statement()))


    # elseif_list: (ELSE IF LPAREN expression RPAREN  block_statement ) elseif_list | (ELSE IF LPAREN expression RPAREN  block_statement );
    def visitElseif_list(self, ctx:MiniGoParser.Elseif_listContext):
        block_statement = self.visit(ctx.block_statement())
        if ctx.elseif_list():
            return [(self.visit(ctx.expression()), Block(block_statement))] + self.visit(ctx.elseif_list())
        else:
            return [(self.visit(ctx.expression()), Block(block_statement))]
        


    # block_statement: LBRACE list_statement_primary RBRACE;
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        return self.visit(ctx.list_statement_primary())


    # for_statement: FOR (for_basic | for_loop_basic | for_loop_range) LBRACE list_statement_primary RBRACE SEMICOLON ;
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        listStmt = self.visit(ctx.list_statement_primary())
        if ctx.for_basic():
            return ForBasic(self.visit(ctx.for_basic()),Block(listStmt))
        elif ctx.for_loop_basic():
            init, cond, upda = self.visit(ctx.for_loop_basic())
            return ForStep(init, cond, upda, Block(listStmt))
        else:
            idx,value,arr = self.visit(ctx.for_loop_range())
            return ForEach(idx,value,arr, Block(listStmt))


    # for_basic:  expression  ;
    def visitFor_basic(self, ctx:MiniGoParser.For_basicContext):
        return self.visit(ctx.expression())


    # for_loop_basic:( var_declaration_for| assignment_for) SEMICOLON expression SEMICOLON assignment_for  ;
    def visitFor_loop_basic(self, ctx:MiniGoParser.For_loop_basicContext):
        init = self.visit(ctx.getChild(0))
        cond = self.visit(ctx.expression())
        upda = self.visit(ctx.getChild(4))
        return init, cond, upda


    # for_loop_range: ID COMMA ID ASS_DECLARE RANGE expression  ;
    def visitFor_loop_range(self, ctx:MiniGoParser.For_loop_rangeContext):
        id1 = Id(ctx.ID(0).getText())
        id2 = Id(ctx.ID(1).getText())
        return id1, id2, self.visit(ctx.expression())


    # assignment_for: ID (assign_oprator expression);
    def visitAssignment_for(self, ctx:MiniGoParser.Assignment_forContext):
        assign_oprator = self.visit(ctx.assign_oprator())
        id = Id(ctx.ID().getText())
        rhs = self.visit(ctx.expression())
        if assign_oprator == "=":
            return Assign(id, rhs)
        return Assign(id,BinaryOp(assign_oprator,id,rhs))

    # var_declaration_for: VAR ID data_type? ASSIGN expression;
    def visitVar_declaration_for(self, ctx:MiniGoParser.Var_declaration_forContext):
        id = ctx.ID().getText()
        data_type = self.visit(ctx.data_type()) if ctx.data_type() else None
        return VarDecl(id, data_type, self.visit(ctx.expression()))


    # break_statement: BREAK SEMICOLON;
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # lhs_aggin: lhs_aggin (LBRACKET expression RBRACKET | DOT ID) | ID;
    def visitLhs_aggin(self, ctx:MiniGoParser.Lhs_agginContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            if ctx.LBRACKET() and ctx.RBRACKET():
                assign_lhs = self.visit(ctx.lhs_aggin())
                if type(assign_lhs) == ArrayCell:
                    return ArrayCell(assign_lhs.arr, assign_lhs.idx + [self.visit(ctx.expression())])
                return ArrayCell(assign_lhs,[self.visit(ctx.expression())])
            else:
                return FieldAccess(self.visit(ctx.lhs_aggin()), ctx.ID().getText())


    # call_statement: ((lhs_aggin DOT) | )ID LPAREN list_expression RPAREN SEMICOLON;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        list_expression = self.visit(ctx.list_expression())
        if ctx.lhs_aggin():
            lhs = self.visit(ctx.lhs_aggin())
            return MethCall(lhs, ctx.ID().getText(), list_expression)
        else:
            return FuncCall(ctx.ID().getText(), list_expression)


    # continue_statement: CONTINUE SEMICOLON;
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # return_statement: RETURN (expression | ) SEMICOLON;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(expr)


    # literal:INTEGER_LITERAL| FLOATING_LITERAL| STRING_LITERAL| BOOLEAN_LIT| array_literal| struct_literal;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INTEGER_LITERAL():
            return IntLiteral(ctx.INTEGER_LITERAL().getText())
        elif ctx.FLOATING_LITERAL():
            return FloatLiteral(ctx.FLOATING_LITERAL().getText())
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.BOOLEAN_LIT():
            return BooleanLiteral(ctx.BOOLEAN_LIT().getText()== 'true')
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        return self.visit(ctx.getChild(0))


    # data_type: ID | INT | FLOAT | BOOLEAN | STRING | array_type;
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.array_type():
            dims, declare_type = self.visit(ctx.array_type())
            return ArrayType(dims, declare_type)
        return VoidType()



    #array_literal: array_type LBRACE list_array_element RBRACE;
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        dims, declare_type = self.visit(ctx.array_type())
        values = self.visit(ctx.list_array_element())
        return ArrayLiteral(dims, declare_type, values)


    # array_type: list_type_arr (data_type);
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        dims = self.visit(ctx.list_type_arr())
        declare_type = self.visit(ctx.data_type())
        return dims, declare_type

    # list_type_arr: LBRACKET (INTEGER_LITERAL | ID) RBRACKET list_type_arr | LBRACKET (INTEGER_LITERAL | ID) RBRACKET;
    def visitList_type_arr(self, ctx:MiniGoParser.List_type_arrContext):
            array_dimen = None
            if ctx.INTEGER_LITERAL():
                text = ctx.INTEGER_LITERAL().getText()
                if text.startswith("0b") or text.startswith("0B"):  
                    array_dimen = IntLiteral(int(text, 2))
                elif text.startswith("0o") or text.startswith("0O"):  
                    array_dimen =  IntLiteral(int(text, 8))
                elif text.startswith("0x") or text.startswith("0X"):  
                    array_dimen =  IntLiteral(int(text, 16))
                else:  
                    array_dimen =  IntLiteral(int(text, 10))
            else:
                array_dimen = Id(ctx.ID().getText())
            if ctx.getChildCount() == 3:
                return [array_dimen]
            return [array_dimen] + self.visit(ctx.list_type_arr())
            

    #list_array_element: array_element COMMA list_array_element | array_element;
    def visitList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        if ctx.list_array_element():
            return [self.visit(ctx.array_element())] + self.visit(ctx.list_array_element())
        return [self.visit(ctx.array_element())]


    # array_element: array_param | (LBRACE list_array_element RBRACE);
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        if ctx.array_param():
            return self.visit(ctx.array_param())
        return self.visit(ctx.list_array_element())

    # array_param :INTEGER_LITERAL| FLOATING_LITERAL| STRING_LITERAL| TRUE | FALSE| NIL| ID| struct_literal;
    def visitArray_param(self, ctx:MiniGoParser.Array_paramContext):
        if ctx.INTEGER_LITERAL():
            return IntLiteral(ctx.INTEGER_LITERAL().getText())
        elif ctx.FLOATING_LITERAL():
            return FloatLiteral(ctx.FLOATING_LITERAL().getText())
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())  
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))

    # struct_literal: ID LBRACE struct_lit_body RBRACE;
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        struct_name = ctx.ID().getText()
        elements= self.visit(ctx.struct_lit_body()) if ctx.struct_lit_body() else []
        return StructLiteral(struct_name, elements)


    #  struct_lit_body: struct_lit_body_element | ;
    def visitStruct_lit_body(self, ctx:MiniGoParser.Struct_lit_bodyContext):
        if not ctx.getChildCount():
            return []
        return self.visit(ctx.struct_lit_body_element())


     # struct_lit_body_element: struct_element COMMA struct_lit_body_element | struct_element;
    def visitStruct_lit_body_element(self, ctx:MiniGoParser.Struct_lit_body_elementContext):
        if ctx.struct_lit_body_element():
            return [self.visit(ctx.struct_element())] + self.visit(ctx.struct_lit_body_element())
        return [self.visit(ctx.struct_element())]

    #struct_element: ID COLON expression   ;
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        field_name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        return (field_name, expr)

    # list_expression: params | ;
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visit(ctx.params()) if ctx.params() else []

    # params: expression COMMA params | expression ;
    def visitParams(self, ctx:MiniGoParser.ParamsContext):
        if ctx.params():
            return [self.visit(ctx.expression())] + self.visit(ctx.params())
        return [self.visit(ctx.expression())]

    # expression: expression OR expression_1 | expression_1;
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1: 
            return self.visitChildren(ctx)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    # expression_1: expression_1 AND expression_2 | expression_2;
    def visitExpression_1(self, ctx:MiniGoParser.Expression_1Context):
        if ctx.getChildCount() == 1: 
            return self.visitChildren(ctx)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    # expression_2: expression_2 COMPARE_OPERATOR expression_3 | expression_3;    
    # # COMPARE_OPERATOR: EQUAL| NOT_EQUAL| LESS| LESS_EQUAL| GREATER| GREATER_EQUAL;
    def visitExpression_2(self, ctx:MiniGoParser.Expression_2Context):
        if ctx.getChildCount() == 1: 
            return self.visitChildren(ctx)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    # expression_3: expression_3 (ADD | SUB ) expression_4 | expression_4 ;
    def visitExpression_3(self, ctx:MiniGoParser.Expression_3Context):
        if ctx.getChildCount() == 1: 
            return self.visitChildren(ctx)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        
    # expression_4: expression_4 (MUL | DIV | MOD) expression_5 | expression_5 ;
    def visitExpression_4(self, ctx:MiniGoParser.Expression_4Context):
        if ctx.getChildCount() == 1: 
            return self.visitChildren(ctx)
        else:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    # expression_5: (NOT | SUB) expression_5 | expression_6 ;
    def visitExpression_5(self, ctx:MiniGoParser.Expression_5Context):
        if ctx.getChildCount() == 1: 
            return self.visitChildren(ctx)
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))

    # expression_6: expression_6 LBRACKET (expression) RBRACKET | expression_6 (DOT (ID |func_call ))| expression_7;
    def visitExpression_6(self, ctx:MiniGoParser.Expression_6Context):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.expression_7())
        elif ctx.expression(): 
            result = self.visit(ctx.expression_6())
            if type(result) == ArrayCell:
                return ArrayCell(result.arr, result.idx  + [self.visit(ctx.expression())])  
            return ArrayCell(result, [self.visit(ctx.expression())])
        elif ctx.getChildCount() == 3:
            if ctx.func_call():
                func_call = self.visit(ctx.func_call())
                return MethCall(self.visit(ctx.expression_6()), func_call.funName, func_call.args)
            return FieldAccess(self.visit(ctx.expression_6()), ctx.ID().getText())

    # expression_7: ID | literal | LPAREN expression RPAREN | func_call | TRUE | FALSE | NIL;
    def visitExpression_7(self, ctx:MiniGoParser.Expression_7Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        else:
            return self.visit(ctx.expression())

    # func_call: ID LPAREN list_expression RPAREN;
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression()))
