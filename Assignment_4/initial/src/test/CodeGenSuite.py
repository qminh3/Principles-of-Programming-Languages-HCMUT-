import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_local_var(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_global_var(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_int_ast(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_local_var_ast(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(500)), FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_global_var_ast(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(5000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_int_literal_2(self):
        input = """func main() {putInt(10);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_local_var_2(self):
        input = """func main() {var a int = 100; putInt(a);};"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_global_var_2(self):
        input = """var a int = 200; func main() { putInt(a);};"""
        expect = "200"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_int_ast_2(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(15)])]))])
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_local_var_ast_2(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(150)), FuncCall("putInt", [Id("a")])]))])
        expect = "150"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_global_var_ast_2(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(10000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "10000"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_int_literal_3(self):
        input = """func main() {putInt(50);};"""
        expect = "50"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_local_var_3(self):
        input = """func main() {var a int = 35; putInt(a);};"""
        expect = "35"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_global_var_3(self):
        input = """var a int = 500; func main() { putInt(a);};"""
        expect = "500"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_int_ast_3(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(30)])]))])
        expect = "30"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_local_var_ast_3(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(300)), FuncCall("putInt", [Id("a")])]))])
        expect = "300"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_global_var_ast_3(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(2500)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "2500"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_int_literal_4(self):
        input = """func main() {putInt(100);};"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_local_var_4(self):
        input = """func main() {var a int = 25; putInt(a);};"""
        expect = "25"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_global_var_4(self):
        input = """var a int = 400; func main() { putInt(a);};"""
        expect = "400"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_int_ast_4(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(80)])]))])
        expect = "80"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_local_var_ast_4(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(800)), FuncCall("putInt", [Id("a")])]))])
        expect = "800"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_global_var_ast_4(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(8000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "8000"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_int_literal_5(self):
        input = """func main() {putInt(200);};"""
        expect = "200"
        self.assertTrue(TestCodeGen.test(input, expect, 525))
    def test_int_literal_6(self):
        input = """func main() {putInt(300);};"""
        expect = "300"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_local_var_5(self):
        input = """func main() {var a int = 600; putInt(a);};"""
        expect = "600"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_global_var_5(self):
        input = """var a int = 1500; func main() { putInt(a);};"""
        expect = "1500"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_int_ast_5(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(120)])]))])
        expect = "120"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_local_var_ast_5(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(450)), FuncCall("putInt", [Id("a")])]))])
        expect = "450"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_global_var_ast_5(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(12000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "12000"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_int_literal_7(self):
        input = """func main() {putInt(700);};"""
        expect = "700"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_local_var_6(self):
        input = """func main() {var a int = 50; putInt(a);};"""
        expect = "50"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_global_var_6(self):
        input = """var a int = 1800; func main() { putInt(a);};"""
        expect = "1800"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_int_ast_6(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(150)])]))])
        expect = "150"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_local_var_ast_6(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(700)), FuncCall("putInt", [Id("a")])]))])
        expect = "700"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_global_var_ast_6(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(7000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "7000"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_int_literal_8(self):
        input = """func main() {putInt(900);};"""
        expect = "900"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_local_var_7(self):
        input = """func main() {var a int = 125; putInt(a);};"""
        expect = "125"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_global_var_7(self):
        input = """var a int = 10000; func main() { putInt(a);};"""
        expect = "10000"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_int_ast_7(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(200)])]))])
        expect = "200"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_local_var_ast_7(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(350)), FuncCall("putInt", [Id("a")])]))])
        expect = "350"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_global_var_ast_7(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(3500)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "3500"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_int_literal_9(self):
        input = """func main() {putInt(50);};"""
        expect = "50"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_local_var_8(self):
        input = """func main() {var a int = 1500; putInt(a);};"""
        expect = "1500"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_global_var_8(self):
        input = """var a int = 2000; func main() { putInt(a);};"""
        expect = "2000"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_int_ast_8(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(170)])]))])
        expect = "170"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_local_var_ast_8(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(1300)), FuncCall("putInt", [Id("a")])]))])
        expect = "1300"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_global_var_ast_8(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(13000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "13000"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_int_literal_10(self):
        input = """func main() {putInt(400);};"""
        expect = "400"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_local_var_9(self):
        input = """func main() {var a int = 130; putInt(a);};"""
        expect = "130"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_global_var_9(self):
        input = """var a int = 45; func main() { putInt(a);};"""
        expect = "45"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_int_ast_9(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(400)])]))])
        expect = "400"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_local_var_ast_9(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(900)), FuncCall("putInt", [Id("a")])]))])
        expect = "900"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_global_var_ast_9(self):  
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(1300)), FuncCall("putInt", [Id("a")])]))])
        expect = "1300"
        self.assertTrue(TestCodeGen.test(input, expect, 555))
    def test_int_literal_11(self):
        input = """func main() {putInt(600);};"""
        expect = "600"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_local_var_10(self):
        input = """func main() {var a int = 500; putInt(a);};"""
        expect = "500"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_global_var_10(self):
        input = """var a int = 2500; func main() { putInt(a);};"""
        expect = "2500"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_int_ast_10(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(1000)])]))])
        expect = "1000"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_local_var_ast_10(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(1000)), FuncCall("putInt", [Id("a")])]))])
        expect = "1000"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_global_var_ast_10(self):  
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(1000)), FuncCall("putInt", [Id("a")])]))])
        expect = "1000"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_int_literal_12(self):
        input = """func main() {var a int = 6000; putInt(a);};"""
        expect = "6000"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_local_var_11(self):
        input = """func main() {var a int = 6000; putInt(a);};"""
        expect = "6000"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_global_var_11(self):
        input = """func main() {var a int = 6000; putInt(a);};"""
        expect = "6000"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_int_ast_11(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(700)])]))])
        expect = "700"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_local_var_ast_11(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(8000)), FuncCall("putInt", [Id("a")])]))])
        expect = "8000"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_global_var_ast_11(self):  
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(8000)), FuncCall("putInt", [Id("a")])]))])
        expect = "8000"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_int_literal_13(self):
        input = """func main() {putInt(2000);};"""
        expect = "2000"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_local_var_12(self):
        input = """func main() {var a int = 800; putInt(a);};"""
        expect = "800"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_global_var_12(self):
        input = """func main() {var a int = 800; putInt(a);};"""
        expect = "800"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_int_ast_12(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(1200)])]))])
        expect = "1200"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_local_var_ast_12(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(1200)), FuncCall("putInt", [Id("a")])]))])
        expect = "1200"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_global_var_ast_12(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(12000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "12000"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_int_literal_14(self):
        input = """func main() {putInt(10000);};"""
        expect = "10000"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_local_var_13(self):
        input = """func main() {var a int = 120; putInt(a);};"""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_global_var_13(self):
        input = """var a int = 15000; func main() { putInt(a);};"""
        expect = "15000"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_int_ast_13(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(1500)])]))])
        expect = "1500"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_local_var_ast_13(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(1500)), FuncCall("putInt", [Id("a")])]))])
        expect = "1500"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_global_var_ast_13(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(15000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "15000"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_int_literal_15(self):
        input = """func main() {putInt(100);};"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_local_var_14(self):
        input = """func main() {var a int = 200; putInt(a);};"""
        expect = "200"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_global_var_14(self):
        input = """var a int = 2500; func main() { putInt(a);};"""
        expect = "2500"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_int_ast_14(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(500)])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_local_var_ast_14(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(500)), FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_global_var_ast_14(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(5000)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input, expect, 585))
    def test_int_literal_16(self):
        input = """func main() {putInt(110);};"""
        expect = "110"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_local_var_15(self):
        input = """func main() {var a int = 220; putInt(a);};"""
        expect = "220"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_global_var_15(self):
        input = """var a int = 330; func main() { putInt(a);};"""
        expect = "330"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_int_ast_15(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(440)])]))])
        expect = "440"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_local_var_ast_15(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(550)), FuncCall("putInt", [Id("a")])]))])
        expect = "550"
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    def test_global_var_ast_15(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(660)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "660"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_int_literal_17(self):
        input = """func main() {putInt(770);};"""
        expect = "770"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_local_var_16(self):
        input = """func main() {var a int = 880; putInt(a);};"""
        expect = "880"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_global_var_16(self):
        input = """var a int = 990; func main() { putInt(a);};"""
        expect = "990"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_int_ast_16(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [IntLiteral(1110)])]))])
        expect = "1110"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_local_var_ast_16(self):
        input = Program([FuncDecl("main", [], VoidType(), Block([VarDecl("a", IntType(), IntLiteral(1220)), FuncCall("putInt", [Id("a")])]))])
        expect = "1220"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_global_var_ast_16(self):  
        input = Program([VarDecl("a", IntType(), IntLiteral(1330)), FuncDecl("main", [], VoidType(), Block([FuncCall("putInt", [Id("a")])]))])
        expect = "1330"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_int_literal_18(self):
        input = """func main() {putInt(1440);};"""
        expect = "1440"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_local_var_17(self):
        input = """func main() {var a int = 1550; putInt(a);};"""
        expect = "1550"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_global_var_17(self):
        input = """var a int = 1660; func main() { putInt(a);};"""
        expect = "1660"
        self.assertTrue(TestCodeGen.test(input, expect, 600))