// 2212019
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
prevtoken = None
def nextToken(self):
	next_token = super().nextToken()    
	self.prevtoken = next_token
	return next_token
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

// program: (CONST ID ASSIGN expression SEMICOLON) EOF;
program: list_declaration EOF;

list_declaration: declaration list_declaration | declaration;
declaration:
	var_declaration| const_declaration| func_declaration| struct_declaration | interface_declaration ;

list_statement_primary: list_statement | ;
list_statement: (statement list_statement) | statement;
statement:
	(
		const_declaration 
        | var_declaration 
		| assign_statement 
		| if_statement 
		| for_statement 
		| break_statement
		| continue_statement
		| func_call
        | call_statement
		| return_statement
	) ;
//--------------------CONST and VAR -----------------
const_declaration : CONST ID ASSIGN expression SEMICOLON ;
var_declaration: VAR ID ((data_type ((ASSIGN (expression)) | )) | (ASSIGN (expression))) SEMICOLON;
// var_declaration: VAR ID (data_type | data_type? ASSIGN expression) SEMICOLON;



// khai báo struct
struct_declaration: TYPE ID STRUCT LBRACE data_struct RBRACE (SEMICOLON);
data_struct: (ID data_type (SEMICOLON)) data_struct | (ID data_type (SEMICOLON));

//method
method_declaration: LPAREN list_method_element RPAREN;
list_method_element: method_element COMMA list_method_element | method_element;
method_element: ID ID;

// function
func_declaration: FUNC (method_declaration | ) ID LPAREN list_func_arguments RPAREN (data_type | ) LBRACE list_statement_primary RBRACE SEMICOLON;
list_func_arguments: list_agruments | ;
list_agruments: func_agrument COMMA list_agruments | func_agrument;
func_agrument: data_element data_type;
data_element: ID COMMA data_element | ID;



//interface

interface_declaration: TYPE ID INTERFACE LBRACE list_method_interface RBRACE (SEMICOLON) ;
    list_method_interface: inter_method list_method_interface | inter_method;
    inter_method: ID LPAREN list_interface_element? RPAREN (data_type |) SEMICOLON;
    list_interface_element: inter_param COMMA list_interface_element | inter_param;
    inter_param: data_element data_type;

// assign
assign_oprator: ASS_DECLARE| ADD_ASSIGN| SUB_ASSIGN| MUL_ASSIGN| DIV_ASSIGN| MOD_ASSIGN;

// assign_statement: 
assign_statement: (assignment_lhs) (assign_oprator expression) SEMICOLON;
assignment_lhs: assignment_lhs (DOT ID | LBRACKET expression RBRACKET) | ID;    

// if_else statement
if_statement: if_stmt (elseif_list| ) (ELSE  block_statement | ) SEMICOLON;
    if_stmt: IF LPAREN expression RPAREN block_statement;
    elseif_list: (ELSE IF LPAREN expression RPAREN  block_statement ) elseif_list | (ELSE IF LPAREN expression RPAREN  block_statement );
    block_statement: LBRACE list_statement_primary RBRACE;

//for statement
for_statement: FOR (for_basic | for_loop_basic | for_loop_range) LBRACE list_statement_primary RBRACE SEMICOLON ;
    for_basic:  expression  ;
    for_loop_basic:( var_declaration_for| assignment_for) SEMICOLON expression SEMICOLON assignment_for  ;
    for_loop_range: ID COMMA ID ASS_DECLARE RANGE expression  ;
    assignment_for: ID (assign_oprator expression);
    var_declaration_for: VAR ID data_type? ASSIGN expression;


break_statement: BREAK SEMICOLON;
lhs_aggin: lhs_aggin (LBRACKET expression RBRACKET | DOT ID) | ID;
call_statement: ((lhs_aggin DOT) | )ID LPAREN list_expression RPAREN SEMICOLON;
continue_statement: CONTINUE SEMICOLON;
return_statement: RETURN (expression | ) SEMICOLON;

literal:
	INTEGER_LITERAL| FLOATING_LITERAL| STRING_LITERAL| BOOLEAN_LIT| array_literal| struct_literal;
data_type: ID | INT | FLOAT | BOOLEAN | STRING | array_type;

//array_literal
array_literal: array_type LBRACE list_array_element RBRACE;
    array_type: list_type_arr (data_type);
    list_type_arr: LBRACKET (INTEGER_LITERAL | ID) RBRACKET list_type_arr 
                | LBRACKET (INTEGER_LITERAL | ID) RBRACKET;

    list_array_element: array_element COMMA list_array_element | array_element;
    array_element: array_param | (LBRACE list_array_element RBRACE);
    array_param :INTEGER_LITERAL| FLOATING_LITERAL| STRING_LITERAL| TRUE | FALSE| NIL| ID| struct_literal;


//struct_literal:
struct_literal: ID LBRACE struct_lit_body RBRACE;
    struct_lit_body: struct_lit_body_element | ;
    struct_lit_body_element: struct_element COMMA struct_lit_body_element 
                            | struct_element;
    struct_element: ID COLON expression   ;


// ------------ EXPRESSION---------------------------------------------------
COMPARE_OPERATOR: EQUAL| NOT_EQUAL| LESS| LESS_EQUAL| GREATER| GREATER_EQUAL;
list_expression: params | ;  // list_expression có thể rỗng 
    params: expression COMMA params | expression ; //param thì không rỗng được
    expression: expression OR expression_1 | expression_1;
    expression_1: expression_1 AND expression_2 | expression_2;
    expression_2: expression_2 COMPARE_OPERATOR expression_3 | expression_3;
    expression_3: expression_3 (ADD | SUB ) expression_4 | expression_4 ;
    expression_4: expression_4 (MUL | DIV | MOD) expression_5 | expression_5 ;
    expression_5: (NOT | SUB) expression_5 | expression_6 ;
    expression_6: 
        expression_6 LBRACKET (expression) RBRACKET 
        | expression_6 (DOT (ID |func_call ))
        | expression_7;
    expression_7: ID | literal | LPAREN expression RPAREN | func_call | TRUE | FALSE | NIL;
                
func_call: ID LPAREN list_expression RPAREN;

// Keywords 
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE:'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT:'int';
FLOAT:'float';
CONST: 'const';
VAR:'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL:'nil';
TRUE:'true';
FALSE:'false';
BOOLEAN:'boolean';

// Operators 
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
// Relational Operators
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';

// Logical Operators
AND: '&&';
OR: '||';
NOT: '!';

// Assig Operators
ASS_DECLARE: ':=';
ASSIGN: '=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';

// Other Operators
DOT: '.';
COLON: ':'; 

//Separators 
LPAREN: '('; 
RPAREN: ')'; 
LBRACE: '{'; 
RBRACE: '}'; 
LBRACKET: '['; 
RBRACKET: ']'; 
COMMA: ','; 
SEMICOLON: ';'; 

// Identifiers 
fragment LETTER : [a-zA-Z_]; 
fragment DIGIT : [0-9]; 
fragment ID_PART : (LETTER | DIGIT) ID_PART |;
ID: LETTER ID_PART;

BOOLEAN_LIT: TRUE | FALSE;


//Literals 
INTEGER_LITERAL:
    DECIMAL_LITERAL
    | BINARY_LITERAL 
    | HEX_LITERAL 
    | OCTAL_LITERAL;


// số nguyên thập phân (decimal)
fragment NON_ZERO_DIGIT: [1-9];
fragment DECIMAL_LIST: DIGIT DECIMAL_LIST | ;
DECIMAL_LITERAL: NON_ZERO_DIGIT DECIMAL_LIST | '0';


// số nguyên nhị phân (binary)
fragment START_BINARY_LIT: '0b' | '0B';
fragment BINARY_LIST: ('0' | '1') BINARY_LIST | ('0' | '1');
BINARY_LITERAL: START_BINARY_LIT BINARY_LIST;

// số nhuyên bát phân ( octal)
fragment START_OCTAL_LIT: '0o' | '0O';
fragment OCTAL_DIGIT: [0-7] OCTAL_DIGIT | [0-7];
OCTAL_LITERAL: START_OCTAL_LIT OCTAL_DIGIT;

// số nguyên thập lục phân (hex)
fragment START_HEX_LIT: '0x' | '0X';
fragment HEX_DIGIT: [0-9a-fA-F] HEX_DIGIT | [0-9a-fA-F];
HEX_LITERAL: START_HEX_LIT HEX_DIGIT;

// số thực (float)
fragment DIGITS: ('0' | [1-9] DIGIT*);
fragment OPT_FRAC: (DIGIT*)?;
fragment OPT_EXP: ([eE]('-'|'+')?DIGIT+)?;
FLOATING_LITERAL: DIGIT+ DOT OPT_FRAC OPT_EXP;

// xử lý chuỗi (string)
fragment STR_CHAR: ESC_SEQ | ~[\r\n\\"];
fragment ESC_SEQ: '\\' [trn"\\];

fragment ESC_ILLEGAL: '\\' ~[trn"\\];

STRING_LITERAL: '"' STR_CHAR* '"';

NIL_LIT: NIL;

COMMENT_BLOCK: '/*' (COMMENT_BLOCK | .)*? '*/' -> skip;
COMMENT_LINE:  '//' ~[\r\n]*  -> skip;


//skip 
WS: [ \t\f\r]+ -> skip; 

NEWLINE: ('\r'? '\n') {
    if self.prevtoken is not None and self.prevtoken.type in {
        self.ID, 
        self.RPAREN, 
        self.RBRACKET, 
        self.RBRACE,
        self.INTEGER_LITERAL, 
        self.BINARY_LITERAL, 
        self.OCTAL_LITERAL, 
        self.HEX_LITERAL,
        self.FLOATING_LITERAL, 
        self.TRUE, 
        self.FALSE, 
        self.STRING_LITERAL,
        self.RETURN, 
        self.CONTINUE, 
        self.BREAK,
        self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.NIL
    }:
        self.text = ";"
        self.type = self.SEMICOLON
    else:
        self.skip()
};




ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* ('\r' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[0:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[0:-1])
    elif (self.text[-1] == '\r'):
        raise UncloseString(self.text[0:-1])
    else:
        raise UncloseString(self.text[0:])
};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[0:])
};