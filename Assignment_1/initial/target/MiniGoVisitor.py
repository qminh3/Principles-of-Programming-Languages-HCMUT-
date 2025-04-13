# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_declaration.
    def visitList_declaration(self, ctx:MiniGoParser.List_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declaration.
    def visitDeclaration(self, ctx:MiniGoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement_primary.
    def visitList_statement_primary(self, ctx:MiniGoParser.List_statement_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_type.
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_declaration.
    def visitConst_declaration(self, ctx:MiniGoParser.Const_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_declaration.
    def visitVar_declaration(self, ctx:MiniGoParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_declaration_global.
    def visitVar_declaration_global(self, ctx:MiniGoParser.Var_declaration_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_declaration_global.
    def visitConst_declaration_global(self, ctx:MiniGoParser.Const_declaration_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declaration.
    def visitStruct_declaration(self, ctx:MiniGoParser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_struct.
    def visitData_struct(self, ctx:MiniGoParser.Data_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declaration.
    def visitMethod_declaration(self, ctx:MiniGoParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_method_element.
    def visitList_method_element(self, ctx:MiniGoParser.List_method_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_element.
    def visitMethod_element(self, ctx:MiniGoParser.Method_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_declaration.
    def visitFunc_declaration(self, ctx:MiniGoParser.Func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_func_arguments.
    def visitList_func_arguments(self, ctx:MiniGoParser.List_func_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_agruments.
    def visitList_agruments(self, ctx:MiniGoParser.List_agrumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_agrument.
    def visitFunc_agrument(self, ctx:MiniGoParser.Func_agrumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_element.
    def visitData_element(self, ctx:MiniGoParser.Data_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declaration.
    def visitInterface_declaration(self, ctx:MiniGoParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_method_interface.
    def visitList_method_interface(self, ctx:MiniGoParser.List_method_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#inter_method.
    def visitInter_method(self, ctx:MiniGoParser.Inter_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_interface_element.
    def visitList_interface_element(self, ctx:MiniGoParser.List_interface_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_oprator.
    def visitAssign_oprator(self, ctx:MiniGoParser.Assign_opratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dot_id.
    def visitDot_id(self, ctx:MiniGoParser.Dot_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseif_list.
    def visitElseif_list(self, ctx:MiniGoParser.Elseif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block_statement.
    def visitBlock_statement(self, ctx:MiniGoParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_basic.
    def visitFor_basic(self, ctx:MiniGoParser.For_basicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_loop_basic.
    def visitFor_loop_basic(self, ctx:MiniGoParser.For_loop_basicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_loop_range.
    def visitFor_loop_range(self, ctx:MiniGoParser.For_loop_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_for.
    def visitAssignment_for(self, ctx:MiniGoParser.Assignment_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_declaration_for.
    def visitVar_declaration_for(self, ctx:MiniGoParser.Var_declaration_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs_aggin.
    def visitLhs_aggin(self, ctx:MiniGoParser.Lhs_agginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_type_arr.
    def visitList_type_arr(self, ctx:MiniGoParser.List_type_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayInit.
    def visitArrayInit(self, ctx:MiniGoParser.ArrayInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_value.
    def visitList_array_value(self, ctx:MiniGoParser.List_array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_body.
    def visitStruct_lit_body(self, ctx:MiniGoParser.Struct_lit_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit_body_element.
    def visitStruct_lit_body_element(self, ctx:MiniGoParser.Struct_lit_body_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_element.
    def visitStruct_element(self, ctx:MiniGoParser.Struct_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#params.
    def visitParams(self, ctx:MiniGoParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_1.
    def visitExpression_1(self, ctx:MiniGoParser.Expression_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_2.
    def visitExpression_2(self, ctx:MiniGoParser.Expression_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_3.
    def visitExpression_3(self, ctx:MiniGoParser.Expression_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_4.
    def visitExpression_4(self, ctx:MiniGoParser.Expression_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_5.
    def visitExpression_5(self, ctx:MiniGoParser.Expression_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_6.
    def visitExpression_6(self, ctx:MiniGoParser.Expression_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_7.
    def visitExpression_7(self, ctx:MiniGoParser.Expression_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)



del MiniGoParser