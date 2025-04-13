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
        buf.write("\u0294\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3\u008c\n\3\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u0093\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u009b\n\5\3\6")
        buf.write("\3\6\5\6\u009f\n\6\3\7\3\7\3\7\3\7\5\7\u00a5\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u00b5\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00bd\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00ca")
        buf.write("\n\13\3\13\3\13\5\13\u00ce\n\13\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00e8\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u00f3")
        buf.write("\n\21\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00fb\n\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u0103\n\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\5\24\u010c\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u0113\n\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u011c\n\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u012a\n\31\3\32")
        buf.write("\3\32\3\32\5\32\u012f\n\32\3\32\3\32\3\32\5\32\u0134\n")
        buf.write("\32\3\32\3\32\3\33\3\33\5\33\u013a\n\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u0140\n\33\3\34\3\34\3\35\3\35\3\35\5\35\u0147")
        buf.write("\n\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0157\n\36\7\36\u0159\n\36\f")
        buf.write("\36\16\36\u015c\13\36\3\37\3\37\3\37\5\37\u0161\n\37\3")
        buf.write("\37\3\37\3\37\5\37\u0166\n\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5")
        buf.write("!\u0180\n!\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u0189\n#\3#\3#")
        buf.write("\3$\3$\3$\3$\3$\3$\3%\3%\3%\5%\u0196\n%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\5(\u01b3\n(\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01c5\n*\7*\u01c7\n*\f*\16")
        buf.write("*\u01ca\13*\3+\3+\3+\3+\5+\u01d0\n+\3+\3+\3+\3+\3+\3+")
        buf.write("\3,\3,\3,\3-\3-\3-\5-\u01de\n-\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01ef\n\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\5\61\u01f6\n\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u01fd\n\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u0207\n\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\5\65\u0210\n\65\3\66\3\66\3\66\3\66\3\66\5")
        buf.write("\66\u0217\n\66\3\67\3\67\3\67\3\67\5\67\u021d\n\67\38")
        buf.write("\38\58\u0221\n8\39\39\39\39\39\59\u0228\n9\3:\3:\3:\3")
        buf.write(":\3:\3:\7:\u0230\n:\f:\16:\u0233\13:\3;\3;\3;\3;\3;\3")
        buf.write(";\7;\u023b\n;\f;\16;\u023e\13;\3<\3<\3<\3<\3<\3<\7<\u0246")
        buf.write("\n<\f<\16<\u0249\13<\3=\3=\3=\3=\3=\3=\7=\u0251\n=\f=")
        buf.write("\16=\u0254\13=\3>\3>\3>\3>\3>\3>\7>\u025c\n>\f>\16>\u025f")
        buf.write("\13>\3?\3?\3?\5?\u0264\n?\3@\3@\3@\3@\3@\3@\3@\3@\5@\u026e")
        buf.write("\n@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u027c\n@\7")
        buf.write("@\u027e\n@\f@\16@\u0281\13@\3A\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\3A\5A\u028d\nA\3B\3B\3B\3B\3B\3B\2\n:Rrtvxz~C\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\2\b")
        buf.write("\4\2&&(,\5\2\35\35&&(,\4\2\67\6799\3\2\30\31\3\2\32\34")
        buf.write("\4\2\31\31%%\2\u02a7\2\u0084\3\2\2\2\4\u008b\3\2\2\2\6")
        buf.write("\u0092\3\2\2\2\b\u009a\3\2\2\2\n\u009e\3\2\2\2\f\u00a4")
        buf.write("\3\2\2\2\16\u00b4\3\2\2\2\20\u00bc\3\2\2\2\22\u00be\3")
        buf.write("\2\2\2\24\u00c3\3\2\2\2\26\u00cf\3\2\2\2\30\u00d2\3\2")
        buf.write("\2\2\32\u00d5\3\2\2\2\34\u00e7\3\2\2\2\36\u00e9\3\2\2")
        buf.write("\2 \u00f2\3\2\2\2\"\u00f4\3\2\2\2$\u00f7\3\2\2\2&\u010b")
        buf.write("\3\2\2\2(\u0112\3\2\2\2*\u0114\3\2\2\2,\u011b\3\2\2\2")
        buf.write(".\u011d\3\2\2\2\60\u0129\3\2\2\2\62\u012b\3\2\2\2\64\u013f")
        buf.write("\3\2\2\2\66\u0141\3\2\2\28\u0143\3\2\2\2:\u014c\3\2\2")
        buf.write("\2<\u015d\3\2\2\2>\u0169\3\2\2\2@\u017f\3\2\2\2B\u0181")
        buf.write("\3\2\2\2D\u0188\3\2\2\2F\u018c\3\2\2\2H\u0192\3\2\2\2")
        buf.write("J\u019f\3\2\2\2L\u01aa\3\2\2\2N\u01ae\3\2\2\2P\u01b7\3")
        buf.write("\2\2\2R\u01ba\3\2\2\2T\u01cf\3\2\2\2V\u01d7\3\2\2\2X\u01da")
        buf.write("\3\2\2\2Z\u01e1\3\2\2\2\\\u01e4\3\2\2\2^\u01ee\3\2\2\2")
        buf.write("`\u01f5\3\2\2\2b\u01fc\3\2\2\2d\u0206\3\2\2\2f\u0208\3")
        buf.write("\2\2\2h\u020f\3\2\2\2j\u0216\3\2\2\2l\u021c\3\2\2\2n\u0220")
        buf.write("\3\2\2\2p\u0227\3\2\2\2r\u0229\3\2\2\2t\u0234\3\2\2\2")
        buf.write("v\u023f\3\2\2\2x\u024a\3\2\2\2z\u0255\3\2\2\2|\u0263\3")
        buf.write("\2\2\2~\u0265\3\2\2\2\u0080\u028c\3\2\2\2\u0082\u028e")
        buf.write("\3\2\2\2\u0084\u0085\5\4\3\2\u0085\u0086\7\2\2\3\u0086")
        buf.write("\3\3\2\2\2\u0087\u0088\5\6\4\2\u0088\u0089\5\4\3\2\u0089")
        buf.write("\u008c\3\2\2\2\u008a\u008c\5\6\4\2\u008b\u0087\3\2\2\2")
        buf.write("\u008b\u008a\3\2\2\2\u008c\5\3\2\2\2\u008d\u0093\5\26")
        buf.write("\f\2\u008e\u0093\5\30\r\2\u008f\u0093\5$\23\2\u0090\u0093")
        buf.write("\5\32\16\2\u0091\u0093\5.\30\2\u0092\u008d\3\2\2\2\u0092")
        buf.write("\u008e\3\2\2\2\u0092\u008f\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0091\3\2\2\2\u0093\7\3\2\2\2\u0094\u009b\79\2")
        buf.write("\2\u0095\u009b\7>\2\2\u0096\u009b\7?\2\2\u0097\u009b\7")
        buf.write("8\2\2\u0098\u009b\5Z.\2\u0099\u009b\5f\64\2\u009a\u0094")
        buf.write("\3\2\2\2\u009a\u0095\3\2\2\2\u009a\u0096\3\2\2\2\u009a")
        buf.write("\u0097\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2")
        buf.write("\u009b\t\3\2\2\2\u009c\u009f\5\f\7\2\u009d\u009f\3\2\2")
        buf.write("\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\13\3")
        buf.write("\2\2\2\u00a0\u00a1\5\16\b\2\u00a1\u00a2\5\f\7\2\u00a2")
        buf.write("\u00a5\3\2\2\2\u00a3\u00a5\5\16\b\2\u00a4\u00a0\3\2\2")
        buf.write("\2\u00a4\u00a3\3\2\2\2\u00a5\r\3\2\2\2\u00a6\u00a7\5\22")
        buf.write("\n\2\u00a7\u00a8\7\66\2\2\u00a8\u00b5\3\2\2\2\u00a9\u00aa")
        buf.write("\5\24\13\2\u00aa\u00ab\7\66\2\2\u00ab\u00b5\3\2\2\2\u00ac")
        buf.write("\u00b5\58\35\2\u00ad\u00b5\5<\37\2\u00ae\u00b5\5D#\2\u00af")
        buf.write("\u00b5\5P)\2\u00b0\u00b5\5V,\2\u00b1\u00b5\5\u0082B\2")
        buf.write("\u00b2\u00b5\5T+\2\u00b3\u00b5\5X-\2\u00b4\u00a6\3\2\2")
        buf.write("\2\u00b4\u00a9\3\2\2\2\u00b4\u00ac\3\2\2\2\u00b4\u00ad")
        buf.write("\3\2\2\2\u00b4\u00ae\3\2\2\2\u00b4\u00af\3\2\2\2\u00b4")
        buf.write("\u00b0\3\2\2\2\u00b4\u00b1\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b4\u00b3\3\2\2\2\u00b5\17\3\2\2\2\u00b6\u00bd\7\67")
        buf.write("\2\2\u00b7\u00bd\7\r\2\2\u00b8\u00bd\7\16\2\2\u00b9\u00bd")
        buf.write("\7\27\2\2\u00ba\u00bd\7\f\2\2\u00bb\u00bd\5\\/\2\u00bc")
        buf.write("\u00b6\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bc\u00b8\3\2\2\2")
        buf.write("\u00bc\u00b9\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3")
        buf.write("\2\2\2\u00bd\21\3\2\2\2\u00be\u00bf\7\17\2\2\u00bf\u00c0")
        buf.write("\7\67\2\2\u00c0\u00c1\7\'\2\2\u00c1\u00c2\5r:\2\u00c2")
        buf.write("\23\3\2\2\2\u00c3\u00c4\7\20\2\2\u00c4\u00cd\7\67\2\2")
        buf.write("\u00c5\u00c9\5\20\t\2\u00c6\u00c7\7\'\2\2\u00c7\u00ca")
        buf.write("\5r:\2\u00c8\u00ca\3\2\2\2\u00c9\u00c6\3\2\2\2\u00c9\u00c8")
        buf.write("\3\2\2\2\u00ca\u00ce\3\2\2\2\u00cb\u00cc\7\'\2\2\u00cc")
        buf.write("\u00ce\5r:\2\u00cd\u00c5\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce")
        buf.write("\25\3\2\2\2\u00cf\u00d0\5\24\13\2\u00d0\u00d1\7\66\2\2")
        buf.write("\u00d1\27\3\2\2\2\u00d2\u00d3\5\22\n\2\u00d3\u00d4\7\66")
        buf.write("\2\2\u00d4\31\3\2\2\2\u00d5\u00d6\7\t\2\2\u00d6\u00d7")
        buf.write("\7\67\2\2\u00d7\u00d8\7\n\2\2\u00d8\u00d9\7\61\2\2\u00d9")
        buf.write("\u00da\5\34\17\2\u00da\u00db\7\62\2\2\u00db\u00dc\7\66")
        buf.write("\2\2\u00dc\33\3\2\2\2\u00dd\u00de\7\67\2\2\u00de\u00df")
        buf.write("\5\20\t\2\u00df\u00e0\7\66\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("\u00e2\5\34\17\2\u00e2\u00e8\3\2\2\2\u00e3\u00e4\7\67")
        buf.write("\2\2\u00e4\u00e5\5\20\t\2\u00e5\u00e6\7\66\2\2\u00e6\u00e8")
        buf.write("\3\2\2\2\u00e7\u00dd\3\2\2\2\u00e7\u00e3\3\2\2\2\u00e8")
        buf.write("\35\3\2\2\2\u00e9\u00ea\7/\2\2\u00ea\u00eb\5 \21\2\u00eb")
        buf.write("\u00ec\7\60\2\2\u00ec\37\3\2\2\2\u00ed\u00ee\5\"\22\2")
        buf.write("\u00ee\u00ef\7\65\2\2\u00ef\u00f0\5 \21\2\u00f0\u00f3")
        buf.write("\3\2\2\2\u00f1\u00f3\5\"\22\2\u00f2\u00ed\3\2\2\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f3!\3\2\2\2\u00f4\u00f5\7\67\2\2\u00f5")
        buf.write("\u00f6\7\67\2\2\u00f6#\3\2\2\2\u00f7\u00fa\7\b\2\2\u00f8")
        buf.write("\u00fb\5\36\20\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2")
        buf.write("\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd")
        buf.write("\7\67\2\2\u00fd\u00fe\7/\2\2\u00fe\u00ff\5&\24\2\u00ff")
        buf.write("\u0102\7\60\2\2\u0100\u0103\5\20\t\2\u0101\u0103\3\2\2")
        buf.write("\2\u0102\u0100\3\2\2\2\u0102\u0101\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0105\7\61\2\2\u0105\u0106\5\n\6\2\u0106")
        buf.write("\u0107\7\62\2\2\u0107\u0108\7\66\2\2\u0108%\3\2\2\2\u0109")
        buf.write("\u010c\5(\25\2\u010a\u010c\3\2\2\2\u010b\u0109\3\2\2\2")
        buf.write("\u010b\u010a\3\2\2\2\u010c\'\3\2\2\2\u010d\u010e\5*\26")
        buf.write("\2\u010e\u010f\7\65\2\2\u010f\u0110\5(\25\2\u0110\u0113")
        buf.write("\3\2\2\2\u0111\u0113\5*\26\2\u0112\u010d\3\2\2\2\u0112")
        buf.write("\u0111\3\2\2\2\u0113)\3\2\2\2\u0114\u0115\5,\27\2\u0115")
        buf.write("\u0116\5\20\t\2\u0116+\3\2\2\2\u0117\u0118\7\67\2\2\u0118")
        buf.write("\u0119\7\65\2\2\u0119\u011c\5,\27\2\u011a\u011c\7\67\2")
        buf.write("\2\u011b\u0117\3\2\2\2\u011b\u011a\3\2\2\2\u011c-\3\2")
        buf.write("\2\2\u011d\u011e\7\t\2\2\u011e\u011f\7\67\2\2\u011f\u0120")
        buf.write("\7\13\2\2\u0120\u0121\7\61\2\2\u0121\u0122\5\60\31\2\u0122")
        buf.write("\u0123\7\62\2\2\u0123\u0124\7\66\2\2\u0124/\3\2\2\2\u0125")
        buf.write("\u0126\5\62\32\2\u0126\u0127\5\60\31\2\u0127\u012a\3\2")
        buf.write("\2\2\u0128\u012a\5\62\32\2\u0129\u0125\3\2\2\2\u0129\u0128")
        buf.write("\3\2\2\2\u012a\61\3\2\2\2\u012b\u012c\7\67\2\2\u012c\u012e")
        buf.write("\7/\2\2\u012d\u012f\5\64\33\2\u012e\u012d\3\2\2\2\u012e")
        buf.write("\u012f\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0133\7\60\2")
        buf.write("\2\u0131\u0134\5\20\t\2\u0132\u0134\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0133\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u0136\7\66\2\2\u0136\63\3\2\2\2\u0137\u0139\7\67\2\2")
        buf.write("\u0138\u013a\5\20\t\2\u0139\u0138\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\7\65\2\2\u013c")
        buf.write("\u0140\5\64\33\2\u013d\u013e\7\67\2\2\u013e\u0140\5\20")
        buf.write("\t\2\u013f\u0137\3\2\2\2\u013f\u013d\3\2\2\2\u0140\65")
        buf.write("\3\2\2\2\u0141\u0142\t\2\2\2\u0142\67\3\2\2\2\u0143\u0146")
        buf.write("\5:\36\2\u0144\u0147\5\66\34\2\u0145\u0147\7\35\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u0149\5r:\2\u0149\u014a\3\2\2\2\u014a\u014b\7\66")
        buf.write("\2\2\u014b9\3\2\2\2\u014c\u014d\b\36\1\2\u014d\u014e\7")
        buf.write("\67\2\2\u014e\u015a\3\2\2\2\u014f\u0156\f\4\2\2\u0150")
        buf.write("\u0151\7-\2\2\u0151\u0157\7\67\2\2\u0152\u0153\7\63\2")
        buf.write("\2\u0153\u0154\5r:\2\u0154\u0155\7\64\2\2\u0155\u0157")
        buf.write("\3\2\2\2\u0156\u0150\3\2\2\2\u0156\u0152\3\2\2\2\u0157")
        buf.write("\u0159\3\2\2\2\u0158\u014f\3\2\2\2\u0159\u015c\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b;\3\2\2")
        buf.write("\2\u015c\u015a\3\2\2\2\u015d\u0160\5> \2\u015e\u0161\5")
        buf.write("@!\2\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161\u0165\3\2\2\2\u0162\u0163\7\5\2\2\u0163")
        buf.write("\u0166\5B\"\2\u0164\u0166\3\2\2\2\u0165\u0162\3\2\2\2")
        buf.write("\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\7")
        buf.write("\66\2\2\u0168=\3\2\2\2\u0169\u016a\7\4\2\2\u016a\u016b")
        buf.write("\7/\2\2\u016b\u016c\5r:\2\u016c\u016d\7\60\2\2\u016d\u016e")
        buf.write("\5B\"\2\u016e?\3\2\2\2\u016f\u0170\7\5\2\2\u0170\u0171")
        buf.write("\7\4\2\2\u0171\u0172\7/\2\2\u0172\u0173\5r:\2\u0173\u0174")
        buf.write("\7\60\2\2\u0174\u0175\5B\"\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0177\5@!\2\u0177\u0180\3\2\2\2\u0178\u0179\7\5\2\2\u0179")
        buf.write("\u017a\7\4\2\2\u017a\u017b\7/\2\2\u017b\u017c\5r:\2\u017c")
        buf.write("\u017d\7\60\2\2\u017d\u017e\5B\"\2\u017e\u0180\3\2\2\2")
        buf.write("\u017f\u016f\3\2\2\2\u017f\u0178\3\2\2\2\u0180A\3\2\2")
        buf.write("\2\u0181\u0182\7\61\2\2\u0182\u0183\5\n\6\2\u0183\u0184")
        buf.write("\7\62\2\2\u0184C\3\2\2\2\u0185\u0189\5F$\2\u0186\u0189")
        buf.write("\5H%\2\u0187\u0189\5J&\2\u0188\u0185\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018b\7\66\2\2\u018bE\3\2\2\2\u018c\u018d\7\6\2\2\u018d")
        buf.write("\u018e\5r:\2\u018e\u018f\7\61\2\2\u018f\u0190\5\n\6\2")
        buf.write("\u0190\u0191\7\62\2\2\u0191G\3\2\2\2\u0192\u0195\7\6\2")
        buf.write("\2\u0193\u0196\5N(\2\u0194\u0196\5L\'\2\u0195\u0193\3")
        buf.write("\2\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198")
        buf.write("\7\66\2\2\u0198\u0199\5r:\2\u0199\u019a\7\66\2\2\u019a")
        buf.write("\u019b\5L\'\2\u019b\u019c\7\61\2\2\u019c\u019d\5\n\6\2")
        buf.write("\u019d\u019e\7\62\2\2\u019eI\3\2\2\2\u019f\u01a0\7\6\2")
        buf.write("\2\u01a0\u01a1\7\67\2\2\u01a1\u01a2\7\65\2\2\u01a2\u01a3")
        buf.write("\7\67\2\2\u01a3\u01a4\7&\2\2\u01a4\u01a5\7\23\2\2\u01a5")
        buf.write("\u01a6\5r:\2\u01a6\u01a7\7\61\2\2\u01a7\u01a8\5\n\6\2")
        buf.write("\u01a8\u01a9\7\62\2\2\u01a9K\3\2\2\2\u01aa\u01ab\7\67")
        buf.write("\2\2\u01ab\u01ac\t\3\2\2\u01ac\u01ad\5r:\2\u01adM\3\2")
        buf.write("\2\2\u01ae\u01af\7\20\2\2\u01af\u01b2\7\67\2\2\u01b0\u01b3")
        buf.write("\5\20\t\2\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\7\'\2\2")
        buf.write("\u01b5\u01b6\5r:\2\u01b6O\3\2\2\2\u01b7\u01b8\7\22\2\2")
        buf.write("\u01b8\u01b9\7\66\2\2\u01b9Q\3\2\2\2\u01ba\u01bb\b*\1")
        buf.write("\2\u01bb\u01bc\7\67\2\2\u01bc\u01c8\3\2\2\2\u01bd\u01c4")
        buf.write("\f\4\2\2\u01be\u01bf\7\63\2\2\u01bf\u01c0\5r:\2\u01c0")
        buf.write("\u01c1\7\64\2\2\u01c1\u01c5\3\2\2\2\u01c2\u01c3\7-\2\2")
        buf.write("\u01c3\u01c5\7\67\2\2\u01c4\u01be\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01bd\3\2\2\2\u01c7")
        buf.write("\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9S\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\5R*\2")
        buf.write("\u01cc\u01cd\7-\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01d0\3")
        buf.write("\2\2\2\u01cf\u01cb\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1\u01d2\7\67\2\2\u01d2\u01d3\7/\2\2\u01d3")
        buf.write("\u01d4\5n8\2\u01d4\u01d5\7\60\2\2\u01d5\u01d6\7\66\2\2")
        buf.write("\u01d6U\3\2\2\2\u01d7\u01d8\7\21\2\2\u01d8\u01d9\7\66")
        buf.write("\2\2\u01d9W\3\2\2\2\u01da\u01dd\7\7\2\2\u01db\u01de\5")
        buf.write("r:\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\7\66\2\2\u01e0")
        buf.write("Y\3\2\2\2\u01e1\u01e2\5\\/\2\u01e2\u01e3\5`\61\2\u01e3")
        buf.write("[\3\2\2\2\u01e4\u01e5\5^\60\2\u01e5\u01e6\5\20\t\2\u01e6")
        buf.write("]\3\2\2\2\u01e7\u01e8\7\63\2\2\u01e8\u01e9\t\4\2\2\u01e9")
        buf.write("\u01ea\7\64\2\2\u01ea\u01ef\5^\60\2\u01eb\u01ec\7\63\2")
        buf.write("\2\u01ec\u01ed\t\4\2\2\u01ed\u01ef\7\64\2\2\u01ee\u01e7")
        buf.write("\3\2\2\2\u01ee\u01eb\3\2\2\2\u01ef_\3\2\2\2\u01f0\u01f1")
        buf.write("\7\61\2\2\u01f1\u01f2\5b\62\2\u01f2\u01f3\7\62\2\2\u01f3")
        buf.write("\u01f6\3\2\2\2\u01f4\u01f6\5d\63\2\u01f5\u01f0\3\2\2\2")
        buf.write("\u01f5\u01f4\3\2\2\2\u01f6a\3\2\2\2\u01f7\u01f8\5`\61")
        buf.write("\2\u01f8\u01f9\7\65\2\2\u01f9\u01fa\5b\62\2\u01fa\u01fd")
        buf.write("\3\2\2\2\u01fb\u01fd\5`\61\2\u01fc\u01f7\3\2\2\2\u01fc")
        buf.write("\u01fb\3\2\2\2\u01fdc\3\2\2\2\u01fe\u0207\79\2\2\u01ff")
        buf.write("\u0207\7>\2\2\u0200\u0207\7?\2\2\u0201\u0207\7\25\2\2")
        buf.write("\u0202\u0207\7\26\2\2\u0203\u0207\7\24\2\2\u0204\u0207")
        buf.write("\7\67\2\2\u0205\u0207\5f\64\2\u0206\u01fe\3\2\2\2\u0206")
        buf.write("\u01ff\3\2\2\2\u0206\u0200\3\2\2\2\u0206\u0201\3\2\2\2")
        buf.write("\u0206\u0202\3\2\2\2\u0206\u0203\3\2\2\2\u0206\u0204\3")
        buf.write("\2\2\2\u0206\u0205\3\2\2\2\u0207e\3\2\2\2\u0208\u0209")
        buf.write("\7\67\2\2\u0209\u020a\7\61\2\2\u020a\u020b\5h\65\2\u020b")
        buf.write("\u020c\7\62\2\2\u020cg\3\2\2\2\u020d\u0210\5j\66\2\u020e")
        buf.write("\u0210\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u020e\3\2\2\2")
        buf.write("\u0210i\3\2\2\2\u0211\u0212\5l\67\2\u0212\u0213\7\65\2")
        buf.write("\2\u0213\u0214\5j\66\2\u0214\u0217\3\2\2\2\u0215\u0217")
        buf.write("\5l\67\2\u0216\u0211\3\2\2\2\u0216\u0215\3\2\2\2\u0217")
        buf.write("k\3\2\2\2\u0218\u0219\7\67\2\2\u0219\u021a\7.\2\2\u021a")
        buf.write("\u021d\5r:\2\u021b\u021d\5$\23\2\u021c\u0218\3\2\2\2\u021c")
        buf.write("\u021b\3\2\2\2\u021dm\3\2\2\2\u021e\u0221\5p9\2\u021f")
        buf.write("\u0221\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u021f\3\2\2\2")
        buf.write("\u0221o\3\2\2\2\u0222\u0223\5r:\2\u0223\u0224\7\65\2\2")
        buf.write("\u0224\u0225\5p9\2\u0225\u0228\3\2\2\2\u0226\u0228\5r")
        buf.write(":\2\u0227\u0222\3\2\2\2\u0227\u0226\3\2\2\2\u0228q\3\2")
        buf.write("\2\2\u0229\u022a\b:\1\2\u022a\u022b\5t;\2\u022b\u0231")
        buf.write("\3\2\2\2\u022c\u022d\f\4\2\2\u022d\u022e\7$\2\2\u022e")
        buf.write("\u0230\5t;\2\u022f\u022c\3\2\2\2\u0230\u0233\3\2\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232s\3\2\2\2\u0233")
        buf.write("\u0231\3\2\2\2\u0234\u0235\b;\1\2\u0235\u0236\5v<\2\u0236")
        buf.write("\u023c\3\2\2\2\u0237\u0238\f\4\2\2\u0238\u0239\7#\2\2")
        buf.write("\u0239\u023b\5v<\2\u023a\u0237\3\2\2\2\u023b\u023e\3\2")
        buf.write("\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023du\3")
        buf.write("\2\2\2\u023e\u023c\3\2\2\2\u023f\u0240\b<\1\2\u0240\u0241")
        buf.write("\5x=\2\u0241\u0247\3\2\2\2\u0242\u0243\f\4\2\2\u0243\u0244")
        buf.write("\7\3\2\2\u0244\u0246\5x=\2\u0245\u0242\3\2\2\2\u0246\u0249")
        buf.write("\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248")
        buf.write("w\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\b=\1\2\u024b")
        buf.write("\u024c\5z>\2\u024c\u0252\3\2\2\2\u024d\u024e\f\4\2\2\u024e")
        buf.write("\u024f\t\5\2\2\u024f\u0251\5z>\2\u0250\u024d\3\2\2\2\u0251")
        buf.write("\u0254\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253\3\2\2\2")
        buf.write("\u0253y\3\2\2\2\u0254\u0252\3\2\2\2\u0255\u0256\b>\1\2")
        buf.write("\u0256\u0257\5|?\2\u0257\u025d\3\2\2\2\u0258\u0259\f\4")
        buf.write("\2\2\u0259\u025a\t\6\2\2\u025a\u025c\5|?\2\u025b\u0258")
        buf.write("\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b\3\2\2\2\u025d")
        buf.write("\u025e\3\2\2\2\u025e{\3\2\2\2\u025f\u025d\3\2\2\2\u0260")
        buf.write("\u0261\t\7\2\2\u0261\u0264\5|?\2\u0262\u0264\5~@\2\u0263")
        buf.write("\u0260\3\2\2\2\u0263\u0262\3\2\2\2\u0264}\3\2\2\2\u0265")
        buf.write("\u0266\b@\1\2\u0266\u0267\5\u0080A\2\u0267\u027f\3\2\2")
        buf.write("\2\u0268\u026d\f\5\2\2\u0269\u026a\7/\2\2\u026a\u026b")
        buf.write("\5r:\2\u026b\u026c\7\60\2\2\u026c\u026e\3\2\2\2\u026d")
        buf.write("\u0269\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u026f\3\2\2\2")
        buf.write("\u026f\u0270\7\63\2\2\u0270\u0271\5r:\2\u0271\u0272\7")
        buf.write("\64\2\2\u0272\u027e\3\2\2\2\u0273\u0274\f\4\2\2\u0274")
        buf.write("\u027b\7-\2\2\u0275\u027c\7\67\2\2\u0276\u0277\7\67\2")
        buf.write("\2\u0277\u0278\7/\2\2\u0278\u0279\5n8\2\u0279\u027a\7")
        buf.write("\60\2\2\u027a\u027c\3\2\2\2\u027b\u0275\3\2\2\2\u027b")
        buf.write("\u0276\3\2\2\2\u027c\u027e\3\2\2\2\u027d\u0268\3\2\2\2")
        buf.write("\u027d\u0273\3\2\2\2\u027e\u0281\3\2\2\2\u027f\u027d\3")
        buf.write("\2\2\2\u027f\u0280\3\2\2\2\u0280\177\3\2\2\2\u0281\u027f")
        buf.write("\3\2\2\2\u0282\u028d\7\67\2\2\u0283\u028d\5\b\5\2\u0284")
        buf.write("\u0285\7/\2\2\u0285\u0286\5r:\2\u0286\u0287\7\60\2\2\u0287")
        buf.write("\u028d\3\2\2\2\u0288\u028d\5\u0082B\2\u0289\u028d\7\25")
        buf.write("\2\2\u028a\u028d\7\26\2\2\u028b\u028d\7\24\2\2\u028c\u0282")
        buf.write("\3\2\2\2\u028c\u0283\3\2\2\2\u028c\u0284\3\2\2\2\u028c")
        buf.write("\u0288\3\2\2\2\u028c\u0289\3\2\2\2\u028c\u028a\3\2\2\2")
        buf.write("\u028c\u028b\3\2\2\2\u028d\u0081\3\2\2\2\u028e\u028f\7")
        buf.write("\67\2\2\u028f\u0290\7/\2\2\u0290\u0291\5n8\2\u0291\u0292")
        buf.write("\7\60\2\2\u0292\u0083\3\2\2\28\u008b\u0092\u009a\u009e")
        buf.write("\u00a4\u00b4\u00bc\u00c9\u00cd\u00e7\u00f2\u00fa\u0102")
        buf.write("\u010b\u0112\u011b\u0129\u012e\u0133\u0139\u013f\u0146")
        buf.write("\u0156\u015a\u0160\u0165\u017f\u0188\u0195\u01b2\u01c4")
        buf.write("\u01c8\u01cf\u01dd\u01ee\u01f5\u01fc\u0206\u020f\u0216")
        buf.write("\u021c\u0220\u0227\u0231\u023c\u0247\u0252\u025d\u0263")
        buf.write("\u026d\u027b\u027d\u027f\u028c")
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
    RULE_literal = 3
    RULE_list_statement_primary = 4
    RULE_list_statement = 5
    RULE_statement = 6
    RULE_data_type = 7
    RULE_const_declaration = 8
    RULE_var_declaration = 9
    RULE_var_declaration_global = 10
    RULE_const_declaration_global = 11
    RULE_struct_declaration = 12
    RULE_data_struct = 13
    RULE_method_declaration = 14
    RULE_list_method_element = 15
    RULE_method_element = 16
    RULE_func_declaration = 17
    RULE_list_func_arguments = 18
    RULE_list_agruments = 19
    RULE_func_agrument = 20
    RULE_data_element = 21
    RULE_interface_declaration = 22
    RULE_list_method_interface = 23
    RULE_inter_method = 24
    RULE_list_interface_element = 25
    RULE_assign_oprator = 26
    RULE_assign_statement = 27
    RULE_dot_id = 28
    RULE_if_statement = 29
    RULE_if_stmt = 30
    RULE_elseif_list = 31
    RULE_block_statement = 32
    RULE_for_statement = 33
    RULE_for_basic = 34
    RULE_for_loop_basic = 35
    RULE_for_loop_range = 36
    RULE_assignment_for = 37
    RULE_var_declaration_for = 38
    RULE_break_statement = 39
    RULE_lhs_aggin = 40
    RULE_call_statement = 41
    RULE_continue_statement = 42
    RULE_return_statement = 43
    RULE_array_literal = 44
    RULE_array_type = 45
    RULE_list_type_arr = 46
    RULE_arrayInit = 47
    RULE_list_array_value = 48
    RULE_array_element = 49
    RULE_struct_literal = 50
    RULE_struct_lit_body = 51
    RULE_struct_lit_body_element = 52
    RULE_struct_element = 53
    RULE_list_expression = 54
    RULE_params = 55
    RULE_expression = 56
    RULE_expression_1 = 57
    RULE_expression_2 = 58
    RULE_expression_3 = 59
    RULE_expression_4 = 60
    RULE_expression_5 = 61
    RULE_expression_6 = 62
    RULE_expression_7 = 63
    RULE_func_call = 64

    ruleNames =  [ "program", "list_declaration", "declaration", "literal", 
                   "list_statement_primary", "list_statement", "statement", 
                   "data_type", "const_declaration", "var_declaration", 
                   "var_declaration_global", "const_declaration_global", 
                   "struct_declaration", "data_struct", "method_declaration", 
                   "list_method_element", "method_element", "func_declaration", 
                   "list_func_arguments", "list_agruments", "func_agrument", 
                   "data_element", "interface_declaration", "list_method_interface", 
                   "inter_method", "list_interface_element", "assign_oprator", 
                   "assign_statement", "dot_id", "if_statement", "if_stmt", 
                   "elseif_list", "block_statement", "for_statement", "for_basic", 
                   "for_loop_basic", "for_loop_range", "assignment_for", 
                   "var_declaration_for", "break_statement", "lhs_aggin", 
                   "call_statement", "continue_statement", "return_statement", 
                   "array_literal", "array_type", "list_type_arr", "arrayInit", 
                   "list_array_value", "array_element", "struct_literal", 
                   "struct_lit_body", "struct_lit_body_element", "struct_element", 
                   "list_expression", "params", "expression", "expression_1", 
                   "expression_2", "expression_3", "expression_4", "expression_5", 
                   "expression_6", "expression_7", "func_call" ]

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
            self.state = 130
            self.list_declaration()
            self.state = 131
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.declaration()
                self.state = 134
                self.list_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
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

        def var_declaration_global(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaration_globalContext,0)


        def const_declaration_global(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declaration_globalContext,0)


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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.var_declaration_global()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.const_declaration_global()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.func_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.struct_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.interface_declaration()
                pass


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
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass
            elif token in [MiniGoParser.FLOATING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(MiniGoParser.FLOATING_LITERAL)
                pass
            elif token in [MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(MiniGoParser.STRING_LITERAL)
                pass
            elif token in [MiniGoParser.BOOLEAN_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(MiniGoParser.BOOLEAN_LIT)
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
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
        self.enterRule(localctx, 8, self.RULE_list_statement_primary)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
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
        self.enterRule(localctx, 10, self.RULE_list_statement)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.statement()
                self.state = 159
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
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


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 164
                self.const_declaration()
                self.state = 165
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.state = 167
                self.var_declaration()
                self.state = 168
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.state = 170
                self.assign_statement()
                pass

            elif la_ == 4:
                self.state = 171
                self.if_statement()
                pass

            elif la_ == 5:
                self.state = 172
                self.for_statement()
                pass

            elif la_ == 6:
                self.state = 173
                self.break_statement()
                pass

            elif la_ == 7:
                self.state = 174
                self.continue_statement()
                pass

            elif la_ == 8:
                self.state = 175
                self.func_call()
                pass

            elif la_ == 9:
                self.state = 176
                self.call_statement()
                pass

            elif la_ == 10:
                self.state = 177
                self.return_statement()
                pass


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
        self.enterRule(localctx, 14, self.RULE_data_type)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 6)
                self.state = 185
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declaration" ):
                return visitor.visitConst_declaration(self)
            else:
                return visitor.visitChildren(self)




    def const_declaration(self):

        localctx = MiniGoParser.Const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_const_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MiniGoParser.CONST)
            self.state = 189
            self.match(MiniGoParser.ID)
            self.state = 190
            self.match(MiniGoParser.ASSIGN)
            self.state = 191
            self.expression(0)
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
        self.enterRule(localctx, 18, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.VAR)
            self.state = 194
            self.match(MiniGoParser.ID)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 195
                self.data_type()
                self.state = 199
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ASSIGN]:
                    self.state = 196
                    self.match(MiniGoParser.ASSIGN)

                    self.state = 197
                    self.expression(0)
                    pass
                elif token in [MiniGoParser.SEMICOLON]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 201
                self.match(MiniGoParser.ASSIGN)

                self.state = 202
                self.expression(0)
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


    class Var_declaration_globalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declarationContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declaration_global

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration_global" ):
                return visitor.visitVar_declaration_global(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration_global(self):

        localctx = MiniGoParser.Var_declaration_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_declaration_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.var_declaration()
            self.state = 206
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declaration_globalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declarationContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declaration_global

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declaration_global" ):
                return visitor.visitConst_declaration_global(self)
            else:
                return visitor.visitChildren(self)




    def const_declaration_global(self):

        localctx = MiniGoParser.Const_declaration_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_const_declaration_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.const_declaration()
            self.state = 209
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
        self.enterRule(localctx, 24, self.RULE_struct_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(MiniGoParser.TYPE)
            self.state = 212
            self.match(MiniGoParser.ID)
            self.state = 213
            self.match(MiniGoParser.STRUCT)
            self.state = 214
            self.match(MiniGoParser.LBRACE)
            self.state = 215
            self.data_struct()
            self.state = 216
            self.match(MiniGoParser.RBRACE)

            self.state = 217
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
        self.enterRule(localctx, 26, self.RULE_data_struct)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(MiniGoParser.ID)
                self.state = 220
                self.data_type()

                self.state = 221
                self.match(MiniGoParser.SEMICOLON)
                self.state = 223
                self.data_struct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(MiniGoParser.ID)
                self.state = 226
                self.data_type()

                self.state = 227
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
        self.enterRule(localctx, 28, self.RULE_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MiniGoParser.LPAREN)
            self.state = 232
            self.list_method_element()
            self.state = 233
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
        self.enterRule(localctx, 30, self.RULE_list_method_element)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.method_element()
                self.state = 236
                self.match(MiniGoParser.COMMA)
                self.state = 237
                self.list_method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
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
        self.enterRule(localctx, 32, self.RULE_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MiniGoParser.ID)
            self.state = 243
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
        self.enterRule(localctx, 34, self.RULE_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MiniGoParser.FUNC)
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN]:
                self.state = 246
                self.method_declaration()
                pass
            elif token in [MiniGoParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 250
            self.match(MiniGoParser.ID)
            self.state = 251
            self.match(MiniGoParser.LPAREN)
            self.state = 252
            self.list_func_arguments()
            self.state = 253
            self.match(MiniGoParser.RPAREN)
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 254
                self.data_type()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 258
            self.match(MiniGoParser.LBRACE)
            self.state = 259
            self.list_statement_primary()
            self.state = 260
            self.match(MiniGoParser.RBRACE)
            self.state = 261
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
        self.enterRule(localctx, 36, self.RULE_list_func_arguments)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
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
        self.enterRule(localctx, 38, self.RULE_list_agruments)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.func_agrument()
                self.state = 268
                self.match(MiniGoParser.COMMA)
                self.state = 269
                self.list_agruments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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
        self.enterRule(localctx, 40, self.RULE_func_agrument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.data_element()
            self.state = 275
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
        self.enterRule(localctx, 42, self.RULE_data_element)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(MiniGoParser.ID)
                self.state = 278
                self.match(MiniGoParser.COMMA)
                self.state = 279
                self.data_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
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
        self.enterRule(localctx, 44, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MiniGoParser.TYPE)
            self.state = 284
            self.match(MiniGoParser.ID)
            self.state = 285
            self.match(MiniGoParser.INTERFACE)
            self.state = 286
            self.match(MiniGoParser.LBRACE)
            self.state = 287
            self.list_method_interface()
            self.state = 288
            self.match(MiniGoParser.RBRACE)

            self.state = 289
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
        self.enterRule(localctx, 46, self.RULE_list_method_interface)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.inter_method()
                self.state = 292
                self.list_method_interface()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
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
        self.enterRule(localctx, 48, self.RULE_inter_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.ID)
            self.state = 298
            self.match(MiniGoParser.LPAREN)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 299
                self.list_interface_element()


            self.state = 302
            self.match(MiniGoParser.RPAREN)
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 303
                self.data_type()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 307
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_interface_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_elementContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_element" ):
                return visitor.visitList_interface_element(self)
            else:
                return visitor.visitChildren(self)




    def list_interface_element(self):

        localctx = MiniGoParser.List_interface_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_interface_element)
        self._la = 0 # Token type
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(MiniGoParser.ID)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 310
                    self.data_type()


                self.state = 313
                self.match(MiniGoParser.COMMA)
                self.state = 314
                self.list_interface_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(MiniGoParser.ID)
                self.state = 316
                self.data_type()
                pass


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
        self.enterRule(localctx, 52, self.RULE_assign_oprator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
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

        def dot_id(self):
            return self.getTypedRuleContext(MiniGoParser.Dot_idContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assign_oprator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opratorContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.dot_id(0)

            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ASS_DECLARE, MiniGoParser.ADD_ASSIGN, MiniGoParser.SUB_ASSIGN, MiniGoParser.MUL_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
                self.state = 322
                self.assign_oprator()
                pass
            elif token in [MiniGoParser.EQUAL]:
                self.state = 323
                self.match(MiniGoParser.EQUAL)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 326
            self.expression(0)
            self.state = 328
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dot_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dot_id(self):
            return self.getTypedRuleContext(MiniGoParser.Dot_idContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dot_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot_id" ):
                return visitor.visitDot_id(self)
            else:
                return visitor.visitChildren(self)



    def dot_id(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Dot_idContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_dot_id, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Dot_idContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dot_id)
                    self.state = 333
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 340
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DOT]:
                        self.state = 334
                        self.match(MiniGoParser.DOT)
                        self.state = 335
                        self.match(MiniGoParser.ID)
                        pass
                    elif token in [MiniGoParser.LBRACKET]:
                        self.state = 336
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 337
                        self.expression(0)
                        self.state = 338
                        self.match(MiniGoParser.RBRACKET)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.if_stmt()
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 348
                self.elseif_list()
                pass

            elif la_ == 2:
                pass


            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ELSE]:
                self.state = 352
                self.match(MiniGoParser.ELSE)
                self.state = 353
                self.block_statement()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 357
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
        self.enterRule(localctx, 60, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MiniGoParser.IF)
            self.state = 360
            self.match(MiniGoParser.LPAREN)
            self.state = 361
            self.expression(0)
            self.state = 362
            self.match(MiniGoParser.RPAREN)
            self.state = 363
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
        self.enterRule(localctx, 62, self.RULE_elseif_list)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(MiniGoParser.ELSE)
                self.state = 366
                self.match(MiniGoParser.IF)
                self.state = 367
                self.match(MiniGoParser.LPAREN)
                self.state = 368
                self.expression(0)
                self.state = 369
                self.match(MiniGoParser.RPAREN)
                self.state = 370
                self.block_statement()
                self.state = 372
                self.elseif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(MiniGoParser.ELSE)
                self.state = 375
                self.match(MiniGoParser.IF)
                self.state = 376
                self.match(MiniGoParser.LPAREN)
                self.state = 377
                self.expression(0)
                self.state = 378
                self.match(MiniGoParser.RPAREN)
                self.state = 379
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
        self.enterRule(localctx, 64, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(MiniGoParser.LBRACE)
            self.state = 384
            self.list_statement_primary()
            self.state = 385
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
        self.enterRule(localctx, 66, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 387
                self.for_basic()
                pass

            elif la_ == 2:
                self.state = 388
                self.for_loop_basic()
                pass

            elif la_ == 3:
                self.state = 389
                self.for_loop_range()
                pass


            self.state = 392
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

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement_primary(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primaryContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_basic" ):
                return visitor.visitFor_basic(self)
            else:
                return visitor.visitChildren(self)




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(MiniGoParser.FOR)
            self.state = 395
            self.expression(0)
            self.state = 396
            self.match(MiniGoParser.LBRACE)
            self.state = 397
            self.list_statement_primary()
            self.state = 398
            self.match(MiniGoParser.RBRACE)
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

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

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


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement_primary(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primaryContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 70, self.RULE_for_loop_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(MiniGoParser.FOR)
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.state = 401
                self.var_declaration_for()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 402
                self.assignment_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 405
            self.match(MiniGoParser.SEMICOLON)
            self.state = 406
            self.expression(0)
            self.state = 407
            self.match(MiniGoParser.SEMICOLON)
            self.state = 408
            self.assignment_for()
            self.state = 409
            self.match(MiniGoParser.LBRACE)
            self.state = 410
            self.list_statement_primary()
            self.state = 411
            self.match(MiniGoParser.RBRACE)
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

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

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


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement_primary(self):
            return self.getTypedRuleContext(MiniGoParser.List_statement_primaryContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_range" ):
                return visitor.visitFor_loop_range(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_range(self):

        localctx = MiniGoParser.For_loop_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_loop_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(MiniGoParser.FOR)
            self.state = 414
            self.match(MiniGoParser.ID)
            self.state = 415
            self.match(MiniGoParser.COMMA)
            self.state = 416
            self.match(MiniGoParser.ID)
            self.state = 417
            self.match(MiniGoParser.ASS_DECLARE)
            self.state = 418
            self.match(MiniGoParser.RANGE)
            self.state = 419
            self.expression(0)
            self.state = 420
            self.match(MiniGoParser.LBRACE)
            self.state = 421
            self.list_statement_primary()
            self.state = 422
            self.match(MiniGoParser.RBRACE)
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASS_DECLARE(self):
            return self.getToken(MiniGoParser.ASS_DECLARE, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

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
            return MiniGoParser.RULE_assignment_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_for" ):
                return visitor.visitAssignment_for(self)
            else:
                return visitor.visitChildren(self)




    def assignment_for(self):

        localctx = MiniGoParser.Assignment_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assignment_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(MiniGoParser.ID)

            self.state = 425
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.ASS_DECLARE) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 426
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
        self.enterRule(localctx, 76, self.RULE_var_declaration_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(MiniGoParser.VAR)
            self.state = 429
            self.match(MiniGoParser.ID)
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.ID]:
                self.state = 430
                self.data_type()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 434
            self.match(MiniGoParser.ASSIGN)
            self.state = 435
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
        self.enterRule(localctx, 78, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.BREAK)
            self.state = 438
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_lhs_aggin, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Lhs_agginContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_aggin)
                    self.state = 443
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 450
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LBRACKET]:
                        self.state = 444
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 445
                        self.expression(0)
                        self.state = 446
                        self.match(MiniGoParser.RBRACKET)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 448
                        self.match(MiniGoParser.DOT)
                        self.state = 449
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 457
                self.lhs_aggin(0)
                self.state = 458
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 463
            self.match(MiniGoParser.ID)
            self.state = 464
            self.match(MiniGoParser.LPAREN)
            self.state = 465
            self.list_expression()
            self.state = 466
            self.match(MiniGoParser.RPAREN)
            self.state = 467
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
        self.enterRule(localctx, 84, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(MiniGoParser.CONTINUE)
            self.state = 470
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
        self.enterRule(localctx, 86, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(MiniGoParser.RETURN)
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.BOOLEAN_LIT, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOATING_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.state = 473
                self.expression(0)
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 477
            self.match(MiniGoParser.SEMICOLON)
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


        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.array_type()
            self.state = 480
            self.arrayInit()
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
        self.enterRule(localctx, 90, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.list_type_arr()

            self.state = 483
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
        self.enterRule(localctx, 92, self.RULE_list_type_arr)
        self._la = 0 # Token type
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(MiniGoParser.LBRACKET)
                self.state = 486
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 487
                self.match(MiniGoParser.RBRACKET)
                self.state = 488
                self.list_type_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(MiniGoParser.LBRACKET)
                self.state = 490
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 491
                self.match(MiniGoParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_array_value(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_valueContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInit" ):
                return visitor.visitArrayInit(self)
            else:
                return visitor.visitChildren(self)




    def arrayInit(self):

        localctx = MiniGoParser.ArrayInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arrayInit)
        try:
            self.state = 499
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(MiniGoParser.LBRACE)
                self.state = 495
                self.list_array_value()
                self.state = 496
                self.match(MiniGoParser.RBRACE)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOATING_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.array_element()
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


    class List_array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayInit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayInitContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_array_value(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_valueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_value" ):
                return visitor.visitList_array_value(self)
            else:
                return visitor.visitChildren(self)




    def list_array_value(self):

        localctx = MiniGoParser.List_array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_list_array_value)
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.arrayInit()
                self.state = 502
                self.match(MiniGoParser.COMMA)
                self.state = 503
                self.list_array_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.arrayInit()
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
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_array_element)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.match(MiniGoParser.FLOATING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 510
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 511
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 512
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 513
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 514
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 515
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
        self.enterRule(localctx, 100, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(MiniGoParser.ID)
            self.state = 519
            self.match(MiniGoParser.LBRACE)
            self.state = 520
            self.struct_lit_body()
            self.state = 521
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
        self.enterRule(localctx, 102, self.RULE_struct_lit_body)
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
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
        self.enterRule(localctx, 104, self.RULE_struct_lit_body_element)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.struct_element()
                self.state = 528
                self.match(MiniGoParser.COMMA)
                self.state = 529
                self.struct_lit_body_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
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


        def func_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_element" ):
                return visitor.visitStruct_element(self)
            else:
                return visitor.visitChildren(self)




    def struct_element(self):

        localctx = MiniGoParser.Struct_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_struct_element)
        try:
            self.state = 538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(MiniGoParser.ID)
                self.state = 535
                self.match(MiniGoParser.COLON)
                self.state = 536
                self.expression(0)
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.func_declaration()
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
        self.enterRule(localctx, 108, self.RULE_list_expression)
        try:
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.BOOLEAN_LIT, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOATING_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
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
        self.enterRule(localctx, 110, self.RULE_params)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.expression(0)
                self.state = 545
                self.match(MiniGoParser.COMMA)
                self.state = 546
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.expression_1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 559
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 554
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 555
                    self.match(MiniGoParser.OR)
                    self.state = 556
                    self.expression_1(0) 
                self.state = 561
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expression_1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.expression_2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 570
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_1)
                    self.state = 565
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 566
                    self.match(MiniGoParser.AND)
                    self.state = 567
                    self.expression_2(0) 
                self.state = 572
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_expression_2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.expression_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 581
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_2)
                    self.state = 576
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 577
                    self.match(MiniGoParser.COMPARE_OPERATOR)
                    self.state = 578
                    self.expression_3(0) 
                self.state = 583
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_expression_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.expression_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 592
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_3)
                    self.state = 587
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 588
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 589
                    self.expression_4(0) 
                self.state = 594
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expression_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.expression_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 603
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_4)
                    self.state = 598
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 599
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 600
                    self.expression_5() 
                self.state = 605
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        self.enterRule(localctx, 122, self.RULE_expression_5)
        self._la = 0 # Token type
        try:
            self.state = 609
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 607
                self.expression_5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.ID, MiniGoParser.BOOLEAN_LIT, MiniGoParser.INTEGER_LITERAL, MiniGoParser.FLOATING_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


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
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expression_6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.expression_7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 637
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 635
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression_6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_6)
                        self.state = 614
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 619
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MiniGoParser.LPAREN:
                            self.state = 615
                            self.match(MiniGoParser.LPAREN)
                            self.state = 616
                            self.expression(0)
                            self.state = 617
                            self.match(MiniGoParser.RPAREN)


                        self.state = 621
                        self.match(MiniGoParser.LBRACKET)

                        self.state = 622
                        self.expression(0)
                        self.state = 623
                        self.match(MiniGoParser.RBRACKET)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression_6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_6)
                        self.state = 625
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 626
                        self.match(MiniGoParser.DOT)
                        self.state = 633
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                        if la_ == 1:
                            self.state = 627
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 628
                            self.match(MiniGoParser.ID)
                            self.state = 629
                            self.match(MiniGoParser.LPAREN)
                            self.state = 630
                            self.list_expression()
                            self.state = 631
                            self.match(MiniGoParser.RPAREN)
                            pass


                        pass

             
                self.state = 639
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        self.enterRule(localctx, 126, self.RULE_expression_7)
        try:
            self.state = 650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 640
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 641
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 642
                self.match(MiniGoParser.LPAREN)
                self.state = 643
                self.expression(0)
                self.state = 644
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 646
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 647
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 648
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 649
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
        self.enterRule(localctx, 128, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.match(MiniGoParser.ID)
            self.state = 653
            self.match(MiniGoParser.LPAREN)
            self.state = 654
            self.list_expression()
            self.state = 655
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
        self._predicates[28] = self.dot_id_sempred
        self._predicates[40] = self.lhs_aggin_sempred
        self._predicates[56] = self.expression_sempred
        self._predicates[57] = self.expression_1_sempred
        self._predicates[58] = self.expression_2_sempred
        self._predicates[59] = self.expression_3_sempred
        self._predicates[60] = self.expression_4_sempred
        self._predicates[62] = self.expression_6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def dot_id_sempred(self, localctx:Dot_idContext, predIndex:int):
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
         




