# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u0275\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u008a\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u0091")
        buf.write("\n\4\3\5\3\5\5\5\u0095\n\5\3\6\3\6\3\6\3\6\5\6\u009b\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a7\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00b5\n\t\3\t\3\t\5\t\u00b9\n\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u00cf\n\13\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00da\n\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\5\17\u00e2\n\17\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00ea\n\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\5\20")
        buf.write("\u00f3\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00fa\n\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u0103\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u0111\n\25\3\26\3\26\3\26\5\26\u0116\n\26\3\26\3")
        buf.write("\26\3\26\5\26\u011b\n\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0124\n\27\3\30\3\30\3\30\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u013b\n\33\7\33\u013d\n\33\f")
        buf.write("\33\16\33\u0140\13\33\3\34\3\34\3\34\5\34\u0145\n\34\3")
        buf.write("\34\3\34\3\34\5\34\u014a\n\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0164\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \5 \u016e\n \3 \3 ")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\5\"\u0179\n\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\5%\u018e")
        buf.write("\n%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\5\'\u01a0\n\'\7\'\u01a2\n\'\f\'\16\'\u01a5\13")
        buf.write("\'\3(\3(\3(\3(\5(\u01ab\n(\3(\3(\3(\3(\3(\3(\3)\3)\3)")
        buf.write("\3*\3*\3*\5*\u01b9\n*\3*\3*\3+\3+\3+\3+\3+\3+\5+\u01c3")
        buf.write("\n+\3,\3,\3,\3,\3,\3,\5,\u01cb\n,\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\5/\u01dc\n/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\5\60\u01e3\n\60\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write("\u01ea\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5")
        buf.write("\62\u01f4\n\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\5\64")
        buf.write("\u01fd\n\64\3\65\3\65\3\65\3\65\3\65\5\65\u0204\n\65\3")
        buf.write("\66\3\66\3\66\3\66\3\67\3\67\5\67\u020c\n\67\38\38\38")
        buf.write("\38\38\58\u0213\n8\39\39\39\39\39\39\79\u021b\n9\f9\16")
        buf.write("9\u021e\139\3:\3:\3:\3:\3:\3:\7:\u0226\n:\f:\16:\u0229")
        buf.write("\13:\3;\3;\3;\3;\3;\3;\7;\u0231\n;\f;\16;\u0234\13;\3")
        buf.write("<\3<\3<\3<\3<\3<\7<\u023c\n<\f<\16<\u023f\13<\3=\3=\3")
        buf.write("=\3=\3=\3=\7=\u0247\n=\f=\16=\u024a\13=\3>\3>\3>\5>\u024f")
        buf.write("\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u025d\n?\7")
        buf.write("?\u025f\n?\f?\16?\u0262\13?\3@\3@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\5@\u026e\n@\3A\3A\3A\3A\3A\3A\2\n\64Lprtvx|B\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\2\7\4\2")
        buf.write("&&(,\4\2\67\6799\3\2\30\31\3\2\32\34\4\2\31\31%%\2\u0285")
        buf.write("\2\u0082\3\2\2\2\4\u0089\3\2\2\2\6\u0090\3\2\2\2\b\u0094")
        buf.write("\3\2\2\2\n\u009a\3\2\2\2\f\u00a6\3\2\2\2\16\u00a8\3\2")
        buf.write("\2\2\20\u00ae\3\2\2\2\22\u00bc\3\2\2\2\24\u00ce\3\2\2")
        buf.write("\2\26\u00d0\3\2\2\2\30\u00d9\3\2\2\2\32\u00db\3\2\2\2")
        buf.write("\34\u00de\3\2\2\2\36\u00f2\3\2\2\2 \u00f9\3\2\2\2\"\u00fb")
        buf.write("\3\2\2\2$\u0102\3\2\2\2&\u0104\3\2\2\2(\u0110\3\2\2\2")
        buf.write("*\u0112\3\2\2\2,\u0123\3\2\2\2.\u0125\3\2\2\2\60\u0128")
        buf.write("\3\2\2\2\62\u012a\3\2\2\2\64\u0130\3\2\2\2\66\u0141\3")
        buf.write("\2\2\28\u014d\3\2\2\2:\u0163\3\2\2\2<\u0165\3\2\2\2>\u0169")
        buf.write("\3\2\2\2@\u0174\3\2\2\2B\u0178\3\2\2\2D\u017f\3\2\2\2")
        buf.write("F\u0186\3\2\2\2H\u018a\3\2\2\2J\u0192\3\2\2\2L\u0195\3")
        buf.write("\2\2\2N\u01aa\3\2\2\2P\u01b2\3\2\2\2R\u01b5\3\2\2\2T\u01c2")
        buf.write("\3\2\2\2V\u01ca\3\2\2\2X\u01cc\3\2\2\2Z\u01d1\3\2\2\2")
        buf.write("\\\u01db\3\2\2\2^\u01e2\3\2\2\2`\u01e9\3\2\2\2b\u01f3")
        buf.write("\3\2\2\2d\u01f5\3\2\2\2f\u01fc\3\2\2\2h\u0203\3\2\2\2")
        buf.write("j\u0205\3\2\2\2l\u020b\3\2\2\2n\u0212\3\2\2\2p\u0214\3")
        buf.write("\2\2\2r\u021f\3\2\2\2t\u022a\3\2\2\2v\u0235\3\2\2\2x\u0240")
        buf.write("\3\2\2\2z\u024e\3\2\2\2|\u0250\3\2\2\2~\u026d\3\2\2\2")
        buf.write("\u0080\u026f\3\2\2\2\u0082\u0083\5\4\3\2\u0083\u0084\7")
        buf.write("\2\2\3\u0084\3\3\2\2\2\u0085\u0086\5\6\4\2\u0086\u0087")
        buf.write("\5\4\3\2\u0087\u008a\3\2\2\2\u0088\u008a\5\6\4\2\u0089")
        buf.write("\u0085\3\2\2\2\u0089\u0088\3\2\2\2\u008a\5\3\2\2\2\u008b")
        buf.write("\u0091\5\20\t\2\u008c\u0091\5\16\b\2\u008d\u0091\5\34")
        buf.write("\17\2\u008e\u0091\5\22\n\2\u008f\u0091\5&\24\2\u0090\u008b")
        buf.write("\3\2\2\2\u0090\u008c\3\2\2\2\u0090\u008d\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091\7\3\2\2\2\u0092")
        buf.write("\u0095\5\n\6\2\u0093\u0095\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0094\u0093\3\2\2\2\u0095\t\3\2\2\2\u0096\u0097\5\f\7")
        buf.write("\2\u0097\u0098\5\n\6\2\u0098\u009b\3\2\2\2\u0099\u009b")
        buf.write("\5\f\7\2\u009a\u0096\3\2\2\2\u009a\u0099\3\2\2\2\u009b")
        buf.write("\13\3\2\2\2\u009c\u00a7\5\16\b\2\u009d\u00a7\5\20\t\2")
        buf.write("\u009e\u00a7\5\62\32\2\u009f\u00a7\5\66\34\2\u00a0\u00a7")
        buf.write("\5> \2\u00a1\u00a7\5J&\2\u00a2\u00a7\5P)\2\u00a3\u00a7")
        buf.write("\5\u0080A\2\u00a4\u00a7\5N(\2\u00a5\u00a7\5R*\2\u00a6")
        buf.write("\u009c\3\2\2\2\u00a6\u009d\3\2\2\2\u00a6\u009e\3\2\2\2")
        buf.write("\u00a6\u009f\3\2\2\2\u00a6\u00a0\3\2\2\2\u00a6\u00a1\3")
        buf.write("\2\2\2\u00a6\u00a2\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\r\3\2\2\2\u00a8\u00a9")
        buf.write("\7\17\2\2\u00a9\u00aa\7\67\2\2\u00aa\u00ab\7\'\2\2\u00ab")
        buf.write("\u00ac\5p9\2\u00ac\u00ad\7\66\2\2\u00ad\17\3\2\2\2\u00ae")
        buf.write("\u00af\7\20\2\2\u00af\u00b8\7\67\2\2\u00b0\u00b4\5V,\2")
        buf.write("\u00b1\u00b2\7\'\2\2\u00b2\u00b5\5p9\2\u00b3\u00b5\3\2")
        buf.write("\2\2\u00b4\u00b1\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b9")
        buf.write("\3\2\2\2\u00b6\u00b7\7\'\2\2\u00b7\u00b9\5p9\2\u00b8\u00b0")
        buf.write("\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bb\7\66\2\2\u00bb\21\3\2\2\2\u00bc\u00bd\7\t\2\2\u00bd")
        buf.write("\u00be\7\67\2\2\u00be\u00bf\7\n\2\2\u00bf\u00c0\7\61\2")
        buf.write("\2\u00c0\u00c1\5\24\13\2\u00c1\u00c2\7\62\2\2\u00c2\u00c3")
        buf.write("\7\66\2\2\u00c3\23\3\2\2\2\u00c4\u00c5\7\67\2\2\u00c5")
        buf.write("\u00c6\5V,\2\u00c6\u00c7\7\66\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00c9\5\24\13\2\u00c9\u00cf\3\2\2\2\u00ca\u00cb")
        buf.write("\7\67\2\2\u00cb\u00cc\5V,\2\u00cc\u00cd\7\66\2\2\u00cd")
        buf.write("\u00cf\3\2\2\2\u00ce\u00c4\3\2\2\2\u00ce\u00ca\3\2\2\2")
        buf.write("\u00cf\25\3\2\2\2\u00d0\u00d1\7/\2\2\u00d1\u00d2\5\30")
        buf.write("\r\2\u00d2\u00d3\7\60\2\2\u00d3\27\3\2\2\2\u00d4\u00d5")
        buf.write("\5\32\16\2\u00d5\u00d6\7\65\2\2\u00d6\u00d7\5\30\r\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00da\5\32\16\2\u00d9\u00d4\3\2\2")
        buf.write("\2\u00d9\u00d8\3\2\2\2\u00da\31\3\2\2\2\u00db\u00dc\7")
        buf.write("\67\2\2\u00dc\u00dd\7\67\2\2\u00dd\33\3\2\2\2\u00de\u00e1")
        buf.write("\7\b\2\2\u00df\u00e2\5\26\f\2\u00e0\u00e2\3\2\2\2\u00e1")
        buf.write("\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e4\7\67\2\2\u00e4\u00e5\7/\2\2\u00e5\u00e6\5")
        buf.write("\36\20\2\u00e6\u00e9\7\60\2\2\u00e7\u00ea\5V,\2\u00e8")
        buf.write("\u00ea\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\u00ec\7\61\2\2\u00ec\u00ed")
        buf.write("\5\b\5\2\u00ed\u00ee\7\62\2\2\u00ee\u00ef\7\66\2\2\u00ef")
        buf.write("\35\3\2\2\2\u00f0\u00f3\5 \21\2\u00f1\u00f3\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\37\3\2\2\2\u00f4")
        buf.write("\u00f5\5\"\22\2\u00f5\u00f6\7\65\2\2\u00f6\u00f7\5 \21")
        buf.write("\2\u00f7\u00fa\3\2\2\2\u00f8\u00fa\5\"\22\2\u00f9\u00f4")
        buf.write("\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa!\3\2\2\2\u00fb\u00fc")
        buf.write("\5$\23\2\u00fc\u00fd\5V,\2\u00fd#\3\2\2\2\u00fe\u00ff")
        buf.write("\7\67\2\2\u00ff\u0100\7\65\2\2\u0100\u0103\5$\23\2\u0101")
        buf.write("\u0103\7\67\2\2\u0102\u00fe\3\2\2\2\u0102\u0101\3\2\2")
        buf.write("\2\u0103%\3\2\2\2\u0104\u0105\7\t\2\2\u0105\u0106\7\67")
        buf.write("\2\2\u0106\u0107\7\13\2\2\u0107\u0108\7\61\2\2\u0108\u0109")
        buf.write("\5(\25\2\u0109\u010a\7\62\2\2\u010a\u010b\7\66\2\2\u010b")
        buf.write("\'\3\2\2\2\u010c\u010d\5*\26\2\u010d\u010e\5(\25\2\u010e")
        buf.write("\u0111\3\2\2\2\u010f\u0111\5*\26\2\u0110\u010c\3\2\2\2")
        buf.write("\u0110\u010f\3\2\2\2\u0111)\3\2\2\2\u0112\u0113\7\67\2")
        buf.write("\2\u0113\u0115\7/\2\2\u0114\u0116\5,\27\2\u0115\u0114")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u011a\7\60\2\2\u0118\u011b\5V,\2\u0119\u011b\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011a\u0119\3\2\2\2\u011b\u011c\3")
        buf.write("\2\2\2\u011c\u011d\7\66\2\2\u011d+\3\2\2\2\u011e\u011f")
        buf.write("\5.\30\2\u011f\u0120\7\65\2\2\u0120\u0121\5,\27\2\u0121")
        buf.write("\u0124\3\2\2\2\u0122\u0124\5.\30\2\u0123\u011e\3\2\2\2")
        buf.write("\u0123\u0122\3\2\2\2\u0124-\3\2\2\2\u0125\u0126\5$\23")
        buf.write("\2\u0126\u0127\5V,\2\u0127/\3\2\2\2\u0128\u0129\t\2\2")
        buf.write("\2\u0129\61\3\2\2\2\u012a\u012b\5\64\33\2\u012b\u012c")
        buf.write("\5\60\31\2\u012c\u012d\5p9\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u012f\7\66\2\2\u012f\63\3\2\2\2\u0130\u0131\b\33\1\2")
        buf.write("\u0131\u0132\7\67\2\2\u0132\u013e\3\2\2\2\u0133\u013a")
        buf.write("\f\4\2\2\u0134\u0135\7-\2\2\u0135\u013b\7\67\2\2\u0136")
        buf.write("\u0137\7\63\2\2\u0137\u0138\5p9\2\u0138\u0139\7\64\2\2")
        buf.write("\u0139\u013b\3\2\2\2\u013a\u0134\3\2\2\2\u013a\u0136\3")
        buf.write("\2\2\2\u013b\u013d\3\2\2\2\u013c\u0133\3\2\2\2\u013d\u0140")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\65\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0144\58\35\2\u0142")
        buf.write("\u0145\5:\36\2\u0143\u0145\3\2\2\2\u0144\u0142\3\2\2\2")
        buf.write("\u0144\u0143\3\2\2\2\u0145\u0149\3\2\2\2\u0146\u0147\7")
        buf.write("\5\2\2\u0147\u014a\5<\37\2\u0148\u014a\3\2\2\2\u0149\u0146")
        buf.write("\3\2\2\2\u0149\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("\u014c\7\66\2\2\u014c\67\3\2\2\2\u014d\u014e\7\4\2\2\u014e")
        buf.write("\u014f\7/\2\2\u014f\u0150\5p9\2\u0150\u0151\7\60\2\2\u0151")
        buf.write("\u0152\5<\37\2\u01529\3\2\2\2\u0153\u0154\7\5\2\2\u0154")
        buf.write("\u0155\7\4\2\2\u0155\u0156\7/\2\2\u0156\u0157\5p9\2\u0157")
        buf.write("\u0158\7\60\2\2\u0158\u0159\5<\37\2\u0159\u015a\3\2\2")
        buf.write("\2\u015a\u015b\5:\36\2\u015b\u0164\3\2\2\2\u015c\u015d")
        buf.write("\7\5\2\2\u015d\u015e\7\4\2\2\u015e\u015f\7/\2\2\u015f")
        buf.write("\u0160\5p9\2\u0160\u0161\7\60\2\2\u0161\u0162\5<\37\2")
        buf.write("\u0162\u0164\3\2\2\2\u0163\u0153\3\2\2\2\u0163\u015c\3")
        buf.write("\2\2\2\u0164;\3\2\2\2\u0165\u0166\7\61\2\2\u0166\u0167")
        buf.write("\5\b\5\2\u0167\u0168\7\62\2\2\u0168=\3\2\2\2\u0169\u016d")
        buf.write("\7\6\2\2\u016a\u016e\5@!\2\u016b\u016e\5B\"\2\u016c\u016e")
        buf.write("\5D#\2\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016c")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\7\61\2\2\u0170")
        buf.write("\u0171\5\b\5\2\u0171\u0172\7\62\2\2\u0172\u0173\7\66\2")
        buf.write("\2\u0173?\3\2\2\2\u0174\u0175\5p9\2\u0175A\3\2\2\2\u0176")
        buf.write("\u0179\5H%\2\u0177\u0179\5F$\2\u0178\u0176\3\2\2\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017b\7\66\2")
        buf.write("\2\u017b\u017c\5p9\2\u017c\u017d\7\66\2\2\u017d\u017e")
        buf.write("\5F$\2\u017eC\3\2\2\2\u017f\u0180\7\67\2\2\u0180\u0181")
        buf.write("\7\65\2\2\u0181\u0182\7\67\2\2\u0182\u0183\7&\2\2\u0183")
        buf.write("\u0184\7\23\2\2\u0184\u0185\5p9\2\u0185E\3\2\2\2\u0186")
        buf.write("\u0187\7\67\2\2\u0187\u0188\5\60\31\2\u0188\u0189\5p9")
        buf.write("\2\u0189G\3\2\2\2\u018a\u018b\7\20\2\2\u018b\u018d\7\67")
        buf.write("\2\2\u018c\u018e\5V,\2\u018d\u018c\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\7\'\2\2\u0190")
        buf.write("\u0191\5p9\2\u0191I\3\2\2\2\u0192\u0193\7\22\2\2\u0193")
        buf.write("\u0194\7\66\2\2\u0194K\3\2\2\2\u0195\u0196\b\'\1\2\u0196")
        buf.write("\u0197\7\67\2\2\u0197\u01a3\3\2\2\2\u0198\u019f\f\4\2")
        buf.write("\2\u0199\u019a\7\63\2\2\u019a\u019b\5p9\2\u019b\u019c")
        buf.write("\7\64\2\2\u019c\u01a0\3\2\2\2\u019d\u019e\7-\2\2\u019e")
        buf.write("\u01a0\7\67\2\2\u019f\u0199\3\2\2\2\u019f\u019d\3\2\2")
        buf.write("\2\u01a0\u01a2\3\2\2\2\u01a1\u0198\3\2\2\2\u01a2\u01a5")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("M\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\5L\'\2\u01a7")
        buf.write("\u01a8\7-\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab\3\2\2\2")
        buf.write("\u01aa\u01a6\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01ad\7\67\2\2\u01ad\u01ae\7/\2\2\u01ae\u01af")
        buf.write("\5l\67\2\u01af\u01b0\7\60\2\2\u01b0\u01b1\7\66\2\2\u01b1")
        buf.write("O\3\2\2\2\u01b2\u01b3\7\21\2\2\u01b3\u01b4\7\66\2\2\u01b4")
        buf.write("Q\3\2\2\2\u01b5\u01b8\7\7\2\2\u01b6\u01b9\5p9\2\u01b7")
        buf.write("\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01ba\u01bb\7\66\2\2\u01bbS\3\2\2")
        buf.write("\2\u01bc\u01c3\79\2\2\u01bd\u01c3\7>\2\2\u01be\u01c3\7")
        buf.write("?\2\2\u01bf\u01c3\78\2\2\u01c0\u01c3\5X-\2\u01c1\u01c3")
        buf.write("\5d\63\2\u01c2\u01bc\3\2\2\2\u01c2\u01bd\3\2\2\2\u01c2")
        buf.write("\u01be\3\2\2\2\u01c2\u01bf\3\2\2\2\u01c2\u01c0\3\2\2\2")
        buf.write("\u01c2\u01c1\3\2\2\2\u01c3U\3\2\2\2\u01c4\u01cb\7\67\2")
        buf.write("\2\u01c5\u01cb\7\r\2\2\u01c6\u01cb\7\16\2\2\u01c7\u01cb")
        buf.write("\7\27\2\2\u01c8\u01cb\7\f\2\2\u01c9\u01cb\5Z.\2\u01ca")
        buf.write("\u01c4\3\2\2\2\u01ca\u01c5\3\2\2\2\u01ca\u01c6\3\2\2\2")
        buf.write("\u01ca\u01c7\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01c9\3")
        buf.write("\2\2\2\u01cbW\3\2\2\2\u01cc\u01cd\5Z.\2\u01cd\u01ce\7")
        buf.write("\61\2\2\u01ce\u01cf\5^\60\2\u01cf\u01d0\7\62\2\2\u01d0")
        buf.write("Y\3\2\2\2\u01d1\u01d2\5\\/\2\u01d2\u01d3\5V,\2\u01d3[")
        buf.write("\3\2\2\2\u01d4\u01d5\7\63\2\2\u01d5\u01d6\t\3\2\2\u01d6")
        buf.write("\u01d7\7\64\2\2\u01d7\u01dc\5\\/\2\u01d8\u01d9\7\63\2")
        buf.write("\2\u01d9\u01da\t\3\2\2\u01da\u01dc\7\64\2\2\u01db\u01d4")
        buf.write("\3\2\2\2\u01db\u01d8\3\2\2\2\u01dc]\3\2\2\2\u01dd\u01de")
        buf.write("\5`\61\2\u01de\u01df\7\65\2\2\u01df\u01e0\5^\60\2\u01e0")
        buf.write("\u01e3\3\2\2\2\u01e1\u01e3\5`\61\2\u01e2\u01dd\3\2\2\2")
        buf.write("\u01e2\u01e1\3\2\2\2\u01e3_\3\2\2\2\u01e4\u01ea\5b\62")
        buf.write("\2\u01e5\u01e6\7\61\2\2\u01e6\u01e7\5^\60\2\u01e7\u01e8")
        buf.write("\7\62\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e4\3\2\2\2\u01e9")
        buf.write("\u01e5\3\2\2\2\u01eaa\3\2\2\2\u01eb\u01f4\79\2\2\u01ec")
        buf.write("\u01f4\7>\2\2\u01ed\u01f4\7?\2\2\u01ee\u01f4\7\25\2\2")
        buf.write("\u01ef\u01f4\7\26\2\2\u01f0\u01f4\7\24\2\2\u01f1\u01f4")
        buf.write("\7\67\2\2\u01f2\u01f4\5d\63\2\u01f3\u01eb\3\2\2\2\u01f3")
        buf.write("\u01ec\3\2\2\2\u01f3\u01ed\3\2\2\2\u01f3\u01ee\3\2\2\2")
        buf.write("\u01f3\u01ef\3\2\2\2\u01f3\u01f0\3\2\2\2\u01f3\u01f1\3")
        buf.write("\2\2\2\u01f3\u01f2\3\2\2\2\u01f4c\3\2\2\2\u01f5\u01f6")
        buf.write("\7\67\2\2\u01f6\u01f7\7\61\2\2\u01f7\u01f8\5f\64\2\u01f8")
        buf.write("\u01f9\7\62\2\2\u01f9e\3\2\2\2\u01fa\u01fd\5h\65\2\u01fb")
        buf.write("\u01fd\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fb\3\2\2\2")
        buf.write("\u01fdg\3\2\2\2\u01fe\u01ff\5j\66\2\u01ff\u0200\7\65\2")
        buf.write("\2\u0200\u0201\5h\65\2\u0201\u0204\3\2\2\2\u0202\u0204")
        buf.write("\5j\66\2\u0203\u01fe\3\2\2\2\u0203\u0202\3\2\2\2\u0204")
        buf.write("i\3\2\2\2\u0205\u0206\7\67\2\2\u0206\u0207\7.\2\2\u0207")
        buf.write("\u0208\5p9\2\u0208k\3\2\2\2\u0209\u020c\5n8\2\u020a\u020c")
        buf.write("\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020a\3\2\2\2\u020c")
        buf.write("m\3\2\2\2\u020d\u020e\5p9\2\u020e\u020f\7\65\2\2\u020f")
        buf.write("\u0210\5n8\2\u0210\u0213\3\2\2\2\u0211\u0213\5p9\2\u0212")
        buf.write("\u020d\3\2\2\2\u0212\u0211\3\2\2\2\u0213o\3\2\2\2\u0214")
        buf.write("\u0215\b9\1\2\u0215\u0216\5r:\2\u0216\u021c\3\2\2\2\u0217")
        buf.write("\u0218\f\4\2\2\u0218\u0219\7$\2\2\u0219\u021b\5r:\2\u021a")
        buf.write("\u0217\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021c\u021d\3\2\2\2\u021dq\3\2\2\2\u021e\u021c\3\2\2")
        buf.write("\2\u021f\u0220\b:\1\2\u0220\u0221\5t;\2\u0221\u0227\3")
        buf.write("\2\2\2\u0222\u0223\f\4\2\2\u0223\u0224\7#\2\2\u0224\u0226")
        buf.write("\5t;\2\u0225\u0222\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225")
        buf.write("\3\2\2\2\u0227\u0228\3\2\2\2\u0228s\3\2\2\2\u0229\u0227")
        buf.write("\3\2\2\2\u022a\u022b\b;\1\2\u022b\u022c\5v<\2\u022c\u0232")
        buf.write("\3\2\2\2\u022d\u022e\f\4\2\2\u022e\u022f\7\3\2\2\u022f")
        buf.write("\u0231\5v<\2\u0230\u022d\3\2\2\2\u0231\u0234\3\2\2\2\u0232")
        buf.write("\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233u\3\2\2\2\u0234")
        buf.write("\u0232\3\2\2\2\u0235\u0236\b<\1\2\u0236\u0237\5x=\2\u0237")
        buf.write("\u023d\3\2\2\2\u0238\u0239\f\4\2\2\u0239\u023a\t\4\2\2")
        buf.write("\u023a\u023c\5x=\2\u023b\u0238\3\2\2\2\u023c\u023f\3\2")
        buf.write("\2\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023ew\3")
        buf.write("\2\2\2\u023f\u023d\3\2\2\2\u0240\u0241\b=\1\2\u0241\u0242")
        buf.write("\5z>\2\u0242\u0248\3\2\2\2\u0243\u0244\f\4\2\2\u0244\u0245")
        buf.write("\t\5\2\2\u0245\u0247\5z>\2\u0246\u0243\3\2\2\2\u0247\u024a")
        buf.write("\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249")
        buf.write("y\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c\t\6\2\2\u024c")
        buf.write("\u024f\5z>\2\u024d\u024f\5|?\2\u024e\u024b\3\2\2\2\u024e")
        buf.write("\u024d\3\2\2\2\u024f{\3\2\2\2\u0250\u0251\b?\1\2\u0251")
        buf.write("\u0252\5~@\2\u0252\u0260\3\2\2\2\u0253\u0254\f\5\2\2\u0254")
        buf.write("\u0255\7\63\2\2\u0255\u0256\5p9\2\u0256\u0257\7\64\2\2")
        buf.write("\u0257\u025f\3\2\2\2\u0258\u0259\f\4\2\2\u0259\u025c\7")
        buf.write("-\2\2\u025a\u025d\7\67\2\2\u025b\u025d\5\u0080A\2\u025c")
        buf.write("\u025a\3\2\2\2\u025c\u025b\3\2\2\2\u025d\u025f\3\2\2\2")
        buf.write("\u025e\u0253\3\2\2\2\u025e\u0258\3\2\2\2\u025f\u0262\3")
        buf.write("\2\2\2\u0260\u025e\3\2\2\2\u0260\u0261\3\2\2\2\u0261}")
        buf.write("\3\2\2\2\u0262\u0260\3\2\2\2\u0263\u026e\7\67\2\2\u0264")
        buf.write("\u026e\5T+\2\u0265\u0266\7/\2\2\u0266\u0267\5p9\2\u0267")
        buf.write("\u0268\7\60\2\2\u0268\u026e\3\2\2\2\u0269\u026e\5\u0080")
        buf.write("A\2\u026a\u026e\7\25\2\2\u026b\u026e\7\26\2\2\u026c\u026e")
        buf.write("\7\24\2\2\u026d\u0263\3\2\2\2\u026d\u0264\3\2\2\2\u026d")
        buf.write("\u0265\3\2\2\2\u026d\u0269\3\2\2\2\u026d\u026a\3\2\2\2")
        buf.write("\u026d\u026b\3\2\2\2\u026d\u026c\3\2\2\2\u026e\177\3\2")
        buf.write("\2\2\u026f\u0270\7\67\2\2\u0270\u0271\7/\2\2\u0271\u0272")
        buf.write("\5l\67\2\u0272\u0273\7\60\2\2\u0273\u0081\3\2\2\2\64\u0089")
        buf.write("\u0090\u0094\u009a\u00a6\u00b4\u00b8\u00ce\u00d9\u00e1")
        buf.write("\u00e9\u00f2\u00f9\u0102\u0110\u0115\u011a\u0123\u013a")
        buf.write("\u013e\u0144\u0149\u0163\u016d\u0178\u018d\u019f\u01a3")
        buf.write("\u01aa\u01b8\u01c2\u01ca\u01db\u01e2\u01e9\u01f3\u01fc")
        buf.write("\u0203\u020b\u0212\u021c\u0227\u0232\u023d\u0248\u024e")
        buf.write("\u025c\u025e\u0260\u026d")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'boolean'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "':='", "'='", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'.'", "':'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "COMPARE_OPERATOR", "IF", "ELSE", "FOR", 
                      "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                      "INT", "FLOAT", "CONST", "VAR", "CONTINUE", "BREAK", 
                      "RANGE", "NIL", "TRUE", "FALSE", "BOOLEAN", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                      "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                      "AND", "OR", "NOT", "ASS_DECLARE", "ASSIGN", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "COLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "COMMA", "SEMICOLON", "ID", 
                      "BOOLEAN_LIT", "INTEGER_LITERAL", "DECIMAL_LITERAL", 
                      "BINARY_LITERAL", "OCTAL_LITERAL", "HEX_LITERAL", 
                      "FLOATING_LITERAL", "STRING_LITERAL", "NIL_LIT", "COMMENT_BLOCK", 
                      "COMMENT_LINE", "WS", "NEWLINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declaration = 1
    RULE_declaration = 2
    RULE_list_statement_primary = 3
    RULE_list_statement = 4
    RULE_statement = 5
    RULE_const_declaration = 6
    RULE_var_declaration = 7
    RULE_struct_declaration = 8
    RULE_data_struct = 9
    RULE_method_declaration = 10
    RULE_list_method_element = 11
    RULE_method_element = 12
    RULE_func_declaration = 13
    RULE_list_func_arguments = 14
    RULE_list_agruments = 15
    RULE_func_agrument = 16
    RULE_data_element = 17
    RULE_interface_declaration = 18
    RULE_list_method_interface = 19
    RULE_inter_method = 20
    RULE_list_interface_element = 21
    RULE_inter_param = 22
    RULE_assign_oprator = 23
    RULE_assign_statement = 24
    RULE_assignment_lhs = 25
    RULE_if_statement = 26
    RULE_if_stmt = 27
    RULE_elseif_list = 28
    RULE_block_statement = 29
    RULE_for_statement = 30
    RULE_for_basic = 31
    RULE_for_loop_basic = 32
    RULE_for_loop_range = 33
    RULE_assignment_for = 34
    RULE_var_declaration_for = 35
    RULE_break_statement = 36
    RULE_lhs_aggin = 37
    RULE_call_statement = 38
    RULE_continue_statement = 39
    RULE_return_statement = 40
    RULE_literal = 41
    RULE_data_type = 42
    RULE_array_literal = 43
    RULE_array_type = 44
    RULE_list_type_arr = 45
    RULE_list_array_element = 46
    RULE_array_element = 47
    RULE_array_param = 48
    RULE_struct_literal = 49
    RULE_struct_lit_body = 50
    RULE_struct_lit_body_element = 51
    RULE_struct_element = 52
    RULE_list_expression = 53
    RULE_params = 54
    RULE_expression = 55
    RULE_expression_1 = 56
    RULE_expression_2 = 57
    RULE_expression_3 = 58
    RULE_expression_4 = 59
    RULE_expression_5 = 60
    RULE_expression_6 = 61
    RULE_expression_7 = 62
    RULE_func_call = 63

    ruleNames =  [ "program", "list_declaration", "declaration", "list_statement_primary", 
                   "list_statement", "statement", "const_declaration", "var_declaration", 
                   "struct_declaration", "data_struct", "method_declaration", 
                   "list_method_element", "method_element", "func_declaration", 
                   "list_func_arguments", "list_agruments", "func_agrument", 
                   "data_element", "interface_declaration", "list_method_interface", 
                   "inter_method", "list_interface_element", "inter_param", 
                   "assign_oprator", "assign_statement", "assignment_lhs", 
                   "if_statement", "if_stmt", "elseif_list", "block_statement", 
                   "for_statement", "for_basic", "for_loop_basic", "for_loop_range", 
                   "assignment_for", "var_declaration_for", "break_statement", 
                   "lhs_aggin", "call_statement", "continue_statement", 
                   "return_statement", "literal", "data_type", "array_literal", 
                   "array_type", "list_type_arr", "list_array_element", 
                   "array_element", "array_param", "struct_literal", "struct_lit_body", 
                   "struct_lit_body_element", "struct_element", "list_expression", 
                   "params", "expression", "expression_1", "expression_2", 
                   "expression_3", "expression_4", "expression_5", "expression_6", 
                   "expression_7", "func_call" ]

    EOF = Token.EOF
    COMPARE_OPERATOR=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STRING=10
    INT=11
    FLOAT=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    BOOLEAN=21
    ADD=22
    SUB=23
    MUL=24
    DIV=25
    MOD=26
    EQUAL=27
    NOT_EQUAL=28
    LESS=29
    LESS_EQUAL=30
    GREATER=31
    GREATER_EQUAL=32
    AND=33
    OR=34
    NOT=35
    ASS_DECLARE=36
    ASSIGN=37
    ADD_ASSIGN=38
    SUB_ASSIGN=39
    MUL_ASSIGN=40
    DIV_ASSIGN=41
    MOD_ASSIGN=42
    DOT=43
    COLON=44
    LPAREN=45
    RPAREN=46
    LBRACE=47
    RBRACE=48
    LBRACKET=49
    RBRACKET=50
    COMMA=51
    SEMICOLON=52
    ID=53
    BOOLEAN_LIT=54
    INTEGER_LITERAL=55
    DECIMAL_LITERAL=56
    BINARY_LITERAL=57
    OCTAL_LITERAL=58
    HEX_LITERAL=59
    FLOATING_LITERAL=60
    STRING_LITERAL=61
    NIL_LIT=62
    COMMENT_BLOCK=63
    COMMENT_LINE=64
    WS=65
    NEWLINE=66
    ERROR_CHAR=67
    UNCLOSE_STRING=68
    ILLEGAL_ESCAPE=69

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_declarationContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.list_declaration()
            self.state = 129
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def list_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.List_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declaration" ):
                return visitor.visitList_declaration(self)
            else:
                return visitor.visitChildren(self)




    def list_declaration(self):

        localctx = MiniGoParser.List_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declaration)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.declaration()
                self.state = 132
                self.list_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declarationContext,0)


        def const_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declarationContext,0)


        def func_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declarationContext,0)


        def struct_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declarationContext,0)


        def interface_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.var_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.const_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.func_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.struct_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.interface_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statement_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement_primary" ):
                return visitor.visitList_statement_primary(self)
            else:
                return visitor.visitChildren(self)




    def list_statement_primary(self):

        localctx = MiniGoParser.List_statement_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_statement_primary)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.list_statement()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list_statement)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.statement()
                self.state = 149
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declarationContext,0)


        def var_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declarationContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 154
                self.const_declaration()
                pass

            elif la_ == 2:
                self.state = 155
                self.var_declaration()
                pass

            elif la_ == 3:
                self.state = 156
                self.assign_statement()
                pass

            elif la_ == 4:
                self.state = 157
                self.if_statement()
                pass

            elif la_ == 5:
                self.state = 158
                self.for_statement()
                pass

            elif la_ == 6:
                self.state = 159
                self.break_statement()
                pass

            elif la_ == 7:
                self.state = 160
                self.continue_statement()
                pass

            elif la_ == 8:
                self.state = 161
                self.func_call()
                pass

            elif la_ == 9:
                self.state = 162
                self.call_statement()
                pass

            elif la_ == 10:
                self.state = 163
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declaration" ):
                return visitor.visitConst_declaration(self)
            else:
                return visitor.visitChildren(self)




    def const_declaration(self):

        localctx = MiniGoParser.Const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MiniGoParser.CONST)
            self.state = 167
            self.match(MiniGoParser.ID)
            self.state = 168
            self.match(MiniGoParser.ASSIGN)
            self.state = 169
            self.expression(0)
            self.state = 170
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration" ):
                return visitor.visitVar_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration(self):

        localctx = MiniGoParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MiniGoParser.VAR)
            self.state = 173
            self.match(MiniGoParser.ID)
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 174
                self.data_type()
                self.state = 178
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ASSIGN]:
                    self.state = 175
                    self.match(MiniGoParser.ASSIGN)

                    self.state = 176
                    self.expression(0)
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 180
                self.match(MiniGoParser.ASSIGN)

                self.state = 181
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 184
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def data_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Data_structContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declaration" ):
                return visitor.visitStruct_declaration(self)
            else:
                return visitor.visitChildren(self)




    def struct_declaration(self):

        localctx = MiniGoParser.Struct_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_struct_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(MiniGoParser.TYPE)
            self.state = 187
            self.match(MiniGoParser.ID)
            self.state = 188
            self.match(MiniGoParser.STRUCT)
            self.state = 189
            self.match(MiniGoParser.LBRACE)
            self.state = 190
            self.data_struct()
            self.state = 191
            self.match(MiniGoParser.RBRACE)

            self.state = 192
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Data_structContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_struct" ):
                return visitor.visitData_struct(self)
            else:
                return visitor.visitChildren(self)




    def data_struct(self):

        localctx = MiniGoParser.Data_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_data_struct)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(MiniGoParser.ID)
                self.state = 195
                self.data_type()

                self.state = 196
                self.match(MiniGoParser.SEMICOLON)
                self.state = 198
                self.data_struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(MiniGoParser.ID)
                self.state = 201
                self.data_type()

                self.state = 202
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_method_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_elementContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = MiniGoParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MiniGoParser.LPAREN)
            self.state = 207
            self.list_method_element()
            self.state = 208
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_method_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_element(self):
            return self.getTypedRuleContext(MiniGoParser.Method_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_method_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_method_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_method_element" ):
                return visitor.visitList_method_element(self)
            else:
                return visitor.visitChildren(self)




    def list_method_element(self):

        localctx = MiniGoParser.List_method_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_method_element)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.method_element()
                self.state = 211
                self.match(MiniGoParser.COMMA)
                self.state = 212
                self.list_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.method_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_element" ):
                return visitor.visitMethod_element(self)
            else:
                return visitor.visitChildren(self)




    def method_element(self):

        localctx = MiniGoParser.Method_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MiniGoParser.ID)
            self.state = 218
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_func_arguments(self):
            return self.getTypedRuleContext(MiniGoParser.List_func_argumentsContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement_primary(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primaryContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def method_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declarationContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declaration" ):
                return visitor.visitFunc_declaration(self)
            else:
                return visitor.visitChildren(self)




    def func_declaration(self):

        localctx = MiniGoParser.Func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MiniGoParser.FUNC)
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN]:
                self.state = 221
                self.method_declaration()
                pass
            elif token in [MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 225
            self.match(MiniGoParser.ID)
            self.state = 226
            self.match(MiniGoParser.LPAREN)
            self.state = 227
            self.list_func_arguments()
            self.state = 228
            self.match(MiniGoParser.RPAREN)
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 229
                self.data_type()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 233
            self.match(MiniGoParser.LBRACE)
            self.state = 234
            self.list_statement_primary()
            self.state = 235
            self.match(MiniGoParser.RBRACE)
            self.state = 236
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_func_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_agruments(self):
            return self.getTypedRuleContext(MiniGoParser.List_agrumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_func_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_func_arguments" ):
                return visitor.visitList_func_arguments(self)
            else:
                return visitor.visitChildren(self)




    def list_func_arguments(self):

        localctx = MiniGoParser.List_func_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_func_arguments)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.list_agruments()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_agrumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_agrument(self):
            return self.getTypedRuleContext(MiniGoParser.Func_agrumentContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_agruments(self):
            return self.getTypedRuleContext(MiniGoParser.List_agrumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_agruments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_agruments" ):
                return visitor.visitList_agruments(self)
            else:
                return visitor.visitChildren(self)




    def list_agruments(self):

        localctx = MiniGoParser.List_agrumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_agruments)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.func_agrument()
                self.state = 243
                self.match(MiniGoParser.COMMA)
                self.state = 244
                self.list_agruments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.func_agrument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_agrumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_element(self):
            return self.getTypedRuleContext(MiniGoParser.Data_elementContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_agrument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_agrument" ):
                return visitor.visitFunc_agrument(self)
            else:
                return visitor.visitChildren(self)




    def func_agrument(self):

        localctx = MiniGoParser.Func_agrumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_agrument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.data_element()
            self.state = 250
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def data_element(self):
            return self.getTypedRuleContext(MiniGoParser.Data_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_element" ):
                return visitor.visitData_element(self)
            else:
                return visitor.visitChildren(self)




    def data_element(self):

        localctx = MiniGoParser.Data_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_data_element)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(MiniGoParser.ID)
                self.state = 253
                self.match(MiniGoParser.COMMA)
                self.state = 254
                self.data_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_method_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_interfaceContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declaration" ):
                return visitor.visitInterface_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_declaration(self):

        localctx = MiniGoParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MiniGoParser.TYPE)
            self.state = 259
            self.match(MiniGoParser.ID)
            self.state = 260
            self.match(MiniGoParser.INTERFACE)
            self.state = 261
            self.match(MiniGoParser.LBRACE)
            self.state = 262
            self.list_method_interface()
            self.state = 263
            self.match(MiniGoParser.RBRACE)

            self.state = 264
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_method_interfaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inter_method(self):
            return self.getTypedRuleContext(MiniGoParser.Inter_methodContext,0)


        def list_method_interface(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_interfaceContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_method_interface

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_method_interface" ):
                return visitor.visitList_method_interface(self)
            else:
                return visitor.visitChildren(self)




    def list_method_interface(self):

        localctx = MiniGoParser.List_method_interfaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_method_interface)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.inter_method()
                self.state = 267
                self.list_method_interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.inter_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inter_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def list_interface_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_inter_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInter_method" ):
                return visitor.visitInter_method(self)
            else:
                return visitor.visitChildren(self)




    def inter_method(self):

        localctx = MiniGoParser.Inter_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_inter_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MiniGoParser.ID)
            self.state = 273
            self.match(MiniGoParser.LPAREN)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 274
                self.list_interface_element()


            self.state = 277
            self.match(MiniGoParser.RPAREN)
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 278
                self.data_type()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 282
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inter_param(self):
            return self.getTypedRuleContext(MiniGoParser.Inter_paramContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_interface_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_element" ):
                return visitor.visitList_interface_element(self)
            else:
                return visitor.visitChildren(self)




    def list_interface_element(self):

        localctx = MiniGoParser.List_interface_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_interface_element)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.inter_param()
                self.state = 285
                self.match(MiniGoParser.COMMA)
                self.state = 286
                self.list_interface_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.inter_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inter_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_element(self):
            return self.getTypedRuleContext(MiniGoParser.Data_elementContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_inter_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInter_param" ):
                return visitor.visitInter_param(self)
            else:
                return visitor.visitChildren(self)




    def inter_param(self):

        localctx = MiniGoParser.Inter_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_inter_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.data_element()
            self.state = 292
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASS_DECLARE(self):
            return self.getToken(MiniGoParser.ASS_DECLARE, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_oprator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_oprator" ):
                return visitor.visitAssign_oprator(self)
            else:
                return visitor.visitChildren(self)




    def assign_oprator(self):

        localctx = MiniGoParser.Assign_opratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign_oprator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASS_DECLARE) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def assign_oprator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opratorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.assignment_lhs(0)

            self.state = 297
            self.assign_oprator()
            self.state = 298
            self.expression(0)
            self.state = 300
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)



    def assignment_lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Assignment_lhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_assignment_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 305
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DOT]:
                        self.state = 306
                        self.match(MiniGoParser.DOT)
                        self.state = 307
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.LBRACKET]:
                        self.state = 308
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 309
                        self.expression(0)
                        self.state = 310
                        self.match(MiniGoParser.RBRACKET)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def elseif_list(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_listContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.if_stmt()
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 320
                self.elseif_list()
                pass

            elif la_ == 2:
                pass


            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.state = 324
                self.match(MiniGoParser.ELSE)
                self.state = 325
                self.block_statement()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 329
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MiniGoParser.IF)
            self.state = 332
            self.match(MiniGoParser.LPAREN)
            self.state = 333
            self.expression(0)
            self.state = 334
            self.match(MiniGoParser.RPAREN)
            self.state = 335
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_list(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_listContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_list" ):
                return visitor.visitElseif_list(self)
            else:
                return visitor.visitChildren(self)




    def elseif_list(self):

        localctx = MiniGoParser.Elseif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elseif_list)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(MiniGoParser.ELSE)
                self.state = 338
                self.match(MiniGoParser.IF)
                self.state = 339
                self.match(MiniGoParser.LPAREN)
                self.state = 340
                self.expression(0)
                self.state = 341
                self.match(MiniGoParser.RPAREN)
                self.state = 342
                self.block_statement()
                self.state = 344
                self.elseif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(MiniGoParser.ELSE)
                self.state = 347
                self.match(MiniGoParser.IF)
                self.state = 348
                self.match(MiniGoParser.LPAREN)
                self.state = 349
                self.expression(0)
                self.state = 350
                self.match(MiniGoParser.RPAREN)
                self.state = 351
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement_primary(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primaryContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MiniGoParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(MiniGoParser.LBRACE)
            self.state = 356
            self.list_statement_primary()
            self.state = 357
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement_primary(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primaryContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def for_basic(self):
            return self.getTypedRuleContext(MiniGoParser.For_basicContext,0)


        def for_loop_basic(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_basicContext,0)


        def for_loop_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MiniGoParser.FOR)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 360
                self.for_basic()
                pass

            elif la_ == 2:
                self.state = 361
                self.for_loop_basic()
                pass

            elif la_ == 3:
                self.state = 362
                self.for_loop_range()
                pass


            self.state = 365
            self.match(MiniGoParser.LBRACE)
            self.state = 366
            self.list_statement_primary()
            self.state = 367
            self.match(MiniGoParser.RBRACE)
            self.state = 368
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_basic" ):
                return visitor.visitFor_basic(self)
            else:
                return visitor.visitChildren(self)




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assignment_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Assignment_forContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Assignment_forContext,i)


        def var_declaration_for(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaration_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_basic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_basic" ):
                return visitor.visitFor_loop_basic(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_basic(self):

        localctx = MiniGoParser.For_loop_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_loop_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.state = 372
                self.var_declaration_for()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 373
                self.assignment_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 376
            self.match(MiniGoParser.SEMICOLON)
            self.state = 377
            self.expression(0)
            self.state = 378
            self.match(MiniGoParser.SEMICOLON)
            self.state = 379
            self.assignment_for()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASS_DECLARE(self):
            return self.getToken(MiniGoParser.ASS_DECLARE, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_range" ):
                return visitor.visitFor_loop_range(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_range(self):

        localctx = MiniGoParser.For_loop_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_loop_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MiniGoParser.ID)
            self.state = 382
            self.match(MiniGoParser.COMMA)
            self.state = 383
            self.match(MiniGoParser.ID)
            self.state = 384
            self.match(MiniGoParser.ASS_DECLARE)
            self.state = 385
            self.match(MiniGoParser.RANGE)
            self.state = 386
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_oprator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opratorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_for" ):
                return visitor.visitAssignment_for(self)
            else:
                return visitor.visitChildren(self)




    def assignment_for(self):

        localctx = MiniGoParser.Assignment_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assignment_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(MiniGoParser.ID)

            self.state = 389
            self.assign_oprator()
            self.state = 390
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declaration_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declaration_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration_for" ):
                return visitor.visitVar_declaration_for(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration_for(self):

        localctx = MiniGoParser.Var_declaration_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_var_declaration_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MiniGoParser.VAR)
            self.state = 393
            self.match(MiniGoParser.ID)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                self.state = 394
                self.data_type()


            self.state = 397
            self.match(MiniGoParser.ASSIGN)
            self.state = 398
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(MiniGoParser.BREAK)
            self.state = 401
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_agginContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs_aggin(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_agginContext,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_aggin

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_aggin" ):
                return visitor.visitLhs_aggin(self)
            else:
                return visitor.visitChildren(self)



    def lhs_aggin(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Lhs_agginContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_lhs_aggin, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Lhs_agginContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_aggin)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 413
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LBRACKET]:
                        self.state = 407
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 408
                        self.expression(0)
                        self.state = 409
                        self.match(MiniGoParser.RBRACKET)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 411
                        self.match(MiniGoParser.DOT)
                        self.state = 412
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def lhs_aggin(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_agginContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 420
                self.lhs_aggin(0)
                self.state = 421
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 426
            self.match(MiniGoParser.ID)
            self.state = 427
            self.match(MiniGoParser.LPAREN)
            self.state = 428
            self.list_expression()
            self.state = 429
            self.match(MiniGoParser.RPAREN)
            self.state = 430
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.CONTINUE)
            self.state = 433
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(MiniGoParser.RETURN)
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.BOOLEAN_LIT, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOATING_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.state = 436
                self.expression(0)
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 440
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def FLOATING_LITERAL(self):
            return self.getToken(MiniGoParser.FLOATING_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(MiniGoParser.BOOLEAN_LIT, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_literal)
        try:
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass
            elif token in [MiniGoParser.FLOATING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.match(MiniGoParser.FLOATING_LITERAL)
                pass
            elif token in [MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 444
                self.match(MiniGoParser.STRING_LITERAL)
                pass
            elif token in [MiniGoParser.BOOLEAN_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                self.match(MiniGoParser.BOOLEAN_LIT)
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 446
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 447
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_data_type)
        try:
            self.state = 456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 453
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 454
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 6)
                self.state = 455
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.array_type()
            self.state = 459
            self.match(MiniGoParser.LBRACE)
            self.state = 460
            self.list_array_element()
            self.state = 461
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_type_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_type_arrContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.list_type_arr()

            self.state = 464
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_type_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def list_type_arr(self):
            return self.getTypedRuleContext(MiniGoParser.List_type_arrContext,0)


        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_type_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_type_arr" ):
                return visitor.visitList_type_arr(self)
            else:
                return visitor.visitChildren(self)




    def list_type_arr(self):

        localctx = MiniGoParser.List_type_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_list_type_arr)
        self._la = 0 # Token type
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(MiniGoParser.LBRACKET)
                self.state = 467
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 468
                self.match(MiniGoParser.RBRACKET)
                self.state = 469
                self.list_type_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(MiniGoParser.LBRACKET)
                self.state = 471
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 472
                self.match(MiniGoParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_element" ):
                return visitor.visitList_array_element(self)
            else:
                return visitor.visitChildren(self)




    def list_array_element(self):

        localctx = MiniGoParser.List_array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_list_array_element)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.array_element()
                self.state = 476
                self.match(MiniGoParser.COMMA)
                self.state = 477
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_param(self):
            return self.getTypedRuleContext(MiniGoParser.Array_paramContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_element)
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOATING_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.array_param()
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.match(MiniGoParser.LBRACE)
                self.state = 484
                self.list_array_element()
                self.state = 485
                self.match(MiniGoParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def FLOATING_LITERAL(self):
            return self.getToken(MiniGoParser.FLOATING_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_param" ):
                return visitor.visitArray_param(self)
            else:
                return visitor.visitChildren(self)




    def array_param(self):

        localctx = MiniGoParser.Array_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array_param)
        try:
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.match(MiniGoParser.FLOATING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 491
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 492
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 493
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 494
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 495
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 496
                self.struct_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_lit_body(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_bodyContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(MiniGoParser.ID)
            self.state = 500
            self.match(MiniGoParser.LBRACE)
            self.state = 501
            self.struct_lit_body()
            self.state = 502
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_lit_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_lit_body_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_body_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_body" ):
                return visitor.visitStruct_lit_body(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit_body(self):

        localctx = MiniGoParser.Struct_lit_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_struct_lit_body)
        try:
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.struct_lit_body_element()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_lit_body_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def struct_lit_body_element(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_lit_body_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit_body_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit_body_element" ):
                return visitor.visitStruct_lit_body_element(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit_body_element(self):

        localctx = MiniGoParser.Struct_lit_body_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_struct_lit_body_element)
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.struct_element()
                self.state = 509
                self.match(MiniGoParser.COMMA)
                self.state = 510
                self.struct_lit_body_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.struct_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_element" ):
                return visitor.visitStruct_element(self)
            else:
                return visitor.visitChildren(self)




    def struct_element(self):

        localctx = MiniGoParser.Struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_struct_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MiniGoParser.ID)
            self.state = 516
            self.match(MiniGoParser.COLON)
            self.state = 517
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_list_expression)
        try:
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.BOOLEAN_LIT, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOATING_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.params()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def params(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = MiniGoParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_params)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.expression(0)
                self.state = 524
                self.match(MiniGoParser.COMMA)
                self.state = 525
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.expression_1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 533
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 534
                    self.match(MiniGoParser.OR)
                    self.state = 535
                    self.expression_1(0) 
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_2Context,0)


        def expression_1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_1" ):
                return visitor.visitExpression_1(self)
            else:
                return visitor.visitChildren(self)



    def expression_1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expression_1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.expression_2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_1)
                    self.state = 544
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 545
                    self.match(MiniGoParser.AND)
                    self.state = 546
                    self.expression_2(0) 
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_3Context,0)


        def expression_2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_2Context,0)


        def COMPARE_OPERATOR(self):
            return self.getToken(MiniGoParser.COMPARE_OPERATOR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_2" ):
                return visitor.visitExpression_2(self)
            else:
                return visitor.visitChildren(self)



    def expression_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expression_2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.expression_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 560
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_2)
                    self.state = 555
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 556
                    self.match(MiniGoParser.COMPARE_OPERATOR)
                    self.state = 557
                    self.expression_3(0) 
                self.state = 562
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_4Context,0)


        def expression_3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_3" ):
                return visitor.visitExpression_3(self)
            else:
                return visitor.visitChildren(self)



    def expression_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_expression_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.expression_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 571
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_3)
                    self.state = 566
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 567
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 568
                    self.expression_4(0) 
                self.state = 573
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_5Context,0)


        def expression_4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_4" ):
                return visitor.visitExpression_4(self)
            else:
                return visitor.visitChildren(self)



    def expression_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_expression_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.expression_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 582
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_4)
                    self.state = 577
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 578
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 579
                    self.expression_5() 
                self.state = 584
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression_6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_5" ):
                return visitor.visitExpression_5(self)
            else:
                return visitor.visitChildren(self)




    def expression_5(self):

        localctx = MiniGoParser.Expression_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_expression_5)
        self._la = 0 # Token type
        try:
            self.state = 588
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 586
                self.expression_5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.BOOLEAN_LIT, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOATING_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 587
                self.expression_6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_7Context,0)


        def expression_6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_6Context,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_6" ):
                return visitor.visitExpression_6(self)
            else:
                return visitor.visitChildren(self)



    def expression_6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression_6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expression_6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.expression_7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 606
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 604
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression_6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_6)
                        self.state = 593
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 594
                        self.match(MiniGoParser.LBRACKET)

                        self.state = 595
                        self.expression(0)
                        self.state = 596
                        self.match(MiniGoParser.RBRACKET)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression_6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_6)
                        self.state = 598
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 599
                        self.match(MiniGoParser.DOT)
                        self.state = 602
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                        if la_ == 1:
                            self.state = 600
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 601
                            self.func_call()
                            pass


                        pass

             
                self.state = 608
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_7" ):
                return visitor.visitExpression_7(self)
            else:
                return visitor.visitChildren(self)




    def expression_7(self):

        localctx = MiniGoParser.Expression_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_expression_7)
        try:
            self.state = 619
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 609
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 611
                self.match(MiniGoParser.LPAREN)
                self.state = 612
                self.expression(0)
                self.state = 613
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 615
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 616
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 617
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 618
                self.match(MiniGoParser.NIL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(MiniGoParser.ID)
            self.state = 622
            self.match(MiniGoParser.LPAREN)
            self.state = 623
            self.list_expression()
            self.state = 624
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.assignment_lhs_sempred
        self._predicates[37] = self.lhs_aggin_sempred
        self._predicates[55] = self.expression_sempred
        self._predicates[56] = self.expression_1_sempred
        self._predicates[57] = self.expression_2_sempred
        self._predicates[58] = self.expression_3_sempred
        self._predicates[59] = self.expression_4_sempred
        self._predicates[61] = self.expression_6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def assignment_lhs_sempred(self, localctx:Assignment_lhsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def lhs_aggin_sempred(self, localctx:Lhs_agginContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression_1_sempred(self, localctx:Expression_1Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression_2_sempred(self, localctx:Expression_2Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression_3_sempred(self, localctx:Expression_3Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expression_4_sempred(self, localctx:Expression_4Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expression_6_sempred(self, localctx:Expression_6Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




