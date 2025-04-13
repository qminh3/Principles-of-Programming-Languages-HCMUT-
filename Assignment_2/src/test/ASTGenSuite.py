import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_1(self):
        input = """const x = foo( 1 ); """
        expect = Program([ConstDecl("x", None, FuncCall("foo", [IntLiteral(1)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 301))

    def test_2(self):
        input = """const y = bar( 2.5, true, "hello" ); """
        expect = Program([ConstDecl("y", None, FuncCall("bar", [FloatLiteral(2.5), BooleanLiteral(True), StringLiteral("\"hello\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 302))

    def test_3(self):
        input = """const z = max( a + b, c * d ); """
        expect = Program([ConstDecl("z", None, FuncCall("max", [BinaryOp("+", Id("a"), Id("b")), BinaryOp("*", Id("c"), Id("d"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 303))

    def test_4(self):
        input = """const result = compute( 10 / 2 - 3, false ); """
        expect = Program([ConstDecl("result", None, FuncCall("compute", [BinaryOp("-", BinaryOp("/", IntLiteral(10), IntLiteral(2)), IntLiteral(3)), BooleanLiteral(False)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 304))

    def test_5(self):
        input = """const val = nested( foo(1), bar(2) ); """
        expect = Program([ConstDecl("val", None, FuncCall("nested", [FuncCall("foo", [IntLiteral(1)]), FuncCall("bar", [IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 305))

    def test_6(self):
        input = """const a = add( 1, 2 ); """
        expect = Program([ConstDecl("a", None, FuncCall("add", [IntLiteral(1), IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 306))

    def test_7(self):
        input = """const b = sub( 10.5, 4.5 ); """
        expect = Program([ConstDecl("b", None, FuncCall("sub", [FloatLiteral(10.5), FloatLiteral(4.5)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 307))

    def test_8(self):
        input = """const c = mul( a, b ); """
        expect = Program([ConstDecl("c", None, FuncCall("mul", [Id("a"), Id("b")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 308))

    def test_9(self):
        input = """const d = divide( 5, 3 ); """
        expect = Program([ConstDecl("d", None, FuncCall("divide", [IntLiteral(5), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 309))

    def test_10(self):
        input = """const e = sqrt( 9 ); """
        expect = Program([ConstDecl("e", None, FuncCall("sqrt", [IntLiteral(9)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 310))

    def test_11(self):
        input = """const f = factorial( 5 ); """
        expect = Program([ConstDecl("f", None, FuncCall("factorial", [IntLiteral(5)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 311))

    def test_12(self):
        input = """const g = is_even( 4 ); """
        expect = Program([ConstDecl("g", None, FuncCall("is_even", [IntLiteral(4)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 312))

    def test_13(self):
        input = """const h = is_odd( 3 ); """
        expect = Program([ConstDecl("h", None, FuncCall("is_odd", [IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 313))
    
    def test_14(self):
        input = """const i = concat( "foo", "bar" ); """
        expect = Program([ConstDecl("i", None, FuncCall("concat", [StringLiteral("\"foo\""), StringLiteral("\"bar\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect),314))

    def test_15(self):
        input = """const j = power( 2, 3 ); """
        expect = Program([ConstDecl("j", None, FuncCall("power", [IntLiteral(2), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 315))

    def test_16(self):
        input = """const k = max( min( 1, 2 ), max( 3, 4 ) ); """
        expect = Program([ConstDecl("k", None, FuncCall("max", [FuncCall("min", [IntLiteral(1), IntLiteral(2)]), FuncCall("max", [IntLiteral(3), IntLiteral(4)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 316))

    def test_17(self):
        input = """const l = max( a + b, c - d ); """
        expect = Program([ConstDecl("l", None, FuncCall("max", [BinaryOp("+", Id("a"), Id("b")), BinaryOp("-", Id("c"), Id("d"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 317))

    def test_18(self):
        input = """const m = min( a * b, c / d ); """
        expect = Program([ConstDecl("m", None, FuncCall("min", [BinaryOp("*", Id("a"), Id("b")), BinaryOp("/", Id("c"), Id("d"))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 318))

    def test_19(self):
        input = """const n = abs( -10 ); """
        expect = Program([ConstDecl("n", None, FuncCall("abs", [UnaryOp("-", IntLiteral(10))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 319))

    def test_20(self):
        input = """const o = sign( -5 ); """
        expect = Program([ConstDecl("o", None, FuncCall("sign", [UnaryOp("-", IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 320))

    def test_21(self):
        input = """const p = add( a, b ); """
        expect = Program([ConstDecl("p", None, FuncCall("add", [Id("a"), Id("b")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 321))

    def test_22(self):
        input = """const q = multiply( 2, 5 ); """
        expect = Program([ConstDecl("q", None, FuncCall("multiply", [IntLiteral(2), IntLiteral(5)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 322))
    def test_23(self):
        input = """const r = subtract( x, y ); """
        expect = Program([ConstDecl("r", None, FuncCall("subtract", [Id("x"), Id("y")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 323))

    def test_24(self):
        input = """const s = divide( 8, 4 ); """
        expect = Program([ConstDecl("s", None, FuncCall("divide", [IntLiteral(8), IntLiteral(4)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 324))

    def test_25(self):
        input = """const t = is_equal( true, false ); """
        expect = Program([ConstDecl("t", None, FuncCall("is_equal", [BooleanLiteral(True), BooleanLiteral(False)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 325))
        
    def test_26(self):
        input = """const u = not( true ); """
        expect = Program([ConstDecl("u", None, FuncCall("not", [BooleanLiteral(True)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 326))

    def test_27(self):
        input = """const v = concat( "hello", "world" ); """
        expect = Program([ConstDecl("v", None, FuncCall("concat", [StringLiteral("\"hello\""), StringLiteral("\"world\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 327))
        
    def test_28(self):
        input = """const w = max( 2, min( 1, 3 ) ); """
        expect = Program([ConstDecl("w", None, FuncCall("max", [IntLiteral(2), FuncCall("min", [IntLiteral(1), IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 328))

    def test_29(self):
        input = """const x = abs( -7 ); """
        expect = Program([ConstDecl("x", None, FuncCall("abs", [UnaryOp("-", IntLiteral(7))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 329))

    def test_30(self):
        input = """const y = power( 2, 5 ); """
        expect = Program([ConstDecl("y", None, FuncCall("power", [IntLiteral(2), IntLiteral(5)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 330))

    def test_31(self):
        input = """const z = factorial( 4 ); """
        expect = Program([ConstDecl("z", None, FuncCall("factorial", [IntLiteral(4)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 331))

    def test_32(self):
        input = """const a1 = sign( -5 ); """
        expect = Program([ConstDecl("a1", None, FuncCall("sign", [UnaryOp("-", IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 332))

    def test_33(self):
        input = """const b1 = floor( 3.7 ); """
        expect = Program([ConstDecl("b1", None, FuncCall("floor", [FloatLiteral(3.7)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 333))

    def test_34(self):
        input = """const c1 = ceil( 7.2 ); """
        expect = Program([ConstDecl("c1", None, FuncCall("ceil", [FloatLiteral(7.2)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 334))

    def test_35(self):
        input = """const d1 = round( 3.14 ); """
        expect = Program([ConstDecl("d1", None, FuncCall("round", [FloatLiteral(3.14)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 335))

    def test_36(self):
        input = """const e1 = length( "hello" ); """
        expect = Program([ConstDecl("e1", None, FuncCall("length", [StringLiteral("\"hello\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 336))

    def test_37(self):
        input = """const f1 = upper( "hello" ); """
        expect = Program([ConstDecl("f1", None, FuncCall("upper", [StringLiteral("\"hello\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 337))

    def test_38(self):
        input = """const g1 = lower( "HELLO" ); """
        expect = Program([ConstDecl("g1", None, FuncCall("lower", [StringLiteral("\"HELLO\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 338))

    def test_39(self):
        input = """const h1 = substring( "hello", 1, 3 ); """
        expect = Program([ConstDecl("h1", None, FuncCall("substring", [StringLiteral("\"hello\""), IntLiteral(1), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 339))

    def test_40(self):
        input = """const i1 = index_of( "hello", "e" ); """
        expect = Program([ConstDecl("i1", None, FuncCall("index_of", [StringLiteral("\"hello\""), StringLiteral("\"e\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 340))

    def test_41(self):
        input = """const j1 = reverse( "hello" ); """
        expect = Program([ConstDecl("j1", None, FuncCall("reverse", [StringLiteral("\"hello\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 341))

    def test_42(self):
        input = """const k1 = mod( 10, 3 ); """
        expect = Program([ConstDecl("k1", None, FuncCall("mod", [IntLiteral(10), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 342))
    def test_43(self):
        input = """const l1 = is_odd( 5 ); """
        expect = Program([ConstDecl("l1", None, FuncCall("is_odd", [IntLiteral(5)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343))
    
    def test_44(self):
        input = """const m1 = is_even( 6 ); """
        expect = Program([ConstDecl("m1", None, FuncCall("is_even", [IntLiteral(6)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344))
    
    def test_45(self):
        input = """const n1 = trim( "  hello  " ); """
        expect = Program([ConstDecl("n1", None, FuncCall("trim", [StringLiteral("\"  hello  \"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 345))
    
    def test_46(self):
        input = """const o1 = concat( "good", "morning" ); """
        expect = Program([ConstDecl("o1", None, FuncCall("concat", [StringLiteral("\"good\""), StringLiteral("\"morning\"")]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 346))
    
    def test_47(self):
        input = """const minh30 = 1 + 2;"""
        expect = str(Program([ConstDecl("minh30",None, BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))
    
    def test_48(self):
        input = """const minh30 = -5;"""
        expect = str(Program([ConstDecl("minh30",None, UnaryOp("-", IntLiteral(5)))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))
    
    def test_49(self):
        input = """const minh30 = MINH();"""
        expect = str(Program([ConstDecl("minh30",None,FuncCall("MINH",[]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))
        
    def test_50(self):
        input = """const minh30 = MINH.deptrai();"""
        expect = str(Program([ConstDecl("minh30", None, MethCall(Id("MINH"), "deptrai", []))]))        
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))
        
    def test_51(self):
        input = """const minh30 = 2 + (3 - 5) > 3;"""
        expect = str(Program([ConstDecl("minh30",None,BinaryOp(">", BinaryOp("+", IntLiteral(2), BinaryOp("-", IntLiteral(3), IntLiteral(5))), IntLiteral(3)))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 351)) 
        
    def test_52(self):
        input = """const minh30 = "MINH";"""
        expect = str(Program([ConstDecl("minh30",None,StringLiteral("\"MINH\""))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 352)) 
        
    def test_53(self):
        input = """const minh30 = [3] int {1, 2, 3};"""
        expect = str(Program([ConstDecl("minh30",None,ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 353)) 
        
    def test_54(self):
        input = """const minh30 = [3][2][4] MINH {{{{{{{{{"minh30"}}}}}}}}};"""
        expect = str(Program([ConstDecl("minh30",None,ArrayLiteral([IntLiteral(3),IntLiteral(2),IntLiteral(4)],Id("MINH"),[[[[[[[[[StringLiteral("\"minh30\"")]]]]]]]]]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 354)) 
        
    def test_55(self):
        input = """const minh30 = MINH{dep: trai, hoc: bachkhoa};"""
        expect = str(Program([ConstDecl("minh30",None,StructLiteral("MINH",[("dep",Id("trai")),("hoc",Id("bachkhoa"))]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 355)) 
        
    def test_56(self):
        input = """const minh30 = [2][3][1] string {"minh", "30", ID{dep: "trai"}};"""
        expect = str(Program([ConstDecl("minh30",None,ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(1)],StringType(),[StringLiteral("\"minh\""),StringLiteral("\"30\""),StructLiteral("ID",[("dep",StringLiteral("\"trai\""))])]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))
    def test_57(self):
        input = """const minh30 = d || e && p || t && r || a && i;"""
        expect = str(Program([ConstDecl("minh30",None,BinaryOp("||", BinaryOp("||", BinaryOp("||", Id("d"), BinaryOp("&&", Id("e"), Id("p"))), BinaryOp("&&", Id("t"), Id("r"))), BinaryOp("&&", Id("a"), Id("i"))))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 357)) 
        
    def test_58(self):
        input = """const minh30 = call(minh.quang);"""
        expect = str(Program([ConstDecl("minh30",None,FuncCall("call",[FieldAccess(Id("minh"),"quang")]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 358)) 
        
    def test_59(self):
        input = """var MINH SAIDEPCHIEU = call(minh.quang);"""
        expect = str(Program([VarDecl("MINH",Id("SAIDEPCHIEU"),FuncCall("call",[FieldAccess(Id("minh"),"quang")]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))
    def test_060(self):
        input = """var MINH [3][2] int = 6 > 3 + 5 - 1 * (2 + call(a.b.c.d()));"""
        expect = str(Program([VarDecl("MINH",ArrayType([IntLiteral(3),IntLiteral(2)],IntType()),BinaryOp(">", IntLiteral(6), BinaryOp("-", BinaryOp("+", IntLiteral(3), IntLiteral(5)), BinaryOp("*", IntLiteral(1), BinaryOp("+", IntLiteral(2), FuncCall("call",[MethCall(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d",[])]))))))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 360)) 

    def test_061(self):
        input = """var MINH string = call(a(), b(), a.v.c.b(), 5+3-1-5);"""
        expect = str(Program([VarDecl("MINH",StringType(),FuncCall("call",[FuncCall("a",[]),FuncCall("b",[]),MethCall(FieldAccess(FieldAccess(Id("a"),"v"),"c"),"b",[]),BinaryOp("-", BinaryOp("-", BinaryOp("+", IntLiteral(5), IntLiteral(3)), IntLiteral(1)), IntLiteral(5))]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 361)) 

    def test_062(self):
        input = """var MINH deptrai = deptrai(ID{name: "hello", num: 6, hel: nil});"""
        expect = str(Program([VarDecl("MINH",Id("deptrai"),FuncCall("deptrai",[StructLiteral("ID",[("name",StringLiteral("\"hello\"")),("num",IntLiteral(6)),("hel",NilLiteral())])]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect,362)) 

    def test_063(self):
        input = """var MINH deptrai = ID{name: "hello", name: "world"}.b;"""
        expect = str(Program([VarDecl("MINH",Id("deptrai"),FieldAccess(StructLiteral("ID",[("name",StringLiteral("\"hello\"")),("name",StringLiteral("\"world\""))]),"b"))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 363)) 

    def test_064(self):
        input = """var MINH string = a([2]int{a}).b([2]int{a}).c([2]int{a}).d([2]int{a});"""
        expect = str(Program([VarDecl("MINH",StringType(),MethCall(MethCall(MethCall(FuncCall("a",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"b",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"c",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"d",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 364)) 

    def test_065(self):
        input = """var MINH string = call(a(b(c(d(e())))));"""
        expect = str(Program([VarDecl("MINH",StringType(),FuncCall("call",[FuncCall("a",[FuncCall("b",[FuncCall("c",[FuncCall("d",[FuncCall("e",[])])])])])]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 365)) 

    def test_066(self):
        input = """var MINH string;"""
        expect = str(Program([VarDecl("MINH",StringType(), None)]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 366)) 

    def test_067(self):
        input = """
        type MINH struct {
            a int;
        }
        """
        expect = str(Program([StructType("MINH",[("a",IntType())],[])]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    def test_068(self):
        input = """var MINH [3][2] int = 6 > 3 + 5 - 1 * (2 + call(a.b.c.d()));"""
        expect = str(Program([VarDecl("MINH",ArrayType([IntLiteral(3),IntLiteral(2)],IntType()),BinaryOp(">", IntLiteral(6), BinaryOp("-", BinaryOp("+", IntLiteral(3), IntLiteral(5)), BinaryOp("*", IntLiteral(1), BinaryOp("+", IntLiteral(2), FuncCall("call",[MethCall(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d",[])]))))))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 368)) 

    def test_069(self):
        input = """var MINH string = call(a(), b(), a.v.c.b(), 5+3-1-5);"""
        expect = str(Program([VarDecl("MINH",StringType(),FuncCall("call",[FuncCall("a",[]),FuncCall("b",[]),MethCall(FieldAccess(FieldAccess(Id("a"),"v"),"c"),"b",[]),BinaryOp("-", BinaryOp("-", BinaryOp("+", IntLiteral(5), IntLiteral(3)), IntLiteral(1)), IntLiteral(5))]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 369)) 

    def test_070(self):
        input = """var MINH deptrai = deptrai(ID{name: "hello", num: 6, hel: nil});"""
        expect = str(Program([VarDecl("MINH",Id("deptrai"),FuncCall("deptrai",[StructLiteral("ID",[("name",StringLiteral("\"hello\"")),("num",IntLiteral(6)),("hel",NilLiteral())])]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 370)) 

    def test_071(self):
        input = """var MINH deptrai = ID{name: "hello", name: "world"}.b;"""
        expect = str(Program([VarDecl("MINH",Id("deptrai"),FieldAccess(StructLiteral("ID",[("name",StringLiteral("\"hello\"")),("name",StringLiteral("\"world\""))]),"b"))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 371)) 

    def test_072(self):
        input = """var MINH string = a([2]int{a}).b([2]int{a}).c([2]int{a}).d([2]int{a});"""
        expect = str(Program([VarDecl("MINH",StringType(),MethCall(MethCall(MethCall(FuncCall("a",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"b",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"c",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"d",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 372)) 

    def test_073(self):
        input = """var MINH string = call(a(b(c(d(e())))));"""
        expect = str(Program([VarDecl("MINH",StringType(),FuncCall("call",[FuncCall("a",[FuncCall("b",[FuncCall("c",[FuncCall("d",[FuncCall("e",[])])])])])]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 373)) 

    def test_074(self):
        input = """var MINH string;"""
        expect = str(Program([VarDecl("MINH",StringType(), None)]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 374)) 

    def test_075(self):
        input = """
        type MINH struct {
            a int;
        }
        """
        expect = str(Program([StructType("MINH",[("a",IntType())],[])]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_076(self):
        input = """
        type MINH struct {
            a int;
            b string;
            c float;
            d [3][2]int;
            e tuanem;
        }
        """
        expect = str(Program([StructType("MINH",[("a",IntType()),("b",StringType()),("c",FloatType()),("d",ArrayType([IntLiteral(3),IntLiteral(2)],IntType())),("e",Id("tuanem"))],[])]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 376)) 

    def test_077(self):
        input = """
        type MINH interface {
            Add ();
        }
        """
        expect = str(Program([InterfaceType("MINH",[Prototype("Add",[],VoidType())])]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 377)) 

    def test_078(self):
        input = """
        type MINH interface {
            Add (x int, y float, c string);
            Sub (x, y int);
        }
        """
        expect = str(Program([InterfaceType("MINH",[Prototype("Add",[IntType(),FloatType(),StringType()],VoidType()),Prototype("Sub",[IntType(),IntType()],VoidType())])]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 378)) 

    def test_079(self):
        input = """
        type MINH interface {
            Add (x int, y float, c string);
            Sub (x, y int);
            Mul (x, y, z float, d string) string;
            Div () [3][2]int;
            test () hack; 
        }
        """
        expect = str(Program([InterfaceType("MINH",[Prototype("Add",[IntType(),FloatType(),StringType()],VoidType()),Prototype("Sub",[IntType(),IntType()],VoidType()),Prototype("Mul",[FloatType(),FloatType(),FloatType(),StringType()],StringType()),Prototype("Div",[],ArrayType([IntLiteral(3),IntLiteral(2)],IntType())),Prototype("test",[],Id("hack"))])]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 379)) 

    def test_080(self):
        input = """
        func MINH(){
            var b int;
            const PI = 3.14;
        }
        """
        expect = str(Program([FuncDecl("MINH",[],VoidType(),Block([VarDecl("b",IntType(), None),ConstDecl("PI",None,FloatLiteral(3.14))]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 380)) 

    def test_081(self):
        input = """
        func MINH(){
            var b int;
            const PI = 3.14;
            const minh30 = MINH.deptrai();
            var MINH string = call(a(b(c(d(e())))));
            var MINH string = a([2]int{a}).b([2]int{a}).c([2]int{a}).d([2]int{a});
            const minh30 = [3][2][4] MINH {{{{{{{{{"minh30"}}}}}}}}};
        }
        """
        expect = str(Program([FuncDecl("MINH",[],VoidType(),Block([VarDecl("b",IntType(), None),ConstDecl("PI",None,FloatLiteral(3.14)),ConstDecl("minh30",None,MethCall(Id("MINH"),"deptrai",[])),VarDecl("MINH",StringType(),FuncCall("call",[FuncCall("a",[FuncCall("b",[FuncCall("c",[FuncCall("d",[FuncCall("e",[])])])])])])),VarDecl("MINH",StringType(),MethCall(MethCall(MethCall(FuncCall("a",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"b",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"c",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])]),"d",[ArrayLiteral([IntLiteral(2)],IntType(),[Id("a")])])),ConstDecl("minh30",None,ArrayLiteral([IntLiteral(3),IntLiteral(2),IntLiteral(4)],Id("MINH"),[[[[[[[[[StringLiteral("\"minh30\"")]]]]]]]]]))]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 381)) 

    def test_082(self):
        input = """
        func MINH(){
            continue;
            break;
            return;
        }
        """
        expect = str(Program([FuncDecl("MINH",[],VoidType(),Block([Continue(),Break(),Return(None)]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 382)) 

    def test_083(self):
        input = """
        func MINH(){
            continue;
            break;
            return;
        }
        """
        expect = str(Program([FuncDecl("MINH",[],VoidType(),Block([Continue(),Break(),Return(None)]))]))      
        self.assertTrue(TestAST.checkASTGen(input, expect, 383)) 
    def test_084(self):
        input = """
        func foo() {
            for a.b.c.d.e.f.g.h.j[ID{b: ID{} }].d(){
                for a.b.c.d.e.f.g.h.j[ID{b: ID{} }].d(){
                    for a.b.c.d.e.f.g.h.j[ID{b: ID{} }].d(){
                        for a.b.c.d.e.f.g.h.j[ID{b: ID{} }].d(){
                            for a.b.c.d.e.f.g.h.j[ID{b: ID{} }].d(){
                                a[1][2][3][4][5][6] := 1;
                            }
                        }
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(MethCall(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"f"),"g"),"h"),"j"),[StructLiteral("ID",[("b",StructLiteral("ID",[]))])]),"d",[]),Block([ForBasic(MethCall(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"f"),"g"),"h"),"j"),[StructLiteral("ID",[("b",StructLiteral("ID",[]))])]),"d",[]),Block([ForBasic(MethCall(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"f"),"g"),"h"),"j"),[StructLiteral("ID",[("b",StructLiteral("ID",[]))])]),"d",[]),Block([ForBasic(MethCall(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"f"),"g"),"h"),"j"),[StructLiteral("ID",[("b",StructLiteral("ID",[]))])]),"d",[]),Block([ForBasic(MethCall(ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"),"f"),"g"),"h"),"j"),[StructLiteral("ID",[("b",StructLiteral("ID",[]))])]),"d",[]),Block([Assign(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)]),IntLiteral(1))]))]))]))]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))
        
    def test_085(self):
        input = """
        func printMatrix(rows int, cols int) {
            for i := 0; i < rows; i += 1 {
                for j := 0; j < cols; j += 1 {
                    print(i * cols + j);
                }
            }
        }
        """
        expect = str(Program([FuncDecl("printMatrix",[ParamDecl("rows",IntType()),ParamDecl("cols",IntType())],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<", Id("i"), Id("rows")),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Block([ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<", Id("j"), Id("cols")),Assign(Id("j"),BinaryOp("+", Id("j"), IntLiteral(1))),Block([FuncCall("print",[BinaryOp("+", BinaryOp("*", Id("i"), Id("cols")), Id("j"))])]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect,385 ))
        
    def test_086(self):
        input = """
        func foo() {
            const a = 3.14e10;
            const b = 3.14e10;
            execute(foo(execute(foot())))
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("a",None,FloatLiteral("3.14e10")),ConstDecl("b",None,FloatLiteral("3.14e10")),FuncCall("execute",[FuncCall("foo",[FuncCall("execute",[FuncCall("foot",[])])])])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))
        
    def test_087(self):
        input = """
        
        func quickSort(arr [10]int, left int, right int) {
            if (left >= right) {return;}
            var pivot = arr[(left + right) / 2];
            var i = left;
            var j = right;
            for i <= j {
                for arr[i] < pivot {i += 1;}
                for arr[j] > pivot {j -= 1;}
                if (i <= j) {
                    var temp = arr[i];
                    arr[i] := arr[j];
                    arr[j] := temp;
                    i += 1;
                    j -= 1;
                }
            }
            quickSort(arr, left, j);
            quickSort(arr, i, right);
        }
        """
        expect = str(Program([FuncDecl("quickSort",[ParamDecl("arr",ArrayType([IntLiteral(10)],IntType())),ParamDecl("left",IntType()),ParamDecl("right",IntType())],VoidType(),Block([If(BinaryOp(">=", Id("left"), Id("right")), Block([Return(None)]), None),VarDecl("pivot", None,ArrayCell(Id("arr"),[BinaryOp("/", BinaryOp("+", Id("left"), Id("right")), IntLiteral(2))])),VarDecl("i", None,Id("left")),VarDecl("j", None,Id("right")),ForBasic(BinaryOp("<=", Id("i"), Id("j")),Block([ForBasic(BinaryOp("<", ArrayCell(Id("arr"),[Id("i")]), Id("pivot")),Block([Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1)))])),ForBasic(BinaryOp(">", ArrayCell(Id("arr"),[Id("j")]), Id("pivot")),Block([Assign(Id("j"),BinaryOp("-", Id("j"), IntLiteral(1)))])),If(BinaryOp("<=", Id("i"), Id("j")), Block([VarDecl("temp", None,ArrayCell(Id("arr"),[Id("i")])),Assign(ArrayCell(Id("arr"),[Id("i")]),ArrayCell(Id("arr"),[Id("j")])),Assign(ArrayCell(Id("arr"),[Id("j")]),Id("temp")),Assign(Id("i"),BinaryOp("+", Id("i"), IntLiteral(1))),Assign(Id("j"),BinaryOp("-", Id("j"), IntLiteral(1)))]), None)])),FuncCall("quickSort",[Id("arr"),Id("left"),Id("j")]),FuncCall("quickSort",[Id("arr"),Id("i"),Id("right")])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))
        
    def test_088(self):
        input = """
        func foo() {
            a[a[a[a[a[a[a[a[1]]]]]]]].d.k.e.c(c(c(c(c(c(c(c(c(c(c(c(c(c(c(c(c(C(c(c())))))))))))))))))));
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([MethCall(FieldAccess(FieldAccess(FieldAccess(ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(1)])])])])])])])]),"d"),"k"),"e"),"c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("C",[FuncCall("c",[FuncCall("c",[])])])])])])])])])])])])])])])])])])])])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))
        
    def test_089(self):
        input = """
        func foo() {
            break;
            continue;
            break;
            for i < 10{
                for i < 10{
                    for a[a[a[a[a[a[a[a[1]]]]]]]].d.k.e.c(c(c(c(c(c(c(c(c(c(c(c(c(c(c(c(c(C(c(c()))))))))))))))))))){
                        return new;
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([Break(),Continue(),Break(),ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(10)),Block([ForBasic(MethCall(FieldAccess(FieldAccess(FieldAccess(ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[IntLiteral(1)])])])])])])])]),"d"),"k"),"e"),"c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("c",[FuncCall("C",[FuncCall("c",[FuncCall("c",[])])])])])])])])])])])])])])])])])])])]),Block([Return(Id("new"))]))]))]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))
        
    def test_090(self):
        input = """
        func test(){
            for index, value := range array {
                x.append(value)
            }   
        };"""
        expect = str(Program([FuncDecl("test",[],VoidType(),Block([ForEach(Id("index"),Id("value"),Id("array"),Block([MethCall(Id("x"),"append",[Id("value")])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))
        
    def test_091(self):
        input = """
        func foo() {
            var x string = "MINH";
            var y int = 6;
            var z = 0.5;
            const x = 3.15;
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("x",StringType(),StringLiteral("\"MINH\"")),VarDecl("y",IntType(),IntLiteral(6)),VarDecl("z", None,FloatLiteral(0.5)),ConstDecl("x",None,FloatLiteral(3.15))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))
        
    def test_092(self):
        input = """
        func foo() {
            x.y.z.b.d.s.e.gv.as.sa.sfas.saga.asg.b(a[d(c[a(b[d(x)])])]);
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([MethCall(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("x"),"y"),"z"),"b"),"d"),"s"),"e"),"gv"),"as"),"sa"),"sfas"),"saga"),"asg"),"b",[ArrayCell(Id("a"),[FuncCall("d",[ArrayCell(Id("c"),[FuncCall("a",[ArrayCell(Id("b"),[FuncCall("d",[Id("x")])])])])])])])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))
        
    def test_093(self):
        input = """
        func foo() {
           const b = 5;
           const b = 5;
           const b = 5;
           const b = 5;
           const b = 5;
           const b = 5;
           print(b, b, b)
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),FuncCall("print",[Id("b"),Id("b"),Id("b")])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))
        
    def test_94(self):
        input = """
        func foo() {
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))
    def test_095(self):
        input = """const chainCall = chainCall( chain(foo(1,2), bar(3,4), baz(5,6)) ); """
        expect = Program([ConstDecl("chainCall", None, FuncCall("chainCall", [FuncCall("chain", [FuncCall("foo", [IntLiteral(1), IntLiteral(2)]), FuncCall("bar", [IntLiteral(3), IntLiteral(4)]), FuncCall("baz", [IntLiteral(5), IntLiteral(6)])])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 395))

    def test_096(self):
        input = """const logicChain = logicChain( (a && b) || (c && d) ); """
        expect = Program([ConstDecl("logicChain", None, FuncCall("logicChain", [BinaryOp("||", BinaryOp("&&", Id("a"), Id("b")), BinaryOp("&&", Id("c"), Id("d")))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 396))

    def test_097(self):
        input = """const nestArith2 = nestArith2( a - (b + (c * d)) ); """
        expect = Program([ConstDecl("nestArith2", None, FuncCall("nestArith2", [BinaryOp("-", Id("a"), BinaryOp("+", Id("b"), BinaryOp("*", Id("c"), Id("d"))))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 397))

    def test_098(self):
        input = """const funcMix = funcMix( mix( foo(1), bar(2.2), baz(true) ) ); """
        expect = Program([ConstDecl("funcMix", None, FuncCall("funcMix", [FuncCall("mix", [FuncCall("foo", [IntLiteral(1)]), FuncCall("bar", [FloatLiteral(2.2)]), FuncCall("baz", [BooleanLiteral(True)])])]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 398))
    def test_099(self):
        input = """
        func foo() {
           const b = 5;
           const b = 5;
           const b = 5;
           const b = 5;
           const b = 5;
           const b = 5;
           print(b, b, b)
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),ConstDecl("b",None,IntLiteral(5)),FuncCall("print",[Id("b"),Id("b"),Id("b")])]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))
        
    def test_100(self):
        input = """
        func foo() {
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
            for i < 5{
                print(i)
            }
        }
        """
        expect = str(Program([FuncDecl("foo",[],VoidType(),Block([ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])])),ForBasic(BinaryOp("<", Id("i"), IntLiteral(5)),Block([FuncCall("print",[Id("i")])]))]))
		]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))
    


