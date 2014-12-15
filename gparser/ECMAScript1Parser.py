# Generated from java-escape by ANTLR 4.4
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ECMAScript1Listener import ECMAScript1Listener
else:
    from ECMAScript1Listener import ECMAScript1Listener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"l\u0287\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3")
        buf.write(u"\2\3\2\5\2s\n\2\3\3\6\3v\n\3\r\3\16\3w\3\4\3\4\5\4|\n")
        buf.write(u"\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\5\5\u008d\n\5\3\6\3\6\5\6\u0091\n\6\3\6\3")
        buf.write(u"\6\3\7\6\7\u0096\n\7\r\7\16\7\u0097\3\b\3\b\3\b\3\b\3")
        buf.write(u"\t\3\t\3\t\7\t\u00a1\n\t\f\t\16\t\u00a4\13\t\3\n\3\n")
        buf.write(u"\5\n\u00a8\n\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3")
        buf.write(u"\16\3\16\3\16\3\16\3\16\3\16\5\16\u00b8\n\16\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\5\17\u00cb\n\17\3\17\3\17\5\17")
        buf.write(u"\u00cf\n\17\3\17\3\17\5\17\u00d3\n\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\5\17\u00dd\n\17\3\17\3\17\5")
        buf.write(u"\17\u00e1\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\5\17\u00f7\n\17\3\20\3\20\5\20\u00fb\n\20\3")
        buf.write(u"\20\3\20\3\21\3\21\5\21\u0101\n\21\3\21\3\21\3\22\3\22")
        buf.write(u"\5\22\u0107\n\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\5\25\u0119")
        buf.write(u"\n\25\3\25\3\25\5\25\u011d\n\25\5\25\u011f\n\25\3\25")
        buf.write(u"\3\25\3\26\6\26\u0124\n\26\r\26\16\26\u0125\3\27\3\27")
        buf.write(u"\3\27\3\27\5\27\u012c\n\27\3\30\3\30\3\30\5\30\u0131")
        buf.write(u"\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\5\33\u0148\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\5\37")
        buf.write(u"\u015a\n\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \7 \u0164")
        buf.write(u"\n \f \16 \u0167\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write(u"!\3!\3!\3!\3!\5!\u0178\n!\3\"\5\"\u017b\n\"\3#\3#\5#")
        buf.write(u"\u017f\n#\3#\5#\u0182\n#\3#\5#\u0185\n#\3#\3#\3$\5$\u018a")
        buf.write(u"\n$\3$\3$\3$\5$\u018f\n$\3$\7$\u0192\n$\f$\16$\u0195")
        buf.write(u"\13$\3%\6%\u0198\n%\r%\16%\u0199\3&\3&\5&\u019e\n&\3")
        buf.write(u"&\5&\u01a1\n&\3&\3&\3\'\3\'\3\'\7\'\u01a8\n\'\f\'\16")
        buf.write(u"\'\u01ab\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\5(\u01c0\n(\3)\3)\3)\5)\u01c5\n)\3")
        buf.write(u"*\3*\3+\3+\5+\u01cb\n+\3+\3+\3,\3,\3,\7,\u01d2\n,\f,")
        buf.write(u"\16,\u01d5\13,\3-\3-\3-\7-\u01da\n-\f-\16-\u01dd\13-")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\5.\u01f6\n.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\5.\u0201\n.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\7.\u0263\n.")
        buf.write(u"\f.\16.\u0266\13.\3/\3/\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write(u"\u026f\n\60\3\61\3\61\3\62\3\62\5\62\u0275\n\62\3\63")
        buf.write(u"\3\63\3\63\3\63\5\63\u027b\n\63\3\64\3\64\3\65\3\65\3")
        buf.write(u"\66\3\66\3\67\3\67\38\38\38\2\3Z9\2\4\6\b\n\f\16\20\22")
        buf.write(u"\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNP")
        buf.write(u"RTVXZ\\^`bdfhjln\2\7\n\2\17\17\23\23\26\26\31\31\37\37")
        buf.write(u"!\"%&\62\63\3\2:<\3\2=V\3\2Wf\4\2\b\b\'\'\u02c7\2r\3")
        buf.write(u"\2\2\2\4u\3\2\2\2\6{\3\2\2\2\b\u008c\3\2\2\2\n\u008e")
        buf.write(u"\3\2\2\2\f\u0095\3\2\2\2\16\u0099\3\2\2\2\20\u009d\3")
        buf.write(u"\2\2\2\22\u00a5\3\2\2\2\24\u00a9\3\2\2\2\26\u00ac\3\2")
        buf.write(u"\2\2\30\u00ae\3\2\2\2\32\u00b0\3\2\2\2\34\u00f6\3\2\2")
        buf.write(u"\2\36\u00f8\3\2\2\2 \u00fe\3\2\2\2\"\u0104\3\2\2\2$\u010a")
        buf.write(u"\3\2\2\2&\u0110\3\2\2\2(\u0116\3\2\2\2*\u0123\3\2\2\2")
        buf.write(u",\u0127\3\2\2\2.\u012d\3\2\2\2\60\u0132\3\2\2\2\62\u0136")
        buf.write(u"\3\2\2\2\64\u0147\3\2\2\2\66\u0149\3\2\2\28\u014f\3\2")
        buf.write(u"\2\2:\u0152\3\2\2\2<\u0155\3\2\2\2>\u0160\3\2\2\2@\u0177")
        buf.write(u"\3\2\2\2B\u017a\3\2\2\2D\u017c\3\2\2\2F\u0189\3\2\2\2")
        buf.write(u"H\u0197\3\2\2\2J\u019b\3\2\2\2L\u01a4\3\2\2\2N\u01bf")
        buf.write(u"\3\2\2\2P\u01c4\3\2\2\2R\u01c6\3\2\2\2T\u01c8\3\2\2\2")
        buf.write(u"V\u01ce\3\2\2\2X\u01d6\3\2\2\2Z\u0200\3\2\2\2\\\u0267")
        buf.write(u"\3\2\2\2^\u026e\3\2\2\2`\u0270\3\2\2\2b\u0274\3\2\2\2")
        buf.write(u"d\u027a\3\2\2\2f\u027c\3\2\2\2h\u027e\3\2\2\2j\u0280")
        buf.write(u"\3\2\2\2l\u0282\3\2\2\2n\u0284\3\2\2\2ps\5\4\3\2qs\3")
        buf.write(u"\2\2\2rp\3\2\2\2rq\3\2\2\2s\3\3\2\2\2tv\5\6\4\2ut\3\2")
        buf.write(u"\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\5\3\2\2\2y|\5\b\5")
        buf.write(u"\2z|\5<\37\2{y\3\2\2\2{z\3\2\2\2|\7\3\2\2\2}\u008d\5")
        buf.write(u"\n\6\2~\u008d\5\16\b\2\177\u008d\5\26\f\2\u0080\u008d")
        buf.write(u"\5\30\r\2\u0081\u008d\5\32\16\2\u0082\u008d\5\34\17\2")
        buf.write(u"\u0083\u008d\5\36\20\2\u0084\u008d\5 \21\2\u0085\u008d")
        buf.write(u"\5\"\22\2\u0086\u008d\5$\23\2\u0087\u008d\5\60\31\2\u0088")
        buf.write(u"\u008d\5&\24\2\u0089\u008d\5\62\32\2\u008a\u008d\5\64")
        buf.write(u"\33\2\u008b\u008d\5:\36\2\u008c}\3\2\2\2\u008c~\3\2\2")
        buf.write(u"\2\u008c\177\3\2\2\2\u008c\u0080\3\2\2\2\u008c\u0081")
        buf.write(u"\3\2\2\2\u008c\u0082\3\2\2\2\u008c\u0083\3\2\2\2\u008c")
        buf.write(u"\u0084\3\2\2\2\u008c\u0085\3\2\2\2\u008c\u0086\3\2\2")
        buf.write(u"\2\u008c\u0087\3\2\2\2\u008c\u0088\3\2\2\2\u008c\u0089")
        buf.write(u"\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d")
        buf.write(u"\t\3\2\2\2\u008e\u0090\7$\2\2\u008f\u0091\5\f\7\2\u0090")
        buf.write(u"\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\3\2\2")
        buf.write(u"\2\u0092\u0093\7\r\2\2\u0093\13\3\2\2\2\u0094\u0096\5")
        buf.write(u"\b\5\2\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write(u"\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\r\3\2\2\2\u0099")
        buf.write(u"\u009a\7D\2\2\u009a\u009b\5\20\t\2\u009b\u009c\5j\66")
        buf.write(u"\2\u009c\17\3\2\2\2\u009d\u00a2\5\22\n\2\u009e\u009f")
        buf.write(u"\7\33\2\2\u009f\u00a1\5\22\n\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write(u"\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2")
        buf.write(u"\2\u00a3\21\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7\7")
        buf.write(u"g\2\2\u00a6\u00a8\5\24\13\2\u00a7\u00a6\3\2\2\2\u00a7")
        buf.write(u"\u00a8\3\2\2\2\u00a8\23\3\2\2\2\u00a9\u00aa\7\21\2\2")
        buf.write(u"\u00aa\u00ab\5Z.\2\u00ab\25\3\2\2\2\u00ac\u00ad\7.\2")
        buf.write(u"\2\u00ad\27\3\2\2\2\u00ae\u00af\5X-\2\u00af\31\3\2\2")
        buf.write(u"\2\u00b0\u00b1\7R\2\2\u00b1\u00b2\7\36\2\2\u00b2\u00b3")
        buf.write(u"\5X-\2\u00b3\u00b4\7\20\2\2\u00b4\u00b7\5\b\5\2\u00b5")
        buf.write(u"\u00b6\7B\2\2\u00b6\u00b8\5\b\5\2\u00b7\u00b5\3\2\2\2")
        buf.write(u"\u00b7\u00b8\3\2\2\2\u00b8\33\3\2\2\2\u00b9\u00ba\7>")
        buf.write(u"\2\2\u00ba\u00bb\5\b\5\2\u00bb\u00bc\7L\2\2\u00bc\u00bd")
        buf.write(u"\7\36\2\2\u00bd\u00be\5X-\2\u00be\u00bf\7\20\2\2\u00bf")
        buf.write(u"\u00c0\5j\66\2\u00c0\u00f7\3\2\2\2\u00c1\u00c2\7L\2\2")
        buf.write(u"\u00c2\u00c3\7\36\2\2\u00c3\u00c4\5X-\2\u00c4\u00c5\7")
        buf.write(u"\20\2\2\u00c5\u00c6\5\b\5\2\u00c6\u00f7\3\2\2\2\u00c7")
        buf.write(u"\u00c8\7J\2\2\u00c8\u00ca\7\36\2\2\u00c9\u00cb\5X-\2")
        buf.write(u"\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc")
        buf.write(u"\3\2\2\2\u00cc\u00ce\7.\2\2\u00cd\u00cf\5X-\2\u00ce\u00cd")
        buf.write(u"\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write(u"\u00d2\7.\2\2\u00d1\u00d3\5X-\2\u00d2\u00d1\3\2\2\2\u00d2")
        buf.write(u"\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\7\20\2")
        buf.write(u"\2\u00d5\u00f7\5\b\5\2\u00d6\u00d7\7J\2\2\u00d7\u00d8")
        buf.write(u"\7\36\2\2\u00d8\u00d9\7D\2\2\u00d9\u00da\5\20\t\2\u00da")
        buf.write(u"\u00dc\7.\2\2\u00db\u00dd\5X-\2\u00dc\u00db\3\2\2\2\u00dc")
        buf.write(u"\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0\7.\2\2")
        buf.write(u"\u00df\u00e1\5X-\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3")
        buf.write(u"\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\7\20\2\2\u00e3")
        buf.write(u"\u00e4\5\b\5\2\u00e4\u00f7\3\2\2\2\u00e5\u00e6\7J\2\2")
        buf.write(u"\u00e6\u00e7\7\36\2\2\u00e7\u00e8\5Z.\2\u00e8\u00e9\7")
        buf.write(u"U\2\2\u00e9\u00ea\5X-\2\u00ea\u00eb\7\20\2\2\u00eb\u00ec")
        buf.write(u"\5\b\5\2\u00ec\u00f7\3\2\2\2\u00ed\u00ee\7J\2\2\u00ee")
        buf.write(u"\u00ef\7\36\2\2\u00ef\u00f0\7D\2\2\u00f0\u00f1\5\22\n")
        buf.write(u"\2\u00f1\u00f2\7U\2\2\u00f2\u00f3\5X-\2\u00f3\u00f4\7")
        buf.write(u"\20\2\2\u00f4\u00f5\5\b\5\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write(u"\u00b9\3\2\2\2\u00f6\u00c1\3\2\2\2\u00f6\u00c7\3\2\2")
        buf.write(u"\2\u00f6\u00d6\3\2\2\2\u00f6\u00e5\3\2\2\2\u00f6\u00ed")
        buf.write(u"\3\2\2\2\u00f7\35\3\2\2\2\u00f8\u00fa\7I\2\2\u00f9\u00fb")
        buf.write(u"\7g\2\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write(u"\u00fc\3\2\2\2\u00fc\u00fd\5j\66\2\u00fd\37\3\2\2\2\u00fe")
        buf.write(u"\u0100\7=\2\2\u00ff\u0101\7g\2\2\u0100\u00ff\3\2\2\2")
        buf.write(u"\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103")
        buf.write(u"\5j\66\2\u0103!\3\2\2\2\u0104\u0106\7G\2\2\u0105\u0107")
        buf.write(u"\5X-\2\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107")
        buf.write(u"\u0108\3\2\2\2\u0108\u0109\5j\66\2\u0109#\3\2\2\2\u010a")
        buf.write(u"\u010b\7P\2\2\u010b\u010c\7\36\2\2\u010c\u010d\5X-\2")
        buf.write(u"\u010d\u010e\7\20\2\2\u010e\u010f\5\b\5\2\u010f%\3\2")
        buf.write(u"\2\2\u0110\u0111\7K\2\2\u0111\u0112\7\36\2\2\u0112\u0113")
        buf.write(u"\5X-\2\u0113\u0114\7\20\2\2\u0114\u0115\5(\25\2\u0115")
        buf.write(u"\'\3\2\2\2\u0116\u0118\7$\2\2\u0117\u0119\5*\26\2\u0118")
        buf.write(u"\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011e\3\2\2")
        buf.write(u"\2\u011a\u011c\5.\30\2\u011b\u011d\5*\26\2\u011c\u011b")
        buf.write(u"\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\3\2\2\2\u011e")
        buf.write(u"\u011a\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\3\2\2")
        buf.write(u"\2\u0120\u0121\7\r\2\2\u0121)\3\2\2\2\u0122\u0124\5,")
        buf.write(u"\27\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0123")
        buf.write(u"\3\2\2\2\u0125\u0126\3\2\2\2\u0126+\3\2\2\2\u0127\u0128")
        buf.write(u"\7A\2\2\u0128\u0129\5X-\2\u0129\u012b\7\35\2\2\u012a")
        buf.write(u"\u012c\5\f\7\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2")
        buf.write(u"\2\u012c-\3\2\2\2\u012d\u012e\7Q\2\2\u012e\u0130\7\35")
        buf.write(u"\2\2\u012f\u0131\5\f\7\2\u0130\u012f\3\2\2\2\u0130\u0131")
        buf.write(u"\3\2\2\2\u0131/\3\2\2\2\u0132\u0133\7g\2\2\u0133\u0134")
        buf.write(u"\7\35\2\2\u0134\u0135\5\b\5\2\u0135\61\3\2\2\2\u0136")
        buf.write(u"\u0137\7S\2\2\u0137\u0138\5X-\2\u0138\u0139\5j\66\2\u0139")
        buf.write(u"\63\3\2\2\2\u013a\u013b\7V\2\2\u013b\u013c\5\n\6\2\u013c")
        buf.write(u"\u013d\5\66\34\2\u013d\u0148\3\2\2\2\u013e\u013f\7V\2")
        buf.write(u"\2\u013f\u0140\5\n\6\2\u0140\u0141\58\35\2\u0141\u0148")
        buf.write(u"\3\2\2\2\u0142\u0143\7V\2\2\u0143\u0144\5\n\6\2\u0144")
        buf.write(u"\u0145\5\66\34\2\u0145\u0146\58\35\2\u0146\u0148\3\2")
        buf.write(u"\2\2\u0147\u013a\3\2\2\2\u0147\u013e\3\2\2\2\u0147\u0142")
        buf.write(u"\3\2\2\2\u0148\65\3\2\2\2\u0149\u014a\7E\2\2\u014a\u014b")
        buf.write(u"\7\36\2\2\u014b\u014c\7g\2\2\u014c\u014d\7\20\2\2\u014d")
        buf.write(u"\u014e\5\n\6\2\u014e\67\3\2\2\2\u014f\u0150\7F\2\2\u0150")
        buf.write(u"\u0151\5\n\6\2\u01519\3\2\2\2\u0152\u0153\7M\2\2\u0153")
        buf.write(u"\u0154\5j\66\2\u0154;\3\2\2\2\u0155\u0156\7N\2\2\u0156")
        buf.write(u"\u0157\7g\2\2\u0157\u0159\7\36\2\2\u0158\u015a\5> \2")
        buf.write(u"\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b")
        buf.write(u"\3\2\2\2\u015b\u015c\7\20\2\2\u015c\u015d\7$\2\2\u015d")
        buf.write(u"\u015e\5B\"\2\u015e\u015f\7\r\2\2\u015f=\3\2\2\2\u0160")
        buf.write(u"\u0165\7g\2\2\u0161\u0162\7\33\2\2\u0162\u0164\7g\2\2")
        buf.write(u"\u0163\u0161\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163")
        buf.write(u"\3\2\2\2\u0165\u0166\3\2\2\2\u0166?\3\2\2\2\u0167\u0165")
        buf.write(u"\3\2\2\2\u0168\u0169\7N\2\2\u0169\u016a\7\36\2\2\u016a")
        buf.write(u"\u016b\5> \2\u016b\u016c\7\20\2\2\u016c\u016d\7$\2\2")
        buf.write(u"\u016d\u016e\5B\"\2\u016e\u016f\7\r\2\2\u016f\u0178\3")
        buf.write(u"\2\2\2\u0170\u0171\7N\2\2\u0171\u0172\7\36\2\2\u0172")
        buf.write(u"\u0173\7\20\2\2\u0173\u0174\7$\2\2\u0174\u0175\5B\"\2")
        buf.write(u"\u0175\u0176\7\r\2\2\u0176\u0178\3\2\2\2\u0177\u0168")
        buf.write(u"\3\2\2\2\u0177\u0170\3\2\2\2\u0178A\3\2\2\2\u0179\u017b")
        buf.write(u"\5\4\3\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write(u"C\3\2\2\2\u017c\u017e\7\4\2\2\u017d\u017f\5F$\2\u017e")
        buf.write(u"\u017d\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2")
        buf.write(u"\2\u0180\u0182\7\33\2\2\u0181\u0180\3\2\2\2\u0181\u0182")
        buf.write(u"\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u0185\5H%\2\u0184")
        buf.write(u"\u0183\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2")
        buf.write(u"\2\u0186\u0187\7\30\2\2\u0187E\3\2\2\2\u0188\u018a\5")
        buf.write(u"H%\2\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b")
        buf.write(u"\3\2\2\2\u018b\u0193\5Z.\2\u018c\u018e\7\33\2\2\u018d")
        buf.write(u"\u018f\5H%\2\u018e\u018d\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write(u"\u018f\u0190\3\2\2\2\u0190\u0192\5Z.\2\u0191\u018c\3")
        buf.write(u"\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write(u"\u0194\3\2\2\2\u0194G\3\2\2\2\u0195\u0193\3\2\2\2\u0196")
        buf.write(u"\u0198\7\33\2\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2")
        buf.write(u"\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019aI\3\2")
        buf.write(u"\2\2\u019b\u019d\7$\2\2\u019c\u019e\5L\'\2\u019d\u019c")
        buf.write(u"\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2\u019f")
        buf.write(u"\u01a1\7\33\2\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2")
        buf.write(u"\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\7\r\2\2\u01a3K\3\2")
        buf.write(u"\2\2\u01a4\u01a9\5N(\2\u01a5\u01a6\7\33\2\2\u01a6\u01a8")
        buf.write(u"\5N(\2\u01a7\u01a5\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9")
        buf.write(u"\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aaM\3\2\2\2\u01ab")
        buf.write(u"\u01a9\3\2\2\2\u01ac\u01ad\5P)\2\u01ad\u01ae\7\35\2\2")
        buf.write(u"\u01ae\u01af\5Z.\2\u01af\u01c0\3\2\2\2\u01b0\u01b1\7")
        buf.write(u"\32\2\2\u01b1\u01b2\7\36\2\2\u01b2\u01b3\7\20\2\2\u01b3")
        buf.write(u"\u01b4\7$\2\2\u01b4\u01b5\5B\"\2\u01b5\u01b6\7\r\2\2")
        buf.write(u"\u01b6\u01c0\3\2\2\2\u01b7\u01b8\7#\2\2\u01b8\u01b9\7")
        buf.write(u"\36\2\2\u01b9\u01ba\5R*\2\u01ba\u01bb\7\20\2\2\u01bb")
        buf.write(u"\u01bc\7$\2\2\u01bc\u01bd\5B\"\2\u01bd\u01be\7\r\2\2")
        buf.write(u"\u01be\u01c0\3\2\2\2\u01bf\u01ac\3\2\2\2\u01bf\u01b0")
        buf.write(u"\3\2\2\2\u01bf\u01b7\3\2\2\2\u01c0O\3\2\2\2\u01c1\u01c5")
        buf.write(u"\5b\62\2\u01c2\u01c5\7h\2\2\u01c3\u01c5\5`\61\2\u01c4")
        buf.write(u"\u01c1\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2")
        buf.write(u"\2\u01c5Q\3\2\2\2\u01c6\u01c7\7g\2\2\u01c7S\3\2\2\2\u01c8")
        buf.write(u"\u01ca\7\36\2\2\u01c9\u01cb\5V,\2\u01ca\u01c9\3\2\2\2")
        buf.write(u"\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd")
        buf.write(u"\7\20\2\2\u01cdU\3\2\2\2\u01ce\u01d3\5Z.\2\u01cf\u01d0")
        buf.write(u"\7\33\2\2\u01d0\u01d2\5Z.\2\u01d1\u01cf\3\2\2\2\u01d2")
        buf.write(u"\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2")
        buf.write(u"\2\u01d4W\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01db\5Z")
        buf.write(u".\2\u01d7\u01d8\7\33\2\2\u01d8\u01da\5Z.\2\u01d9\u01d7")
        buf.write(u"\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db")
        buf.write(u"\u01dc\3\2\2\2\u01dcY\3\2\2\2\u01dd\u01db\3\2\2\2\u01de")
        buf.write(u"\u01df\b.\1\2\u01df\u01e0\7T\2\2\u01e0\u0201\5Z.+\u01e1")
        buf.write(u"\u01e2\7H\2\2\u01e2\u0201\5Z.*\u01e3\u01e4\7@\2\2\u01e4")
        buf.write(u"\u0201\5Z.)\u01e5\u01e6\7(\2\2\u01e6\u0201\5Z.(\u01e7")
        buf.write(u"\u01e8\7\7\2\2\u01e8\u0201\5Z.\'\u01e9\u01ea\7,\2\2\u01ea")
        buf.write(u"\u0201\5Z.&\u01eb\u01ec\7\34\2\2\u01ec\u0201\5Z.%\u01ed")
        buf.write(u"\u01ee\7\66\2\2\u01ee\u0201\5Z.$\u01ef\u01f0\7\25\2\2")
        buf.write(u"\u01f0\u0201\5Z.#\u01f1\u0201\5@!\2\u01f2\u01f3\7C\2")
        buf.write(u"\2\u01f3\u01f5\5Z.\2\u01f4\u01f6\5T+\2\u01f5\u01f4\3")
        buf.write(u"\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u0201\3\2\2\2\u01f7")
        buf.write(u"\u0201\7O\2\2\u01f8\u0201\7g\2\2\u01f9\u0201\5^\60\2")
        buf.write(u"\u01fa\u0201\5D#\2\u01fb\u0201\5J&\2\u01fc\u01fd\7\36")
        buf.write(u"\2\2\u01fd\u01fe\5X-\2\u01fe\u01ff\7\20\2\2\u01ff\u0201")
        buf.write(u"\3\2\2\2\u0200\u01de\3\2\2\2\u0200\u01e1\3\2\2\2\u0200")
        buf.write(u"\u01e3\3\2\2\2\u0200\u01e5\3\2\2\2\u0200\u01e7\3\2\2")
        buf.write(u"\2\u0200\u01e9\3\2\2\2\u0200\u01eb\3\2\2\2\u0200\u01ed")
        buf.write(u"\3\2\2\2\u0200\u01ef\3\2\2\2\u0200\u01f1\3\2\2\2\u0200")
        buf.write(u"\u01f2\3\2\2\2\u0200\u01f7\3\2\2\2\u0200\u01f8\3\2\2")
        buf.write(u"\2\u0200\u01f9\3\2\2\2\u0200\u01fa\3\2\2\2\u0200\u01fb")
        buf.write(u"\3\2\2\2\u0200\u01fc\3\2\2\2\u0201\u0264\3\2\2\2\u0202")
        buf.write(u"\u0203\f\"\2\2\u0203\u0204\7\5\2\2\u0204\u0263\5Z.#\u0205")
        buf.write(u"\u0206\f!\2\2\u0206\u0207\7\65\2\2\u0207\u0263\5Z.\"")
        buf.write(u"\u0208\u0209\f \2\2\u0209\u020a\7\16\2\2\u020a\u0263")
        buf.write(u"\5Z.!\u020b\u020c\f\37\2\2\u020c\u020d\7,\2\2\u020d\u0263")
        buf.write(u"\5Z. \u020e\u020f\f\36\2\2\u020f\u0210\7\34\2\2\u0210")
        buf.write(u"\u0263\5Z.\37\u0211\u0212\f\35\2\2\u0212\u0213\7\f\2")
        buf.write(u"\2\u0213\u0263\5Z.\36\u0214\u0215\f\34\2\2\u0215\u0216")
        buf.write(u"\7)\2\2\u0216\u0263\5Z.\35\u0217\u0218\f\33\2\2\u0218")
        buf.write(u"\u0219\7\27\2\2\u0219\u0263\5Z.\34\u021a\u021b\f\32\2")
        buf.write(u"\2\u021b\u021c\7\6\2\2\u021c\u0263\5Z.\33\u021d\u021e")
        buf.write(u"\f\31\2\2\u021e\u021f\7\61\2\2\u021f\u0263\5Z.\32\u0220")
        buf.write(u"\u0221\f\30\2\2\u0221\u0222\7\13\2\2\u0222\u0263\5Z.")
        buf.write(u"\31\u0223\u0224\f\27\2\2\u0224\u0225\7\67\2\2\u0225\u0263")
        buf.write(u"\5Z.\30\u0226\u0227\f\26\2\2\u0227\u0228\7?\2\2\u0228")
        buf.write(u"\u0263\5Z.\27\u0229\u022a\f\25\2\2\u022a\u022b\7U\2\2")
        buf.write(u"\u022b\u0263\5Z.\26\u022c\u022d\f\24\2\2\u022d\u022e")
        buf.write(u"\7\64\2\2\u022e\u0263\5Z.\25\u022f\u0230\f\23\2\2\u0230")
        buf.write(u"\u0231\7\n\2\2\u0231\u0263\5Z.\24\u0232\u0233\f\22\2")
        buf.write(u"\2\u0233\u0234\7-\2\2\u0234\u0263\5Z.\23\u0235\u0236")
        buf.write(u"\f\21\2\2\u0236\u0237\7\t\2\2\u0237\u0263\5Z.\22\u0238")
        buf.write(u"\u0239\f\20\2\2\u0239\u023a\7\3\2\2\u023a\u0263\5Z.\21")
        buf.write(u"\u023b\u023c\f\17\2\2\u023c\u023d\7*\2\2\u023d\u0263")
        buf.write(u"\5Z.\20\u023e\u023f\f\16\2\2\u023f\u0240\7\24\2\2\u0240")
        buf.write(u"\u0263\5Z.\17\u0241\u0242\f\r\2\2\u0242\u0243\7/\2\2")
        buf.write(u"\u0243\u0263\5Z.\16\u0244\u0245\f\f\2\2\u0245\u0246\7")
        buf.write(u"\60\2\2\u0246\u0263\5Z.\r\u0247\u0248\f\13\2\2\u0248")
        buf.write(u"\u0249\7 \2\2\u0249\u024a\5Z.\2\u024a\u024b\7\35\2\2")
        buf.write(u"\u024b\u024c\5Z.\f\u024c\u0263\3\2\2\2\u024d\u024e\f")
        buf.write(u"\61\2\2\u024e\u024f\7\4\2\2\u024f\u0250\5X-\2\u0250\u0251")
        buf.write(u"\7\30\2\2\u0251\u0263\3\2\2\2\u0252\u0253\f\60\2\2\u0253")
        buf.write(u"\u0254\7+\2\2\u0254\u0263\5b\62\2\u0255\u0256\f/\2\2")
        buf.write(u"\u0256\u0263\5T+\2\u0257\u0258\f-\2\2\u0258\u0263\7(")
        buf.write(u"\2\2\u0259\u025a\f,\2\2\u025a\u0263\7\7\2\2\u025b\u025c")
        buf.write(u"\f\n\2\2\u025c\u025d\7\21\2\2\u025d\u0263\5X-\2\u025e")
        buf.write(u"\u025f\f\t\2\2\u025f\u0260\5\\/\2\u0260\u0261\5X-\2\u0261")
        buf.write(u"\u0263\3\2\2\2\u0262\u0202\3\2\2\2\u0262\u0205\3\2\2")
        buf.write(u"\2\u0262\u0208\3\2\2\2\u0262\u020b\3\2\2\2\u0262\u020e")
        buf.write(u"\3\2\2\2\u0262\u0211\3\2\2\2\u0262\u0214\3\2\2\2\u0262")
        buf.write(u"\u0217\3\2\2\2\u0262\u021a\3\2\2\2\u0262\u021d\3\2\2")
        buf.write(u"\2\u0262\u0220\3\2\2\2\u0262\u0223\3\2\2\2\u0262\u0226")
        buf.write(u"\3\2\2\2\u0262\u0229\3\2\2\2\u0262\u022c\3\2\2\2\u0262")
        buf.write(u"\u022f\3\2\2\2\u0262\u0232\3\2\2\2\u0262\u0235\3\2\2")
        buf.write(u"\2\u0262\u0238\3\2\2\2\u0262\u023b\3\2\2\2\u0262\u023e")
        buf.write(u"\3\2\2\2\u0262\u0241\3\2\2\2\u0262\u0244\3\2\2\2\u0262")
        buf.write(u"\u0247\3\2\2\2\u0262\u024d\3\2\2\2\u0262\u0252\3\2\2")
        buf.write(u"\2\u0262\u0255\3\2\2\2\u0262\u0257\3\2\2\2\u0262\u0259")
        buf.write(u"\3\2\2\2\u0262\u025b\3\2\2\2\u0262\u025e\3\2\2\2\u0263")
        buf.write(u"\u0266\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2")
        buf.write(u"\2\u0265[\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u0268\t\2")
        buf.write(u"\2\2\u0268]\3\2\2\2\u0269\u026f\5l\67\2\u026a\u026f\5")
        buf.write(u"n8\2\u026b\u026f\7h\2\2\u026c\u026f\78\2\2\u026d\u026f")
        buf.write(u"\5`\61\2\u026e\u0269\3\2\2\2\u026e\u026a\3\2\2\2\u026e")
        buf.write(u"\u026b\3\2\2\2\u026e\u026c\3\2\2\2\u026e\u026d\3\2\2")
        buf.write(u"\2\u026f_\3\2\2\2\u0270\u0271\t\3\2\2\u0271a\3\2\2\2")
        buf.write(u"\u0272\u0275\7g\2\2\u0273\u0275\5d\63\2\u0274\u0272\3")
        buf.write(u"\2\2\2\u0274\u0273\3\2\2\2\u0275c\3\2\2\2\u0276\u027b")
        buf.write(u"\5f\64\2\u0277\u027b\5h\65\2\u0278\u027b\5l\67\2\u0279")
        buf.write(u"\u027b\5n8\2\u027a\u0276\3\2\2\2\u027a\u0277\3\2\2\2")
        buf.write(u"\u027a\u0278\3\2\2\2\u027a\u0279\3\2\2\2\u027be\3\2\2")
        buf.write(u"\2\u027c\u027d\t\4\2\2\u027dg\3\2\2\2\u027e\u027f\t\5")
        buf.write(u"\2\2\u027fi\3\2\2\2\u0280\u0281\7.\2\2\u0281k\3\2\2\2")
        buf.write(u"\u0282\u0283\7\22\2\2\u0283m\3\2\2\2\u0284\u0285\t\6")
        buf.write(u"\2\2\u0285o\3\2\2\2\65rw{\u008c\u0090\u0097\u00a2\u00a7")
        buf.write(u"\u00b7\u00ca\u00ce\u00d2\u00dc\u00e0\u00f6\u00fa\u0100")
        buf.write(u"\u0106\u0118\u011c\u011e\u0125\u012b\u0130\u0147\u0159")
        buf.write(u"\u0165\u0177\u017a\u017e\u0181\u0184\u0189\u018e\u0193")
        buf.write(u"\u0199\u019d\u01a0\u01a9\u01bf\u01c4\u01ca\u01d3\u01db")
        buf.write(u"\u01f5\u0200\u0262\u0264\u026e\u0274\u027a")
        return buf.getvalue()
		

class ECMAScript1Parser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__52=1
    T__51=2
    T__50=3
    T__49=4
    T__48=5
    T__47=6
    T__46=7
    T__45=8
    T__44=9
    T__43=10
    T__42=11
    T__41=12
    T__40=13
    T__39=14
    T__38=15
    T__37=16
    T__36=17
    T__35=18
    T__34=19
    T__33=20
    T__32=21
    T__31=22
    T__30=23
    T__29=24
    T__28=25
    T__27=26
    T__26=27
    T__25=28
    T__24=29
    T__23=30
    T__22=31
    T__21=32
    T__20=33
    T__19=34
    T__18=35
    T__17=36
    T__16=37
    T__15=38
    T__14=39
    T__13=40
    T__12=41
    T__11=42
    T__10=43
    T__9=44
    T__8=45
    T__7=46
    T__6=47
    T__5=48
    T__4=49
    T__3=50
    T__2=51
    T__1=52
    T__0=53
    RegularExpressionLiteral=54
    LineTerminator=55
    DecimalLiteral=56
    HexIntegerLiteral=57
    OctalIntegerLiteral=58
    Break=59
    Do=60
    Instanceof=61
    Typeof=62
    Case=63
    Else=64
    New=65
    Var=66
    Catch=67
    Finally=68
    Return=69
    Void=70
    Continue=71
    For=72
    Switch=73
    While=74
    Debugger=75
    Function=76
    This=77
    With=78
    Default=79
    If=80
    Throw=81
    Delete=82
    In=83
    Try=84
    Class=85
    Enum=86
    Extends=87
    Super=88
    Const=89
    Export=90
    Import=91
    Implements=92
    Let=93
    Private=94
    Public=95
    Interface=96
    Package=97
    Protected=98
    Static=99
    Yield=100
    Identifier=101
    StringLiteral=102
    WhiteSpaces=103
    MultiLineComment=104
    SingleLineComment=105
    UnexpectedCharacter=106

    tokenNames = [ u"<INVALID>", u"'&'", u"'['", u"'*'", u"'<'", u"'--'", 
                   u"'false'", u"'!=='", u"'!='", u"'<='", u"'<<'", u"'}'", 
                   u"'%'", u"'*='", u"')'", u"'='", u"'null'", u"'|='", 
                   u"'|'", u"'!'", u"'<<='", u"'>>>'", u"']'", u"'-='", 
                   u"'get'", u"','", u"'-'", u"':'", u"'('", u"'&='", u"'?'", 
                   u"'>>>='", u"'>>='", u"'set'", u"'{'", u"'+='", u"'^='", 
                   u"'true'", u"'++'", u"'>>'", u"'^'", u"'.'", u"'+'", 
                   u"'==='", u"';'", u"'&&'", u"'||'", u"'>'", u"'%='", 
                   u"'/='", u"'=='", u"'/'", u"'~'", u"'>='", u"RegularExpressionLiteral", 
                   u"LineTerminator", u"DecimalLiteral", u"HexIntegerLiteral", 
                   u"OctalIntegerLiteral", u"'break'", u"'do'", u"'instanceof'", 
                   u"'typeof'", u"'case'", u"'else'", u"'new'", u"'var'", 
                   u"'catch'", u"'finally'", u"'return'", u"'void'", u"'continue'", 
                   u"'for'", u"'switch'", u"'while'", u"'debugger'", u"'function'", 
                   u"'this'", u"'with'", u"'default'", u"'if'", u"'throw'", 
                   u"'delete'", u"'in'", u"'try'", u"'class'", u"'enum'", 
                   u"'extends'", u"'super'", u"'const'", u"'export'", u"'import'", 
                   u"'implements'", u"'let'", u"'private'", u"'public'", 
                   u"'interface'", u"'package'", u"'protected'", u"'static'", 
                   u"'yield'", u"Identifier", u"StringLiteral", u"WhiteSpaces", 
                   u"MultiLineComment", u"SingleLineComment", u"UnexpectedCharacter" ]

    RULE_program = 0
    RULE_sourceElements = 1
    RULE_sourceElement = 2
    RULE_statement = 3
    RULE_block = 4
    RULE_statementList = 5
    RULE_variableStatement = 6
    RULE_variableDeclarationList = 7
    RULE_variableDeclaration = 8
    RULE_initialiser = 9
    RULE_emptyStatement = 10
    RULE_expressionStatement = 11
    RULE_ifStatement = 12
    RULE_iterationStatement = 13
    RULE_continueStatement = 14
    RULE_breakStatement = 15
    RULE_returnStatement = 16
    RULE_withStatement = 17
    RULE_switchStatement = 18
    RULE_caseBlock = 19
    RULE_caseClauses = 20
    RULE_caseClause = 21
    RULE_defaultClause = 22
    RULE_labelledStatement = 23
    RULE_throwStatement = 24
    RULE_tryStatement = 25
    RULE_catchProduction = 26
    RULE_finallyProduction = 27
    RULE_debuggerStatement = 28
    RULE_functionDeclaration = 29
    RULE_formalParameterList = 30
    RULE_functionExpression = 31
    RULE_functionBody = 32
    RULE_arrayLiteral = 33
    RULE_elementList = 34
    RULE_elision = 35
    RULE_objectLiteral = 36
    RULE_propertyNameAndValueList = 37
    RULE_propertyAssignment = 38
    RULE_propertyName = 39
    RULE_propertySetParameterList = 40
    RULE_arguments = 41
    RULE_argumentList = 42
    RULE_expressionSequence = 43
    RULE_singleExpression = 44
    RULE_assignmentOperator = 45
    RULE_literal = 46
    RULE_numericLiteral = 47
    RULE_identifierName = 48
    RULE_reservedWord = 49
    RULE_keyword = 50
    RULE_futureReservedWord = 51
    RULE_eos = 52
    RULE_nullLiteral = 53
    RULE_booleanLiteral = 54

    ruleNames =  [ u"program", u"sourceElements", u"sourceElement", u"statement", 
                   u"block", u"statementList", u"variableStatement", u"variableDeclarationList", 
                   u"variableDeclaration", u"initialiser", u"emptyStatement", 
                   u"expressionStatement", u"ifStatement", u"iterationStatement", 
                   u"continueStatement", u"breakStatement", u"returnStatement", 
                   u"withStatement", u"switchStatement", u"caseBlock", u"caseClauses", 
                   u"caseClause", u"defaultClause", u"labelledStatement", 
                   u"throwStatement", u"tryStatement", u"catchProduction", 
                   u"finallyProduction", u"debuggerStatement", u"functionDeclaration", 
                   u"formalParameterList", u"functionExpression", u"functionBody", 
                   u"arrayLiteral", u"elementList", u"elision", u"objectLiteral", 
                   u"propertyNameAndValueList", u"propertyAssignment", u"propertyName", 
                   u"propertySetParameterList", u"arguments", u"argumentList", 
                   u"expressionSequence", u"singleExpression", u"assignmentOperator", 
                   u"literal", u"numericLiteral", u"identifierName", u"reservedWord", 
                   u"keyword", u"futureReservedWord", u"eos", u"nullLiteral", 
                   u"booleanLiteral" ]

    def __init__(self, input):
        super(ECMAScript1Parser, self).__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sourceElements(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SourceElementsContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_program

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitProgram(self)




    def program(self):

        localctx = ECMAScript1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 112
            token = self._input.LA(1)
            if token in [self.T__51, self.T__48, self.T__47, self.T__37, self.T__34, self.T__27, self.T__25, self.T__19, self.T__16, self.T__15, self.T__11, self.T__9, self.T__1, self.RegularExpressionLiteral, self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral, self.Break, self.Do, self.Typeof, self.New, self.Var, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.If, self.Throw, self.Delete, self.Try, self.Identifier, self.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110 
                self.sourceElements()

            elif token in [self.EOF]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SourceElementsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.SourceElementsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sourceElement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SourceElementContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SourceElementContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_sourceElements

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterSourceElements(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitSourceElements(self)




    def sourceElements(self):

        localctx = ECMAScript1Parser.SourceElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sourceElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114 
                self.sourceElement()
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SourceElementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.SourceElementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FunctionDeclarationContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_sourceElement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterSourceElement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitSourceElement(self)




    def sourceElement(self):

        localctx = ECMAScript1Parser.SourceElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sourceElement)
        try:
            self.state = 121
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119 
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120 
                self.functionDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def labelledStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.LabelledStatementContext,0)


        def debuggerStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.DebuggerStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.BreakStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.TryStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.IfStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ThrowStatementContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.EmptyStatementContext,0)


        def withStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.WithStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ReturnStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SwitchStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionStatementContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.VariableStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.IterationStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ContinueStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(ECMAScript1Parser.BlockContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ECMAScript1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 138
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123 
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124 
                self.variableStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125 
                self.emptyStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126 
                self.expressionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 127 
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 128 
                self.iterationStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 129 
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 130 
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 131 
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 132 
                self.withStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 133 
                self.labelledStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 134 
                self.switchStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 135 
                self.throwStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 136 
                self.tryStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 137 
                self.debuggerStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitBlock(self)




    def block(self):

        localctx = ECMAScript1Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(self.T__19)
            self.state = 142
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 141 
                self.statementList()


            self.state = 144
            self.match(self.T__42)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.StatementListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_statementList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = ECMAScript1Parser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146 
                self.statement()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.VariableStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScript1Parser.EosContext,0)


        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.VariableDeclarationListContext,0)


        def Var(self):
            return self.getToken(ECMAScript1Parser.Var, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_variableStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterVariableStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitVariableStatement(self)




    def variableStatement(self):

        localctx = ECMAScript1Parser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(self.Var)
            self.state = 152 
            self.variableDeclarationList()
            self.state = 153 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.VariableDeclarationListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_variableDeclarationList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterVariableDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitVariableDeclarationList(self)




    def variableDeclarationList(self):

        localctx = ECMAScript1Parser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155 
            self.variableDeclaration()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScript1Parser.T__28:
                self.state = 156
                self.match(self.T__28)
                self.state = 157 
                self.variableDeclaration()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.VariableDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def initialiser(self):
            return self.getTypedRuleContext(ECMAScript1Parser.InitialiserContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_variableDeclaration

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = ECMAScript1Parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(self.Identifier)
            self.state = 165
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.T__38:
                self.state = 164 
                self.initialiser()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitialiserContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.InitialiserContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_initialiser

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterInitialiser(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitInitialiser(self)




    def initialiser(self):

        localctx = ECMAScript1Parser.InitialiserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_initialiser)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(self.T__38)
            self.state = 168 
            self.singleExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptyStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.EmptyStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_emptyStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitEmptyStatement(self)




    def emptyStatement(self):

        localctx = ECMAScript1Parser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(self.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ExpressionStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_expressionStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = ECMAScript1Parser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172 
            self.expressionSequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.IfStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def Else(self):
            return self.getToken(ECMAScript1Parser.Else, 0)

        def If(self):
            return self.getToken(ECMAScript1Parser.If, 0)

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_ifStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = ECMAScript1Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(self.If)
            self.state = 175
            self.match(self.T__25)
            self.state = 176 
            self.expressionSequence()
            self.state = 177
            self.match(self.T__39)
            self.state = 178 
            self.statement()
            self.state = 181
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 179
                self.match(self.Else)
                self.state = 180 
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.IterationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_iterationStatement

     
        def copyFrom(self, ctx):
            super(ECMAScript1Parser.IterationStatementContext, self).copyFrom(ctx)



    class DoStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.IterationStatementContext)
            super(ECMAScript1Parser.DoStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def eos(self):
            return self.getTypedRuleContext(ECMAScript1Parser.EosContext,0)

        def While(self):
            return self.getToken(ECMAScript1Parser.While, 0)
        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)

        def Do(self):
            return self.getToken(ECMAScript1Parser.Do, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterDoStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitDoStatement(self)


    class ForVarInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.IterationStatementContext)
            super(ECMAScript1Parser.ForVarInStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)

        def For(self):
            return self.getToken(ECMAScript1Parser.For, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)

        def Var(self):
            return self.getToken(ECMAScript1Parser.Var, 0)
        def In(self):
            return self.getToken(ECMAScript1Parser.In, 0)
        def variableDeclaration(self):
            return self.getTypedRuleContext(ECMAScript1Parser.VariableDeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterForVarInStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitForVarInStatement(self)


    class ForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.IterationStatementContext)
            super(ECMAScript1Parser.ForStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)

        def For(self):
            return self.getToken(ECMAScript1Parser.For, 0)
        def expressionSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterForStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitForStatement(self)


    class WhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.IterationStatementContext)
            super(ECMAScript1Parser.WhileStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)

        def While(self):
            return self.getToken(ECMAScript1Parser.While, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitWhileStatement(self)


    class ForInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.IterationStatementContext)
            super(ECMAScript1Parser.ForInStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)

        def For(self):
            return self.getToken(ECMAScript1Parser.For, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)

        def In(self):
            return self.getToken(ECMAScript1Parser.In, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterForInStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitForInStatement(self)


    class ForVarStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.IterationStatementContext)
            super(ECMAScript1Parser.ForVarStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)

        def For(self):
            return self.getToken(ECMAScript1Parser.For, 0)
        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.VariableDeclarationListContext,0)

        def expressionSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,i)

        def Var(self):
            return self.getToken(ECMAScript1Parser.Var, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterForVarStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitForVarStatement(self)



    def iterationStatement(self):

        localctx = ECMAScript1Parser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 244
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = ECMAScript1Parser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(self.Do)
                self.state = 184 
                self.statement()
                self.state = 185
                self.match(self.While)
                self.state = 186
                self.match(self.T__25)
                self.state = 187 
                self.expressionSequence()
                self.state = 188
                self.match(self.T__39)
                self.state = 189 
                self.eos()
                pass

            elif la_ == 2:
                localctx = ECMAScript1Parser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(self.While)
                self.state = 192
                self.match(self.T__25)
                self.state = 193 
                self.expressionSequence()
                self.state = 194
                self.match(self.T__39)
                self.state = 195 
                self.statement()
                pass

            elif la_ == 3:
                localctx = ECMAScript1Parser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.match(self.For)
                self.state = 198
                self.match(self.T__25)
                self.state = 200
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 199 
                    self.expressionSequence()


                self.state = 202
                self.match(self.T__9)
                self.state = 204
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 203 
                    self.expressionSequence()


                self.state = 206
                self.match(self.T__9)
                self.state = 208
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 207 
                    self.expressionSequence()


                self.state = 210
                self.match(self.T__39)
                self.state = 211 
                self.statement()
                pass

            elif la_ == 4:
                localctx = ECMAScript1Parser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.match(self.For)
                self.state = 213
                self.match(self.T__25)
                self.state = 214
                self.match(self.Var)
                self.state = 215 
                self.variableDeclarationList()
                self.state = 216
                self.match(self.T__9)
                self.state = 218
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 217 
                    self.expressionSequence()


                self.state = 220
                self.match(self.T__9)
                self.state = 222
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 221 
                    self.expressionSequence()


                self.state = 224
                self.match(self.T__39)
                self.state = 225 
                self.statement()
                pass

            elif la_ == 5:
                localctx = ECMAScript1Parser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.match(self.For)
                self.state = 228
                self.match(self.T__25)
                self.state = 229 
                self.singleExpression(0)
                self.state = 230
                self.match(self.In)
                self.state = 231 
                self.expressionSequence()
                self.state = 232
                self.match(self.T__39)
                self.state = 233 
                self.statement()
                pass

            elif la_ == 6:
                localctx = ECMAScript1Parser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 235
                self.match(self.For)
                self.state = 236
                self.match(self.T__25)
                self.state = 237
                self.match(self.Var)
                self.state = 238 
                self.variableDeclaration()
                self.state = 239
                self.match(self.In)
                self.state = 240 
                self.expressionSequence()
                self.state = 241
                self.match(self.T__39)
                self.state = 242 
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ContinueStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScript1Parser.EosContext,0)


        def Continue(self):
            return self.getToken(ECMAScript1Parser.Continue, 0)

        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_continueStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = ECMAScript1Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_continueStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(self.Continue)
            self.state = 248
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.Identifier:
                self.state = 247
                self.match(self.Identifier)


            self.state = 250 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.BreakStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScript1Parser.EosContext,0)


        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def Break(self):
            return self.getToken(ECMAScript1Parser.Break, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_breakStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = ECMAScript1Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_breakStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(self.Break)
            self.state = 254
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.Identifier:
                self.state = 253
                self.match(self.Identifier)


            self.state = 256 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ReturnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScript1Parser.EosContext,0)


        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def Return(self):
            return self.getToken(ECMAScript1Parser.Return, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_returnStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = ECMAScript1Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(self.Return)
            self.state = 260
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 259 
                self.expressionSequence()


            self.state = 262 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.WithStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)


        def With(self):
            return self.getToken(ECMAScript1Parser.With, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_withStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterWithStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitWithStatement(self)




    def withStatement(self):

        localctx = ECMAScript1Parser.WithStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_withStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(self.With)
            self.state = 265
            self.match(self.T__25)
            self.state = 266 
            self.expressionSequence()
            self.state = 267
            self.match(self.T__39)
            self.state = 268 
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SwitchStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.SwitchStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def Switch(self):
            return self.getToken(ECMAScript1Parser.Switch, 0)

        def caseBlock(self):
            return self.getTypedRuleContext(ECMAScript1Parser.CaseBlockContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_switchStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = ECMAScript1Parser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(self.Switch)
            self.state = 271
            self.match(self.T__25)
            self.state = 272 
            self.expressionSequence()
            self.state = 273
            self.match(self.T__39)
            self.state = 274 
            self.caseBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.CaseBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def defaultClause(self):
            return self.getTypedRuleContext(ECMAScript1Parser.DefaultClauseContext,0)


        def caseClauses(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.CaseClausesContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.CaseClausesContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_caseBlock

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitCaseBlock(self)




    def caseBlock(self):

        localctx = ECMAScript1Parser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(self.T__19)
            self.state = 278
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.Case:
                self.state = 277 
                self.caseClauses()


            self.state = 284
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.Default:
                self.state = 280 
                self.defaultClause()
                self.state = 282
                _la = self._input.LA(1)
                if _la==ECMAScript1Parser.Case:
                    self.state = 281 
                    self.caseClauses()




            self.state = 286
            self.match(self.T__42)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseClausesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.CaseClausesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def caseClause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.CaseClauseContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_caseClauses

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterCaseClauses(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitCaseClauses(self)




    def caseClauses(self):

        localctx = ECMAScript1Parser.CaseClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_caseClauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 288 
                self.caseClause()
                self.state = 291 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScript1Parser.Case):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.CaseClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def Case(self):
            return self.getToken(ECMAScript1Parser.Case, 0)

        def statementList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_caseClause

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterCaseClause(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitCaseClause(self)




    def caseClause(self):

        localctx = ECMAScript1Parser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(self.Case)
            self.state = 294 
            self.expressionSequence()
            self.state = 295
            self.match(self.T__26)
            self.state = 297
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 296 
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefaultClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.DefaultClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Default(self):
            return self.getToken(ECMAScript1Parser.Default, 0)

        def statementList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_defaultClause

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitDefaultClause(self)




    def defaultClause(self):

        localctx = ECMAScript1Parser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(self.Default)
            self.state = 300
            self.match(self.T__26)
            self.state = 302
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 301 
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.LabelledStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ECMAScript1Parser.StatementContext,0)


        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_labelledStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterLabelledStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitLabelledStatement(self)




    def labelledStatement(self):

        localctx = ECMAScript1Parser.LabelledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_labelledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(self.Identifier)
            self.state = 305
            self.match(self.T__26)
            self.state = 306 
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ThrowStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ThrowStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScript1Parser.EosContext,0)


        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def Throw(self):
            return self.getToken(ECMAScript1Parser.Throw, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_throwStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitThrowStatement(self)




    def throwStatement(self):

        localctx = ECMAScript1Parser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(self.Throw)
            self.state = 309 
            self.expressionSequence()
            self.state = 310 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TryStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.TryStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(ECMAScript1Parser.Try, 0)

        def catchProduction(self):
            return self.getTypedRuleContext(ECMAScript1Parser.CatchProductionContext,0)


        def block(self):
            return self.getTypedRuleContext(ECMAScript1Parser.BlockContext,0)


        def finallyProduction(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FinallyProductionContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_tryStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitTryStatement(self)




    def tryStatement(self):

        localctx = ECMAScript1Parser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_tryStatement)
        try:
            self.state = 325
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(self.Try)
                self.state = 313 
                self.block()
                self.state = 314 
                self.catchProduction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(self.Try)
                self.state = 317 
                self.block()
                self.state = 318 
                self.finallyProduction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.match(self.Try)
                self.state = 321 
                self.block()
                self.state = 322 
                self.catchProduction()
                self.state = 323 
                self.finallyProduction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CatchProductionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.CatchProductionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(ECMAScript1Parser.Catch, 0)

        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScript1Parser.BlockContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_catchProduction

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterCatchProduction(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitCatchProduction(self)




    def catchProduction(self):

        localctx = ECMAScript1Parser.CatchProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_catchProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(self.Catch)
            self.state = 328
            self.match(self.T__25)
            self.state = 329
            self.match(self.Identifier)
            self.state = 330
            self.match(self.T__39)
            self.state = 331 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FinallyProductionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.FinallyProductionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ECMAScript1Parser.BlockContext,0)


        def Finally(self):
            return self.getToken(ECMAScript1Parser.Finally, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_finallyProduction

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterFinallyProduction(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitFinallyProduction(self)




    def finallyProduction(self):

        localctx = ECMAScript1Parser.FinallyProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_finallyProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(self.Finally)
            self.state = 334 
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DebuggerStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.DebuggerStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScript1Parser.EosContext,0)


        def Debugger(self):
            return self.getToken(ECMAScript1Parser.Debugger, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_debuggerStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterDebuggerStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitDebuggerStatement(self)




    def debuggerStatement(self):

        localctx = ECMAScript1Parser.DebuggerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_debuggerStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(self.Debugger)
            self.state = 337 
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.FunctionDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(ECMAScript1Parser.Function, 0)

        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_functionDeclaration

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = ECMAScript1Parser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(self.Function)
            self.state = 340
            self.match(self.Identifier)
            self.state = 341
            self.match(self.T__25)
            self.state = 343
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.Identifier:
                self.state = 342 
                self.formalParameterList()


            self.state = 345
            self.match(self.T__39)
            self.state = 346
            self.match(self.T__19)
            self.state = 347 
            self.functionBody()
            self.state = 348
            self.match(self.T__42)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.FormalParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i=None):
            if i is None:
                return self.getTokens(ECMAScript1Parser.Identifier)
            else:
                return self.getToken(ECMAScript1Parser.Identifier, i)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_formalParameterList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitFormalParameterList(self)




    def formalParameterList(self):

        localctx = ECMAScript1Parser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(self.Identifier)
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScript1Parser.T__28:
                self.state = 351
                self.match(self.T__28)
                self.state = 352
                self.match(self.Identifier)
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.FunctionExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(ECMAScript1Parser.Function, 0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_functionExpression

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitFunctionExpression(self)




    def functionExpression(self):

        localctx = ECMAScript1Parser.FunctionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionExpression)
        try:
            self.state = 373
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(self.Function)
                self.state = 359
                self.match(self.T__25)
                self.state = 360 
                self.formalParameterList()
                self.state = 361
                self.match(self.T__39)
                self.state = 362
                self.match(self.T__19)
                self.state = 363 
                self.functionBody()
                self.state = 364
                self.match(self.T__42)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(self.Function)
                self.state = 367
                self.match(self.T__25)
                self.state = 368
                self.match(self.T__39)
                self.state = 369
                self.match(self.T__19)
                self.state = 370 
                self.functionBody()
                self.state = 371
                self.match(self.T__42)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.FunctionBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sourceElements(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SourceElementsContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_functionBody

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitFunctionBody(self)




    def functionBody(self):

        localctx = ECMAScript1Parser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 375 
                self.sourceElements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ArrayLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def elementList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ElementListContext,0)


        def elision(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ElisionContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_arrayLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitArrayLiteral(self)




    def arrayLiteral(self):

        localctx = ECMAScript1Parser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(self.T__51)
            self.state = 380
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 379 
                self.elementList()


            self.state = 383
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 382
                self.match(self.T__28)


            self.state = 386
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.T__28:
                self.state = 385 
                self.elision()


            self.state = 388
            self.match(self.T__31)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ElementListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def elision(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.ElisionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.ElisionContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_elementList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterElementList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitElementList(self)




    def elementList(self):

        localctx = ECMAScript1Parser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.T__28:
                self.state = 390 
                self.elision()


            self.state = 393 
            self.singleExpression(0)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 394
                    self.match(self.T__28)
                    self.state = 396
                    _la = self._input.LA(1)
                    if _la==ECMAScript1Parser.T__28:
                        self.state = 395 
                        self.elision()


                    self.state = 398 
                    self.singleExpression(0) 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElisionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ElisionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_elision

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterElision(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitElision(self)




    def elision(self):

        localctx = ECMAScript1Parser.ElisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 404
                self.match(self.T__28)
                self.state = 407 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScript1Parser.T__28):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ObjectLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyNameAndValueList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.PropertyNameAndValueListContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_objectLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterObjectLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitObjectLiteral(self)




    def objectLiteral(self):

        localctx = ECMAScript1Parser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(self.T__19)
            self.state = 411
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__47) | (1 << self.T__37) | (1 << self.T__29) | (1 << self.T__20) | (1 << self.T__16) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Instanceof) | (1 << self.Typeof) | (1 << self.Case))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.Else - 64)) | (1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Catch - 64)) | (1 << (self.Finally - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.Default - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.In - 64)) | (1 << (self.Try - 64)) | (1 << (self.Class - 64)) | (1 << (self.Enum - 64)) | (1 << (self.Extends - 64)) | (1 << (self.Super - 64)) | (1 << (self.Const - 64)) | (1 << (self.Export - 64)) | (1 << (self.Import - 64)) | (1 << (self.Implements - 64)) | (1 << (self.Let - 64)) | (1 << (self.Private - 64)) | (1 << (self.Public - 64)) | (1 << (self.Interface - 64)) | (1 << (self.Package - 64)) | (1 << (self.Protected - 64)) | (1 << (self.Static - 64)) | (1 << (self.Yield - 64)) | (1 << (self.Identifier - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                self.state = 410 
                self.propertyNameAndValueList()


            self.state = 414
            _la = self._input.LA(1)
            if _la==ECMAScript1Parser.T__28:
                self.state = 413
                self.match(self.T__28)


            self.state = 416
            self.match(self.T__42)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyNameAndValueListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.PropertyNameAndValueListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyAssignment(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.PropertyAssignmentContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.PropertyAssignmentContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_propertyNameAndValueList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPropertyNameAndValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPropertyNameAndValueList(self)




    def propertyNameAndValueList(self):

        localctx = ECMAScript1Parser.PropertyNameAndValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_propertyNameAndValueList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418 
            self.propertyAssignment()
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 419
                    self.match(self.T__28)
                    self.state = 420 
                    self.propertyAssignment() 
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.PropertyAssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_propertyAssignment

     
        def copyFrom(self, ctx):
            super(ECMAScript1Parser.PropertyAssignmentContext, self).copyFrom(ctx)



    class PropertyGetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.PropertyAssignmentContext)
            super(ECMAScript1Parser.PropertyGetterContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FunctionBodyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPropertyGetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPropertyGetter(self)


    class PropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.PropertyAssignmentContext)
            super(ECMAScript1Parser.PropertyExpressionAssignmentContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)

        def propertyName(self):
            return self.getTypedRuleContext(ECMAScript1Parser.PropertyNameContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPropertyExpressionAssignment(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPropertyExpressionAssignment(self)


    class PropertySetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.PropertyAssignmentContext)
            super(ECMAScript1Parser.PropertySetterContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FunctionBodyContext,0)

        def propertySetParameterList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.PropertySetParameterListContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPropertySetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPropertySetter(self)



    def propertyAssignment(self):

        localctx = ECMAScript1Parser.PropertyAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_propertyAssignment)
        try:
            self.state = 445
            token = self._input.LA(1)
            if token in [self.T__47, self.T__37, self.T__16, self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral, self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try, self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield, self.Identifier, self.StringLiteral]:
                localctx = ECMAScript1Parser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 426 
                self.propertyName()
                self.state = 427
                self.match(self.T__26)
                self.state = 428 
                self.singleExpression(0)

            elif token in [self.T__29]:
                localctx = ECMAScript1Parser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(self.T__29)
                self.state = 431
                self.match(self.T__25)
                self.state = 432
                self.match(self.T__39)
                self.state = 433
                self.match(self.T__19)
                self.state = 434 
                self.functionBody()
                self.state = 435
                self.match(self.T__42)

            elif token in [self.T__20]:
                localctx = ECMAScript1Parser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(self.T__20)
                self.state = 438
                self.match(self.T__25)
                self.state = 439 
                self.propertySetParameterList()
                self.state = 440
                self.match(self.T__39)
                self.state = 441
                self.match(self.T__19)
                self.state = 442 
                self.functionBody()
                self.state = 443
                self.match(self.T__42)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.PropertyNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScript1Parser.IdentifierNameContext,0)


        def StringLiteral(self):
            return self.getToken(ECMAScript1Parser.StringLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(ECMAScript1Parser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_propertyName

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPropertyName(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPropertyName(self)




    def propertyName(self):

        localctx = ECMAScript1Parser.PropertyNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_propertyName)
        try:
            self.state = 450
            token = self._input.LA(1)
            if token in [self.T__47, self.T__37, self.T__16, self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try, self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield, self.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447 
                self.identifierName()

            elif token in [self.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(self.StringLiteral)

            elif token in [self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449 
                self.numericLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertySetParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.PropertySetParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_propertySetParameterList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPropertySetParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPropertySetParameterList(self)




    def propertySetParameterList(self):

        localctx = ECMAScript1Parser.PropertySetParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_propertySetParameterList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(self.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ArgumentsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argumentList(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ArgumentListContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_arguments

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterArguments(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = ECMAScript1Parser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(self.T__25)
            self.state = 456
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Identifier - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 455 
                self.argumentList()


            self.state = 458
            self.match(self.T__39)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ArgumentListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_argumentList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = ECMAScript1Parser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460 
            self.singleExpression(0)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScript1Parser.T__28:
                self.state = 461
                self.match(self.T__28)
                self.state = 462 
                self.singleExpression(0)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ExpressionSequenceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_expressionSequence

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterExpressionSequence(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitExpressionSequence(self)




    def expressionSequence(self):

        localctx = ECMAScript1Parser.ExpressionSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expressionSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468 
            self.singleExpression(0)
            self.state = 473
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 469
                    self.match(self.T__28)
                    self.state = 470 
                    self.singleExpression(0) 
                self.state = 475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SingleExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.SingleExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_singleExpression

     
        def copyFrom(self, ctx):
            super(ECMAScript1Parser.SingleExpressionContext, self).copyFrom(ctx)


    class RightShiftLogicalExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.RightShiftLogicalExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterRightShiftLogicalExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitRightShiftLogicalExpression(self)


    class TernaryExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.TernaryExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitTernaryExpression(self)


    class BitOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.BitOrExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterBitOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitBitOrExpression(self)


    class AssignmentExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.AssignmentExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitAssignmentExpression(self)


    class OrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.OrExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitOrExpression(self)


    class EqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.EqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitEqualsExpression(self)


    class InstanceofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.InstanceofExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Instanceof(self):
            return self.getToken(ECMAScript1Parser.Instanceof, 0)
        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterInstanceofExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitInstanceofExpression(self)


    class ModulusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.ModulusExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterModulusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitModulusExpression(self)


    class LeftShiftArithmeticExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.LeftShiftArithmeticExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterLeftShiftArithmeticExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitLeftShiftArithmeticExpression(self)


    class ObjectLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.ObjectLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def objectLiteral(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ObjectLiteralContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterObjectLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitObjectLiteralExpression(self)


    class PreDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.PreDecreaseExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPreDecreaseExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPreDecreaseExpression(self)


    class NotEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.NotEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.InExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)

        def In(self):
            return self.getToken(ECMAScript1Parser.In, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitInExpression(self)


    class ArrayLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.ArrayLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ArrayLiteralContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterArrayLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitArrayLiteralExpression(self)


    class IdentityNotEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.IdentityNotEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterIdentityNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitIdentityNotEqualsExpression(self)


    class ArgumentsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.ArgumentsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ArgumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterArgumentsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitArgumentsExpression(self)


    class MemberDotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.MemberDotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScript1Parser.IdentifierNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterMemberDotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitMemberDotExpression(self)


    class IdentityEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.IdentityEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterIdentityEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitIdentityEqualsExpression(self)


    class NotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.NotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitNotExpression(self)


    class DeleteExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.DeleteExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)

        def Delete(self):
            return self.getToken(ECMAScript1Parser.Delete, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterDeleteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitDeleteExpression(self)


    class IdentifierExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.IdentifierExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitIdentifierExpression(self)


    class GreaterThanExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.GreaterThanExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitGreaterThanExpression(self)


    class FnExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.FnExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functionExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FunctionExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterFnExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitFnExpression(self)


    class AddExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.AddExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitAddExpression(self)


    class BitAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.BitAndExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterBitAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitBitAndExpression(self)


    class UnaryMinusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.UnaryMinusExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterUnaryMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitUnaryMinusExpression(self)


    class PreIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.PreIncrementExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPreIncrementExpression(self)


    class MultiplyExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.MultiplyExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitMultiplyExpression(self)


    class AndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.AndExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitAndExpression(self)


    class VoidExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.VoidExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)

        def Void(self):
            return self.getToken(ECMAScript1Parser.Void, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterVoidExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitVoidExpression(self)


    class ParenthesizedExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.ParenthesizedExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitParenthesizedExpression(self)


    class DivideExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.DivideExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitDivideExpression(self)


    class UnaryPlusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.UnaryPlusExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterUnaryPlusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitUnaryPlusExpression(self)


    class LiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.LiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ECMAScript1Parser.LiteralContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitLiteralExpression(self)


    class BitNotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.BitNotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterBitNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitBitNotExpression(self)


    class PostIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.PostIncrementExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPostIncrementExpression(self)


    class TypeofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.TypeofExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)

        def Typeof(self):
            return self.getToken(ECMAScript1Parser.Typeof, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterTypeofExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitTypeofExpression(self)


    class LessThanExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.LessThanExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitLessThanExpression(self)


    class AssignmentOperatorExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.AssignmentOperatorExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)

        def assignmentOperator(self):
            return self.getTypedRuleContext(ECMAScript1Parser.AssignmentOperatorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterAssignmentOperatorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitAssignmentOperatorExpression(self)


    class NewExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.NewExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def New(self):
            return self.getToken(ECMAScript1Parser.New, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ArgumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterNewExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitNewExpression(self)


    class PostDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.PostDecreaseExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterPostDecreaseExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitPostDecreaseExpression(self)


    class SubtractExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.SubtractExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterSubtractExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitSubtractExpression(self)


    class RightShiftArithmeticExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.RightShiftArithmeticExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterRightShiftArithmeticExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitRightShiftArithmeticExpression(self)


    class BitXOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.BitXOrExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterBitXOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitBitXOrExpression(self)


    class GreaterThanEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.GreaterThanEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterGreaterThanEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitGreaterThanEqualsExpression(self)


    class MemberIndexExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.MemberIndexExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterMemberIndexExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitMemberIndexExpression(self)


    class ThisExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.ThisExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def This(self):
            return self.getToken(ECMAScript1Parser.This, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitThisExpression(self)


    class LessThanEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScript1Parser.SingleExpressionContext)
            super(ECMAScript1Parser.LessThanEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScript1Parser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScript1Parser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterLessThanEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitLessThanEqualsExpression(self)



    def singleExpression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ECMAScript1Parser.SingleExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_singleExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            token = self._input.LA(1)
            if token in [self.Delete]:
                localctx = ECMAScript1Parser.DeleteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 477
                self.match(self.Delete)
                self.state = 478 
                self.singleExpression(41)

            elif token in [self.Void]:
                localctx = ECMAScript1Parser.VoidExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 479
                self.match(self.Void)
                self.state = 480 
                self.singleExpression(40)

            elif token in [self.Typeof]:
                localctx = ECMAScript1Parser.TypeofExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 481
                self.match(self.Typeof)
                self.state = 482 
                self.singleExpression(39)

            elif token in [self.T__15]:
                localctx = ECMAScript1Parser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 483
                self.match(self.T__15)
                self.state = 484 
                self.singleExpression(38)

            elif token in [self.T__48]:
                localctx = ECMAScript1Parser.PreDecreaseExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 485
                self.match(self.T__48)
                self.state = 486 
                self.singleExpression(37)

            elif token in [self.T__11]:
                localctx = ECMAScript1Parser.UnaryPlusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 487
                self.match(self.T__11)
                self.state = 488 
                self.singleExpression(36)

            elif token in [self.T__27]:
                localctx = ECMAScript1Parser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 489
                self.match(self.T__27)
                self.state = 490 
                self.singleExpression(35)

            elif token in [self.T__1]:
                localctx = ECMAScript1Parser.BitNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 491
                self.match(self.T__1)
                self.state = 492 
                self.singleExpression(34)

            elif token in [self.T__34]:
                localctx = ECMAScript1Parser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 493
                self.match(self.T__34)
                self.state = 494 
                self.singleExpression(33)

            elif token in [self.Function]:
                localctx = ECMAScript1Parser.FnExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 495 
                self.functionExpression()

            elif token in [self.New]:
                localctx = ECMAScript1Parser.NewExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 496
                self.match(self.New)
                self.state = 497 
                self.singleExpression(0)
                self.state = 499
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 498 
                    self.arguments()



            elif token in [self.This]:
                localctx = ECMAScript1Parser.ThisExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 501
                self.match(self.This)

            elif token in [self.Identifier]:
                localctx = ECMAScript1Parser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 502
                self.match(self.Identifier)

            elif token in [self.T__47, self.T__37, self.T__16, self.RegularExpressionLiteral, self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral, self.StringLiteral]:
                localctx = ECMAScript1Parser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 503 
                self.literal()

            elif token in [self.T__51]:
                localctx = ECMAScript1Parser.ArrayLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 504 
                self.arrayLiteral()

            elif token in [self.T__19]:
                localctx = ECMAScript1Parser.ObjectLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 505 
                self.objectLiteral()

            elif token in [self.T__25]:
                localctx = ECMAScript1Parser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 506
                self.match(self.T__25)
                self.state = 507 
                self.expressionSequence()
                self.state = 508
                self.match(self.T__39)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 610
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 608
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = ECMAScript1Parser.MultiplyExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 512
                        if not self.precpred(self._ctx, 32):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 513
                        self.match(self.T__50)
                        self.state = 514 
                        self.singleExpression(33)
                        pass

                    elif la_ == 2:
                        localctx = ECMAScript1Parser.DivideExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 515
                        if not self.precpred(self._ctx, 31):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 516
                        self.match(self.T__2)
                        self.state = 517 
                        self.singleExpression(32)
                        pass

                    elif la_ == 3:
                        localctx = ECMAScript1Parser.ModulusExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 518
                        if not self.precpred(self._ctx, 30):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 519
                        self.match(self.T__41)
                        self.state = 520 
                        self.singleExpression(31)
                        pass

                    elif la_ == 4:
                        localctx = ECMAScript1Parser.AddExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 521
                        if not self.precpred(self._ctx, 29):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 522
                        self.match(self.T__11)
                        self.state = 523 
                        self.singleExpression(30)
                        pass

                    elif la_ == 5:
                        localctx = ECMAScript1Parser.SubtractExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 524
                        if not self.precpred(self._ctx, 28):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 525
                        self.match(self.T__27)
                        self.state = 526 
                        self.singleExpression(29)
                        pass

                    elif la_ == 6:
                        localctx = ECMAScript1Parser.LeftShiftArithmeticExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 527
                        if not self.precpred(self._ctx, 27):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 528
                        self.match(self.T__43)
                        self.state = 529 
                        self.singleExpression(28)
                        pass

                    elif la_ == 7:
                        localctx = ECMAScript1Parser.RightShiftArithmeticExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 530
                        if not self.precpred(self._ctx, 26):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 531
                        self.match(self.T__14)
                        self.state = 532 
                        self.singleExpression(27)
                        pass

                    elif la_ == 8:
                        localctx = ECMAScript1Parser.RightShiftLogicalExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 533
                        if not self.precpred(self._ctx, 25):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 534
                        self.match(self.T__32)
                        self.state = 535 
                        self.singleExpression(26)
                        pass

                    elif la_ == 9:
                        localctx = ECMAScript1Parser.LessThanExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 536
                        if not self.precpred(self._ctx, 24):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 537
                        self.match(self.T__49)
                        self.state = 538 
                        self.singleExpression(25)
                        pass

                    elif la_ == 10:
                        localctx = ECMAScript1Parser.GreaterThanExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 539
                        if not self.precpred(self._ctx, 23):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 540
                        self.match(self.T__6)
                        self.state = 541 
                        self.singleExpression(24)
                        pass

                    elif la_ == 11:
                        localctx = ECMAScript1Parser.LessThanEqualsExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 542
                        if not self.precpred(self._ctx, 22):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 543
                        self.match(self.T__44)
                        self.state = 544 
                        self.singleExpression(23)
                        pass

                    elif la_ == 12:
                        localctx = ECMAScript1Parser.GreaterThanEqualsExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 545
                        if not self.precpred(self._ctx, 21):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 546
                        self.match(self.T__0)
                        self.state = 547 
                        self.singleExpression(22)
                        pass

                    elif la_ == 13:
                        localctx = ECMAScript1Parser.InstanceofExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 548
                        if not self.precpred(self._ctx, 20):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 549
                        self.match(self.Instanceof)
                        self.state = 550 
                        self.singleExpression(21)
                        pass

                    elif la_ == 14:
                        localctx = ECMAScript1Parser.InExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 551
                        if not self.precpred(self._ctx, 19):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 552
                        self.match(self.In)
                        self.state = 553 
                        self.singleExpression(20)
                        pass

                    elif la_ == 15:
                        localctx = ECMAScript1Parser.EqualsExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 554
                        if not self.precpred(self._ctx, 18):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 555
                        self.match(self.T__3)
                        self.state = 556 
                        self.singleExpression(19)
                        pass

                    elif la_ == 16:
                        localctx = ECMAScript1Parser.NotEqualsExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 557
                        if not self.precpred(self._ctx, 17):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 558
                        self.match(self.T__45)
                        self.state = 559 
                        self.singleExpression(18)
                        pass

                    elif la_ == 17:
                        localctx = ECMAScript1Parser.IdentityEqualsExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 560
                        if not self.precpred(self._ctx, 16):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 561
                        self.match(self.T__10)
                        self.state = 562 
                        self.singleExpression(17)
                        pass

                    elif la_ == 18:
                        localctx = ECMAScript1Parser.IdentityNotEqualsExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 563
                        if not self.precpred(self._ctx, 15):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 564
                        self.match(self.T__46)
                        self.state = 565 
                        self.singleExpression(16)
                        pass

                    elif la_ == 19:
                        localctx = ECMAScript1Parser.BitAndExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 566
                        if not self.precpred(self._ctx, 14):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 567
                        self.match(self.T__52)
                        self.state = 568 
                        self.singleExpression(15)
                        pass

                    elif la_ == 20:
                        localctx = ECMAScript1Parser.BitXOrExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 569
                        if not self.precpred(self._ctx, 13):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 570
                        self.match(self.T__13)
                        self.state = 571 
                        self.singleExpression(14)
                        pass

                    elif la_ == 21:
                        localctx = ECMAScript1Parser.BitOrExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 572
                        if not self.precpred(self._ctx, 12):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 573
                        self.match(self.T__35)
                        self.state = 574 
                        self.singleExpression(13)
                        pass

                    elif la_ == 22:
                        localctx = ECMAScript1Parser.AndExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 575
                        if not self.precpred(self._ctx, 11):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 576
                        self.match(self.T__8)
                        self.state = 577 
                        self.singleExpression(12)
                        pass

                    elif la_ == 23:
                        localctx = ECMAScript1Parser.OrExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 578
                        if not self.precpred(self._ctx, 10):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 579
                        self.match(self.T__7)
                        self.state = 580 
                        self.singleExpression(11)
                        pass

                    elif la_ == 24:
                        localctx = ECMAScript1Parser.TernaryExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 581
                        if not self.precpred(self._ctx, 9):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 582
                        self.match(self.T__23)
                        self.state = 583 
                        self.singleExpression(0)
                        self.state = 584
                        self.match(self.T__26)
                        self.state = 585 
                        self.singleExpression(10)
                        pass

                    elif la_ == 25:
                        localctx = ECMAScript1Parser.MemberIndexExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 587
                        if not self.precpred(self._ctx, 47):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 47)")
                        self.state = 588
                        self.match(self.T__51)
                        self.state = 589 
                        self.expressionSequence()
                        self.state = 590
                        self.match(self.T__31)
                        pass

                    elif la_ == 26:
                        localctx = ECMAScript1Parser.MemberDotExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 592
                        if not self.precpred(self._ctx, 46):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 46)")
                        self.state = 593
                        self.match(self.T__12)
                        self.state = 594 
                        self.identifierName()
                        pass

                    elif la_ == 27:
                        localctx = ECMAScript1Parser.ArgumentsExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 595
                        if not self.precpred(self._ctx, 45):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 45)")
                        self.state = 596 
                        self.arguments()
                        pass

                    elif la_ == 28:
                        localctx = ECMAScript1Parser.PostIncrementExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 597
                        if not self.precpred(self._ctx, 43):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 43)")
                        self.state = 598
                        self.match(self.T__15)
                        pass

                    elif la_ == 29:
                        localctx = ECMAScript1Parser.PostDecreaseExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 599
                        if not self.precpred(self._ctx, 42):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 42)")
                        self.state = 600
                        self.match(self.T__48)
                        pass

                    elif la_ == 30:
                        localctx = ECMAScript1Parser.AssignmentExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 601
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 602
                        self.match(self.T__38)
                        self.state = 603 
                        self.expressionSequence()
                        pass

                    elif la_ == 31:
                        localctx = ECMAScript1Parser.AssignmentOperatorExpressionContext(self, ECMAScript1Parser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 604
                        if not self.precpred(self._ctx, 7):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 605 
                        self.assignmentOperator()
                        self.state = 606 
                        self.expressionSequence()
                        pass

             
                self.state = 612
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.AssignmentOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_assignmentOperator

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitAssignmentOperator(self)




    def assignmentOperator(self):

        localctx = ECMAScript1Parser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__40) | (1 << self.T__36) | (1 << self.T__33) | (1 << self.T__30) | (1 << self.T__24) | (1 << self.T__22) | (1 << self.T__21) | (1 << self.T__18) | (1 << self.T__17) | (1 << self.T__5) | (1 << self.T__4))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.LiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RegularExpressionLiteral(self):
            return self.getToken(ECMAScript1Parser.RegularExpressionLiteral, 0)

        def nullLiteral(self):
            return self.getTypedRuleContext(ECMAScript1Parser.NullLiteralContext,0)


        def StringLiteral(self):
            return self.getToken(ECMAScript1Parser.StringLiteral, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(ECMAScript1Parser.BooleanLiteralContext,0)


        def numericLiteral(self):
            return self.getTypedRuleContext(ECMAScript1Parser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_literal

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ECMAScript1Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literal)
        try:
            self.state = 620
            token = self._input.LA(1)
            if token in [self.T__37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 615 
                self.nullLiteral()

            elif token in [self.T__47, self.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 616 
                self.booleanLiteral()

            elif token in [self.StringLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 617
                self.match(self.StringLiteral)

            elif token in [self.RegularExpressionLiteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 618
                self.match(self.RegularExpressionLiteral)

            elif token in [self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 5)
                self.state = 619 
                self.numericLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.NumericLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def HexIntegerLiteral(self):
            return self.getToken(ECMAScript1Parser.HexIntegerLiteral, 0)

        def OctalIntegerLiteral(self):
            return self.getToken(ECMAScript1Parser.OctalIntegerLiteral, 0)

        def DecimalLiteral(self):
            return self.getToken(ECMAScript1Parser.DecimalLiteral, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_numericLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitNumericLiteral(self)




    def numericLiteral(self):

        localctx = ECMAScript1Parser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.IdentifierNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(ECMAScript1Parser.Identifier, 0)

        def reservedWord(self):
            return self.getTypedRuleContext(ECMAScript1Parser.ReservedWordContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_identifierName

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterIdentifierName(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitIdentifierName(self)




    def identifierName(self):

        localctx = ECMAScript1Parser.IdentifierNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_identifierName)
        try:
            self.state = 626
            token = self._input.LA(1)
            if token in [self.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 624
                self.match(self.Identifier)

            elif token in [self.T__47, self.T__37, self.T__16, self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try, self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 625 
                self.reservedWord()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.ReservedWordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(ECMAScript1Parser.KeywordContext,0)


        def nullLiteral(self):
            return self.getTypedRuleContext(ECMAScript1Parser.NullLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(ECMAScript1Parser.BooleanLiteralContext,0)


        def futureReservedWord(self):
            return self.getTypedRuleContext(ECMAScript1Parser.FutureReservedWordContext,0)


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_reservedWord

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterReservedWord(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitReservedWord(self)




    def reservedWord(self):

        localctx = ECMAScript1Parser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_reservedWord)
        try:
            self.state = 632
            token = self._input.LA(1)
            if token in [self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try]:
                self.enterOuterAlt(localctx, 1)
                self.state = 628 
                self.keyword()

            elif token in [self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 629 
                self.futureReservedWord()

            elif token in [self.T__37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 630 
                self.nullLiteral()

            elif token in [self.T__47, self.T__16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 631 
                self.booleanLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.KeywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(ECMAScript1Parser.While, 0)

        def With(self):
            return self.getToken(ECMAScript1Parser.With, 0)

        def Case(self):
            return self.getToken(ECMAScript1Parser.Case, 0)

        def Do(self):
            return self.getToken(ECMAScript1Parser.Do, 0)

        def Else(self):
            return self.getToken(ECMAScript1Parser.Else, 0)

        def If(self):
            return self.getToken(ECMAScript1Parser.If, 0)

        def Switch(self):
            return self.getToken(ECMAScript1Parser.Switch, 0)

        def Delete(self):
            return self.getToken(ECMAScript1Parser.Delete, 0)

        def For(self):
            return self.getToken(ECMAScript1Parser.For, 0)

        def Try(self):
            return self.getToken(ECMAScript1Parser.Try, 0)

        def Default(self):
            return self.getToken(ECMAScript1Parser.Default, 0)

        def This(self):
            return self.getToken(ECMAScript1Parser.This, 0)

        def Return(self):
            return self.getToken(ECMAScript1Parser.Return, 0)

        def Void(self):
            return self.getToken(ECMAScript1Parser.Void, 0)

        def Catch(self):
            return self.getToken(ECMAScript1Parser.Catch, 0)

        def Function(self):
            return self.getToken(ECMAScript1Parser.Function, 0)

        def Var(self):
            return self.getToken(ECMAScript1Parser.Var, 0)

        def Typeof(self):
            return self.getToken(ECMAScript1Parser.Typeof, 0)

        def Throw(self):
            return self.getToken(ECMAScript1Parser.Throw, 0)

        def In(self):
            return self.getToken(ECMAScript1Parser.In, 0)

        def New(self):
            return self.getToken(ECMAScript1Parser.New, 0)

        def Instanceof(self):
            return self.getToken(ECMAScript1Parser.Instanceof, 0)

        def Continue(self):
            return self.getToken(ECMAScript1Parser.Continue, 0)

        def Break(self):
            return self.getToken(ECMAScript1Parser.Break, 0)

        def Finally(self):
            return self.getToken(ECMAScript1Parser.Finally, 0)

        def Debugger(self):
            return self.getToken(ECMAScript1Parser.Debugger, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_keyword

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterKeyword(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = ECMAScript1Parser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            _la = self._input.LA(1)
            if not(((((_la - 59)) & ~0x3f) == 0 and ((1 << (_la - 59)) & ((1 << (self.Break - 59)) | (1 << (self.Do - 59)) | (1 << (self.Instanceof - 59)) | (1 << (self.Typeof - 59)) | (1 << (self.Case - 59)) | (1 << (self.Else - 59)) | (1 << (self.New - 59)) | (1 << (self.Var - 59)) | (1 << (self.Catch - 59)) | (1 << (self.Finally - 59)) | (1 << (self.Return - 59)) | (1 << (self.Void - 59)) | (1 << (self.Continue - 59)) | (1 << (self.For - 59)) | (1 << (self.Switch - 59)) | (1 << (self.While - 59)) | (1 << (self.Debugger - 59)) | (1 << (self.Function - 59)) | (1 << (self.This - 59)) | (1 << (self.With - 59)) | (1 << (self.Default - 59)) | (1 << (self.If - 59)) | (1 << (self.Throw - 59)) | (1 << (self.Delete - 59)) | (1 << (self.In - 59)) | (1 << (self.Try - 59)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FutureReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.FutureReservedWordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Enum(self):
            return self.getToken(ECMAScript1Parser.Enum, 0)

        def Extends(self):
            return self.getToken(ECMAScript1Parser.Extends, 0)

        def Implements(self):
            return self.getToken(ECMAScript1Parser.Implements, 0)

        def Let(self):
            return self.getToken(ECMAScript1Parser.Let, 0)

        def Protected(self):
            return self.getToken(ECMAScript1Parser.Protected, 0)

        def Interface(self):
            return self.getToken(ECMAScript1Parser.Interface, 0)

        def Export(self):
            return self.getToken(ECMAScript1Parser.Export, 0)

        def Import(self):
            return self.getToken(ECMAScript1Parser.Import, 0)

        def Class(self):
            return self.getToken(ECMAScript1Parser.Class, 0)

        def Package(self):
            return self.getToken(ECMAScript1Parser.Package, 0)

        def Public(self):
            return self.getToken(ECMAScript1Parser.Public, 0)

        def Static(self):
            return self.getToken(ECMAScript1Parser.Static, 0)

        def Super(self):
            return self.getToken(ECMAScript1Parser.Super, 0)

        def Private(self):
            return self.getToken(ECMAScript1Parser.Private, 0)

        def Yield(self):
            return self.getToken(ECMAScript1Parser.Yield, 0)

        def Const(self):
            return self.getToken(ECMAScript1Parser.Const, 0)

        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_futureReservedWord

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterFutureReservedWord(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitFutureReservedWord(self)




    def futureReservedWord(self):

        localctx = ECMAScript1Parser.FutureReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_futureReservedWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            _la = self._input.LA(1)
            if not(((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (self.Class - 85)) | (1 << (self.Enum - 85)) | (1 << (self.Extends - 85)) | (1 << (self.Super - 85)) | (1 << (self.Const - 85)) | (1 << (self.Export - 85)) | (1 << (self.Import - 85)) | (1 << (self.Implements - 85)) | (1 << (self.Let - 85)) | (1 << (self.Private - 85)) | (1 << (self.Public - 85)) | (1 << (self.Interface - 85)) | (1 << (self.Package - 85)) | (1 << (self.Protected - 85)) | (1 << (self.Static - 85)) | (1 << (self.Yield - 85)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.EosContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_eos

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterEos(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitEos(self)




    def eos(self):

        localctx = ECMAScript1Parser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_eos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(self.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NullLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.NullLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_nullLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitNullLiteral(self)




    def nullLiteral(self):

        localctx = ECMAScript1Parser.NullLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_nullLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.match(self.T__37)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScript1Parser.BooleanLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScript1Parser.RULE_booleanLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScript1Listener ):
                listener.exitBooleanLiteral(self)




    def booleanLiteral(self):

        localctx = ECMAScript1Parser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            _la = self._input.LA(1)
            if not(_la==ECMAScript1Parser.T__47 or _la==ECMAScript1Parser.T__16):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[44] = self.singleExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def singleExpression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 26)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 25)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 46)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 47)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 43)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 45)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 42)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 7)
         



