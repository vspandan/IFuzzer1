# Generated from java-escape by ANTLR 4.4
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ECMAScriptListener import ECMAScriptListener
else:
    from ECMAScriptListener import ECMAScriptListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"l\u028b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\3\2\3\2\5\2u\n\2\3\3\6\3x\n\3\r\3\16\3y\3\4\3\4")
        buf.write(u"\5\4~\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\5\5\u008f\n\5\3\6\3\6\5\6\u0093\n\6")
        buf.write(u"\3\6\3\6\3\7\6\7\u0098\n\7\r\7\16\7\u0099\3\b\3\b\3\b")
        buf.write(u"\3\b\3\t\3\t\3\t\7\t\u00a3\n\t\f\t\16\t\u00a6\13\t\3")
        buf.write(u"\n\3\n\5\n\u00aa\n\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write(u"\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ba\n\16\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\5\17\u00cd\n\17\3\17\3\17")
        buf.write(u"\5\17\u00d1\n\17\3\17\3\17\5\17\u00d5\n\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00df\n\17\3\17\3")
        buf.write(u"\17\5\17\u00e3\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\5\17\u00f9\n\17\3\20\3\20\5\20\u00fd\n")
        buf.write(u"\20\3\20\3\20\3\21\3\21\5\21\u0103\n\21\3\21\3\21\3\22")
        buf.write(u"\3\22\5\22\u0109\n\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\5\25")
        buf.write(u"\u011b\n\25\3\25\3\25\5\25\u011f\n\25\5\25\u0121\n\25")
        buf.write(u"\3\25\3\25\3\26\6\26\u0126\n\26\r\26\16\26\u0127\3\27")
        buf.write(u"\3\27\3\27\3\27\5\27\u012e\n\27\3\30\3\30\3\30\5\30\u0133")
        buf.write(u"\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\5\33\u014a\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\5\37")
        buf.write(u"\u015c\n\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \7 \u0166")
        buf.write(u"\n \f \16 \u0169\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write(u"!\3!\3!\3!\3!\5!\u017a\n!\3\"\5\"\u017d\n\"\3#\3#\5#")
        buf.write(u"\u0181\n#\3#\5#\u0184\n#\3#\5#\u0187\n#\3#\3#\3$\5$\u018c")
        buf.write(u"\n$\3$\3$\3$\5$\u0191\n$\3$\7$\u0194\n$\f$\16$\u0197")
        buf.write(u"\13$\3%\6%\u019a\n%\r%\16%\u019b\3&\3&\5&\u01a0\n&\3")
        buf.write(u"&\5&\u01a3\n&\3&\3&\3\'\3\'\3\'\7\'\u01aa\n\'\f\'\16")
        buf.write(u"\'\u01ad\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write(u"\3(\3(\3(\3(\3(\3(\5(\u01c2\n(\3)\3)\3)\5)\u01c7\n)\3")
        buf.write(u"*\3*\3+\3+\5+\u01cd\n+\3+\3+\3,\3,\3,\7,\u01d4\n,\f,")
        buf.write(u"\16,\u01d7\13,\3-\3-\3-\7-\u01dc\n-\f-\16-\u01df\13-")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\5.\u01f8\n.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\5.\u0203\n.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\7.\u0265\n.")
        buf.write(u"\f.\16.\u0268\13.\3/\3/\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write(u"\u0271\n\60\3\61\3\61\3\62\3\62\5\62\u0277\n\62\3\63")
        buf.write(u"\3\63\3\63\3\63\5\63\u027d\n\63\3\64\3\64\3\65\3\65\3")
        buf.write(u"\66\3\66\3\67\3\67\38\38\39\39\39\2\3Z:\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BD")
        buf.write(u"FHJLNPRTVXZ\\^`bdfhjlnp\2\7\n\2\17\17\23\23\26\26\31")
        buf.write(u"\31\37\37!\"%&\62\63\3\2:<\3\2=V\3\2Wf\4\2\b\b\'\'\u02ca")
        buf.write(u"\2t\3\2\2\2\4w\3\2\2\2\6}\3\2\2\2\b\u008e\3\2\2\2\n\u0090")
        buf.write(u"\3\2\2\2\f\u0097\3\2\2\2\16\u009b\3\2\2\2\20\u009f\3")
        buf.write(u"\2\2\2\22\u00a7\3\2\2\2\24\u00ab\3\2\2\2\26\u00ae\3\2")
        buf.write(u"\2\2\30\u00b0\3\2\2\2\32\u00b2\3\2\2\2\34\u00f8\3\2\2")
        buf.write(u"\2\36\u00fa\3\2\2\2 \u0100\3\2\2\2\"\u0106\3\2\2\2$\u010c")
        buf.write(u"\3\2\2\2&\u0112\3\2\2\2(\u0118\3\2\2\2*\u0125\3\2\2\2")
        buf.write(u",\u0129\3\2\2\2.\u012f\3\2\2\2\60\u0134\3\2\2\2\62\u0138")
        buf.write(u"\3\2\2\2\64\u0149\3\2\2\2\66\u014b\3\2\2\28\u0151\3\2")
        buf.write(u"\2\2:\u0154\3\2\2\2<\u0157\3\2\2\2>\u0162\3\2\2\2@\u0179")
        buf.write(u"\3\2\2\2B\u017c\3\2\2\2D\u017e\3\2\2\2F\u018b\3\2\2\2")
        buf.write(u"H\u0199\3\2\2\2J\u019d\3\2\2\2L\u01a6\3\2\2\2N\u01c1")
        buf.write(u"\3\2\2\2P\u01c6\3\2\2\2R\u01c8\3\2\2\2T\u01ca\3\2\2\2")
        buf.write(u"V\u01d0\3\2\2\2X\u01d8\3\2\2\2Z\u0202\3\2\2\2\\\u0269")
        buf.write(u"\3\2\2\2^\u0270\3\2\2\2`\u0272\3\2\2\2b\u0276\3\2\2\2")
        buf.write(u"d\u027c\3\2\2\2f\u027e\3\2\2\2h\u0280\3\2\2\2j\u0282")
        buf.write(u"\3\2\2\2l\u0284\3\2\2\2n\u0286\3\2\2\2p\u0288\3\2\2\2")
        buf.write(u"ru\5\4\3\2su\3\2\2\2tr\3\2\2\2ts\3\2\2\2u\3\3\2\2\2v")
        buf.write(u"x\5\6\4\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\5")
        buf.write(u"\3\2\2\2{~\5\b\5\2|~\5<\37\2}{\3\2\2\2}|\3\2\2\2~\7\3")
        buf.write(u"\2\2\2\177\u008f\5\n\6\2\u0080\u008f\5\16\b\2\u0081\u008f")
        buf.write(u"\5\26\f\2\u0082\u008f\5\30\r\2\u0083\u008f\5\32\16\2")
        buf.write(u"\u0084\u008f\5\34\17\2\u0085\u008f\5\36\20\2\u0086\u008f")
        buf.write(u"\5 \21\2\u0087\u008f\5\"\22\2\u0088\u008f\5$\23\2\u0089")
        buf.write(u"\u008f\5\60\31\2\u008a\u008f\5&\24\2\u008b\u008f\5\62")
        buf.write(u"\32\2\u008c\u008f\5\64\33\2\u008d\u008f\5:\36\2\u008e")
        buf.write(u"\177\3\2\2\2\u008e\u0080\3\2\2\2\u008e\u0081\3\2\2\2")
        buf.write(u"\u008e\u0082\3\2\2\2\u008e\u0083\3\2\2\2\u008e\u0084")
        buf.write(u"\3\2\2\2\u008e\u0085\3\2\2\2\u008e\u0086\3\2\2\2\u008e")
        buf.write(u"\u0087\3\2\2\2\u008e\u0088\3\2\2\2\u008e\u0089\3\2\2")
        buf.write(u"\2\u008e\u008a\3\2\2\2\u008e\u008b\3\2\2\2\u008e\u008c")
        buf.write(u"\3\2\2\2\u008e\u008d\3\2\2\2\u008f\t\3\2\2\2\u0090\u0092")
        buf.write(u"\7$\2\2\u0091\u0093\5\f\7\2\u0092\u0091\3\2\2\2\u0092")
        buf.write(u"\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\7\r\2")
        buf.write(u"\2\u0095\13\3\2\2\2\u0096\u0098\5\b\5\2\u0097\u0096\3")
        buf.write(u"\2\2\2\u0098\u0099\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write(u"\u009a\3\2\2\2\u009a\r\3\2\2\2\u009b\u009c\7D\2\2\u009c")
        buf.write(u"\u009d\5\20\t\2\u009d\u009e\5j\66\2\u009e\17\3\2\2\2")
        buf.write(u"\u009f\u00a4\5\22\n\2\u00a0\u00a1\7\33\2\2\u00a1\u00a3")
        buf.write(u"\5\22\n\2\u00a2\u00a0\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4")
        buf.write(u"\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\21\3\2\2\2\u00a6")
        buf.write(u"\u00a4\3\2\2\2\u00a7\u00a9\5p9\2\u00a8\u00aa\5\24\13")
        buf.write(u"\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\23\3")
        buf.write(u"\2\2\2\u00ab\u00ac\7\21\2\2\u00ac\u00ad\5Z.\2\u00ad\25")
        buf.write(u"\3\2\2\2\u00ae\u00af\7.\2\2\u00af\27\3\2\2\2\u00b0\u00b1")
        buf.write(u"\5X-\2\u00b1\31\3\2\2\2\u00b2\u00b3\7R\2\2\u00b3\u00b4")
        buf.write(u"\7\36\2\2\u00b4\u00b5\5X-\2\u00b5\u00b6\7\20\2\2\u00b6")
        buf.write(u"\u00b9\5\b\5\2\u00b7\u00b8\7B\2\2\u00b8\u00ba\5\b\5\2")
        buf.write(u"\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\33\3\2")
        buf.write(u"\2\2\u00bb\u00bc\7>\2\2\u00bc\u00bd\5\b\5\2\u00bd\u00be")
        buf.write(u"\7L\2\2\u00be\u00bf\7\36\2\2\u00bf\u00c0\5X-\2\u00c0")
        buf.write(u"\u00c1\7\20\2\2\u00c1\u00c2\5j\66\2\u00c2\u00f9\3\2\2")
        buf.write(u"\2\u00c3\u00c4\7L\2\2\u00c4\u00c5\7\36\2\2\u00c5\u00c6")
        buf.write(u"\5X-\2\u00c6\u00c7\7\20\2\2\u00c7\u00c8\5\b\5\2\u00c8")
        buf.write(u"\u00f9\3\2\2\2\u00c9\u00ca\7J\2\2\u00ca\u00cc\7\36\2")
        buf.write(u"\2\u00cb\u00cd\5X-\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd")
        buf.write(u"\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\7.\2\2\u00cf")
        buf.write(u"\u00d1\5X-\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write(u"\u00d1\u00d2\3\2\2\2\u00d2\u00d4\7.\2\2\u00d3\u00d5\5")
        buf.write(u"X-\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6")
        buf.write(u"\3\2\2\2\u00d6\u00d7\7\20\2\2\u00d7\u00f9\5\b\5\2\u00d8")
        buf.write(u"\u00d9\7J\2\2\u00d9\u00da\7\36\2\2\u00da\u00db\7D\2\2")
        buf.write(u"\u00db\u00dc\5\20\t\2\u00dc\u00de\7.\2\2\u00dd\u00df")
        buf.write(u"\5X-\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write(u"\u00e0\3\2\2\2\u00e0\u00e2\7.\2\2\u00e1\u00e3\5X-\2\u00e2")
        buf.write(u"\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3\2\2")
        buf.write(u"\2\u00e4\u00e5\7\20\2\2\u00e5\u00e6\5\b\5\2\u00e6\u00f9")
        buf.write(u"\3\2\2\2\u00e7\u00e8\7J\2\2\u00e8\u00e9\7\36\2\2\u00e9")
        buf.write(u"\u00ea\5Z.\2\u00ea\u00eb\7U\2\2\u00eb\u00ec\5X-\2\u00ec")
        buf.write(u"\u00ed\7\20\2\2\u00ed\u00ee\5\b\5\2\u00ee\u00f9\3\2\2")
        buf.write(u"\2\u00ef\u00f0\7J\2\2\u00f0\u00f1\7\36\2\2\u00f1\u00f2")
        buf.write(u"\7D\2\2\u00f2\u00f3\5\22\n\2\u00f3\u00f4\7U\2\2\u00f4")
        buf.write(u"\u00f5\5X-\2\u00f5\u00f6\7\20\2\2\u00f6\u00f7\5\b\5\2")
        buf.write(u"\u00f7\u00f9\3\2\2\2\u00f8\u00bb\3\2\2\2\u00f8\u00c3")
        buf.write(u"\3\2\2\2\u00f8\u00c9\3\2\2\2\u00f8\u00d8\3\2\2\2\u00f8")
        buf.write(u"\u00e7\3\2\2\2\u00f8\u00ef\3\2\2\2\u00f9\35\3\2\2\2\u00fa")
        buf.write(u"\u00fc\7I\2\2\u00fb\u00fd\5p9\2\u00fc\u00fb\3\2\2\2\u00fc")
        buf.write(u"\u00fd\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\5j\66")
        buf.write(u"\2\u00ff\37\3\2\2\2\u0100\u0102\7=\2\2\u0101\u0103\5")
        buf.write(u"p9\2\u0102\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104")
        buf.write(u"\3\2\2\2\u0104\u0105\5j\66\2\u0105!\3\2\2\2\u0106\u0108")
        buf.write(u"\7G\2\2\u0107\u0109\5X-\2\u0108\u0107\3\2\2\2\u0108\u0109")
        buf.write(u"\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\5j\66\2\u010b")
        buf.write(u"#\3\2\2\2\u010c\u010d\7P\2\2\u010d\u010e\7\36\2\2\u010e")
        buf.write(u"\u010f\5X-\2\u010f\u0110\7\20\2\2\u0110\u0111\5\b\5\2")
        buf.write(u"\u0111%\3\2\2\2\u0112\u0113\7K\2\2\u0113\u0114\7\36\2")
        buf.write(u"\2\u0114\u0115\5X-\2\u0115\u0116\7\20\2\2\u0116\u0117")
        buf.write(u"\5(\25\2\u0117\'\3\2\2\2\u0118\u011a\7$\2\2\u0119\u011b")
        buf.write(u"\5*\26\2\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write(u"\u0120\3\2\2\2\u011c\u011e\5.\30\2\u011d\u011f\5*\26")
        buf.write(u"\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121")
        buf.write(u"\3\2\2\2\u0120\u011c\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write(u"\u0122\3\2\2\2\u0122\u0123\7\r\2\2\u0123)\3\2\2\2\u0124")
        buf.write(u"\u0126\5,\27\2\u0125\u0124\3\2\2\2\u0126\u0127\3\2\2")
        buf.write(u"\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128+\3\2")
        buf.write(u"\2\2\u0129\u012a\7A\2\2\u012a\u012b\5X-\2\u012b\u012d")
        buf.write(u"\7\35\2\2\u012c\u012e\5\f\7\2\u012d\u012c\3\2\2\2\u012d")
        buf.write(u"\u012e\3\2\2\2\u012e-\3\2\2\2\u012f\u0130\7Q\2\2\u0130")
        buf.write(u"\u0132\7\35\2\2\u0131\u0133\5\f\7\2\u0132\u0131\3\2\2")
        buf.write(u"\2\u0132\u0133\3\2\2\2\u0133/\3\2\2\2\u0134\u0135\5p")
        buf.write(u"9\2\u0135\u0136\7\35\2\2\u0136\u0137\5\b\5\2\u0137\61")
        buf.write(u"\3\2\2\2\u0138\u0139\7S\2\2\u0139\u013a\5X-\2\u013a\u013b")
        buf.write(u"\5j\66\2\u013b\63\3\2\2\2\u013c\u013d\7V\2\2\u013d\u013e")
        buf.write(u"\5\n\6\2\u013e\u013f\5\66\34\2\u013f\u014a\3\2\2\2\u0140")
        buf.write(u"\u0141\7V\2\2\u0141\u0142\5\n\6\2\u0142\u0143\58\35\2")
        buf.write(u"\u0143\u014a\3\2\2\2\u0144\u0145\7V\2\2\u0145\u0146\5")
        buf.write(u"\n\6\2\u0146\u0147\5\66\34\2\u0147\u0148\58\35\2\u0148")
        buf.write(u"\u014a\3\2\2\2\u0149\u013c\3\2\2\2\u0149\u0140\3\2\2")
        buf.write(u"\2\u0149\u0144\3\2\2\2\u014a\65\3\2\2\2\u014b\u014c\7")
        buf.write(u"E\2\2\u014c\u014d\7\36\2\2\u014d\u014e\5p9\2\u014e\u014f")
        buf.write(u"\7\20\2\2\u014f\u0150\5\n\6\2\u0150\67\3\2\2\2\u0151")
        buf.write(u"\u0152\7F\2\2\u0152\u0153\5\n\6\2\u01539\3\2\2\2\u0154")
        buf.write(u"\u0155\7M\2\2\u0155\u0156\5j\66\2\u0156;\3\2\2\2\u0157")
        buf.write(u"\u0158\7N\2\2\u0158\u0159\5p9\2\u0159\u015b\7\36\2\2")
        buf.write(u"\u015a\u015c\5> \2\u015b\u015a\3\2\2\2\u015b\u015c\3")
        buf.write(u"\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\7\20\2\2\u015e")
        buf.write(u"\u015f\7$\2\2\u015f\u0160\5B\"\2\u0160\u0161\7\r\2\2")
        buf.write(u"\u0161=\3\2\2\2\u0162\u0167\5p9\2\u0163\u0164\7\33\2")
        buf.write(u"\2\u0164\u0166\5p9\2\u0165\u0163\3\2\2\2\u0166\u0169")
        buf.write(u"\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write(u"?\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b\7N\2\2\u016b")
        buf.write(u"\u016c\7\36\2\2\u016c\u016d\5> \2\u016d\u016e\7\20\2")
        buf.write(u"\2\u016e\u016f\7$\2\2\u016f\u0170\5B\"\2\u0170\u0171")
        buf.write(u"\7\r\2\2\u0171\u017a\3\2\2\2\u0172\u0173\7N\2\2\u0173")
        buf.write(u"\u0174\7\36\2\2\u0174\u0175\7\20\2\2\u0175\u0176\7$\2")
        buf.write(u"\2\u0176\u0177\5B\"\2\u0177\u0178\7\r\2\2\u0178\u017a")
        buf.write(u"\3\2\2\2\u0179\u016a\3\2\2\2\u0179\u0172\3\2\2\2\u017a")
        buf.write(u"A\3\2\2\2\u017b\u017d\5\4\3\2\u017c\u017b\3\2\2\2\u017c")
        buf.write(u"\u017d\3\2\2\2\u017dC\3\2\2\2\u017e\u0180\7\4\2\2\u017f")
        buf.write(u"\u0181\5F$\2\u0180\u017f\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write(u"\u0181\u0183\3\2\2\2\u0182\u0184\7\33\2\2\u0183\u0182")
        buf.write(u"\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\3\2\2\2\u0185")
        buf.write(u"\u0187\5H%\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write(u"\u0187\u0188\3\2\2\2\u0188\u0189\7\30\2\2\u0189E\3\2")
        buf.write(u"\2\2\u018a\u018c\5H%\2\u018b\u018a\3\2\2\2\u018b\u018c")
        buf.write(u"\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u0195\5Z.\2\u018e")
        buf.write(u"\u0190\7\33\2\2\u018f\u0191\5H%\2\u0190\u018f\3\2\2\2")
        buf.write(u"\u0190\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0194")
        buf.write(u"\5Z.\2\u0193\u018e\3\2\2\2\u0194\u0197\3\2\2\2\u0195")
        buf.write(u"\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196G\3\2\2\2\u0197")
        buf.write(u"\u0195\3\2\2\2\u0198\u019a\7\33\2\2\u0199\u0198\3\2\2")
        buf.write(u"\2\u019a\u019b\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c")
        buf.write(u"\3\2\2\2\u019cI\3\2\2\2\u019d\u019f\7$\2\2\u019e\u01a0")
        buf.write(u"\5L\'\2\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write(u"\u01a2\3\2\2\2\u01a1\u01a3\7\33\2\2\u01a2\u01a1\3\2\2")
        buf.write(u"\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5")
        buf.write(u"\7\r\2\2\u01a5K\3\2\2\2\u01a6\u01ab\5N(\2\u01a7\u01a8")
        buf.write(u"\7\33\2\2\u01a8\u01aa\5N(\2\u01a9\u01a7\3\2\2\2\u01aa")
        buf.write(u"\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2")
        buf.write(u"\2\u01acM\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01af\5P")
        buf.write(u")\2\u01af\u01b0\7\35\2\2\u01b0\u01b1\5Z.\2\u01b1\u01c2")
        buf.write(u"\3\2\2\2\u01b2\u01b3\7\32\2\2\u01b3\u01b4\7\36\2\2\u01b4")
        buf.write(u"\u01b5\7\20\2\2\u01b5\u01b6\7$\2\2\u01b6\u01b7\5B\"\2")
        buf.write(u"\u01b7\u01b8\7\r\2\2\u01b8\u01c2\3\2\2\2\u01b9\u01ba")
        buf.write(u"\7#\2\2\u01ba\u01bb\7\36\2\2\u01bb\u01bc\5R*\2\u01bc")
        buf.write(u"\u01bd\7\20\2\2\u01bd\u01be\7$\2\2\u01be\u01bf\5B\"\2")
        buf.write(u"\u01bf\u01c0\7\r\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01ae")
        buf.write(u"\3\2\2\2\u01c1\u01b2\3\2\2\2\u01c1\u01b9\3\2\2\2\u01c2")
        buf.write(u"O\3\2\2\2\u01c3\u01c7\5b\62\2\u01c4\u01c7\7h\2\2\u01c5")
        buf.write(u"\u01c7\5`\61\2\u01c6\u01c3\3\2\2\2\u01c6\u01c4\3\2\2")
        buf.write(u"\2\u01c6\u01c5\3\2\2\2\u01c7Q\3\2\2\2\u01c8\u01c9\5p")
        buf.write(u"9\2\u01c9S\3\2\2\2\u01ca\u01cc\7\36\2\2\u01cb\u01cd\5")
        buf.write(u"V,\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce")
        buf.write(u"\3\2\2\2\u01ce\u01cf\7\20\2\2\u01cfU\3\2\2\2\u01d0\u01d5")
        buf.write(u"\5Z.\2\u01d1\u01d2\7\33\2\2\u01d2\u01d4\5Z.\2\u01d3\u01d1")
        buf.write(u"\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5")
        buf.write(u"\u01d6\3\2\2\2\u01d6W\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8")
        buf.write(u"\u01dd\5Z.\2\u01d9\u01da\7\33\2\2\u01da\u01dc\5Z.\2\u01db")
        buf.write(u"\u01d9\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2")
        buf.write(u"\2\u01dd\u01de\3\2\2\2\u01deY\3\2\2\2\u01df\u01dd\3\2")
        buf.write(u"\2\2\u01e0\u01e1\b.\1\2\u01e1\u01e2\7T\2\2\u01e2\u0203")
        buf.write(u"\5Z.+\u01e3\u01e4\7H\2\2\u01e4\u0203\5Z.*\u01e5\u01e6")
        buf.write(u"\7@\2\2\u01e6\u0203\5Z.)\u01e7\u01e8\7(\2\2\u01e8\u0203")
        buf.write(u"\5Z.(\u01e9\u01ea\7\7\2\2\u01ea\u0203\5Z.\'\u01eb\u01ec")
        buf.write(u"\7,\2\2\u01ec\u0203\5Z.&\u01ed\u01ee\7\34\2\2\u01ee\u0203")
        buf.write(u"\5Z.%\u01ef\u01f0\7\66\2\2\u01f0\u0203\5Z.$\u01f1\u01f2")
        buf.write(u"\7\25\2\2\u01f2\u0203\5Z.#\u01f3\u0203\5@!\2\u01f4\u01f5")
        buf.write(u"\7C\2\2\u01f5\u01f7\5Z.\2\u01f6\u01f8\5T+\2\u01f7\u01f6")
        buf.write(u"\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u0203\3\2\2\2\u01f9")
        buf.write(u"\u0203\7O\2\2\u01fa\u0203\5p9\2\u01fb\u0203\5^\60\2\u01fc")
        buf.write(u"\u0203\5D#\2\u01fd\u0203\5J&\2\u01fe\u01ff\7\36\2\2\u01ff")
        buf.write(u"\u0200\5X-\2\u0200\u0201\7\20\2\2\u0201\u0203\3\2\2\2")
        buf.write(u"\u0202\u01e0\3\2\2\2\u0202\u01e3\3\2\2\2\u0202\u01e5")
        buf.write(u"\3\2\2\2\u0202\u01e7\3\2\2\2\u0202\u01e9\3\2\2\2\u0202")
        buf.write(u"\u01eb\3\2\2\2\u0202\u01ed\3\2\2\2\u0202\u01ef\3\2\2")
        buf.write(u"\2\u0202\u01f1\3\2\2\2\u0202\u01f3\3\2\2\2\u0202\u01f4")
        buf.write(u"\3\2\2\2\u0202\u01f9\3\2\2\2\u0202\u01fa\3\2\2\2\u0202")
        buf.write(u"\u01fb\3\2\2\2\u0202\u01fc\3\2\2\2\u0202\u01fd\3\2\2")
        buf.write(u"\2\u0202\u01fe\3\2\2\2\u0203\u0266\3\2\2\2\u0204\u0205")
        buf.write(u"\f\"\2\2\u0205\u0206\7\5\2\2\u0206\u0265\5Z.#\u0207\u0208")
        buf.write(u"\f!\2\2\u0208\u0209\7\65\2\2\u0209\u0265\5Z.\"\u020a")
        buf.write(u"\u020b\f \2\2\u020b\u020c\7\16\2\2\u020c\u0265\5Z.!\u020d")
        buf.write(u"\u020e\f\37\2\2\u020e\u020f\7,\2\2\u020f\u0265\5Z. \u0210")
        buf.write(u"\u0211\f\36\2\2\u0211\u0212\7\34\2\2\u0212\u0265\5Z.")
        buf.write(u"\37\u0213\u0214\f\35\2\2\u0214\u0215\7\f\2\2\u0215\u0265")
        buf.write(u"\5Z.\36\u0216\u0217\f\34\2\2\u0217\u0218\7)\2\2\u0218")
        buf.write(u"\u0265\5Z.\35\u0219\u021a\f\33\2\2\u021a\u021b\7\27\2")
        buf.write(u"\2\u021b\u0265\5Z.\34\u021c\u021d\f\32\2\2\u021d\u021e")
        buf.write(u"\7\6\2\2\u021e\u0265\5Z.\33\u021f\u0220\f\31\2\2\u0220")
        buf.write(u"\u0221\7\61\2\2\u0221\u0265\5Z.\32\u0222\u0223\f\30\2")
        buf.write(u"\2\u0223\u0224\7\13\2\2\u0224\u0265\5Z.\31\u0225\u0226")
        buf.write(u"\f\27\2\2\u0226\u0227\7\67\2\2\u0227\u0265\5Z.\30\u0228")
        buf.write(u"\u0229\f\26\2\2\u0229\u022a\7?\2\2\u022a\u0265\5Z.\27")
        buf.write(u"\u022b\u022c\f\25\2\2\u022c\u022d\7U\2\2\u022d\u0265")
        buf.write(u"\5Z.\26\u022e\u022f\f\24\2\2\u022f\u0230\7\64\2\2\u0230")
        buf.write(u"\u0265\5Z.\25\u0231\u0232\f\23\2\2\u0232\u0233\7\n\2")
        buf.write(u"\2\u0233\u0265\5Z.\24\u0234\u0235\f\22\2\2\u0235\u0236")
        buf.write(u"\7-\2\2\u0236\u0265\5Z.\23\u0237\u0238\f\21\2\2\u0238")
        buf.write(u"\u0239\7\t\2\2\u0239\u0265\5Z.\22\u023a\u023b\f\20\2")
        buf.write(u"\2\u023b\u023c\7\3\2\2\u023c\u0265\5Z.\21\u023d\u023e")
        buf.write(u"\f\17\2\2\u023e\u023f\7*\2\2\u023f\u0265\5Z.\20\u0240")
        buf.write(u"\u0241\f\16\2\2\u0241\u0242\7\24\2\2\u0242\u0265\5Z.")
        buf.write(u"\17\u0243\u0244\f\r\2\2\u0244\u0245\7/\2\2\u0245\u0265")
        buf.write(u"\5Z.\16\u0246\u0247\f\f\2\2\u0247\u0248\7\60\2\2\u0248")
        buf.write(u"\u0265\5Z.\r\u0249\u024a\f\13\2\2\u024a\u024b\7 \2\2")
        buf.write(u"\u024b\u024c\5Z.\2\u024c\u024d\7\35\2\2\u024d\u024e\5")
        buf.write(u"Z.\f\u024e\u0265\3\2\2\2\u024f\u0250\f\61\2\2\u0250\u0251")
        buf.write(u"\7\4\2\2\u0251\u0252\5X-\2\u0252\u0253\7\30\2\2\u0253")
        buf.write(u"\u0265\3\2\2\2\u0254\u0255\f\60\2\2\u0255\u0256\7+\2")
        buf.write(u"\2\u0256\u0265\5b\62\2\u0257\u0258\f/\2\2\u0258\u0265")
        buf.write(u"\5T+\2\u0259\u025a\f-\2\2\u025a\u0265\7(\2\2\u025b\u025c")
        buf.write(u"\f,\2\2\u025c\u0265\7\7\2\2\u025d\u025e\f\n\2\2\u025e")
        buf.write(u"\u025f\7\21\2\2\u025f\u0265\5X-\2\u0260\u0261\f\t\2\2")
        buf.write(u"\u0261\u0262\5\\/\2\u0262\u0263\5X-\2\u0263\u0265\3\2")
        buf.write(u"\2\2\u0264\u0204\3\2\2\2\u0264\u0207\3\2\2\2\u0264\u020a")
        buf.write(u"\3\2\2\2\u0264\u020d\3\2\2\2\u0264\u0210\3\2\2\2\u0264")
        buf.write(u"\u0213\3\2\2\2\u0264\u0216\3\2\2\2\u0264\u0219\3\2\2")
        buf.write(u"\2\u0264\u021c\3\2\2\2\u0264\u021f\3\2\2\2\u0264\u0222")
        buf.write(u"\3\2\2\2\u0264\u0225\3\2\2\2\u0264\u0228\3\2\2\2\u0264")
        buf.write(u"\u022b\3\2\2\2\u0264\u022e\3\2\2\2\u0264\u0231\3\2\2")
        buf.write(u"\2\u0264\u0234\3\2\2\2\u0264\u0237\3\2\2\2\u0264\u023a")
        buf.write(u"\3\2\2\2\u0264\u023d\3\2\2\2\u0264\u0240\3\2\2\2\u0264")
        buf.write(u"\u0243\3\2\2\2\u0264\u0246\3\2\2\2\u0264\u0249\3\2\2")
        buf.write(u"\2\u0264\u024f\3\2\2\2\u0264\u0254\3\2\2\2\u0264\u0257")
        buf.write(u"\3\2\2\2\u0264\u0259\3\2\2\2\u0264\u025b\3\2\2\2\u0264")
        buf.write(u"\u025d\3\2\2\2\u0264\u0260\3\2\2\2\u0265\u0268\3\2\2")
        buf.write(u"\2\u0266\u0264\3\2\2\2\u0266\u0267\3\2\2\2\u0267[\3\2")
        buf.write(u"\2\2\u0268\u0266\3\2\2\2\u0269\u026a\t\2\2\2\u026a]\3")
        buf.write(u"\2\2\2\u026b\u0271\5l\67\2\u026c\u0271\5n8\2\u026d\u0271")
        buf.write(u"\7h\2\2\u026e\u0271\78\2\2\u026f\u0271\5`\61\2\u0270")
        buf.write(u"\u026b\3\2\2\2\u0270\u026c\3\2\2\2\u0270\u026d\3\2\2")
        buf.write(u"\2\u0270\u026e\3\2\2\2\u0270\u026f\3\2\2\2\u0271_\3\2")
        buf.write(u"\2\2\u0272\u0273\t\3\2\2\u0273a\3\2\2\2\u0274\u0277\5")
        buf.write(u"p9\2\u0275\u0277\5d\63\2\u0276\u0274\3\2\2\2\u0276\u0275")
        buf.write(u"\3\2\2\2\u0277c\3\2\2\2\u0278\u027d\5f\64\2\u0279\u027d")
        buf.write(u"\5h\65\2\u027a\u027d\5l\67\2\u027b\u027d\5n8\2\u027c")
        buf.write(u"\u0278\3\2\2\2\u027c\u0279\3\2\2\2\u027c\u027a\3\2\2")
        buf.write(u"\2\u027c\u027b\3\2\2\2\u027de\3\2\2\2\u027e\u027f\t\4")
        buf.write(u"\2\2\u027fg\3\2\2\2\u0280\u0281\t\5\2\2\u0281i\3\2\2")
        buf.write(u"\2\u0282\u0283\7.\2\2\u0283k\3\2\2\2\u0284\u0285\7\22")
        buf.write(u"\2\2\u0285m\3\2\2\2\u0286\u0287\t\6\2\2\u0287o\3\2\2")
        buf.write(u"\2\u0288\u0289\7g\2\2\u0289q\3\2\2\2\65ty}\u008e\u0092")
        buf.write(u"\u0099\u00a4\u00a9\u00b9\u00cc\u00d0\u00d4\u00de\u00e2")
        buf.write(u"\u00f8\u00fc\u0102\u0108\u011a\u011e\u0120\u0127\u012d")
        buf.write(u"\u0132\u0149\u015b\u0167\u0179\u017c\u0180\u0183\u0186")
        buf.write(u"\u018b\u0190\u0195\u019b\u019f\u01a2\u01ab\u01c1\u01c6")
        buf.write(u"\u01cc\u01d5\u01dd\u01f7\u0202\u0264\u0266\u0270\u0276")
        buf.write(u"\u027c")
        return buf.getvalue()
		

class ECMAScriptParser ( Parser ):

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
    Ident=101
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
                   u"'yield'", u"Ident", u"StringLiteral", u"WhiteSpaces", 
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
    RULE_identifier = 55

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
                   u"booleanLiteral", u"identifier" ]

    def __init__(self, input):
        super(ECMAScriptParser, self).__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sourceElements(self):
            return self.getTypedRuleContext(ECMAScriptParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_program

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitProgram(self)




    def program(self):

        localctx = ECMAScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 114
            token = self._input.LA(1)
            if token in [self.T__51, self.T__48, self.T__47, self.T__37, self.T__34, self.T__27, self.T__25, self.T__19, self.T__16, self.T__15, self.T__11, self.T__9, self.T__1, self.RegularExpressionLiteral, self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral, self.Break, self.Do, self.Typeof, self.New, self.Var, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.If, self.Throw, self.Delete, self.Try, self.Ident, self.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112 
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
            super(ECMAScriptParser.SourceElementsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sourceElement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SourceElementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SourceElementContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_sourceElements

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSourceElements(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSourceElements(self)




    def sourceElements(self):

        localctx = ECMAScriptParser.SourceElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sourceElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116 
                self.sourceElement()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0)):
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
            super(ECMAScriptParser.SourceElementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionDeclarationContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_sourceElement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSourceElement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSourceElement(self)




    def sourceElement(self):

        localctx = ECMAScriptParser.SourceElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sourceElement)
        try:
            self.state = 123
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121 
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122 
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
            super(ECMAScriptParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def labelledStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.LabelledStatementContext,0)


        def debuggerStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.DebuggerStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.BreakStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.TryStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IfStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ThrowStatementContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.EmptyStatementContext,0)


        def withStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.WithStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReturnStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.SwitchStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionStatementContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IterationStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ContinueStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ECMAScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 140
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125 
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126 
                self.variableStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127 
                self.emptyStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128 
                self.expressionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129 
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130 
                self.iterationStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 131 
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 132 
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 133 
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 134 
                self.withStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 135 
                self.labelledStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 136 
                self.switchStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 137 
                self.throwStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 138 
                self.tryStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 139 
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
            super(ECMAScriptParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBlock(self)




    def block(self):

        localctx = ECMAScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(self.T__19)
            self.state = 144
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 143 
                self.statementList()


            self.state = 146
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
            super(ECMAScriptParser.StatementListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_statementList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterStatementList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = ECMAScriptParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 148 
                self.statement()
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0)):
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
            super(ECMAScriptParser.VariableStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationListContext,0)


        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableStatement(self)




    def variableStatement(self):

        localctx = ECMAScriptParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(self.Var)
            self.state = 154 
            self.variableDeclarationList()
            self.state = 155 
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
            super(ECMAScriptParser.VariableDeclarationListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableDeclarationList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableDeclarationList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableDeclarationList(self)




    def variableDeclarationList(self):

        localctx = ECMAScriptParser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157 
            self.variableDeclaration()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.T__28:
                self.state = 158
                self.match(self.T__28)
                self.state = 159 
                self.variableDeclaration()
                self.state = 164
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
            super(ECMAScriptParser.VariableDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def initialiser(self):
            return self.getTypedRuleContext(ECMAScriptParser.InitialiserContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_variableDeclaration

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = ECMAScriptParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165 
            self.identifier()
            self.state = 167
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.T__38:
                self.state = 166 
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
            super(ECMAScriptParser.InitialiserContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_initialiser

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterInitialiser(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitInitialiser(self)




    def initialiser(self):

        localctx = ECMAScriptParser.InitialiserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_initialiser)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(self.T__38)
            self.state = 170 
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
            super(ECMAScriptParser.EmptyStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_emptyStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEmptyStatement(self)




    def emptyStatement(self):

        localctx = ECMAScriptParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
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
            super(ECMAScriptParser.ExpressionStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_expressionStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = ECMAScriptParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174 
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
            super(ECMAScriptParser.IfStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def Else(self):
            return self.getToken(ECMAScriptParser.Else, 0)

        def If(self):
            return self.getToken(ECMAScriptParser.If, 0)

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_ifStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = ECMAScriptParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(self.If)
            self.state = 177
            self.match(self.T__25)
            self.state = 178 
            self.expressionSequence()
            self.state = 179
            self.match(self.T__39)
            self.state = 180 
            self.statement()
            self.state = 183
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 181
                self.match(self.Else)
                self.state = 182 
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
            super(ECMAScriptParser.IterationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_iterationStatement

     
        def copyFrom(self, ctx):
            super(ECMAScriptParser.IterationStatementContext, self).copyFrom(ctx)



    class DoStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.DoStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)
        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def Do(self):
            return self.getToken(ECMAScriptParser.Do, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDoStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDoStatement(self)


    class ForVarInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.ForVarInStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)
        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)
        def variableDeclaration(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForVarInStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForVarInStatement(self)


    class ForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.ForStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def expressionSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForStatement(self)


    class WhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.WhileStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitWhileStatement(self)


    class ForInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.ForInStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForInStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForInStatement(self)


    class ForVarStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.IterationStatementContext)
            super(ECMAScriptParser.ForVarStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationListContext,0)

        def expressionSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,i)

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterForVarStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitForVarStatement(self)



    def iterationStatement(self):

        localctx = ECMAScriptParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 246
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(self.Do)
                self.state = 186 
                self.statement()
                self.state = 187
                self.match(self.While)
                self.state = 188
                self.match(self.T__25)
                self.state = 189 
                self.expressionSequence()
                self.state = 190
                self.match(self.T__39)
                self.state = 191 
                self.eos()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(self.While)
                self.state = 194
                self.match(self.T__25)
                self.state = 195 
                self.expressionSequence()
                self.state = 196
                self.match(self.T__39)
                self.state = 197 
                self.statement()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(self.For)
                self.state = 200
                self.match(self.T__25)
                self.state = 202
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 201 
                    self.expressionSequence()


                self.state = 204
                self.match(self.T__9)
                self.state = 206
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 205 
                    self.expressionSequence()


                self.state = 208
                self.match(self.T__9)
                self.state = 210
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 209 
                    self.expressionSequence()


                self.state = 212
                self.match(self.T__39)
                self.state = 213 
                self.statement()
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.match(self.For)
                self.state = 215
                self.match(self.T__25)
                self.state = 216
                self.match(self.Var)
                self.state = 217 
                self.variableDeclarationList()
                self.state = 218
                self.match(self.T__9)
                self.state = 220
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 219 
                    self.expressionSequence()


                self.state = 222
                self.match(self.T__9)
                self.state = 224
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                    self.state = 223 
                    self.expressionSequence()


                self.state = 226
                self.match(self.T__39)
                self.state = 227 
                self.statement()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.match(self.For)
                self.state = 230
                self.match(self.T__25)
                self.state = 231 
                self.singleExpression(0)
                self.state = 232
                self.match(self.In)
                self.state = 233 
                self.expressionSequence()
                self.state = 234
                self.match(self.T__39)
                self.state = 235 
                self.statement()
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 237
                self.match(self.For)
                self.state = 238
                self.match(self.T__25)
                self.state = 239
                self.match(self.Var)
                self.state = 240 
                self.variableDeclaration()
                self.state = 241
                self.match(self.In)
                self.state = 242 
                self.expressionSequence()
                self.state = 243
                self.match(self.T__39)
                self.state = 244 
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
            super(ECMAScriptParser.ContinueStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def Continue(self):
            return self.getToken(ECMAScriptParser.Continue, 0)

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_continueStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = ECMAScriptParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_continueStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(self.Continue)
            self.state = 250
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Ident:
                self.state = 249 
                self.identifier()


            self.state = 252 
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
            super(ECMAScriptParser.BreakStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def Break(self):
            return self.getToken(ECMAScriptParser.Break, 0)

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_breakStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = ECMAScriptParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_breakStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(self.Break)
            self.state = 256
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Ident:
                self.state = 255 
                self.identifier()


            self.state = 258 
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
            super(ECMAScriptParser.ReturnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def Return(self):
            return self.getToken(ECMAScriptParser.Return, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_returnStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = ECMAScriptParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(self.Return)
            self.state = 262
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 261 
                self.expressionSequence()


            self.state = 264 
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
            super(ECMAScriptParser.WithStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def With(self):
            return self.getToken(ECMAScriptParser.With, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_withStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterWithStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitWithStatement(self)




    def withStatement(self):

        localctx = ECMAScriptParser.WithStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_withStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(self.With)
            self.state = 267
            self.match(self.T__25)
            self.state = 268 
            self.expressionSequence()
            self.state = 269
            self.match(self.T__39)
            self.state = 270 
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
            super(ECMAScriptParser.SwitchStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def Switch(self):
            return self.getToken(ECMAScriptParser.Switch, 0)

        def caseBlock(self):
            return self.getTypedRuleContext(ECMAScriptParser.CaseBlockContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_switchStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = ECMAScriptParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(self.Switch)
            self.state = 273
            self.match(self.T__25)
            self.state = 274 
            self.expressionSequence()
            self.state = 275
            self.match(self.T__39)
            self.state = 276 
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
            super(ECMAScriptParser.CaseBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def defaultClause(self):
            return self.getTypedRuleContext(ECMAScriptParser.DefaultClauseContext,0)


        def caseClauses(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.CaseClausesContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.CaseClausesContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_caseBlock

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCaseBlock(self)




    def caseBlock(self):

        localctx = ECMAScriptParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(self.T__19)
            self.state = 280
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Case:
                self.state = 279 
                self.caseClauses()


            self.state = 286
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Default:
                self.state = 282 
                self.defaultClause()
                self.state = 284
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.Case:
                    self.state = 283 
                    self.caseClauses()




            self.state = 288
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
            super(ECMAScriptParser.CaseClausesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def caseClause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.CaseClauseContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_caseClauses

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCaseClauses(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCaseClauses(self)




    def caseClauses(self):

        localctx = ECMAScriptParser.CaseClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_caseClauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 290 
                self.caseClause()
                self.state = 293 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.Case):
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
            super(ECMAScriptParser.CaseClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def Case(self):
            return self.getToken(ECMAScriptParser.Case, 0)

        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_caseClause

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCaseClause(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCaseClause(self)




    def caseClause(self):

        localctx = ECMAScriptParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(self.Case)
            self.state = 296 
            self.expressionSequence()
            self.state = 297
            self.match(self.T__26)
            self.state = 299
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 298 
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
            super(ECMAScriptParser.DefaultClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Default(self):
            return self.getToken(ECMAScriptParser.Default, 0)

        def statementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_defaultClause

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDefaultClause(self)




    def defaultClause(self):

        localctx = ECMAScriptParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(self.Default)
            self.state = 302
            self.match(self.T__26)
            self.state = 304
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 303 
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
            super(ECMAScriptParser.LabelledStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_labelledStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLabelledStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLabelledStatement(self)




    def labelledStatement(self):

        localctx = ECMAScriptParser.LabelledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_labelledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306 
            self.identifier()
            self.state = 307
            self.match(self.T__26)
            self.state = 308 
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
            super(ECMAScriptParser.ThrowStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def Throw(self):
            return self.getToken(ECMAScriptParser.Throw, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_throwStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitThrowStatement(self)




    def throwStatement(self):

        localctx = ECMAScriptParser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(self.Throw)
            self.state = 311 
            self.expressionSequence()
            self.state = 312 
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
            super(ECMAScriptParser.TryStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(ECMAScriptParser.Try, 0)

        def catchProduction(self):
            return self.getTypedRuleContext(ECMAScriptParser.CatchProductionContext,0)


        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def finallyProduction(self):
            return self.getTypedRuleContext(ECMAScriptParser.FinallyProductionContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_tryStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterTryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitTryStatement(self)




    def tryStatement(self):

        localctx = ECMAScriptParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_tryStatement)
        try:
            self.state = 327
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(self.Try)
                self.state = 315 
                self.block()
                self.state = 316 
                self.catchProduction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(self.Try)
                self.state = 319 
                self.block()
                self.state = 320 
                self.finallyProduction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.match(self.Try)
                self.state = 323 
                self.block()
                self.state = 324 
                self.catchProduction()
                self.state = 325 
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
            super(ECMAScriptParser.CatchProductionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(ECMAScriptParser.Catch, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_catchProduction

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterCatchProduction(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitCatchProduction(self)




    def catchProduction(self):

        localctx = ECMAScriptParser.CatchProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_catchProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(self.Catch)
            self.state = 330
            self.match(self.T__25)
            self.state = 331 
            self.identifier()
            self.state = 332
            self.match(self.T__39)
            self.state = 333 
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
            super(ECMAScriptParser.FinallyProductionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def Finally(self):
            return self.getToken(ECMAScriptParser.Finally, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_finallyProduction

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFinallyProduction(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFinallyProduction(self)




    def finallyProduction(self):

        localctx = ECMAScriptParser.FinallyProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_finallyProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(self.Finally)
            self.state = 336 
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
            super(ECMAScriptParser.DebuggerStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def Debugger(self):
            return self.getToken(ECMAScriptParser.Debugger, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_debuggerStatement

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDebuggerStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDebuggerStatement(self)




    def debuggerStatement(self):

        localctx = ECMAScriptParser.DebuggerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_debuggerStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(self.Debugger)
            self.state = 339 
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
            super(ECMAScriptParser.FunctionDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.FormalParameterListContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_functionDeclaration

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = ECMAScriptParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(self.Function)
            self.state = 342 
            self.identifier()
            self.state = 343
            self.match(self.T__25)
            self.state = 345
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Ident:
                self.state = 344 
                self.formalParameterList()


            self.state = 347
            self.match(self.T__39)
            self.state = 348
            self.match(self.T__19)
            self.state = 349 
            self.functionBody()
            self.state = 350
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
            super(ECMAScriptParser.FormalParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_formalParameterList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFormalParameterList(self)




    def formalParameterList(self):

        localctx = ECMAScriptParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352 
            self.identifier()
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.T__28:
                self.state = 353
                self.match(self.T__28)
                self.state = 354 
                self.identifier()
                self.state = 359
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
            super(ECMAScriptParser.FunctionExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_functionExpression

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFunctionExpression(self)




    def functionExpression(self):

        localctx = ECMAScriptParser.FunctionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionExpression)
        try:
            self.state = 375
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(self.Function)
                self.state = 361
                self.match(self.T__25)
                self.state = 362 
                self.formalParameterList()
                self.state = 363
                self.match(self.T__39)
                self.state = 364
                self.match(self.T__19)
                self.state = 365 
                self.functionBody()
                self.state = 366
                self.match(self.T__42)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(self.Function)
                self.state = 369
                self.match(self.T__25)
                self.state = 370
                self.match(self.T__39)
                self.state = 371
                self.match(self.T__19)
                self.state = 372 
                self.functionBody()
                self.state = 373
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
            super(ECMAScriptParser.FunctionBodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sourceElements(self):
            return self.getTypedRuleContext(ECMAScriptParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_functionBody

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFunctionBody(self)




    def functionBody(self):

        localctx = ECMAScriptParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__9) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Var - 65)) | (1 << (self.Return - 65)) | (1 << (self.Void - 65)) | (1 << (self.Continue - 65)) | (1 << (self.For - 65)) | (1 << (self.Switch - 65)) | (1 << (self.While - 65)) | (1 << (self.Debugger - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.With - 65)) | (1 << (self.If - 65)) | (1 << (self.Throw - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Try - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 377 
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
            super(ECMAScriptParser.ArrayLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def elementList(self):
            return self.getTypedRuleContext(ECMAScriptParser.ElementListContext,0)


        def elision(self):
            return self.getTypedRuleContext(ECMAScriptParser.ElisionContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_arrayLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArrayLiteral(self)




    def arrayLiteral(self):

        localctx = ECMAScriptParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(self.T__51)
            self.state = 382
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 381 
                self.elementList()


            self.state = 385
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 384
                self.match(self.T__28)


            self.state = 388
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.T__28:
                self.state = 387 
                self.elision()


            self.state = 390
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
            super(ECMAScriptParser.ElementListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def elision(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ElisionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ElisionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_elementList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterElementList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitElementList(self)




    def elementList(self):

        localctx = ECMAScriptParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.T__28:
                self.state = 392 
                self.elision()


            self.state = 395 
            self.singleExpression(0)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 396
                    self.match(self.T__28)
                    self.state = 398
                    _la = self._input.LA(1)
                    if _la==ECMAScriptParser.T__28:
                        self.state = 397 
                        self.elision()


                    self.state = 400 
                    self.singleExpression(0) 
                self.state = 405
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
            super(ECMAScriptParser.ElisionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_elision

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterElision(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitElision(self)




    def elision(self):

        localctx = ECMAScriptParser.ElisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 406
                self.match(self.T__28)
                self.state = 409 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.T__28):
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
            super(ECMAScriptParser.ObjectLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyNameAndValueList(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertyNameAndValueListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_objectLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterObjectLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitObjectLiteral(self)




    def objectLiteral(self):

        localctx = ECMAScriptParser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(self.T__19)
            self.state = 413
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__47) | (1 << self.T__37) | (1 << self.T__29) | (1 << self.T__20) | (1 << self.T__16) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Break) | (1 << self.Do) | (1 << self.Instanceof) | (1 << self.Typeof) | (1 << self.Case))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (self.Else - 64)) | (1 << (self.New - 64)) | (1 << (self.Var - 64)) | (1 << (self.Catch - 64)) | (1 << (self.Finally - 64)) | (1 << (self.Return - 64)) | (1 << (self.Void - 64)) | (1 << (self.Continue - 64)) | (1 << (self.For - 64)) | (1 << (self.Switch - 64)) | (1 << (self.While - 64)) | (1 << (self.Debugger - 64)) | (1 << (self.Function - 64)) | (1 << (self.This - 64)) | (1 << (self.With - 64)) | (1 << (self.Default - 64)) | (1 << (self.If - 64)) | (1 << (self.Throw - 64)) | (1 << (self.Delete - 64)) | (1 << (self.In - 64)) | (1 << (self.Try - 64)) | (1 << (self.Class - 64)) | (1 << (self.Enum - 64)) | (1 << (self.Extends - 64)) | (1 << (self.Super - 64)) | (1 << (self.Const - 64)) | (1 << (self.Export - 64)) | (1 << (self.Import - 64)) | (1 << (self.Implements - 64)) | (1 << (self.Let - 64)) | (1 << (self.Private - 64)) | (1 << (self.Public - 64)) | (1 << (self.Interface - 64)) | (1 << (self.Package - 64)) | (1 << (self.Protected - 64)) | (1 << (self.Static - 64)) | (1 << (self.Yield - 64)) | (1 << (self.Ident - 64)) | (1 << (self.StringLiteral - 64)))) != 0):
                self.state = 412 
                self.propertyNameAndValueList()


            self.state = 416
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.T__28:
                self.state = 415
                self.match(self.T__28)


            self.state = 418
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
            super(ECMAScriptParser.PropertyNameAndValueListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyAssignment(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.PropertyAssignmentContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.PropertyAssignmentContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertyNameAndValueList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyNameAndValueList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyNameAndValueList(self)




    def propertyNameAndValueList(self):

        localctx = ECMAScriptParser.PropertyNameAndValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_propertyNameAndValueList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420 
            self.propertyAssignment()
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 421
                    self.match(self.T__28)
                    self.state = 422 
                    self.propertyAssignment() 
                self.state = 427
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
            super(ECMAScriptParser.PropertyAssignmentContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertyAssignment

     
        def copyFrom(self, ctx):
            super(ECMAScriptParser.PropertyAssignmentContext, self).copyFrom(ctx)



    class PropertyGetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super(ECMAScriptParser.PropertyGetterContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyGetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyGetter(self)


    class PropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super(ECMAScriptParser.PropertyExpressionAssignmentContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def propertyName(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertyNameContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyExpressionAssignment(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyExpressionAssignment(self)


    class PropertySetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.PropertyAssignmentContext)
            super(ECMAScriptParser.PropertySetterContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)

        def propertySetParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertySetParameterListContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertySetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertySetter(self)



    def propertyAssignment(self):

        localctx = ECMAScriptParser.PropertyAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_propertyAssignment)
        try:
            self.state = 447
            token = self._input.LA(1)
            if token in [self.T__47, self.T__37, self.T__16, self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral, self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try, self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield, self.Ident, self.StringLiteral]:
                localctx = ECMAScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 428 
                self.propertyName()
                self.state = 429
                self.match(self.T__26)
                self.state = 430 
                self.singleExpression(0)

            elif token in [self.T__29]:
                localctx = ECMAScriptParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(self.T__29)
                self.state = 433
                self.match(self.T__25)
                self.state = 434
                self.match(self.T__39)
                self.state = 435
                self.match(self.T__19)
                self.state = 436 
                self.functionBody()
                self.state = 437
                self.match(self.T__42)

            elif token in [self.T__20]:
                localctx = ECMAScriptParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.match(self.T__20)
                self.state = 440
                self.match(self.T__25)
                self.state = 441 
                self.propertySetParameterList()
                self.state = 442
                self.match(self.T__39)
                self.state = 443
                self.match(self.T__19)
                self.state = 444 
                self.functionBody()
                self.state = 445
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
            super(ECMAScriptParser.PropertyNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)


        def StringLiteral(self):
            return self.getToken(ECMAScriptParser.StringLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertyName

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertyName(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertyName(self)




    def propertyName(self):

        localctx = ECMAScriptParser.PropertyNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_propertyName)
        try:
            self.state = 452
            token = self._input.LA(1)
            if token in [self.T__47, self.T__37, self.T__16, self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try, self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield, self.Ident]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449 
                self.identifierName()

            elif token in [self.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.match(self.StringLiteral)

            elif token in [self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 451 
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
            super(ECMAScriptParser.PropertySetParameterListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_propertySetParameterList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPropertySetParameterList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPropertySetParameterList(self)




    def propertySetParameterList(self):

        localctx = ECMAScriptParser.PropertySetParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_propertySetParameterList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454 
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ArgumentsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def argumentList(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_arguments

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArguments(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = ECMAScriptParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(self.T__25)
            self.state = 458
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__51) | (1 << self.T__48) | (1 << self.T__47) | (1 << self.T__37) | (1 << self.T__34) | (1 << self.T__27) | (1 << self.T__25) | (1 << self.T__19) | (1 << self.T__16) | (1 << self.T__15) | (1 << self.T__11) | (1 << self.T__1) | (1 << self.RegularExpressionLiteral) | (1 << self.DecimalLiteral) | (1 << self.HexIntegerLiteral) | (1 << self.OctalIntegerLiteral) | (1 << self.Typeof))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.New - 65)) | (1 << (self.Void - 65)) | (1 << (self.Function - 65)) | (1 << (self.This - 65)) | (1 << (self.Delete - 65)) | (1 << (self.Ident - 65)) | (1 << (self.StringLiteral - 65)))) != 0):
                self.state = 457 
                self.argumentList()


            self.state = 460
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
            super(ECMAScriptParser.ArgumentListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_argumentList

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArgumentList(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = ECMAScriptParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462 
            self.singleExpression(0)
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.T__28:
                self.state = 463
                self.match(self.T__28)
                self.state = 464 
                self.singleExpression(0)
                self.state = 469
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
            super(ECMAScriptParser.ExpressionSequenceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_expressionSequence

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterExpressionSequence(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitExpressionSequence(self)




    def expressionSequence(self):

        localctx = ECMAScriptParser.ExpressionSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expressionSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470 
            self.singleExpression(0)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 471
                    self.match(self.T__28)
                    self.state = 472 
                    self.singleExpression(0) 
                self.state = 477
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
            super(ECMAScriptParser.SingleExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_singleExpression

     
        def copyFrom(self, ctx):
            super(ECMAScriptParser.SingleExpressionContext, self).copyFrom(ctx)


    class RightShiftLogicalExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.RightShiftLogicalExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterRightShiftLogicalExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitRightShiftLogicalExpression(self)


    class TernaryExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.TernaryExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitTernaryExpression(self)


    class BitOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.BitOrExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBitOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBitOrExpression(self)


    class AssignmentExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.AssignmentExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAssignmentExpression(self)


    class OrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.OrExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitOrExpression(self)


    class EqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.EqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEqualsExpression(self)


    class InstanceofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.InstanceofExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Instanceof(self):
            return self.getToken(ECMAScriptParser.Instanceof, 0)
        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterInstanceofExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitInstanceofExpression(self)


    class ModulusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ModulusExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterModulusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitModulusExpression(self)


    class LeftShiftArithmeticExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.LeftShiftArithmeticExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLeftShiftArithmeticExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLeftShiftArithmeticExpression(self)


    class ObjectLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ObjectLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def objectLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.ObjectLiteralContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterObjectLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitObjectLiteralExpression(self)


    class PreDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.PreDecreaseExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPreDecreaseExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPreDecreaseExpression(self)


    class NotEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.NotEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNotEqualsExpression(self)


    class InExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.InExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterInExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitInExpression(self)


    class ArrayLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ArrayLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArrayLiteralContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArrayLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArrayLiteralExpression(self)


    class IdentityNotEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.IdentityNotEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentityNotEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentityNotEqualsExpression(self)


    class ArgumentsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ArgumentsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterArgumentsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitArgumentsExpression(self)


    class MemberDotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.MemberDotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMemberDotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMemberDotExpression(self)


    class IdentityEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.IdentityEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentityEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentityEqualsExpression(self)


    class NotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.NotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNotExpression(self)


    class DeleteExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.DeleteExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def Delete(self):
            return self.getToken(ECMAScriptParser.Delete, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDeleteExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDeleteExpression(self)


    class IdentifierExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.IdentifierExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentifierExpression(self)


    class GreaterThanExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.GreaterThanExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterGreaterThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitGreaterThanExpression(self)


    class FnExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.FnExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functionExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFnExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFnExpression(self)


    class AddExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.AddExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAddExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAddExpression(self)


    class BitAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.BitAndExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBitAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBitAndExpression(self)


    class UnaryMinusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.UnaryMinusExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterUnaryMinusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitUnaryMinusExpression(self)


    class PreIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.PreIncrementExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPreIncrementExpression(self)


    class MultiplyExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.MultiplyExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMultiplyExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMultiplyExpression(self)


    class AndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.AndExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAndExpression(self)


    class VoidExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.VoidExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def Void(self):
            return self.getToken(ECMAScriptParser.Void, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVoidExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVoidExpression(self)


    class ParenthesizedExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ParenthesizedExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitParenthesizedExpression(self)


    class DivideExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.DivideExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterDivideExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitDivideExpression(self)


    class UnaryPlusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.UnaryPlusExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterUnaryPlusExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitUnaryPlusExpression(self)


    class LiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.LiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ECMAScriptParser.LiteralContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLiteralExpression(self)


    class BitNotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.BitNotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBitNotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBitNotExpression(self)


    class PostIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.PostIncrementExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPostIncrementExpression(self)


    class TypeofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.TypeofExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def Typeof(self):
            return self.getToken(ECMAScriptParser.Typeof, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterTypeofExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitTypeofExpression(self)


    class LessThanExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.LessThanExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLessThanExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLessThanExpression(self)


    class AssignmentOperatorExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.AssignmentOperatorExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def assignmentOperator(self):
            return self.getTypedRuleContext(ECMAScriptParser.AssignmentOperatorContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAssignmentOperatorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAssignmentOperatorExpression(self)


    class NewExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.NewExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def New(self):
            return self.getToken(ECMAScriptParser.New, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(ECMAScriptParser.ArgumentsContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNewExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNewExpression(self)


    class PostDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.PostDecreaseExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterPostDecreaseExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitPostDecreaseExpression(self)


    class SubtractExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.SubtractExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSubtractExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSubtractExpression(self)


    class RightShiftArithmeticExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.RightShiftArithmeticExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterRightShiftArithmeticExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitRightShiftArithmeticExpression(self)


    class BitXOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.BitXOrExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBitXOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBitXOrExpression(self)


    class GreaterThanEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.GreaterThanEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterGreaterThanEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitGreaterThanEqualsExpression(self)


    class MemberIndexExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.MemberIndexExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMemberIndexExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMemberIndexExpression(self)


    class ThisExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.ThisExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def This(self):
            return self.getToken(ECMAScriptParser.This, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterThisExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitThisExpression(self)


    class LessThanEqualsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.LessThanEqualsExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLessThanEqualsExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLessThanEqualsExpression(self)



    def singleExpression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ECMAScriptParser.SingleExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_singleExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            token = self._input.LA(1)
            if token in [self.Delete]:
                localctx = ECMAScriptParser.DeleteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 479
                self.match(self.Delete)
                self.state = 480 
                self.singleExpression(41)

            elif token in [self.Void]:
                localctx = ECMAScriptParser.VoidExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 481
                self.match(self.Void)
                self.state = 482 
                self.singleExpression(40)

            elif token in [self.Typeof]:
                localctx = ECMAScriptParser.TypeofExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 483
                self.match(self.Typeof)
                self.state = 484 
                self.singleExpression(39)

            elif token in [self.T__15]:
                localctx = ECMAScriptParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 485
                self.match(self.T__15)
                self.state = 486 
                self.singleExpression(38)

            elif token in [self.T__48]:
                localctx = ECMAScriptParser.PreDecreaseExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 487
                self.match(self.T__48)
                self.state = 488 
                self.singleExpression(37)

            elif token in [self.T__11]:
                localctx = ECMAScriptParser.UnaryPlusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 489
                self.match(self.T__11)
                self.state = 490 
                self.singleExpression(36)

            elif token in [self.T__27]:
                localctx = ECMAScriptParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 491
                self.match(self.T__27)
                self.state = 492 
                self.singleExpression(35)

            elif token in [self.T__1]:
                localctx = ECMAScriptParser.BitNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 493
                self.match(self.T__1)
                self.state = 494 
                self.singleExpression(34)

            elif token in [self.T__34]:
                localctx = ECMAScriptParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 495
                self.match(self.T__34)
                self.state = 496 
                self.singleExpression(33)

            elif token in [self.Function]:
                localctx = ECMAScriptParser.FnExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 497 
                self.functionExpression()

            elif token in [self.New]:
                localctx = ECMAScriptParser.NewExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 498
                self.match(self.New)
                self.state = 499 
                self.singleExpression(0)
                self.state = 501
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 500 
                    self.arguments()



            elif token in [self.This]:
                localctx = ECMAScriptParser.ThisExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 503
                self.match(self.This)

            elif token in [self.Ident]:
                localctx = ECMAScriptParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 504 
                self.identifier()

            elif token in [self.T__47, self.T__37, self.T__16, self.RegularExpressionLiteral, self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral, self.StringLiteral]:
                localctx = ECMAScriptParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 505 
                self.literal()

            elif token in [self.T__51]:
                localctx = ECMAScriptParser.ArrayLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 506 
                self.arrayLiteral()

            elif token in [self.T__19]:
                localctx = ECMAScriptParser.ObjectLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 507 
                self.objectLiteral()

            elif token in [self.T__25]:
                localctx = ECMAScriptParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 508
                self.match(self.T__25)
                self.state = 509 
                self.expressionSequence()
                self.state = 510
                self.match(self.T__39)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 612
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 610
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = ECMAScriptParser.MultiplyExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 514
                        if not self.precpred(self._ctx, 32):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 515
                        self.match(self.T__50)
                        self.state = 516 
                        self.singleExpression(33)
                        pass

                    elif la_ == 2:
                        localctx = ECMAScriptParser.DivideExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 517
                        if not self.precpred(self._ctx, 31):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 518
                        self.match(self.T__2)
                        self.state = 519 
                        self.singleExpression(32)
                        pass

                    elif la_ == 3:
                        localctx = ECMAScriptParser.ModulusExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 520
                        if not self.precpred(self._ctx, 30):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 521
                        self.match(self.T__41)
                        self.state = 522 
                        self.singleExpression(31)
                        pass

                    elif la_ == 4:
                        localctx = ECMAScriptParser.AddExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 523
                        if not self.precpred(self._ctx, 29):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 524
                        self.match(self.T__11)
                        self.state = 525 
                        self.singleExpression(30)
                        pass

                    elif la_ == 5:
                        localctx = ECMAScriptParser.SubtractExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 526
                        if not self.precpred(self._ctx, 28):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 527
                        self.match(self.T__27)
                        self.state = 528 
                        self.singleExpression(29)
                        pass

                    elif la_ == 6:
                        localctx = ECMAScriptParser.LeftShiftArithmeticExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 529
                        if not self.precpred(self._ctx, 27):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 530
                        self.match(self.T__43)
                        self.state = 531 
                        self.singleExpression(28)
                        pass

                    elif la_ == 7:
                        localctx = ECMAScriptParser.RightShiftArithmeticExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 532
                        if not self.precpred(self._ctx, 26):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 533
                        self.match(self.T__14)
                        self.state = 534 
                        self.singleExpression(27)
                        pass

                    elif la_ == 8:
                        localctx = ECMAScriptParser.RightShiftLogicalExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 535
                        if not self.precpred(self._ctx, 25):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 536
                        self.match(self.T__32)
                        self.state = 537 
                        self.singleExpression(26)
                        pass

                    elif la_ == 9:
                        localctx = ECMAScriptParser.LessThanExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 538
                        if not self.precpred(self._ctx, 24):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 539
                        self.match(self.T__49)
                        self.state = 540 
                        self.singleExpression(25)
                        pass

                    elif la_ == 10:
                        localctx = ECMAScriptParser.GreaterThanExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 541
                        if not self.precpred(self._ctx, 23):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 542
                        self.match(self.T__6)
                        self.state = 543 
                        self.singleExpression(24)
                        pass

                    elif la_ == 11:
                        localctx = ECMAScriptParser.LessThanEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 544
                        if not self.precpred(self._ctx, 22):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 545
                        self.match(self.T__44)
                        self.state = 546 
                        self.singleExpression(23)
                        pass

                    elif la_ == 12:
                        localctx = ECMAScriptParser.GreaterThanEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 547
                        if not self.precpred(self._ctx, 21):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 548
                        self.match(self.T__0)
                        self.state = 549 
                        self.singleExpression(22)
                        pass

                    elif la_ == 13:
                        localctx = ECMAScriptParser.InstanceofExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 550
                        if not self.precpred(self._ctx, 20):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 551
                        self.match(self.Instanceof)
                        self.state = 552 
                        self.singleExpression(21)
                        pass

                    elif la_ == 14:
                        localctx = ECMAScriptParser.InExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 553
                        if not self.precpred(self._ctx, 19):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 554
                        self.match(self.In)
                        self.state = 555 
                        self.singleExpression(20)
                        pass

                    elif la_ == 15:
                        localctx = ECMAScriptParser.EqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 556
                        if not self.precpred(self._ctx, 18):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 557
                        self.match(self.T__3)
                        self.state = 558 
                        self.singleExpression(19)
                        pass

                    elif la_ == 16:
                        localctx = ECMAScriptParser.NotEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 559
                        if not self.precpred(self._ctx, 17):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 560
                        self.match(self.T__45)
                        self.state = 561 
                        self.singleExpression(18)
                        pass

                    elif la_ == 17:
                        localctx = ECMAScriptParser.IdentityEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 562
                        if not self.precpred(self._ctx, 16):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 563
                        self.match(self.T__10)
                        self.state = 564 
                        self.singleExpression(17)
                        pass

                    elif la_ == 18:
                        localctx = ECMAScriptParser.IdentityNotEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 565
                        if not self.precpred(self._ctx, 15):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 566
                        self.match(self.T__46)
                        self.state = 567 
                        self.singleExpression(16)
                        pass

                    elif la_ == 19:
                        localctx = ECMAScriptParser.BitAndExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 568
                        if not self.precpred(self._ctx, 14):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 569
                        self.match(self.T__52)
                        self.state = 570 
                        self.singleExpression(15)
                        pass

                    elif la_ == 20:
                        localctx = ECMAScriptParser.BitXOrExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 571
                        if not self.precpred(self._ctx, 13):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 572
                        self.match(self.T__13)
                        self.state = 573 
                        self.singleExpression(14)
                        pass

                    elif la_ == 21:
                        localctx = ECMAScriptParser.BitOrExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 574
                        if not self.precpred(self._ctx, 12):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 575
                        self.match(self.T__35)
                        self.state = 576 
                        self.singleExpression(13)
                        pass

                    elif la_ == 22:
                        localctx = ECMAScriptParser.AndExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 577
                        if not self.precpred(self._ctx, 11):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 578
                        self.match(self.T__8)
                        self.state = 579 
                        self.singleExpression(12)
                        pass

                    elif la_ == 23:
                        localctx = ECMAScriptParser.OrExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 580
                        if not self.precpred(self._ctx, 10):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 581
                        self.match(self.T__7)
                        self.state = 582 
                        self.singleExpression(11)
                        pass

                    elif la_ == 24:
                        localctx = ECMAScriptParser.TernaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 583
                        if not self.precpred(self._ctx, 9):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 584
                        self.match(self.T__23)
                        self.state = 585 
                        self.singleExpression(0)
                        self.state = 586
                        self.match(self.T__26)
                        self.state = 587 
                        self.singleExpression(10)
                        pass

                    elif la_ == 25:
                        localctx = ECMAScriptParser.MemberIndexExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 589
                        if not self.precpred(self._ctx, 47):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 47)")
                        self.state = 590
                        self.match(self.T__51)
                        self.state = 591 
                        self.expressionSequence()
                        self.state = 592
                        self.match(self.T__31)
                        pass

                    elif la_ == 26:
                        localctx = ECMAScriptParser.MemberDotExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 594
                        if not self.precpred(self._ctx, 46):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 46)")
                        self.state = 595
                        self.match(self.T__12)
                        self.state = 596 
                        self.identifierName()
                        pass

                    elif la_ == 27:
                        localctx = ECMAScriptParser.ArgumentsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 597
                        if not self.precpred(self._ctx, 45):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 45)")
                        self.state = 598 
                        self.arguments()
                        pass

                    elif la_ == 28:
                        localctx = ECMAScriptParser.PostIncrementExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 599
                        if not self.precpred(self._ctx, 43):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 43)")
                        self.state = 600
                        self.match(self.T__15)
                        pass

                    elif la_ == 29:
                        localctx = ECMAScriptParser.PostDecreaseExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 601
                        if not self.precpred(self._ctx, 42):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 42)")
                        self.state = 602
                        self.match(self.T__48)
                        pass

                    elif la_ == 30:
                        localctx = ECMAScriptParser.AssignmentExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 603
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 604
                        self.match(self.T__38)
                        self.state = 605 
                        self.expressionSequence()
                        pass

                    elif la_ == 31:
                        localctx = ECMAScriptParser.AssignmentOperatorExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 606
                        if not self.precpred(self._ctx, 7):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 607 
                        self.assignmentOperator()
                        self.state = 608 
                        self.expressionSequence()
                        pass

             
                self.state = 614
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
            super(ECMAScriptParser.AssignmentOperatorContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_assignmentOperator

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAssignmentOperator(self)




    def assignmentOperator(self):

        localctx = ECMAScriptParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
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
            super(ECMAScriptParser.LiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RegularExpressionLiteral(self):
            return self.getToken(ECMAScriptParser.RegularExpressionLiteral, 0)

        def nullLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NullLiteralContext,0)


        def StringLiteral(self):
            return self.getToken(ECMAScriptParser.StringLiteral, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.BooleanLiteralContext,0)


        def numericLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_literal

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ECMAScriptParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literal)
        try:
            self.state = 622
            token = self._input.LA(1)
            if token in [self.T__37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 617 
                self.nullLiteral()

            elif token in [self.T__47, self.T__16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 618 
                self.booleanLiteral()

            elif token in [self.StringLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 619
                self.match(self.StringLiteral)

            elif token in [self.RegularExpressionLiteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 620
                self.match(self.RegularExpressionLiteral)

            elif token in [self.DecimalLiteral, self.HexIntegerLiteral, self.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 5)
                self.state = 621 
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
            super(ECMAScriptParser.NumericLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def HexIntegerLiteral(self):
            return self.getToken(ECMAScriptParser.HexIntegerLiteral, 0)

        def OctalIntegerLiteral(self):
            return self.getToken(ECMAScriptParser.OctalIntegerLiteral, 0)

        def DecimalLiteral(self):
            return self.getToken(ECMAScriptParser.DecimalLiteral, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_numericLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNumericLiteral(self)




    def numericLiteral(self):

        localctx = ECMAScriptParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
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
            super(ECMAScriptParser.IdentifierNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def reservedWord(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReservedWordContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_identifierName

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentifierName(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentifierName(self)




    def identifierName(self):

        localctx = ECMAScriptParser.IdentifierNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_identifierName)
        try:
            self.state = 628
            token = self._input.LA(1)
            if token in [self.Ident]:
                self.enterOuterAlt(localctx, 1)
                self.state = 626 
                self.identifier()

            elif token in [self.T__47, self.T__37, self.T__16, self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try, self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 627 
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
            super(ECMAScriptParser.ReservedWordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(ECMAScriptParser.KeywordContext,0)


        def nullLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NullLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.BooleanLiteralContext,0)


        def futureReservedWord(self):
            return self.getTypedRuleContext(ECMAScriptParser.FutureReservedWordContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_reservedWord

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterReservedWord(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitReservedWord(self)




    def reservedWord(self):

        localctx = ECMAScriptParser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_reservedWord)
        try:
            self.state = 634
            token = self._input.LA(1)
            if token in [self.Break, self.Do, self.Instanceof, self.Typeof, self.Case, self.Else, self.New, self.Var, self.Catch, self.Finally, self.Return, self.Void, self.Continue, self.For, self.Switch, self.While, self.Debugger, self.Function, self.This, self.With, self.Default, self.If, self.Throw, self.Delete, self.In, self.Try]:
                self.enterOuterAlt(localctx, 1)
                self.state = 630 
                self.keyword()

            elif token in [self.Class, self.Enum, self.Extends, self.Super, self.Const, self.Export, self.Import, self.Implements, self.Let, self.Private, self.Public, self.Interface, self.Package, self.Protected, self.Static, self.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 631 
                self.futureReservedWord()

            elif token in [self.T__37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 632 
                self.nullLiteral()

            elif token in [self.T__47, self.T__16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 633 
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
            super(ECMAScriptParser.KeywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)

        def With(self):
            return self.getToken(ECMAScriptParser.With, 0)

        def Case(self):
            return self.getToken(ECMAScriptParser.Case, 0)

        def Do(self):
            return self.getToken(ECMAScriptParser.Do, 0)

        def Else(self):
            return self.getToken(ECMAScriptParser.Else, 0)

        def If(self):
            return self.getToken(ECMAScriptParser.If, 0)

        def Switch(self):
            return self.getToken(ECMAScriptParser.Switch, 0)

        def Delete(self):
            return self.getToken(ECMAScriptParser.Delete, 0)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)

        def Try(self):
            return self.getToken(ECMAScriptParser.Try, 0)

        def Default(self):
            return self.getToken(ECMAScriptParser.Default, 0)

        def This(self):
            return self.getToken(ECMAScriptParser.This, 0)

        def Return(self):
            return self.getToken(ECMAScriptParser.Return, 0)

        def Void(self):
            return self.getToken(ECMAScriptParser.Void, 0)

        def Catch(self):
            return self.getToken(ECMAScriptParser.Catch, 0)

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def Typeof(self):
            return self.getToken(ECMAScriptParser.Typeof, 0)

        def Throw(self):
            return self.getToken(ECMAScriptParser.Throw, 0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)

        def New(self):
            return self.getToken(ECMAScriptParser.New, 0)

        def Instanceof(self):
            return self.getToken(ECMAScriptParser.Instanceof, 0)

        def Continue(self):
            return self.getToken(ECMAScriptParser.Continue, 0)

        def Break(self):
            return self.getToken(ECMAScriptParser.Break, 0)

        def Finally(self):
            return self.getToken(ECMAScriptParser.Finally, 0)

        def Debugger(self):
            return self.getToken(ECMAScriptParser.Debugger, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_keyword

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterKeyword(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = ECMAScriptParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
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
            super(ECMAScriptParser.FutureReservedWordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Enum(self):
            return self.getToken(ECMAScriptParser.Enum, 0)

        def Extends(self):
            return self.getToken(ECMAScriptParser.Extends, 0)

        def Implements(self):
            return self.getToken(ECMAScriptParser.Implements, 0)

        def Let(self):
            return self.getToken(ECMAScriptParser.Let, 0)

        def Protected(self):
            return self.getToken(ECMAScriptParser.Protected, 0)

        def Interface(self):
            return self.getToken(ECMAScriptParser.Interface, 0)

        def Export(self):
            return self.getToken(ECMAScriptParser.Export, 0)

        def Import(self):
            return self.getToken(ECMAScriptParser.Import, 0)

        def Class(self):
            return self.getToken(ECMAScriptParser.Class, 0)

        def Package(self):
            return self.getToken(ECMAScriptParser.Package, 0)

        def Public(self):
            return self.getToken(ECMAScriptParser.Public, 0)

        def Static(self):
            return self.getToken(ECMAScriptParser.Static, 0)

        def Super(self):
            return self.getToken(ECMAScriptParser.Super, 0)

        def Private(self):
            return self.getToken(ECMAScriptParser.Private, 0)

        def Yield(self):
            return self.getToken(ECMAScriptParser.Yield, 0)

        def Const(self):
            return self.getToken(ECMAScriptParser.Const, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_futureReservedWord

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterFutureReservedWord(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitFutureReservedWord(self)




    def futureReservedWord(self):

        localctx = ECMAScriptParser.FutureReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_futureReservedWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
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
            super(ECMAScriptParser.EosContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_eos

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterEos(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitEos(self)




    def eos(self):

        localctx = ECMAScriptParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_eos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
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
            super(ECMAScriptParser.NullLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_nullLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterNullLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitNullLiteral(self)




    def nullLiteral(self):

        localctx = ECMAScriptParser.NullLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_nullLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
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
            super(ECMAScriptParser.BooleanLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_booleanLiteral

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitBooleanLiteral(self)




    def booleanLiteral(self):

        localctx = ECMAScriptParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            _la = self._input.LA(1)
            if not(_la==ECMAScriptParser.T__47 or _la==ECMAScriptParser.T__16):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Ident(self):
            return self.getToken(ECMAScriptParser.Ident, 0)

        def getRuleIndex(self):
            return ECMAScriptParser.RULE_identifier

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = ECMAScriptParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.match(self.Ident)
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
         



