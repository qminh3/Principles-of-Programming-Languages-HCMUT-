import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared(self):
        input = """var a int; var b int; var a int = a; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_type_mismatch(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_s(self):
        input = """var a int; const a = 12; """
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_func(self):
        input = """func a(a,b int) int { var a int = a; }; """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_func2(self):
        input = """func a(b int) int { var a int = c; }; """
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_func3(self):
        input = """func a(b int, c float) int { var a float = b; }; """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_func4(self):
        input = """func a(b int, c float) int { var a int = c; }; """
        expect = "Type Mismatch: VarDecl(a,IntType,Id(c))\n"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_408(self):
        input = """func a(b int, c float) int { var a int = 1 + 2;}; """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_409(self):
        input = """func a(b int, c float) int { var a int = 1 + b*2 + 2.2;}; """
        expect = "Type Mismatch: VarDecl(a,IntType,BinaryOp(BinaryOp(IntLiteral(1),+,BinaryOp(Id(b),*,IntLiteral(2))),+,FloatLiteral(2.2)))\n"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_410(self):
        input = """func a(b int, c float) int { var a float = 1.7;}; """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_411(self):
        input = """var getInt int;"""
        expect = "Redeclared Variable: getInt\n"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_412(self):
        input = """var a int = 3; var b int = a*3+4/4;"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_413(self):
        input = """var a int = 3; var b int = a+3*1.0;"""
        expect = "Type Mismatch: VarDecl(b,IntType,BinaryOp(Id(a),+,BinaryOp(IntLiteral(3),*,FloatLiteral(1.0))))\n"
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_414(self):
        input = """var a float = 10.7; var b int = 10;"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_415(self):
        input = """ 
                    func m (a int) { var a int; m(a);};"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_416(self):
        input = """func main (a int) { 
            var a int = 3;
            if (a==5+2-4) {
                return;
            }
        
        };"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_417(self):
        input = """func main (a int) { 
            var a int = 3;
            if (3+2) {
                return ;
            }
        
        };"""
        expect = "Type Mismatch: If(BinaryOp(IntLiteral(3),+,IntLiteral(2)),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_418(self):
        input = """func main (a int) { 
            var a int = 3;
            if (a==3) {
                var b int;
                if (b==4){
                    var c = a+b;
                }
            }
        
        };"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_419(self):
        input = """
        var a = 3 ;  
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,419))
    def test_420(self):
        input = """
        var a = 3 ;  
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_421(self):
        input = """
        var a = 3 ;  
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_422(self):
        input = """
        var a = 3 ;  
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_423(self):
        input = """
                 type A interface {
                     Add(x, y int) int;
                     Subtract(a, b float, c int) float;
                     Reset()
                     test_boolean(a boolean) boolean
                     SayHello(name string) string
                 }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_424(self):
        input = """
                 type A interface {
                     Add(x, y int) int;
                     Subtract(a, b float, c int) float;
                     Add()
                     test_boolean(a boolean) boolean
                     SayHello(name string) string
                 }
                """
        expect = "Redeclared Prototype: Add\n"
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_425(self):
        input = """
                 type A struct {
                    a string
                    b float
                    c int
                 }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,425))  
    def test_426(self):
        input = """
                 type A struct {
                    a string
                    b float
                    c int
                    a int
                 }
                """
        expect = "Redeclared Field: a\n"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_427(self):
        input = Program([StructType("S1",[("v",IntType()),("t",IntType())],[]),VarDecl("a", None,StructLiteral("S1",[("v",IntLiteral(1)),("t",IntLiteral(2))])),VarDecl("b",Id("S1"),Id("a")),VarDecl("c",IntType(),Id("b"))])
        expect = "Type Mismatch: VarDecl(c,IntType,Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_428(self):
        input = Program([FuncDecl("foo",[],VoidType(),Block([VarDecl("array",ArrayType([IntLiteral(2),IntLiteral(3)],FloatType()), None),Assign(Id("index"),IntLiteral(1)),Assign(Id("value"),ArrayLiteral([IntLiteral(3)],FloatType(),[FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0)])),ForEach(Id("index"),Id("value"),Id("array"),Block([Assign(Id("value"),ArrayCell(Id("array"),[IntLiteral(0)])),Assign(Id("index"),IntLiteral(1)),VarDecl("index",IntType(), None),VarDecl("value",ArrayType([IntLiteral(3)],FloatType()), None)]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_429(self):
        input = Program([FuncDecl("Declra",[ParamDecl("a",IntType()),ParamDecl("a",IntType())],VoidType(),Block([Return(None)]))])
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_430(self):
        input = Program([FuncDecl("Declra",[ParamDecl("b",IntType())],VoidType(),Block([VarDecl("b", None,IntLiteral(1)),VarDecl("a", None,IntLiteral(1)),ConstDecl("a",None,IntLiteral(1))]))])
        
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,430)) 
    def test_431(self):
        input = Program([FuncDecl("Declra",[ParamDecl("b",IntType())],VoidType(),Block([ForStep(VarDecl("a", None,IntLiteral(1)),BinaryOp("<", Id("a"), IntLiteral(1)),Assign(Id("a"),BinaryOp("+", Id("a"), IntLiteral(1))),Block([ConstDecl("a",None,IntLiteral(2))]))]))])
        
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_432(self):
        input = Program([VarDecl("a", None,IntLiteral(1)),VarDecl("b", None,Id("a")),VarDecl("c", None,Id("d"))])
        
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_433(self):
        input = Program([FuncDecl("Declra",[],IntType(),Block([Return(IntLiteral(1))])),FuncDecl("foo",[],VoidType(),Block([VarDecl("b", None,FuncCall("Declra",[])),FuncCall("foo_abb",[]),Return(None)]))])
        
        expect = "Undeclared Function: foo_abb\n"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_434(self):
        input = Program([FuncDecl("Declas",[],VoidType(),Block([Return(None)])),VarDecl("Declas", None,IntLiteral(1))])
        expect = """Redeclared Variable: Declas\n"""
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_435(self):
        input = """
                type B struct {
                    a int
                 }
                 type C struct {
                    b B
                 }
                 type A struct {
                    a string
                    b B
                    c C
                    d boolean
                 }

                 var a A = A {a:"string",b: B { a: 3 },c: C { b: B { a: 3 }}};
                 var b A = a;
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_436(self):
        input = """
                type B struct {
                    a int
                 }
                 type C struct {
                    b B
                 }
                 type A struct {
                    a string
                    b B
                    c C
                    d boolean
                 }
                 var z int;
                 var a A = A {a:"string",b: B { a: 3 },c: C { b: B { a: 3 }}};
                 var b B = B {a:z};
                 var c A = A {b: b}
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_437(self):
        input = """
                type B struct {
                    a int
                 }
                 type C struct {
                    b B
                 }
                 type A struct {
                    a string
                    b B
                    c C
                    d boolean
                 }
                 var z int;
                 var a A = A {a:"string",b: B { a: 3 },c: C { b: B { a: 3 }}};
                 var b B = B {a:z};
                 var c A = b
                """
        expect = """Type Mismatch: VarDecl(c,Id(A),Id(b))\n"""
        self.assertTrue(TestChecker.test(input,expect,437))





    def test_438(self):
        input = """
                type Vehicle interface {
                    GetSpeed() int
                    SetSpeed(speed int)
                }
                type Car struct {
                    speed int
                }
                func (c Car) GetSpeed() int {
                    return 3
                }
                func (c Car) SetSpeed(speed int) {
                    var a = 12;
                }
                var a Vehicle = Car { speed: 10};
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_439(self):
        input = """
                type Vehicle interface {
                    GetSpeed() int
                    SetSpeed(speed int)
                }
                type Car struct {
                    speed int
                }
                func (c Car) GetSpeed() int {
                    return 3
                }
                var a Vehicle = Car { speed: 10};
                """
        expect = """Type Mismatch: VarDecl(a,Id(Vehicle),StructLiteral(Car,[(speed,IntLiteral(10))]))\n"""
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_440(self):
        input = """
                type Vehicle interface {
                    GetSpeed() int
                    SetSpeed(speed int)
                }
                type Car struct {
                    speed int
                }
                func (c Car) GetSpeed() int {
                    return 3
                }
                func (c Car) SetSpeed(speed int) {
                    var a = 12;
                }
                var a Vehicle = Car { speed: 10};
                a.SetSpeed(10);
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_441(self):
        input = Program([VarDecl("getInt", None,IntLiteral(1))])
        expect = "Redeclared Variable: getInt\n"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_442(self):
        input = Program([VarDecl("getInt", None,IntLiteral(1)),VarDecl("getInt", None,IntLiteral(1))])
        expect = "Redeclared Variable: getInt\n"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_443(self):
        input = Program([
        StructType("A", [("x", IntType())], []),
        StructType("B", [("x", StringType()), ("y", IntType()), ("y", FloatType())], [])
    ])
        expect = "Redeclared Field: y\n"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_444(self):
        input = Program([
        MethodDecl("v", Id("A"), FuncDecl("f1", [], VoidType(), Block([Return(None)]))),
        MethodDecl("v", Id("A"), FuncDecl("f2", [], VoidType(), Block([Return(None)]))),
        MethodDecl("v", Id("A"), FuncDecl("f2", [], VoidType(), Block([Return(None)]))),
        StructType("A", [("x", IntType())], [])
    ])
        expect = "Redeclared Method: f2\n"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_445(self):
        input = Program([
        InterfaceType("I", [
            Prototype("m", [], VoidType()),
            Prototype("m", [IntType()], VoidType())
        ])
    ])
        expect = "Redeclared Prototype: m\n"
        self.assertTrue(TestChecker.test(input,expect,445))
    def test_446(self):
        input = Program([
            FuncDecl("foo", [ParamDecl("x", IntType())], VoidType(), Block([
                VarDecl("x", None, IntLiteral(1)),
                VarDecl("y", None, IntLiteral(1)),
                ConstDecl("y", None, IntLiteral(1))
            ]))
        ])
        expect = "Redeclared Constant: y\n"
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test_447(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("s", Id("A"), FuncDecl("get", [], VoidType(), Block([
                ConstDecl("c", None, FieldAccess(Id("s"), "x")),
                VarDecl("d", None, FieldAccess(Id("s"), "y"))  # 'y' không tồn tại
            ])))
        ])
        expect = "Undeclared Field: y\n"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("s", Id("A"), FuncDecl("get", [], VoidType(), Block([
                MethCall(Id("s"), "get", []),
                MethCall(Id("s"), "print", [])  # 'print' không tồn tại
            ])))
        ])
        expect = "Undeclared Method: print\n"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            StructType("A", [("y", IntType())], [])
        ])
        expect = "Redeclared Type: A\n"
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_450(self):
        input = Program([
            InterfaceType("I", [Prototype("foo", [], VoidType())]),
            InterfaceType("I", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: I\n"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = Program([
            StructType("A", [("a", IntType())], []),
            StructType("B", [("a", IntType())], []),
            InterfaceType("A", [Prototype("foo", [], VoidType())])
        ])
        expect = "Redeclared Type: A\n"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = Program([
            FuncDecl("putInt", [], VoidType(), Block([Return(None)]))  # built-in bị override
        ])
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("x", Id("A"), FuncDecl("foo", [ParamDecl("x", IntType())], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [], VoidType(), Block([Return(None)]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_454(self):
        input = Program([
            MethodDecl("s", Id("A"), FuncDecl("foo", [
                ParamDecl("a", IntType()), ParamDecl("b", IntType())
            ], VoidType(), Block([
                VarDecl("a", None, IntLiteral(1))  
            ]))),
            StructType("A", [("x", IntType())], []),
            StructType("B", [("x", IntType())], []),
            MethodDecl("s", Id("B"), FuncDecl("foo", [
                ParamDecl("a", IntType()), ParamDecl("b", IntType())
            ], VoidType(), Block([
                VarDecl("a", None, IntLiteral(1))  
            ])))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))    
    def test_455(self):
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("a", None, IntLiteral(1)),
                ForEach(Id("a"), Id("b"),
                        ArrayLiteral([IntLiteral(3)], IntType(), [
                            IntLiteral(1), IntLiteral(2), IntLiteral(3)
                        ]),
                        Block([
                            VarDecl("b", None, IntLiteral(1))  
                        ])
                )
            ]))
        ])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_456(self):
        input = Program([
            VarDecl("x", None, FuncCall("foo", [])),
            FuncDecl("foo", [], IntType(), Block([
                VarDecl("a", None, FuncCall("bar", [])),
                VarDecl("c", None, FuncCall("getInt", [])),
                FuncCall("putInt", [Id("c")]),
                FuncCall("putIntLn", [Id("c")]),
                Return(IntLiteral(1))
            ])),
            VarDecl("d", None, FuncCall("foo", [])),
            FuncDecl("bar", [], IntType(), Block([
                VarDecl("a", None, FuncCall("foo", [])),
                Return(IntLiteral(1))
            ]))
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_457(self):
        input = Program([
            VarDecl("x", None, Id("y")),
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("b", None, IntLiteral(1)),
                ForEach(Id("x"), Id("z"),
                        ArrayLiteral([IntLiteral(3)], IntType(), [
                            IntLiteral(1), IntLiteral(2), IntLiteral(3)
                        ]),
                        Block([VarDecl("y", None, Id("z"))])
                ),
                VarDecl("y", None, Id("x")),
                VarDecl("x", None, IntLiteral(1))
            ])),
            VarDecl("y", None, Id("x"))
        ])
        expect = "Undeclared Identifier: y\n"
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test_458(self):
        input = Program([
            VarDecl("A", None, IntLiteral(1)),
            StructType("A", [("a", IntType())], [])
        ])
        expect = "Redeclared Type: A\n"
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test_459(self):
        input = Program([
            InterfaceType("A", [Prototype("foo", [], VoidType())]),
            ConstDecl("A", None, IntLiteral(2))
        ])
        expect = "Redeclared Constant: A\n"
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_460(self):
        input = Program([
            StructType("A", [("x", IntType())], []),
            MethodDecl("s", Id("A"), FuncDecl("foo", [ParamDecl("x", IntType())], VoidType(), Block([Return(None)]))),
            FuncDecl("foo", [], VoidType(), Block([Return(None)]))
        ])
        expect = ""  
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test_461(self):
        input = Program([
            ConstDecl("a", None, IntLiteral(2)),
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("a", None, IntLiteral(1)),
                ForStep(VarDecl("a", None, IntLiteral(1)), BinaryOp("<", Id("a"), IntLiteral(1)), Assign(Id("b"), IntLiteral(2)), Block([
                    ConstDecl("b", None, IntLiteral(1))
                ]))
            ]))
        ])
        expect = "Redeclared Constant: b\n"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = Program([
            VarDecl("v", FloatType(), IntLiteral(1))
        ])
        expect = ""  
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = Program([
            VarDecl("v", Id("A"), None),
            ConstDecl("b", None, MethCall(Id("v"), "foo", [])),
            StructType("A", [("a", IntType())], []),
            MethodDecl("v", Id("A"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))),
            MethodDecl("v", Id("A"), FuncDecl("koo", [], IntType(), Block([Return(IntLiteral(1))]))),
            ConstDecl("c", None, MethCall(Id("v"), "koo", [])),
            ConstDecl("d", None, MethCall(Id("v"), "zoo", []))
        ])
        expect = "Undeclared Method: zoo\n"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = Program([
            VarDecl("v", Id("A"), None),
            StructType("A", [("a", IntType())], []),
            InterfaceType("I", [Prototype("foo", [], IntType())]),
            MethodDecl("v", Id("A"), FuncDecl("foo", [], IntType(), Block([Return(IntLiteral(1))]))),
            MethodDecl("v", Id("A"), FuncDecl("koo", [], VoidType(), Block([
                MethCall(Id("v"), "koo", [])
            ]))),
            FuncDecl("test", [], VoidType(), Block([
                VarDecl("x", Id("I"), None),
                ConstDecl("b", None, MethCall(Id("x"), "foo", [])),
                MethCall(Id("x"), "koo", [])
            ]))
        ])
        expect = "Undeclared Method: koo\n"
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test_465(self):
        input = """
                type People interface {
                    GetName() string
                }
                type Student struct {
                    name string
                    age int
                }
                func (s Student) GetName() string {
                    return "s.name"
                }
                type Car struct {
                    speed int
                    name string
                    driver Student
                }
                type Abc struct {
                    age int
                }
                func getDriver(c Car) Student {
                    return c.driver
                }
                func main () {

                    var c = Car{speed:100,name:"abc",driver:Student{ age:20 }}
                    var d = getDriver(c.driver)
                    var z string = d.name+"OK";
                    var t int = d.age*2+4;
                    return;
                }
                """
        expect = """Type Mismatch: FuncCall(getDriver,[FieldAccess(Id(c),driver)])\n"""
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_466(self):
        input = """
                type People interface {
                    GetName() string
                }
                type Student struct {
                    name string
                    age int
                }
                func (s Student) GetName() string {
                    return "s.name"
                }
                type Car struct {
                    speed int
                    name string
                    driver Student
                }
                type Abc struct {
                    age int
                }
                func getDriver(c Car) Student {
                    return c.driver
                }
                func main () {

                    var c = Car{speed:100,name:"abc",driver:Student{ age:20 }}
                    var d = getDriver(c.driver)
                    var z string = d.name+"OK";
                    var t int = d.age*2+4;
                    return;
                }
                """
        expect = """Type Mismatch: FuncCall(getDriver,[FieldAccess(Id(c),driver)])\n"""
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_467(self):
        input = """
                type People interface {
                    GetName() string
                }
                type Student struct {
                    name string
                    age int
                }
                func (s Student) GetName() string {
                    return "s.name"
                }
                type Car struct {
                    speed int
                    name string
                    driver Student
                }
                type Abc struct {
                    age int
                }
                func (c Car) getDriver() Student {
                    return Student { name: "s.name" };
                }
                func main () {

                    var c = Car{speed:100,name:"abc",driver:Student{ age:20 }}
                    c.getDriver()                    
                    return;
                }
                """
        expect = """Type Mismatch: MethodCall(Id(c),getDriver,[])\n"""
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_468(self):
        input = """
                type People interface {
                    GetName() string
                }
                type Student struct {
                    name string
                    age int
                }
                func (s Student) GetName() string {
                    return "s.name"
                }
                type Car struct {
                    speed int
                    name string
                    driver Student
                }
                type Abc struct {
                    age int
                }
                func (c Car) getDriver() Student {
                    return Student { name: "s.name" };
                }
                func main () {

                    var c = Car{speed:100,name:"abc",driver:Student{ age:20 }}
                    var a int ;
                    a.getDriver()                    
                    return;
                }
                """
        expect = """Type Mismatch: MethodCall(Id(a),getDriver,[])\n"""
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_469(self):
        input = """
                type People interface {
                    GetName() string
                }
                type Student struct {
                    name string
                    age int
                }
                func (s Student) GetName() string {
                    return s.name
                }
                func (s Student) getDriver(a int) Student {
                    return Student { name: "s.name" };
                }
                type Car struct {
                    speed int
                    name string
                    driver Student
                }
                type Abc struct {
                    age int
                }
                func (c Car) getDriver() Student {
                    return Student { name: "s.name" };
                }
                func main () {

                    var c = Car{speed:100,name:"abc",driver:Student{ age:20 }}
                    var d = Student { name: "s.name" };
                    d.getDriver()                    
                    return;
                }
                """
        expect = """Type Mismatch: MethodCall(Id(d),getDriver,[])\n"""
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_470(self):
        input = """
                type People interface {
                    GetName() string
                }
                type Student struct {
                    name string
                    age int
                }
                func (s Student) GetName() string {
                    return s.name
                }
                func (s Student) getDriver(a int) Student {
                    return Student { name: "s.name" };
                }
                type Car struct {
                    speed int
                    name string
                    driver Student
                }
                type Abc struct {
                    age int
                }
                func (c Car) getDriver() Student {
                    return Student { name: "s.name" };
                }
                func main () {

                    var c = Car{speed:100,name:"abc",driver:Student{ age:20 }}
                    var d = Student { name: "s.name" };
                    d.doSomething()                    
                    return;
                }
                """
        expect = """Undeclared Method: doSomething\n"""
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_471(self):
        input = Program([
            ConstDecl("a", None, IntLiteral(3)),
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("a", None, IntLiteral(2)),
                ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)), Block([
                    ConstDecl("a", None, IntLiteral(1)),
                    ForBasic(BinaryOp("<", Id("a"), IntLiteral(1)), Block([
                        ConstDecl("a", None, IntLiteral(0)),
                        ConstDecl("b", None, IntLiteral(1))
                    ])),
                    ConstDecl("b", None, IntLiteral(1)),
                    VarDecl("a", None, IntLiteral(1))
                ]))
            ]))
        ])
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("a", None, IntLiteral(1)),
                ForEach(Id("a"), Id("b"),
                    ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                    Block([VarDecl("b", None, IntLiteral(1))])
                )
            ]))
        ])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("b", None, IntLiteral(1)),
                ForEach(Id("a"), Id("b"),
                    ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                    Block([VarDecl("d", None, Id("b"))])
                ),
                VarDecl("d", None, Id("b")),
                VarDecl("a", None, IntLiteral(1))
            ])),
            VarDecl("d", None, Id("a"))
        ])
        expect = ""  
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("b", None, IntLiteral(1)),
                ForEach(Id("a"), Id("c"),
                    ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                    Block([VarDecl("d", None, Id("e"))])
                ),
                VarDecl("d", None, Id("b")),
                VarDecl("a", None, IntLiteral(1))
            ])),
            VarDecl("d", None, Id("a"))
        ])
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = Program([
            VarDecl("a", None, IntLiteral(1)),
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("b", None, IntLiteral(1)),
                ForEach(Id("a"), Id("c"),
                    ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                    Block([VarDecl("d", None, Id("c"))])
                ),
                VarDecl("d", None, Id("c")),
                VarDecl("z", None, Id("c")),
                VarDecl("a", None, IntLiteral(1))
            ])),
            VarDecl("d", None, Id("a"))
        ])
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = Program([
            VarDecl("a", None, Id("d")),
            FuncDecl("foo", [], VoidType(), Block([
                ConstDecl("b", None, IntLiteral(1)),
                ForEach(Id("a"), Id("c"),
                    ArrayLiteral([IntLiteral(3)], IntType(), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]),
                    Block([VarDecl("d", None, Id("c"))])
                ),
                VarDecl("d", None, Id("a")),
                VarDecl("a", None, IntLiteral(1))
            ])),
            VarDecl("d", None, Id("a"))
        ])
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = Program([
            VarDecl("a", None, FuncCall("foo", [])),
            FuncDecl("foo", [], IntType(), Block([
                VarDecl("a", None, FuncCall("koo", [])),
                VarDecl("c", None, FuncCall("getInt", [])),
                FuncCall("putInt", [Id("c")]),
                FuncCall("putIntLn", [Id("c")]),
                Return(IntLiteral(1))
            ])),
            VarDecl("d", None, FuncCall("foo", [])),
            FuncDecl("koo", [], IntType(), Block([
                VarDecl("a", None, FuncCall("foo", [])),
                Return(IntLiteral(1))
            ]))
        ])
        expect = ""  
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test_478(self):
        input = """     
                var a = 1;
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_479(self):
        input = """     
                func main () {
                    putInt(1);
                    putIntLn(2);
                    putFloat(3.0);
                    
                }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_480(self):
        input = """     
                type Student struct {
                    name string
                    age int
                }
                func (s Student) getName() string {
                    return s.name
                }
                func main () {
                    var s = Student { name: "s.name" };
                    s.getName();
                }
                """
        expect = """Type Mismatch: MethodCall(Id(s),getName,[])\n"""
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_481(self):
        input = """     
                type Student struct {
                    name string
                    age int
                }
                func (s Student) getName() {
                    return 
                }
                func main () {
                    var s = Student { name: "s.name" };
                    s.getName();
                }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,481))
    def test_482(self):
        input = Program([
            FuncDecl("foo", [], VoidType(), Block([
                VarDecl("v", IntType(), None),
                ConstDecl("x", None, Id("v")),
                VarDecl("k", FloatType(), Id("x")),
                VarDecl("y", BoolType(), Id("x"))
            ]))
        ])
        expect = "Type Mismatch: VarDecl(y,BoolType,Id(x))\n"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = Program([
            StructType("A", [("v", IntType())], []),
            VarDecl("v", Id("A"), None),
            FuncDecl("foo", [], VoidType(), Block([
                ForBasic(IntLiteral(1), Block([
                    VarDecl("a", IntType(), FloatLiteral(1.2))
                ]))
            ]))
        ])
        expect = "Type Mismatch: For(IntLiteral(1),Block([VarDecl(a,IntType,FloatLiteral(1.2))]))\n"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = Program([
            VarDecl("a", ArrayType([IntLiteral(2), IntLiteral(3)], IntType()), None),
            VarDecl("b", None, ArrayCell(Id("a"), [IntLiteral(1)])),
            VarDecl("c", ArrayType([IntLiteral(2)], IntType()), Id("b")),
            VarDecl("d", ArrayType([IntLiteral(1)], StringType()), Id("b"))
        ])
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(2)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = Program([
            VarDecl("a", IntType(), BinaryOp("%", IntLiteral(1), IntLiteral(2))),
            VarDecl("b", IntType(), BinaryOp("%", IntLiteral(1), FloatLiteral(2.0)))
        ])
        expect = "Type Mismatch: BinaryOp(IntLiteral(1),%,FloatLiteral(2.0))\n"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = Program([
            FuncDecl("foo", [], IntType(), Block([
                Return(IntLiteral(1))
            ])),
            FuncDecl("bar", [], IntType(), Block([
                Return(FuncCall("bar", [])),
                FuncCall("foo", [])
            ]))
        ])
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 486))
    def test_487(self):
        input = """     
                func create() [3] int {
                    var a [3] int;
                    return a
                }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_488(self):
        input = """     
                func create()  int {
                    const c = 3;
                    
                    return c
                }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_489(self):
        input = """
                var a = [3][4] boolean { {true,false,true},{false,true,false},{true,false,true}}
                var b = [3][4] float { {1.1,2.2,3.34},{4.4,5.5,6.6},{7.7,8.8,9.9}}
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_490(self):
        input = """
                var a [3] int = [3] int {7,2,3}
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,490))
    def test_491(self):
        input = """
                var a [3] int = [3] int {7,2,3}
                var b [3] int = a
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,491))
    def test_492(self):
        input = """
                var a [3] int = [3] int {7,2,3}
                var b [3] int = a
                var c [3] int = b
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_493(self):
        input = """
                var c =  6/2 + 3 - 1*2;
                
                """
        
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_494(self):
        input = """
                var a = 1;
                var b = 2;
                var c = 3;
                var d = a + b * c - 1 / 2;
                
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,494))
    def test_495(self):
        input = """
                func main () {
                    for (true) {
                        return
                    }
                }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_496(self):
        input = """
                func main () {
                    var a boolean
                    for (a) {
                        return
                    }
                }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_497(self):
        input = Program([VarDecl("v",IntType(),FloatLiteral(1.2))])
        expect = "Type Mismatch: VarDecl(v,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_498(self):
        input = Program([VarDecl("a", None,ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)])),VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("a"))])
        expect = "Type Mismatch: VarDecl(c,ArrayType(IntType,[IntLiteral(3)]),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_499(self):
        
        """
var a [2][3] int;
var b = a[1];
var c [3] int = b;
var d [3] string = b;
        """
        input = Program([
            VarDecl("a",ArrayType([IntLiteral(2),IntLiteral(3)],IntType()), None),
            VarDecl("b", None,ArrayCell(Id("a"),[IntLiteral(1)])),
            VarDecl("c",ArrayType([IntLiteral(3)],IntType()),Id("b")),
            VarDecl("d",ArrayType([IntLiteral(3)],StringType()),Id("b"))])
        expect = "Type Mismatch: VarDecl(d,ArrayType(StringType,[IntLiteral(3)]),Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect,499))
   