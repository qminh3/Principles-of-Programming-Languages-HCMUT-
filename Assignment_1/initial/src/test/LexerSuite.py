import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # Keywords (tests 101-121)
    def test_keyword_if(self):
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 101))
    def test_keyword_else(self):
        self.assertTrue(TestLexer.checkLexeme("else", "else,<EOF>", 102))
    def test_keyword_for(self):
        self.assertTrue(TestLexer.checkLexeme("for", "for,<EOF>", 103))
    def test_keyword_return(self):
        self.assertTrue(TestLexer.checkLexeme("return", "return,<EOF>", 104))
    def test_keyword_func(self):
        self.assertTrue(TestLexer.checkLexeme("func", "func,<EOF>", 105))
    def test_keyword_type(self):
        self.assertTrue(TestLexer.checkLexeme("type", "type,<EOF>", 106))
    def test_keyword_struct(self):
        self.assertTrue(TestLexer.checkLexeme("struct", "struct,<EOF>", 107))
    def test_keyword_interface(self):
        self.assertTrue(TestLexer.checkLexeme("interface", "interface,<EOF>", 108))
    def test_keyword_const(self):
        self.assertTrue(TestLexer.checkLexeme("const", "const,<EOF>", 109))
    def test_keyword_var(self):
        self.assertTrue(TestLexer.checkLexeme("var", "var,<EOF>", 110))
    def test_keyword_continue(self):
        self.assertTrue(TestLexer.checkLexeme("continue", "continue,<EOF>", 111))
    def test_keyword_break(self):
        self.assertTrue(TestLexer.checkLexeme("break", "break,<EOF>", 112))
    def test_keyword_range(self):
        self.assertTrue(TestLexer.checkLexeme("range", "range,<EOF>", 113))
    def test_keyword_nil(self):
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 114))
    def test_keyword_true(self):
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 115))
    def test_keyword_false(self):
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 116))
    def test_keyword_int(self):
        self.assertTrue(TestLexer.checkLexeme("int", "int,<EOF>", 117))
    def test_keyword_string(self):
        self.assertTrue(TestLexer.checkLexeme("string", "string,<EOF>", 118))
    def test_keyword_float(self):
        self.assertTrue(TestLexer.checkLexeme("float", "float,<EOF>", 119))
    def test_keyword_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("boolean", "boolean,<EOF>", 120))
    def test_operator_add(self):
        self.assertTrue(TestLexer.checkLexeme("+", "+,<EOF>", 121))
    def test_operator_sub(self):
        self.assertTrue(TestLexer.checkLexeme("-", "-,<EOF>", 122))
    def test_operator_mul(self):
        self.assertTrue(TestLexer.checkLexeme("*", "*,<EOF>", 123))
    def test_operator_div(self):
        self.assertTrue(TestLexer.checkLexeme("/", "/,<EOF>", 124))
    def test_operator_mod(self):
        self.assertTrue(TestLexer.checkLexeme("%", "%,<EOF>", 125))
    def test_operator_and(self):
        self.assertTrue(TestLexer.checkLexeme("&&", "&&,<EOF>", 126))
    def test_operator_or(self):
        self.assertTrue(TestLexer.checkLexeme("||", "||,<EOF>", 127))
    def test_operator_not(self):
        self.assertTrue(TestLexer.checkLexeme("!", "!,<EOF>", 128))
    def test_operator_equal(self):
        self.assertTrue(TestLexer.checkLexeme("==", "==,<EOF>", 129))
    def test_operator_not_equal(self):
        self.assertTrue(TestLexer.checkLexeme("!=", "!=,<EOF>", 130))
    def test_operator_less(self):
        self.assertTrue(TestLexer.checkLexeme("<", "<,<EOF>", 131))
    def test_operator_greater(self):
        self.assertTrue(TestLexer.checkLexeme(">", ">,<EOF>", 132))
    def test_operator_less_equal(self):
        self.assertTrue(TestLexer.checkLexeme("<=", "<=,<EOF>", 133))
    def test_operator_greater_equal(self):
        self.assertTrue(TestLexer.checkLexeme(">=", ">=,<EOF>", 134))
    def test_operator_declare(self):
        self.assertTrue(TestLexer.checkLexeme(":=", ":=,<EOF>", 135))
    def test_operator_assign(self):
        self.assertTrue(TestLexer.checkLexeme("=", "=,<EOF>", 136))
    def test_operator_ADD_ASSIGN(self):
        self.assertTrue(TestLexer.checkLexeme("+=", "+=,<EOF>", 137))
    def test_operator_SUB_ASSIGN(self):
        self.assertTrue(TestLexer.checkLexeme("-=", "-=,<EOF>", 138))
    def test_operator_MUL_ASSIGN(self):
        self.assertTrue(TestLexer.checkLexeme("*=", "*=,<EOF>", 139))
    def test_operator_DIV_ASSIGN(self):
        self.assertTrue(TestLexer.checkLexeme("/=", "/=,<EOF>", 140))
    def test_operator_MOD_ASSIGN(self):
        self.assertTrue(TestLexer.checkLexeme("%=", "%=,<EOF>", 141))
    def test_operator_dot(self):
        self.assertTrue(TestLexer.checkLexeme(".", ".,<EOF>", 142))
    def test_operator_comma(self):
        self.assertTrue(TestLexer.checkLexeme(",", ",,<EOF>", 143))
    def test_operator_semicolon(self):
        self.assertTrue(TestLexer.checkLexeme(";", ";,<EOF>", 144))
    def test_operator_left_parenthesis(self):
        self.assertTrue(TestLexer.checkLexeme("(", "(,<EOF>", 145))
    def test_operator_right_parenthesis(self):
        self.assertTrue(TestLexer.checkLexeme( ")", "),<EOF>", 146))
    def test_operator_left_brace(self):
        self.assertTrue(TestLexer.checkLexeme("{", "{,<EOF>", 147))
    def test_operator_right_brace(self):
        self.assertTrue(TestLexer.checkLexeme("}", "},<EOF>", 148))
    def test_operator_left_bracket(self):
        self.assertTrue(TestLexer.checkLexeme("[", "[,<EOF>", 149))
    def test_operator_right_bracket(self):
        self.assertTrue(TestLexer.checkLexeme("]", "],<EOF>", 150))       
    def test_identifier1(self):
        # Valid identifiers
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 151))
    def test_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme("abc123", "abc123,<EOF>", 152))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("_abc", "_abc,<EOF>", 153))
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("_123", "_123,<EOF>", 154))
    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("ABC_123", "ABC_123,<EOF>", 155))
        
    def test_literal1(self):
        # Integer literals
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 156))
    def test_literal2(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 157))
    def test_literal3(self):
        self.assertTrue(TestLexer.checkLexeme("-123", "-,123,<EOF>", 158))
    def test_literal4(self):
        self.assertTrue(TestLexer.checkLexeme("0b1010", "0b1010,<EOF>", 159))
    def test_literal5(self): 
        self.assertTrue(TestLexer.checkLexeme("0o765", "0o765,<EOF>", 160))
    def test_literal6(self):
        self.assertTrue(TestLexer.checkLexeme("0xABCD", "0xABCD,<EOF>", 161))
    def test_float_1(self):   
        # Float literals
        self.assertTrue(TestLexer.checkLexeme("123.456", "123.456,<EOF>", 162))
    def test_float_2(self): 
        self.assertTrue(TestLexer.checkLexeme("0.123", "0.123,<EOF>", 163))
    def test_float_3(self): 
        self.assertTrue(TestLexer.checkLexeme("123.", "123.,<EOF>", 164))
    def test_float_4(self): 
        self.assertTrue(TestLexer.checkLexeme("1.23e-4", "1.23e-4,<EOF>", 165))
    def test_float_5(self): 
        self.assertTrue(TestLexer.checkLexeme("1e10", "1,e10,<EOF>", 166))
    def test_string_1(self):
        # String literals
        self.assertTrue(TestLexer.checkLexeme('"Hello"', '"Hello",<EOF>', 167))
    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme('"Hello World"', '"Hello World",<EOF>', 168))
    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme('""', '"",<EOF>', 169))
    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme("\"Hello\"", "\"Hello\",<EOF>", 170))
    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme("\"Hello\\nWorld\"", "\"Hello\\nWorld\",<EOF>", 171))
    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme("\"Hello\\r\\nWorld\"", "\"Hello\\r\\nWorld\",<EOF>", 172))
    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme("\"Hello\\tWorld\"", "\"Hello\\tWorld\",<EOF>", 173))
    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme("HelloWorld111", "HelloWorld111,<EOF>", 174))
    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme("\"\"", "\"\",<EOF>", 175))
    
    def test_invalid_string_closing(self):
        self.assertTrue(TestLexer.checkLexeme('"Hello World\\"', 'Unclosed string: "Hello World\\"', 176))
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"Unclosed", 'Unclosed string: "Unclosed', 177))
    def test_illegal_escape_string(self):
        self.assertTrue(TestLexer.checkLexeme("\"Illegal \\a escape\"", "Illegal escape in string: \"Illegal \\a", 178))
    def test_error_char_1(self):
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^", 179))  
    def test_error_char_2(self):
        self.assertTrue(TestLexer.checkLexeme("?", "ErrorToken ?", 180))
    def test_error_char_3(self):
        self.assertTrue(TestLexer.checkLexeme("@", "ErrorToken @", 181))
            
    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("//This is a comment", "<EOF>", 182))
    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("// Multiple // comments", "<EOF>",183))
    def test_comment_3(self):    
        # Multi-line comments
        self.assertTrue(TestLexer.checkLexeme("/* This is a comment */", "<EOF>", 184))
    def test_comment_4(self):
        self.assertTrue(TestLexer.checkLexeme("/* Multiple \n lines \n comment */", "<EOF>", 185))
        
    def test_whitespace_1(self):
        # Various whitespace characters
        self.assertTrue(TestLexer.checkLexeme(" ", "<EOF>", 186))
    def test_whitespace_2(self):
        self.assertTrue(TestLexer.checkLexeme("\t", "<EOF>", 187))
    def test_whitespace_3(self):
        self.assertTrue(TestLexer.checkLexeme("\n", "<EOF>", 188))
    def test_whitespace_4(self):
        self.assertTrue(TestLexer.checkLexeme("\r", "<EOF>", 189))
        
    def test_combination_1(self):
        # Combined tokens
        self.assertTrue(TestLexer.checkLexeme("a+b", "a,+,b,<EOF>", 190))
    def test_combination_2(self):
        self.assertTrue(TestLexer.checkLexeme("1+2", "1,+,2,<EOF>", 191))
    def test_combination_3(self):
        self.assertTrue(TestLexer.checkLexeme("a = b + c;", "a,=,b,+,c,;,<EOF>", 192))
    def test_combination_4(self):
        self.assertTrue(TestLexer.checkLexeme("if(a>b){return;}", "if,(,a,>,b,),{,return,;,},<EOF>", 193))
        
    def test_UNCLOSE_STRING1(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123" """, "123,Unclosed string: \" ", 194))
    def test_UNCLOSE_STRING2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123
        " """, "Unclosed string: \"123", 195))
    def test_UNCLOSE_STRING3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "&\\&" """, "Illegal escape in string: \"&\\&", 196))
    def test_UNCLOSE_STRING4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\z" """, "Illegal escape in string: \"\\z", 197))
    def test_UNCLOSE_STRING5(self):
        self.assertTrue(TestLexer.checkLexeme("""
            1
        """, "1,;,<EOF>", 198))
    def test_unary_minus(self):
        self.assertTrue(TestLexer.checkLexeme("-a", "-,a,<EOF>", 199))
    def test_increment(self):
        self.assertTrue(TestLexer.checkLexeme("a++", "a,+,+,<EOF>", 200))
                                              