# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


#2212019    
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0244\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u00b6\n\2\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\58\u017d\n8\38\38\38\5")
        buf.write("8\u0182\n8\39\39\39\3:\3:\5:\u0189\n:\3;\3;\3;\3;\5;\u018f")
        buf.write("\n;\3<\3<\3=\3=\3=\3=\5=\u0197\n=\3>\3>\3>\3>\5>\u019d")
        buf.write("\n>\3?\3?\3?\3?\5?\u01a3\n?\3@\3@\3@\5@\u01a8\n@\3A\3")
        buf.write("A\3A\3B\3B\3B\3B\5B\u01b1\nB\3C\3C\3C\5C\u01b6\nC\3D\3")
        buf.write("D\3D\3E\3E\3E\3E\5E\u01bf\nE\3F\3F\3F\5F\u01c4\nF\3G\3")
        buf.write("G\3G\3H\3H\3H\7H\u01cc\nH\fH\16H\u01cf\13H\5H\u01d1\n")
        buf.write("H\3I\7I\u01d4\nI\fI\16I\u01d7\13I\5I\u01d9\nI\3J\3J\5")
        buf.write("J\u01dd\nJ\3J\6J\u01e0\nJ\rJ\16J\u01e1\5J\u01e4\nJ\3K")
        buf.write("\6K\u01e7\nK\rK\16K\u01e8\3K\3K\3K\3K\3L\3L\5L\u01f1\n")
        buf.write("L\3M\3M\3M\3N\3N\3N\3O\3O\7O\u01fb\nO\fO\16O\u01fe\13")
        buf.write("O\3O\3O\3P\3P\3Q\3Q\3Q\3Q\3Q\7Q\u0209\nQ\fQ\16Q\u020c")
        buf.write("\13Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\7R\u0217\nR\fR\16R\u021a")
        buf.write("\13R\3R\3R\3S\6S\u021f\nS\rS\16S\u0220\3S\3S\3T\5T\u0226")
        buf.write("\nT\3T\3T\3T\3T\3U\3U\3U\3V\3V\7V\u0231\nV\fV\16V\u0234")
        buf.write("\13V\3V\5V\u0237\nV\3V\3V\3W\3W\7W\u023d\nW\fW\16W\u0240")
        buf.write("\13W\3W\3W\3W\3\u020a\2X\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\2m\2o\2q\67s8u9w\2y\2{:}\2\177\2\u0081;")
        buf.write("\u0083\2\u0085\2\u0087<\u0089\2\u008b\2\u008d=\u008f\2")
        buf.write("\u0091\2\u0093\2\u0095>\u0097\2\u0099\2\u009b\2\u009d")
        buf.write("?\u009f@\u00a1A\u00a3B\u00a5C\u00a7D\u00a9E\u00abF\u00ad")
        buf.write("G\3\2\16\5\2C\\aac|\3\2\62;\3\2\63;\3\2\629\5\2\62;CH")
        buf.write("ch\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\4\2")
        buf.write("\f\f\17\17\5\2\13\13\16\17\"\"\4\3\f\f\17\17\2\u0256\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2{")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0087\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\3\u00b5")
        buf.write("\3\2\2\2\5\u00b7\3\2\2\2\7\u00ba\3\2\2\2\t\u00bf\3\2\2")
        buf.write("\2\13\u00c3\3\2\2\2\r\u00ca\3\2\2\2\17\u00cf\3\2\2\2\21")
        buf.write("\u00d4\3\2\2\2\23\u00db\3\2\2\2\25\u00e5\3\2\2\2\27\u00ec")
        buf.write("\3\2\2\2\31\u00f0\3\2\2\2\33\u00f6\3\2\2\2\35\u00fc\3")
        buf.write("\2\2\2\37\u0100\3\2\2\2!\u0109\3\2\2\2#\u010f\3\2\2\2")
        buf.write("%\u0115\3\2\2\2\'\u0119\3\2\2\2)\u011e\3\2\2\2+\u0124")
        buf.write("\3\2\2\2-\u012c\3\2\2\2/\u012e\3\2\2\2\61\u0130\3\2\2")
        buf.write("\2\63\u0132\3\2\2\2\65\u0134\3\2\2\2\67\u0136\3\2\2\2")
        buf.write("9\u0139\3\2\2\2;\u013c\3\2\2\2=\u013e\3\2\2\2?\u0141\3")
        buf.write("\2\2\2A\u0143\3\2\2\2C\u0146\3\2\2\2E\u0149\3\2\2\2G\u014c")
        buf.write("\3\2\2\2I\u014e\3\2\2\2K\u0151\3\2\2\2M\u0153\3\2\2\2")
        buf.write("O\u0156\3\2\2\2Q\u0159\3\2\2\2S\u015c\3\2\2\2U\u015f\3")
        buf.write("\2\2\2W\u0162\3\2\2\2Y\u0164\3\2\2\2[\u0166\3\2\2\2]\u0168")
        buf.write("\3\2\2\2_\u016a\3\2\2\2a\u016c\3\2\2\2c\u016e\3\2\2\2")
        buf.write("e\u0170\3\2\2\2g\u0172\3\2\2\2i\u0174\3\2\2\2k\u0176\3")
        buf.write("\2\2\2m\u0178\3\2\2\2o\u0181\3\2\2\2q\u0183\3\2\2\2s\u0188")
        buf.write("\3\2\2\2u\u018e\3\2\2\2w\u0190\3\2\2\2y\u0196\3\2\2\2")
        buf.write("{\u019c\3\2\2\2}\u01a2\3\2\2\2\177\u01a7\3\2\2\2\u0081")
        buf.write("\u01a9\3\2\2\2\u0083\u01b0\3\2\2\2\u0085\u01b5\3\2\2\2")
        buf.write("\u0087\u01b7\3\2\2\2\u0089\u01be\3\2\2\2\u008b\u01c3\3")
        buf.write("\2\2\2\u008d\u01c5\3\2\2\2\u008f\u01d0\3\2\2\2\u0091\u01d8")
        buf.write("\3\2\2\2\u0093\u01e3\3\2\2\2\u0095\u01e6\3\2\2\2\u0097")
        buf.write("\u01f0\3\2\2\2\u0099\u01f2\3\2\2\2\u009b\u01f5\3\2\2\2")
        buf.write("\u009d\u01f8\3\2\2\2\u009f\u0201\3\2\2\2\u00a1\u0203\3")
        buf.write("\2\2\2\u00a3\u0212\3\2\2\2\u00a5\u021e\3\2\2\2\u00a7\u0225")
        buf.write("\3\2\2\2\u00a9\u022b\3\2\2\2\u00ab\u022e\3\2\2\2\u00ad")
        buf.write("\u023a\3\2\2\2\u00af\u00b6\5\67\34\2\u00b0\u00b6\59\35")
        buf.write("\2\u00b1\u00b6\5;\36\2\u00b2\u00b6\5=\37\2\u00b3\u00b6")
        buf.write("\5? \2\u00b4\u00b6\5A!\2\u00b5\u00af\3\2\2\2\u00b5\u00b0")
        buf.write("\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5\u00b2\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\4\3\2\2\2\u00b7")
        buf.write("\u00b8\7k\2\2\u00b8\u00b9\7h\2\2\u00b9\6\3\2\2\2\u00ba")
        buf.write("\u00bb\7g\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd\7u\2\2\u00bd")
        buf.write("\u00be\7g\2\2\u00be\b\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0")
        buf.write("\u00c1\7q\2\2\u00c1\u00c2\7t\2\2\u00c2\n\3\2\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7v\2\2\u00c6")
        buf.write("\u00c7\7w\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7p\2\2\u00c9")
        buf.write("\f\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7w\2\2\u00cc")
        buf.write("\u00cd\7p\2\2\u00cd\u00ce\7e\2\2\u00ce\16\3\2\2\2\u00cf")
        buf.write("\u00d0\7v\2\2\u00d0\u00d1\7{\2\2\u00d1\u00d2\7r\2\2\u00d2")
        buf.write("\u00d3\7g\2\2\u00d3\20\3\2\2\2\u00d4\u00d5\7u\2\2\u00d5")
        buf.write("\u00d6\7v\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7w\2\2\u00d8")
        buf.write("\u00d9\7e\2\2\u00d9\u00da\7v\2\2\u00da\22\3\2\2\2\u00db")
        buf.write("\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7v\2\2\u00de")
        buf.write("\u00df\7g\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7h\2\2\u00e1")
        buf.write("\u00e2\7c\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4\7g\2\2\u00e4")
        buf.write("\24\3\2\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7\7v\2\2\u00e7")
        buf.write("\u00e8\7t\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea")
        buf.write("\u00eb\7i\2\2\u00eb\26\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed")
        buf.write("\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\30\3\2\2\2\u00f0")
        buf.write("\u00f1\7h\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7q\2\2\u00f3")
        buf.write("\u00f4\7c\2\2\u00f4\u00f5\7v\2\2\u00f5\32\3\2\2\2\u00f6")
        buf.write("\u00f7\7e\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write("\u00fa\7u\2\2\u00fa\u00fb\7v\2\2\u00fb\34\3\2\2\2\u00fc")
        buf.write("\u00fd\7x\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("\36\3\2\2\2\u0100\u0101\7e\2\2\u0101\u0102\7q\2\2\u0102")
        buf.write("\u0103\7p\2\2\u0103\u0104\7v\2\2\u0104\u0105\7k\2\2\u0105")
        buf.write("\u0106\7p\2\2\u0106\u0107\7w\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write(" \3\2\2\2\u0109\u010a\7d\2\2\u010a\u010b\7t\2\2\u010b")
        buf.write("\u010c\7g\2\2\u010c\u010d\7c\2\2\u010d\u010e\7m\2\2\u010e")
        buf.write("\"\3\2\2\2\u010f\u0110\7t\2\2\u0110\u0111\7c\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112\u0113\7i\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("$\3\2\2\2\u0115\u0116\7p\2\2\u0116\u0117\7k\2\2\u0117")
        buf.write("\u0118\7n\2\2\u0118&\3\2\2\2\u0119\u011a\7v\2\2\u011a")
        buf.write("\u011b\7t\2\2\u011b\u011c\7w\2\2\u011c\u011d\7g\2\2\u011d")
        buf.write("(\3\2\2\2\u011e\u011f\7h\2\2\u011f\u0120\7c\2\2\u0120")
        buf.write("\u0121\7n\2\2\u0121\u0122\7u\2\2\u0122\u0123\7g\2\2\u0123")
        buf.write("*\3\2\2\2\u0124\u0125\7d\2\2\u0125\u0126\7q\2\2\u0126")
        buf.write("\u0127\7q\2\2\u0127\u0128\7n\2\2\u0128\u0129\7g\2\2\u0129")
        buf.write("\u012a\7c\2\2\u012a\u012b\7p\2\2\u012b,\3\2\2\2\u012c")
        buf.write("\u012d\7-\2\2\u012d.\3\2\2\2\u012e\u012f\7/\2\2\u012f")
        buf.write("\60\3\2\2\2\u0130\u0131\7,\2\2\u0131\62\3\2\2\2\u0132")
        buf.write("\u0133\7\61\2\2\u0133\64\3\2\2\2\u0134\u0135\7\'\2\2\u0135")
        buf.write("\66\3\2\2\2\u0136\u0137\7?\2\2\u0137\u0138\7?\2\2\u0138")
        buf.write("8\3\2\2\2\u0139\u013a\7#\2\2\u013a\u013b\7?\2\2\u013b")
        buf.write(":\3\2\2\2\u013c\u013d\7>\2\2\u013d<\3\2\2\2\u013e\u013f")
        buf.write("\7>\2\2\u013f\u0140\7?\2\2\u0140>\3\2\2\2\u0141\u0142")
        buf.write("\7@\2\2\u0142@\3\2\2\2\u0143\u0144\7@\2\2\u0144\u0145")
        buf.write("\7?\2\2\u0145B\3\2\2\2\u0146\u0147\7(\2\2\u0147\u0148")
        buf.write("\7(\2\2\u0148D\3\2\2\2\u0149\u014a\7~\2\2\u014a\u014b")
        buf.write("\7~\2\2\u014bF\3\2\2\2\u014c\u014d\7#\2\2\u014dH\3\2\2")
        buf.write("\2\u014e\u014f\7<\2\2\u014f\u0150\7?\2\2\u0150J\3\2\2")
        buf.write("\2\u0151\u0152\7?\2\2\u0152L\3\2\2\2\u0153\u0154\7-\2")
        buf.write("\2\u0154\u0155\7?\2\2\u0155N\3\2\2\2\u0156\u0157\7/\2")
        buf.write("\2\u0157\u0158\7?\2\2\u0158P\3\2\2\2\u0159\u015a\7,\2")
        buf.write("\2\u015a\u015b\7?\2\2\u015bR\3\2\2\2\u015c\u015d\7\61")
        buf.write("\2\2\u015d\u015e\7?\2\2\u015eT\3\2\2\2\u015f\u0160\7\'")
        buf.write("\2\2\u0160\u0161\7?\2\2\u0161V\3\2\2\2\u0162\u0163\7\60")
        buf.write("\2\2\u0163X\3\2\2\2\u0164\u0165\7<\2\2\u0165Z\3\2\2\2")
        buf.write("\u0166\u0167\7*\2\2\u0167\\\3\2\2\2\u0168\u0169\7+\2\2")
        buf.write("\u0169^\3\2\2\2\u016a\u016b\7}\2\2\u016b`\3\2\2\2\u016c")
        buf.write("\u016d\7\177\2\2\u016db\3\2\2\2\u016e\u016f\7]\2\2\u016f")
        buf.write("d\3\2\2\2\u0170\u0171\7_\2\2\u0171f\3\2\2\2\u0172\u0173")
        buf.write("\7.\2\2\u0173h\3\2\2\2\u0174\u0175\7=\2\2\u0175j\3\2\2")
        buf.write("\2\u0176\u0177\t\2\2\2\u0177l\3\2\2\2\u0178\u0179\t\3")
        buf.write("\2\2\u0179n\3\2\2\2\u017a\u017d\5k\66\2\u017b\u017d\5")
        buf.write("m\67\2\u017c\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017f\5o8\2\u017f\u0182\3\2\2\2\u0180\u0182")
        buf.write("\3\2\2\2\u0181\u017c\3\2\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("p\3\2\2\2\u0183\u0184\5k\66\2\u0184\u0185\5o8\2\u0185")
        buf.write("r\3\2\2\2\u0186\u0189\5\'\24\2\u0187\u0189\5)\25\2\u0188")
        buf.write("\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189t\3\2\2\2\u018a")
        buf.write("\u018f\5{>\2\u018b\u018f\5\u0081A\2\u018c\u018f\5\u008d")
        buf.write("G\2\u018d\u018f\5\u0087D\2\u018e\u018a\3\2\2\2\u018e\u018b")
        buf.write("\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("v\3\2\2\2\u0190\u0191\t\4\2\2\u0191x\3\2\2\2\u0192\u0193")
        buf.write("\5m\67\2\u0193\u0194\5y=\2\u0194\u0197\3\2\2\2\u0195\u0197")
        buf.write("\3\2\2\2\u0196\u0192\3\2\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("z\3\2\2\2\u0198\u0199\5w<\2\u0199\u019a\5y=\2\u019a\u019d")
        buf.write("\3\2\2\2\u019b\u019d\7\62\2\2\u019c\u0198\3\2\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d|\3\2\2\2\u019e\u019f\7\62\2\2\u019f")
        buf.write("\u01a3\7d\2\2\u01a0\u01a1\7\62\2\2\u01a1\u01a3\7D\2\2")
        buf.write("\u01a2\u019e\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3~\3\2\2")
        buf.write("\2\u01a4\u01a5\4\62\63\2\u01a5\u01a8\5\177@\2\u01a6\u01a8")
        buf.write("\4\62\63\2\u01a7\u01a4\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8")
        buf.write("\u0080\3\2\2\2\u01a9\u01aa\5}?\2\u01aa\u01ab\5\177@\2")
        buf.write("\u01ab\u0082\3\2\2\2\u01ac\u01ad\7\62\2\2\u01ad\u01b1")
        buf.write("\7q\2\2\u01ae\u01af\7\62\2\2\u01af\u01b1\7Q\2\2\u01b0")
        buf.write("\u01ac\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u0084\3\2\2\2")
        buf.write("\u01b2\u01b3\t\5\2\2\u01b3\u01b6\5\u0085C\2\u01b4\u01b6")
        buf.write("\t\5\2\2\u01b5\u01b2\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("\u0086\3\2\2\2\u01b7\u01b8\5\u0083B\2\u01b8\u01b9\5\u0085")
        buf.write("C\2\u01b9\u0088\3\2\2\2\u01ba\u01bb\7\62\2\2\u01bb\u01bf")
        buf.write("\7z\2\2\u01bc\u01bd\7\62\2\2\u01bd\u01bf\7Z\2\2\u01be")
        buf.write("\u01ba\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u008a\3\2\2\2")
        buf.write("\u01c0\u01c1\t\6\2\2\u01c1\u01c4\5\u008bF\2\u01c2\u01c4")
        buf.write("\t\6\2\2\u01c3\u01c0\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("\u008c\3\2\2\2\u01c5\u01c6\5\u0089E\2\u01c6\u01c7\5\u008b")
        buf.write("F\2\u01c7\u008e\3\2\2\2\u01c8\u01d1\7\62\2\2\u01c9\u01cd")
        buf.write("\t\4\2\2\u01ca\u01cc\5m\67\2\u01cb\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01c8\3")
        buf.write("\2\2\2\u01d0\u01c9\3\2\2\2\u01d1\u0090\3\2\2\2\u01d2\u01d4")
        buf.write("\5m\67\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d9\3\2\2\2")
        buf.write("\u01d7\u01d5\3\2\2\2\u01d8\u01d5\3\2\2\2\u01d8\u01d9\3")
        buf.write("\2\2\2\u01d9\u0092\3\2\2\2\u01da\u01dc\t\7\2\2\u01db\u01dd")
        buf.write("\t\b\2\2\u01dc\u01db\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write("\u01df\3\2\2\2\u01de\u01e0\5m\67\2\u01df\u01de\3\2\2\2")
        buf.write("\u01e0\u01e1\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3")
        buf.write("\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01da\3\2\2\2\u01e3\u01e4")
        buf.write("\3\2\2\2\u01e4\u0094\3\2\2\2\u01e5\u01e7\5m\67\2\u01e6")
        buf.write("\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e8\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\5")
        buf.write("W,\2\u01eb\u01ec\5\u0091I\2\u01ec\u01ed\5\u0093J\2\u01ed")
        buf.write("\u0096\3\2\2\2\u01ee\u01f1\5\u0099M\2\u01ef\u01f1\n\t")
        buf.write("\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1\u0098")
        buf.write("\3\2\2\2\u01f2\u01f3\7^\2\2\u01f3\u01f4\t\n\2\2\u01f4")
        buf.write("\u009a\3\2\2\2\u01f5\u01f6\7^\2\2\u01f6\u01f7\n\n\2\2")
        buf.write("\u01f7\u009c\3\2\2\2\u01f8\u01fc\7$\2\2\u01f9\u01fb\5")
        buf.write("\u0097L\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc")
        buf.write("\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2")
        buf.write("\u01fe\u01fc\3\2\2\2\u01ff\u0200\7$\2\2\u0200\u009e\3")
        buf.write("\2\2\2\u0201\u0202\5%\23\2\u0202\u00a0\3\2\2\2\u0203\u0204")
        buf.write("\7\61\2\2\u0204\u0205\7,\2\2\u0205\u020a\3\2\2\2\u0206")
        buf.write("\u0209\5\u00a1Q\2\u0207\u0209\13\2\2\2\u0208\u0206\3\2")
        buf.write("\2\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u020b")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020d\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020d\u020e\7,\2\2\u020e\u020f\7\61\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210\u0211\bQ\2\2\u0211\u00a2\3")
        buf.write("\2\2\2\u0212\u0213\7\61\2\2\u0213\u0214\7\61\2\2\u0214")
        buf.write("\u0218\3\2\2\2\u0215\u0217\n\13\2\2\u0216\u0215\3\2\2")
        buf.write("\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219")
        buf.write("\3\2\2\2\u0219\u021b\3\2\2\2\u021a\u0218\3\2\2\2\u021b")
        buf.write("\u021c\bR\2\2\u021c\u00a4\3\2\2\2\u021d\u021f\t\f\2\2")
        buf.write("\u021e\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u021e\3")
        buf.write("\2\2\2\u0220\u0221\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0223")
        buf.write("\bS\2\2\u0223\u00a6\3\2\2\2\u0224\u0226\7\17\2\2\u0225")
        buf.write("\u0224\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\3\2\2\2")
        buf.write("\u0227\u0228\7\f\2\2\u0228\u0229\3\2\2\2\u0229\u022a\b")
        buf.write("T\3\2\u022a\u00a8\3\2\2\2\u022b\u022c\13\2\2\2\u022c\u022d")
        buf.write("\bU\4\2\u022d\u00aa\3\2\2\2\u022e\u0232\7$\2\2\u022f\u0231")
        buf.write("\5\u0097L\2\u0230\u022f\3\2\2\2\u0231\u0234\3\2\2\2\u0232")
        buf.write("\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0236\3\2\2\2")
        buf.write("\u0234\u0232\3\2\2\2\u0235\u0237\t\r\2\2\u0236\u0235\3")
        buf.write("\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239\bV\5\2\u0239\u00ac")
        buf.write("\3\2\2\2\u023a\u023e\7$\2\2\u023b\u023d\5\u0097L\2\u023c")
        buf.write("\u023b\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2")
        buf.write("\u023e\u023f\3\2\2\2\u023f\u0241\3\2\2\2\u0240\u023e\3")
        buf.write("\2\2\2\u0241\u0242\5\u009bN\2\u0242\u0243\bW\6\2\u0243")
        buf.write("\u00ae\3\2\2\2\"\2\u00b5\u017c\u0181\u0188\u018e\u0196")
        buf.write("\u019c\u01a2\u01a7\u01b0\u01b5\u01be\u01c3\u01cd\u01d0")
        buf.write("\u01d5\u01d8\u01dc\u01e1\u01e3\u01e8\u01f0\u01fc\u0208")
        buf.write("\u020a\u0218\u0220\u0225\u0232\u0236\u023e\7\b\2\2\3T")
        buf.write("\2\3U\3\3V\4\3W\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMPARE_OPERATOR = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    BOOLEAN = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    EQUAL = 27
    NOT_EQUAL = 28
    LESS = 29
    LESS_EQUAL = 30
    GREATER = 31
    GREATER_EQUAL = 32
    AND = 33
    OR = 34
    NOT = 35
    ASS_DECLARE = 36
    ASSIGN = 37
    ADD_ASSIGN = 38
    SUB_ASSIGN = 39
    MUL_ASSIGN = 40
    DIV_ASSIGN = 41
    MOD_ASSIGN = 42
    DOT = 43
    COLON = 44
    LPAREN = 45
    RPAREN = 46
    LBRACE = 47
    RBRACE = 48
    LBRACKET = 49
    RBRACKET = 50
    COMMA = 51
    SEMICOLON = 52
    ID = 53
    BOOLEAN_LIT = 54
    INTEGER_LITERAL = 55
    DECIMAL_LITERAL = 56
    BINARY_LITERAL = 57
    OCTAL_LITERAL = 58
    HEX_LITERAL = 59
    FLOATING_LITERAL = 60
    STRING_LITERAL = 61
    NIL_LIT = 62
    COMMENT_BLOCK = 63
    COMMENT_LINE = 64
    WS = 65
    NEWLINE = 66
    ERROR_CHAR = 67
    UNCLOSE_STRING = 68
    ILLEGAL_ESCAPE = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'const'", "'var'", 
            "'continue'", "'break'", "'range'", "'nil'", "'true'", "'false'", 
            "'boolean'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "':='", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "':'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "COMPARE_OPERATOR", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
            "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "CONST", "VAR", 
            "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "BOOLEAN", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", 
            "LESS_EQUAL", "GREATER", "GREATER_EQUAL", "AND", "OR", "NOT", 
            "ASS_DECLARE", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "COMMA", "SEMICOLON", 
            "ID", "BOOLEAN_LIT", "INTEGER_LITERAL", "DECIMAL_LITERAL", "BINARY_LITERAL", 
            "OCTAL_LITERAL", "HEX_LITERAL", "FLOATING_LITERAL", "STRING_LITERAL", 
            "NIL_LIT", "COMMENT_BLOCK", "COMMENT_LINE", "WS", "NEWLINE", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMPARE_OPERATOR", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                  "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "BOOLEAN", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", 
                  "GREATER_EQUAL", "AND", "OR", "NOT", "ASS_DECLARE", "ASSIGN", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DOT", "COLON", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACKET", "RBRACKET", "COMMA", "SEMICOLON", 
                  "LETTER", "DIGIT", "ID_PART", "ID", "BOOLEAN_LIT", "INTEGER_LITERAL", 
                  "NON_ZERO_DIGIT", "DECIMAL_LIST", "DECIMAL_LITERAL", "START_BINARY_LIT", 
                  "BINARY_LIST", "BINARY_LITERAL", "START_OCTAL_LIT", "OCTAL_DIGIT", 
                  "OCTAL_LITERAL", "START_HEX_LIT", "HEX_DIGIT", "HEX_LITERAL", 
                  "DIGITS", "OPT_FRAC", "OPT_EXP", "FLOATING_LITERAL", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "STRING_LITERAL", "NIL_LIT", 
                  "COMMENT_BLOCK", "COMMENT_LINE", "WS", "NEWLINE", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[82] = self.NEWLINE_action 
            actions[83] = self.ERROR_CHAR_action 
            actions[84] = self.UNCLOSE_STRING_action 
            actions[85] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

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

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[0:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[0:-1])
                elif (self.text[-1] == '\r'):
                    raise UncloseString(self.text[0:-1])
                else:
                    raise UncloseString(self.text[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[0:])

     


