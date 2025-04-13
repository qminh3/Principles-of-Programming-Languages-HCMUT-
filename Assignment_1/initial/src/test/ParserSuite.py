import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """var a int = 100;
        var b float = 2.718;
        var c string = "world";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_202(self):

        input = """type Circle struct {
            radius float;
            color string;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_203(self):

        input = """    
            func Add(x int, y [2]int) [2]id {return ;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_204(self):
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_205(self):
        input = "const Minh = [5][0]string{1, \"string\"};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_206(self):
        input = "const Minh = Person{name: \"Alice\", age: 30};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_207(self):
        input = "const Minh = 1 || 2 && c + 3 / 2 - -1;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_208(self):
        input = "const Minh = 1[2] + foo()[2] + ID[2].b.b;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_209(self):       
        input = "const Minh = ca.he(132) + b.d[2];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_210(self):
        input = """
            var x int = go() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_211(self):
        input = """
            const Minh = b.c() + 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_212(self):
        input = """
            func Minh(x int, y int) int {return;}
            func Minh1() [2][3] ID {return;};        
            func Minh22() {return;}                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_213(self):
        input = """func main() {
            var num int = 15;
            if (num > 10) {
                putStringLn("num is greater than 10");
            } else {
                putStringLn("num is less than or equal to 10");
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_214(self):
        input = """func main() {
            var values [3]int = [3]int{7, 8, 9};
            for index, val := range values {
                putIntLn(index);
                putIntLn(val);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_215(self):
        input = """func multiply(a int, b int) int {
            return a * b;
        }
        func main() {
            var product int = multiply(6, 7);
            putIntLn(product);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_216(self):
        input = """type BankAccount struct {
            balance int;
        }
        func (acc BankAccount) deposit(amount int) int {
            acc.balance += amount;
            return acc.balance;
        }
        func main() {
            var account BankAccount = BankAccount{balance: 100};
            var newBalance int = account.deposit(50);
            putIntLn(newBalance);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_217(self):
        input = """func main() {
            var x int = 5;
            var y int = 10;
            if (x > y) {
                putStringLn("x is greater than y");
            } else if (x < y) {
                putStringLn("x is less than y");
            } else {
                putStringLn("x is equal to y");
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_218(self):
        input = """func main() {
            for i := 1; i <= 10; i += 1 {
                if (i == 7) {
                    break;
                }
                if (i % 3 == 0) {
                    continue;
                }
                putIntLn(i);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_219(self):
        input = """func multiply(a int, b int) int {
            return a * b;
        }
        func divide(a int, b int) int {
            return a / b;
        }
        func main() {
            var x int = 12;
            var y int = 4;
            var product int = multiply(x, y);
            var quotient int = divide(x, y);
            putIntLn(product);
            putIntLn(quotient);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_220(self):
        input = """func main() {
            var a int = 15;
            var b int = 25;
            var result int = a * b + (b - a);
            putIntLn(result);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))
        
    def test_221(self):
        input = """    
            func Minh() {
                x  := goo() + 5 / 4;
                x.c[1][2] := 2 + 2;                       
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_222(self):
        input = """    
            func Minh() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var h str;
                } else {
                    var h ID;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_223(self):
        input = """    
            func Minh() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_224(self):
        input = """    
            const a = 0b11;                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_225(self):
        input = """    
            var z Minh = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                            
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_226(self):
        input = """    
            var z Minh = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_227(self):
        input = """    
            var h Minh = 1 && 2 && 3 || 1 || 1;                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_228(self):
       
        input = """func main() {};"""

        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_229(self):
        input ="""func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_230(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_231(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_232(self):
        
        input = """    
            var z MINH = a.b.a.c.e.g;                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_233(self):
        input = """    
            var z MINH = a[2][3][a + 2];                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_234(self):
        input = """    
            var z MINH = a.b.b[2].foo(1);                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_235(self):
        input = """    
            const k = -a + -!-!c - ---[2]int{2};                         
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_236(self):
        
        input = """    
            var d [2][3]ID
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_237(self):
        input = """    
            func Add(x int, y [2]int) [2]id {return ;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_238(self):
        input = """    
            func Add() {return ;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_239(self):
        input = """    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_240(self):
        input = """    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))
    def test_241(self):
        input = """    
            func Add(x int, y int) int  {return ;};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_242(self):
        input = """
                                    func Add() {
                                         var a int;      
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_243(self):
        input = """
                                    func Add() {
                                         var a = a[2].b;      
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_244(self):
        input = """
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_245(self):
        input = """
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_246(self):
        input = """
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_247(self):
        input = """
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return; 
                                        } else {
                                            a := 2;
                                        }   
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_248(self):
        input = """
            func Add() {
                for true + 2 + foo().b {return; }
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_249(self):
        input = """
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_250(self):
        input = """
                                    func Add() {
                                        for index, value := range 23 {return; 
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_251(self):
        
        input = """
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_252(self):
        input = """
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_253(self):
        input = """
                                    func Add() {
                                        a.go(2 + 3, a {a:2})
                                        go(2 + 3, a {a:2});
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_254(self):
        input = """
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_255(self):
        input = """
                                            const a = [ID][2][VT]int{{{1}}}                              
                                        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_256(self):
 
        input = """
                                            const a = [ID][2][VT]int{{{1}}}                              
                                        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_257(self):
        input = """
                                            const a = [ID][2][VT]int{{{1}}}                              
                                        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_258(self):
        input = """
                                            const a = [ID][2][VT]int{{{1}}}                              
                                        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_259(self):
        input = """
                                            const a = [ID][2][VT]int{{{1}}}                              
                                        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_260(self):
        input = """
                                            const a = [ID][2][VT]int{{{1}}}                              
                                        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))
    def test_261(self):
        input = """func main() {
            return;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_262(self):
        input = """func add(a int, b int) int {
            return a + b;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_263(self):
        input = """func main() {
            var x int = 10;
            if (x > 5) {
                if (x < 20) {
                    putIntLn(x);
                }
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_264(self):
        input = """func main() {
            var i int;
            var j int;
            for i := 0; i < 3; i := i + 1 {
                for j := 0; j < 3; j := j + 1 {
                    putIntLn(i * 10 + j);
                }
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_265(self):
        input = """func main() {
            putIntLn(100);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_266(self):
        input = """func main() {
            var c int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_267(self):
        input = """func main() {
            var arr [5]int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_268(self):
        input = """func main() {
            var arr [3]int = [3]int{1, 2,4};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_269(self):
        input = """func main() {
            var arr [3]int = [3]int{1,3,4};
            putIntLn(arr[1]);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_270(self):
        input = """func main() {
            var arr [3]int;
            arr[0] := 10;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))
    def test_271(self):
        input = """func main() {
            var x int = 5 + 3 * 2 - 1 / 4;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272(self):
        input = """func main() {
            var b bool = true && false || true;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_273(self):
        input = """func main() {
            var x int = 10;
            var y int = 20;
            if (x <= y && x != y) {
                putIntLn(x);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_274(self):
        input = """func main() {
            var str string = "Hello" + " World";
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_275(self):
        input = """func foo() {
            putIntLn(100);
        }
        func bar() {
            putIntLn(200);
        }
        func main() {
            foo();
            bar();
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_276(self):
        input = """func main() {
            putIntLn(foo(bar(2)));
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_277(self):
        input = """func main() {
            var arr [2][3]int;
            arr[0][0] := 1;
            arr[1][2] := 2;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_278(self):
        input = """func printArray(arr [5]int) {
            var i int;
            for i := 0; i < 5; i := i + 1 {
                putIntLn(arr[i]);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_279(self):
        input = """func main() {
            var x int = 1;
            var y int = 3;
            putIntLn(x + y);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_280(self):
        input = """func square(x int) int {
            return x * x;
        };
        func main() {
            var sum int = 0;
            for i := 1; i <= 5; i := i + 1 {
                var temp int = square(i);
                if (temp % 2 == 0) {
                    sum := sum + temp;
                } else {
                    sum := sum - temp;
                }
            }
            putIntLn(sum);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281(self):
        input = """func fact(n int) int {
            if (n == 0) {
                return 1;
            }
            return n * fact(n - 1);
        };
        func main() {
            putIntLn(fct());
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282(self):
        input = """func main() {
            var sum int = 0;
            for i := 0; i < 5; i := i + 1 {
                for j := 0; j < 5; j := j + 1 {
                    if ((i + j) % 2 == 0) {
                        sum := sum + 1;
                    }
                }
            }
            putIntLn(sum);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_283(self):
        input = """func main() {
            var i int;
            for i := 0; i < 10; i := i + 1 {
                if (i == 5) {
                    break;
                }
                putIntLn(i);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284(self):
        input = """func main() {
            var i int;
            for i := 0; i < 5; i := i + 1 {
                if (i == 2) {
                    continue;
                }
                putIntLn(i);
            }
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_285(self):
        input = """func main() {
            var arr [3]int;
            arr[1 + 1] := arr[2 - 1] * 2;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_286(self):
        input = """func main() {
            var i int = 0;
            var count int = 0;
            
                i := i + 1;
                if (i == 3) {
                    continue;
                }
                if (i == 8) {
                    break;
                }
                count := count + i;
            
            putIntLn(count);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287(self):
        input = """func multiply(a int, b int) int {
            return a * b;
        };
        func square(x int) int {
            return multiply(x, x);
        };
        func main() {
            putIntLn(squre());
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288(self):
        input = """func main() {
            var matrix [2][2]int = [2][2]int{{1,2},{3,4}};
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_289(self):
        input = """func main() {
            var x int = 5;
            x += 3;
            x *= 2;
            x /= 4;
            x -= 1;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_290(self):
        input = """func main() {
            var i int = 0;
            i := i + 1;  // increment
            i := i - 1;  // decrement
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    def test_291(self):
        input = """func main() {
            var str string = "Hello";
            var len int = str.length();
            var sub string = str.substring(0, 2);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_292(self):
        input = """
        func main() {
            var area float = PI * r * r;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_293(self):
        input = """func fibonacci(n int) int {
            if (n <= 1) {
                return n;
            }
            return fibonacci(n - 1) + fibonacci(n - 2);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_294(self):
        input = """func getArray() [5]int {
            var arr [5]int = [5]int{1, 2, 3, 4, 5};
            return arr;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_295(self):
        input =  """func main() {
            var result bool = (a > b) && (c < d) || !(e == f) && (g >= h);
            var value int = (a + b) * c / (d - e) % f;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_296(self):
        input = """func sum(a int, b int) int {
            return a + b;
        }
        func sum(a float, b float) float {
            return a + b;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_297(self):
        input = """type Point struct {
            x float;
            y float;
        };
        func main() {
            var p Point;
            p.x := 1.0;
            p.y := 2.0;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_298(self):
        input = """type Student struct {
            name string;
            grades [5]float;
        };
        func main() {
            var s Student;
            s.grades[0] := 8.5;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_299(self):
        input = """func printPoint(p Point) void {
            putFloat(p.x);
            putString(", ");
            putFloatLn(p.y);
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_300(self):
        input = """func main() {
            printInt(1 + 2 * (3 + foo(bar(2 + 3) * 2)));
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    
        