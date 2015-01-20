# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
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
        buf.write(u"j\u029b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\3\2\3\2\5\2y\n\2\3\3\6\3|\n\3\r\3\16")
        buf.write(u"\3}\3\4\3\4\5\4\u0082\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0093\n\5\3\6\3")
        buf.write(u"\6\5\6\u0097\n\6\3\6\3\6\3\7\6\7\u009c\n\7\r\7\16\7\u009d")
        buf.write(u"\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u00a7\n\t\f\t\16\t\u00aa")
        buf.write(u"\13\t\3\n\3\n\5\n\u00ae\n\n\3\13\3\13\3\13\3\f\3\f\3")
        buf.write(u"\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00be")
        buf.write(u"\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d1\n\17")
        buf.write(u"\3\17\3\17\5\17\u00d5\n\17\3\17\3\17\5\17\u00d9\n\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00e3\n")
        buf.write(u"\17\3\17\3\17\5\17\u00e7\n\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\5\17\u00fd\n\17\3\20\3\20\5\20")
        buf.write(u"\u0101\n\20\3\20\3\20\3\21\3\21\5\21\u0107\n\21\3\21")
        buf.write(u"\3\21\3\22\3\22\5\22\u010d\n\22\3\22\3\22\3\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write(u"\3\25\5\25\u011f\n\25\3\25\3\25\5\25\u0123\n\25\5\25")
        buf.write(u"\u0125\n\25\3\25\3\25\3\26\6\26\u012a\n\26\r\26\16\26")
        buf.write(u"\u012b\3\27\3\27\3\27\3\27\5\27\u0132\n\27\3\30\3\30")
        buf.write(u"\3\30\5\30\u0137\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3")
        buf.write(u"\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\5\33\u014e\n\33\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write(u"\3\37\3\37\5\37\u0160\n\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u" \3 \3 \7 \u016a\n \f \16 \u016d\13 \3!\3!\3!\3!\3!\3")
        buf.write(u"!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u017e\n!\3\"\5\"\u0181")
        buf.write(u"\n\"\3#\3#\5#\u0185\n#\3#\5#\u0188\n#\3#\5#\u018b\n#")
        buf.write(u"\3#\3#\3$\5$\u0190\n$\3$\3$\3$\5$\u0195\n$\3$\7$\u0198")
        buf.write(u"\n$\f$\16$\u019b\13$\3%\6%\u019e\n%\r%\16%\u019f\3&\3")
        buf.write(u"&\5&\u01a4\n&\3&\5&\u01a7\n&\3&\3&\3\'\3\'\3\'\7\'\u01ae")
        buf.write(u"\n\'\f\'\16\'\u01b1\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write(u"(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01c6\n(\3)\3)\3)\5)")
        buf.write(u"\u01cb\n)\3*\3*\3+\3+\5+\u01d1\n+\3+\3+\3,\3,\3,\7,\u01d8")
        buf.write(u"\n,\f,\16,\u01db\13,\3-\3-\3-\7-\u01e0\n-\f-\16-\u01e3")
        buf.write(u"\13-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\5.\u01fc\n.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\5.\u0207\n.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(u".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\7")
        buf.write(u".\u026b\n.\f.\16.\u026e\13.\3/\3/\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\5\60\u0277\n\60\3\61\3\61\3\62\3\62\5\62\u027d")
        buf.write(u"\n\62\3\63\3\63\3\63\3\63\5\63\u0283\n\63\3\64\3\64\3")
        buf.write(u"\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\3:\3:\3:")
        buf.write(u"\3;\3;\3;\3;\5;\u0299\n;\3;\2\3Z<\2\4\6\b\n\f\16\20\22")
        buf.write(u"\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNP")
        buf.write(u"RTVXZ\\^`bdfhjlnprt\2\7\3\2(\62\3\28:\3\2;T\3\2Ud\3\2")
        buf.write(u"\64\65\u02db\2x\3\2\2\2\4{\3\2\2\2\6\u0081\3\2\2\2\b")
        buf.write(u"\u0092\3\2\2\2\n\u0094\3\2\2\2\f\u009b\3\2\2\2\16\u009f")
        buf.write(u"\3\2\2\2\20\u00a3\3\2\2\2\22\u00ab\3\2\2\2\24\u00af\3")
        buf.write(u"\2\2\2\26\u00b2\3\2\2\2\30\u00b4\3\2\2\2\32\u00b6\3\2")
        buf.write(u"\2\2\34\u00fc\3\2\2\2\36\u00fe\3\2\2\2 \u0104\3\2\2\2")
        buf.write(u"\"\u010a\3\2\2\2$\u0110\3\2\2\2&\u0116\3\2\2\2(\u011c")
        buf.write(u"\3\2\2\2*\u0129\3\2\2\2,\u012d\3\2\2\2.\u0133\3\2\2\2")
        buf.write(u"\60\u0138\3\2\2\2\62\u013c\3\2\2\2\64\u014d\3\2\2\2\66")
        buf.write(u"\u014f\3\2\2\28\u0155\3\2\2\2:\u0158\3\2\2\2<\u015b\3")
        buf.write(u"\2\2\2>\u0166\3\2\2\2@\u017d\3\2\2\2B\u0180\3\2\2\2D")
        buf.write(u"\u0182\3\2\2\2F\u018f\3\2\2\2H\u019d\3\2\2\2J\u01a1\3")
        buf.write(u"\2\2\2L\u01aa\3\2\2\2N\u01c5\3\2\2\2P\u01ca\3\2\2\2R")
        buf.write(u"\u01cc\3\2\2\2T\u01ce\3\2\2\2V\u01d4\3\2\2\2X\u01dc\3")
        buf.write(u"\2\2\2Z\u0206\3\2\2\2\\\u026f\3\2\2\2^\u0276\3\2\2\2")
        buf.write(u"`\u0278\3\2\2\2b\u027c\3\2\2\2d\u0282\3\2\2\2f\u0284")
        buf.write(u"\3\2\2\2h\u0286\3\2\2\2j\u0288\3\2\2\2l\u028a\3\2\2\2")
        buf.write(u"n\u028c\3\2\2\2p\u028e\3\2\2\2r\u0291\3\2\2\2t\u0298")
        buf.write(u"\3\2\2\2vy\5\4\3\2wy\3\2\2\2xv\3\2\2\2xw\3\2\2\2y\3\3")
        buf.write(u"\2\2\2z|\5\6\4\2{z\3\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2")
        buf.write(u"\2\2~\5\3\2\2\2\177\u0082\5\b\5\2\u0080\u0082\5<\37\2")
        buf.write(u"\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\7\3\2\2")
        buf.write(u"\2\u0083\u0093\5\n\6\2\u0084\u0093\5\16\b\2\u0085\u0093")
        buf.write(u"\5\26\f\2\u0086\u0093\5\30\r\2\u0087\u0093\5\32\16\2")
        buf.write(u"\u0088\u0093\5\34\17\2\u0089\u0093\5\36\20\2\u008a\u0093")
        buf.write(u"\5 \21\2\u008b\u0093\5\"\22\2\u008c\u0093\5$\23\2\u008d")
        buf.write(u"\u0093\5\60\31\2\u008e\u0093\5&\24\2\u008f\u0093\5\62")
        buf.write(u"\32\2\u0090\u0093\5\64\33\2\u0091\u0093\5:\36\2\u0092")
        buf.write(u"\u0083\3\2\2\2\u0092\u0084\3\2\2\2\u0092\u0085\3\2\2")
        buf.write(u"\2\u0092\u0086\3\2\2\2\u0092\u0087\3\2\2\2\u0092\u0088")
        buf.write(u"\3\2\2\2\u0092\u0089\3\2\2\2\u0092\u008a\3\2\2\2\u0092")
        buf.write(u"\u008b\3\2\2\2\u0092\u008c\3\2\2\2\u0092\u008d\3\2\2")
        buf.write(u"\2\u0092\u008e\3\2\2\2\u0092\u008f\3\2\2\2\u0092\u0090")
        buf.write(u"\3\2\2\2\u0092\u0091\3\2\2\2\u0093\t\3\2\2\2\u0094\u0096")
        buf.write(u"\7\3\2\2\u0095\u0097\5\f\7\2\u0096\u0095\3\2\2\2\u0096")
        buf.write(u"\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\7\4\2")
        buf.write(u"\2\u0099\13\3\2\2\2\u009a\u009c\5\b\5\2\u009b\u009a\3")
        buf.write(u"\2\2\2\u009c\u009d\3\2\2\2\u009d\u009b\3\2\2\2\u009d")
        buf.write(u"\u009e\3\2\2\2\u009e\r\3\2\2\2\u009f\u00a0\7B\2\2\u00a0")
        buf.write(u"\u00a1\5\20\t\2\u00a1\u00a2\5t;\2\u00a2\17\3\2\2\2\u00a3")
        buf.write(u"\u00a8\5\22\n\2\u00a4\u00a5\7\5\2\2\u00a5\u00a7\5\22")
        buf.write(u"\n\2\u00a6\u00a4\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6")
        buf.write(u"\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\21\3\2\2\2\u00aa\u00a8")
        buf.write(u"\3\2\2\2\u00ab\u00ad\5n8\2\u00ac\u00ae\5\24\13\2\u00ad")
        buf.write(u"\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\23\3\2\2\2\u00af")
        buf.write(u"\u00b0\7\6\2\2\u00b0\u00b1\5Z.\2\u00b1\25\3\2\2\2\u00b2")
        buf.write(u"\u00b3\7\7\2\2\u00b3\27\3\2\2\2\u00b4\u00b5\5X-\2\u00b5")
        buf.write(u"\31\3\2\2\2\u00b6\u00b7\7P\2\2\u00b7\u00b8\7\b\2\2\u00b8")
        buf.write(u"\u00b9\5X-\2\u00b9\u00ba\7\t\2\2\u00ba\u00bd\5\b\5\2")
        buf.write(u"\u00bb\u00bc\7@\2\2\u00bc\u00be\5\b\5\2\u00bd\u00bb\3")
        buf.write(u"\2\2\2\u00bd\u00be\3\2\2\2\u00be\33\3\2\2\2\u00bf\u00c0")
        buf.write(u"\7<\2\2\u00c0\u00c1\5\b\5\2\u00c1\u00c2\7J\2\2\u00c2")
        buf.write(u"\u00c3\7\b\2\2\u00c3\u00c4\5X-\2\u00c4\u00c5\7\t\2\2")
        buf.write(u"\u00c5\u00c6\5t;\2\u00c6\u00fd\3\2\2\2\u00c7\u00c8\7")
        buf.write(u"J\2\2\u00c8\u00c9\7\b\2\2\u00c9\u00ca\5X-\2\u00ca\u00cb")
        buf.write(u"\7\t\2\2\u00cb\u00cc\5\b\5\2\u00cc\u00fd\3\2\2\2\u00cd")
        buf.write(u"\u00ce\7H\2\2\u00ce\u00d0\7\b\2\2\u00cf\u00d1\5X-\2\u00d0")
        buf.write(u"\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2")
        buf.write(u"\2\u00d2\u00d4\7\7\2\2\u00d3\u00d5\5X-\2\u00d4\u00d3")
        buf.write(u"\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write(u"\u00d8\7\7\2\2\u00d7\u00d9\5X-\2\u00d8\u00d7\3\2\2\2")
        buf.write(u"\u00d8\u00d9\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db")
        buf.write(u"\7\t\2\2\u00db\u00fd\5\b\5\2\u00dc\u00dd\7H\2\2\u00dd")
        buf.write(u"\u00de\7\b\2\2\u00de\u00df\7B\2\2\u00df\u00e0\5\20\t")
        buf.write(u"\2\u00e0\u00e2\7\7\2\2\u00e1\u00e3\5X-\2\u00e2\u00e1")
        buf.write(u"\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write(u"\u00e6\7\7\2\2\u00e5\u00e7\5X-\2\u00e6\u00e5\3\2\2\2")
        buf.write(u"\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9")
        buf.write(u"\7\t\2\2\u00e9\u00ea\5\b\5\2\u00ea\u00fd\3\2\2\2\u00eb")
        buf.write(u"\u00ec\7H\2\2\u00ec\u00ed\7\b\2\2\u00ed\u00ee\5Z.\2\u00ee")
        buf.write(u"\u00ef\7S\2\2\u00ef\u00f0\5X-\2\u00f0\u00f1\7\t\2\2\u00f1")
        buf.write(u"\u00f2\5\b\5\2\u00f2\u00fd\3\2\2\2\u00f3\u00f4\7H\2\2")
        buf.write(u"\u00f4\u00f5\7\b\2\2\u00f5\u00f6\7B\2\2\u00f6\u00f7\5")
        buf.write(u"\22\n\2\u00f7\u00f8\7S\2\2\u00f8\u00f9\5X-\2\u00f9\u00fa")
        buf.write(u"\7\t\2\2\u00fa\u00fb\5\b\5\2\u00fb\u00fd\3\2\2\2\u00fc")
        buf.write(u"\u00bf\3\2\2\2\u00fc\u00c7\3\2\2\2\u00fc\u00cd\3\2\2")
        buf.write(u"\2\u00fc\u00dc\3\2\2\2\u00fc\u00eb\3\2\2\2\u00fc\u00f3")
        buf.write(u"\3\2\2\2\u00fd\35\3\2\2\2\u00fe\u0100\7G\2\2\u00ff\u0101")
        buf.write(u"\5n8\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write(u"\u0102\3\2\2\2\u0102\u0103\5t;\2\u0103\37\3\2\2\2\u0104")
        buf.write(u"\u0106\7;\2\2\u0105\u0107\5n8\2\u0106\u0105\3\2\2\2\u0106")
        buf.write(u"\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\5t;\2")
        buf.write(u"\u0109!\3\2\2\2\u010a\u010c\7E\2\2\u010b\u010d\5X-\2")
        buf.write(u"\u010c\u010b\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e")
        buf.write(u"\3\2\2\2\u010e\u010f\5t;\2\u010f#\3\2\2\2\u0110\u0111")
        buf.write(u"\7N\2\2\u0111\u0112\7\b\2\2\u0112\u0113\5X-\2\u0113\u0114")
        buf.write(u"\7\t\2\2\u0114\u0115\5\b\5\2\u0115%\3\2\2\2\u0116\u0117")
        buf.write(u"\7I\2\2\u0117\u0118\7\b\2\2\u0118\u0119\5X-\2\u0119\u011a")
        buf.write(u"\7\t\2\2\u011a\u011b\5(\25\2\u011b\'\3\2\2\2\u011c\u011e")
        buf.write(u"\7\3\2\2\u011d\u011f\5*\26\2\u011e\u011d\3\2\2\2\u011e")
        buf.write(u"\u011f\3\2\2\2\u011f\u0124\3\2\2\2\u0120\u0122\5.\30")
        buf.write(u"\2\u0121\u0123\5*\26\2\u0122\u0121\3\2\2\2\u0122\u0123")
        buf.write(u"\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0120\3\2\2\2\u0124")
        buf.write(u"\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\7\4\2")
        buf.write(u"\2\u0127)\3\2\2\2\u0128\u012a\5,\27\2\u0129\u0128\3\2")
        buf.write(u"\2\2\u012a\u012b\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c")
        buf.write(u"\3\2\2\2\u012c+\3\2\2\2\u012d\u012e\7?\2\2\u012e\u012f")
        buf.write(u"\5X-\2\u012f\u0131\7\n\2\2\u0130\u0132\5\f\7\2\u0131")
        buf.write(u"\u0130\3\2\2\2\u0131\u0132\3\2\2\2\u0132-\3\2\2\2\u0133")
        buf.write(u"\u0134\7O\2\2\u0134\u0136\7\n\2\2\u0135\u0137\5\f\7\2")
        buf.write(u"\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137/\3\2\2")
        buf.write(u"\2\u0138\u0139\5n8\2\u0139\u013a\7\n\2\2\u013a\u013b")
        buf.write(u"\5\b\5\2\u013b\61\3\2\2\2\u013c\u013d\7Q\2\2\u013d\u013e")
        buf.write(u"\5X-\2\u013e\u013f\5t;\2\u013f\63\3\2\2\2\u0140\u0141")
        buf.write(u"\7T\2\2\u0141\u0142\5\n\6\2\u0142\u0143\5\66\34\2\u0143")
        buf.write(u"\u014e\3\2\2\2\u0144\u0145\7T\2\2\u0145\u0146\5\n\6\2")
        buf.write(u"\u0146\u0147\58\35\2\u0147\u014e\3\2\2\2\u0148\u0149")
        buf.write(u"\7T\2\2\u0149\u014a\5\n\6\2\u014a\u014b\5\66\34\2\u014b")
        buf.write(u"\u014c\58\35\2\u014c\u014e\3\2\2\2\u014d\u0140\3\2\2")
        buf.write(u"\2\u014d\u0144\3\2\2\2\u014d\u0148\3\2\2\2\u014e\65\3")
        buf.write(u"\2\2\2\u014f\u0150\7C\2\2\u0150\u0151\7\b\2\2\u0151\u0152")
        buf.write(u"\5n8\2\u0152\u0153\7\t\2\2\u0153\u0154\5\n\6\2\u0154")
        buf.write(u"\67\3\2\2\2\u0155\u0156\7D\2\2\u0156\u0157\5\n\6\2\u0157")
        buf.write(u"9\3\2\2\2\u0158\u0159\7K\2\2\u0159\u015a\5t;\2\u015a")
        buf.write(u";\3\2\2\2\u015b\u015c\7L\2\2\u015c\u015d\5n8\2\u015d")
        buf.write(u"\u015f\7\b\2\2\u015e\u0160\5> \2\u015f\u015e\3\2\2\2")
        buf.write(u"\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162")
        buf.write(u"\7\t\2\2\u0162\u0163\7\3\2\2\u0163\u0164\5B\"\2\u0164")
        buf.write(u"\u0165\7\4\2\2\u0165=\3\2\2\2\u0166\u016b\5n8\2\u0167")
        buf.write(u"\u0168\7\5\2\2\u0168\u016a\5n8\2\u0169\u0167\3\2\2\2")
        buf.write(u"\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c")
        buf.write(u"\3\2\2\2\u016c?\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u016f")
        buf.write(u"\7L\2\2\u016f\u0170\7\b\2\2\u0170\u0171\5> \2\u0171\u0172")
        buf.write(u"\7\t\2\2\u0172\u0173\7\3\2\2\u0173\u0174\5B\"\2\u0174")
        buf.write(u"\u0175\7\4\2\2\u0175\u017e\3\2\2\2\u0176\u0177\7L\2\2")
        buf.write(u"\u0177\u0178\7\b\2\2\u0178\u0179\7\t\2\2\u0179\u017a")
        buf.write(u"\7\3\2\2\u017a\u017b\5B\"\2\u017b\u017c\7\4\2\2\u017c")
        buf.write(u"\u017e\3\2\2\2\u017d\u016e\3\2\2\2\u017d\u0176\3\2\2")
        buf.write(u"\2\u017eA\3\2\2\2\u017f\u0181\5\4\3\2\u0180\u017f\3\2")
        buf.write(u"\2\2\u0180\u0181\3\2\2\2\u0181C\3\2\2\2\u0182\u0184\7")
        buf.write(u"\13\2\2\u0183\u0185\5F$\2\u0184\u0183\3\2\2\2\u0184\u0185")
        buf.write(u"\3\2\2\2\u0185\u0187\3\2\2\2\u0186\u0188\7\5\2\2\u0187")
        buf.write(u"\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2")
        buf.write(u"\2\u0189\u018b\5H%\2\u018a\u0189\3\2\2\2\u018a\u018b")
        buf.write(u"\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\7\f\2\2\u018d")
        buf.write(u"E\3\2\2\2\u018e\u0190\5H%\2\u018f\u018e\3\2\2\2\u018f")
        buf.write(u"\u0190\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0199\5Z.\2")
        buf.write(u"\u0192\u0194\7\5\2\2\u0193\u0195\5H%\2\u0194\u0193\3")
        buf.write(u"\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write(u"\u0198\5Z.\2\u0197\u0192\3\2\2\2\u0198\u019b\3\2\2\2")
        buf.write(u"\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019aG\3\2\2")
        buf.write(u"\2\u019b\u0199\3\2\2\2\u019c\u019e\7\5\2\2\u019d\u019c")
        buf.write(u"\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write(u"\u01a0\3\2\2\2\u01a0I\3\2\2\2\u01a1\u01a3\7\3\2\2\u01a2")
        buf.write(u"\u01a4\5L\'\2\u01a3\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write(u"\u01a4\u01a6\3\2\2\2\u01a5\u01a7\7\5\2\2\u01a6\u01a5")
        buf.write(u"\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write(u"\u01a9\7\4\2\2\u01a9K\3\2\2\2\u01aa\u01af\5N(\2\u01ab")
        buf.write(u"\u01ac\7\5\2\2\u01ac\u01ae\5N(\2\u01ad\u01ab\3\2\2\2")
        buf.write(u"\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0")
        buf.write(u"\3\2\2\2\u01b0M\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3")
        buf.write(u"\5P)\2\u01b3\u01b4\7\n\2\2\u01b4\u01b5\5Z.\2\u01b5\u01c6")
        buf.write(u"\3\2\2\2\u01b6\u01b7\5p9\2\u01b7\u01b8\7\b\2\2\u01b8")
        buf.write(u"\u01b9\7\t\2\2\u01b9\u01ba\7\3\2\2\u01ba\u01bb\5B\"\2")
        buf.write(u"\u01bb\u01bc\7\4\2\2\u01bc\u01c6\3\2\2\2\u01bd\u01be")
        buf.write(u"\5r:\2\u01be\u01bf\7\b\2\2\u01bf\u01c0\5R*\2\u01c0\u01c1")
        buf.write(u"\7\t\2\2\u01c1\u01c2\7\3\2\2\u01c2\u01c3\5B\"\2\u01c3")
        buf.write(u"\u01c4\7\4\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01b2\3\2\2")
        buf.write(u"\2\u01c5\u01b6\3\2\2\2\u01c5\u01bd\3\2\2\2\u01c6O\3\2")
        buf.write(u"\2\2\u01c7\u01cb\5b\62\2\u01c8\u01cb\7f\2\2\u01c9\u01cb")
        buf.write(u"\5`\61\2\u01ca\u01c7\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write(u"\u01c9\3\2\2\2\u01cbQ\3\2\2\2\u01cc\u01cd\5n8\2\u01cd")
        buf.write(u"S\3\2\2\2\u01ce\u01d0\7\b\2\2\u01cf\u01d1\5V,\2\u01d0")
        buf.write(u"\u01cf\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\3\2\2")
        buf.write(u"\2\u01d2\u01d3\7\t\2\2\u01d3U\3\2\2\2\u01d4\u01d9\5Z")
        buf.write(u".\2\u01d5\u01d6\7\5\2\2\u01d6\u01d8\5Z.\2\u01d7\u01d5")
        buf.write(u"\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write(u"\u01da\3\2\2\2\u01daW\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc")
        buf.write(u"\u01e1\5Z.\2\u01dd\u01de\7\5\2\2\u01de\u01e0\5Z.\2\u01df")
        buf.write(u"\u01dd\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2")
        buf.write(u"\2\u01e1\u01e2\3\2\2\2\u01e2Y\3\2\2\2\u01e3\u01e1\3\2")
        buf.write(u"\2\2\u01e4\u01e5\b.\1\2\u01e5\u01e6\7R\2\2\u01e6\u0207")
        buf.write(u"\5Z.+\u01e7\u01e8\7F\2\2\u01e8\u0207\5Z.*\u01e9\u01ea")
        buf.write(u"\7>\2\2\u01ea\u0207\5Z.)\u01eb\u01ec\7\16\2\2\u01ec\u0207")
        buf.write(u"\5Z.(\u01ed\u01ee\7\17\2\2\u01ee\u0207\5Z.\'\u01ef\u01f0")
        buf.write(u"\7\20\2\2\u01f0\u0207\5Z.&\u01f1\u01f2\7\21\2\2\u01f2")
        buf.write(u"\u0207\5Z.%\u01f3\u01f4\7\22\2\2\u01f4\u0207\5Z.$\u01f5")
        buf.write(u"\u01f6\7\23\2\2\u01f6\u0207\5Z.#\u01f7\u0207\5@!\2\u01f8")
        buf.write(u"\u01f9\7A\2\2\u01f9\u01fb\5Z.\2\u01fa\u01fc\5T+\2\u01fb")
        buf.write(u"\u01fa\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u0207\3\2\2")
        buf.write(u"\2\u01fd\u0207\7M\2\2\u01fe\u0207\5n8\2\u01ff\u0207\5")
        buf.write(u"^\60\2\u0200\u0207\5D#\2\u0201\u0207\5J&\2\u0202\u0203")
        buf.write(u"\7\b\2\2\u0203\u0204\5X-\2\u0204\u0205\7\t\2\2\u0205")
        buf.write(u"\u0207\3\2\2\2\u0206\u01e4\3\2\2\2\u0206\u01e7\3\2\2")
        buf.write(u"\2\u0206\u01e9\3\2\2\2\u0206\u01eb\3\2\2\2\u0206\u01ed")
        buf.write(u"\3\2\2\2\u0206\u01ef\3\2\2\2\u0206\u01f1\3\2\2\2\u0206")
        buf.write(u"\u01f3\3\2\2\2\u0206\u01f5\3\2\2\2\u0206\u01f7\3\2\2")
        buf.write(u"\2\u0206\u01f8\3\2\2\2\u0206\u01fd\3\2\2\2\u0206\u01fe")
        buf.write(u"\3\2\2\2\u0206\u01ff\3\2\2\2\u0206\u0200\3\2\2\2\u0206")
        buf.write(u"\u0201\3\2\2\2\u0206\u0202\3\2\2\2\u0207\u026c\3\2\2")
        buf.write(u"\2\u0208\u0209\f\"\2\2\u0209\u020a\7\24\2\2\u020a\u026b")
        buf.write(u"\5Z.#\u020b\u020c\f!\2\2\u020c\u020d\7\25\2\2\u020d\u026b")
        buf.write(u"\5Z.\"\u020e\u020f\f \2\2\u020f\u0210\7\26\2\2\u0210")
        buf.write(u"\u026b\5Z.!\u0211\u0212\f\37\2\2\u0212\u0213\7\20\2\2")
        buf.write(u"\u0213\u026b\5Z. \u0214\u0215\f\36\2\2\u0215\u0216\7")
        buf.write(u"\21\2\2\u0216\u026b\5Z.\37\u0217\u0218\f\35\2\2\u0218")
        buf.write(u"\u0219\7\27\2\2\u0219\u026b\5Z.\36\u021a\u021b\f\34\2")
        buf.write(u"\2\u021b\u021c\7\30\2\2\u021c\u026b\5Z.\35\u021d\u021e")
        buf.write(u"\f\33\2\2\u021e\u021f\7\31\2\2\u021f\u026b\5Z.\34\u0220")
        buf.write(u"\u0221\f\32\2\2\u0221\u0222\7\32\2\2\u0222\u026b\5Z.")
        buf.write(u"\33\u0223\u0224\f\31\2\2\u0224\u0225\7\33\2\2\u0225\u026b")
        buf.write(u"\5Z.\32\u0226\u0227\f\30\2\2\u0227\u0228\7\34\2\2\u0228")
        buf.write(u"\u026b\5Z.\31\u0229\u022a\f\27\2\2\u022a\u022b\7\35\2")
        buf.write(u"\2\u022b\u026b\5Z.\30\u022c\u022d\f\26\2\2\u022d\u022e")
        buf.write(u"\7=\2\2\u022e\u026b\5Z.\27\u022f\u0230\f\25\2\2\u0230")
        buf.write(u"\u0231\7S\2\2\u0231\u026b\5Z.\26\u0232\u0233\f\24\2\2")
        buf.write(u"\u0233\u0234\7\36\2\2\u0234\u026b\5Z.\25\u0235\u0236")
        buf.write(u"\f\23\2\2\u0236\u0237\7\37\2\2\u0237\u026b\5Z.\24\u0238")
        buf.write(u"\u0239\f\22\2\2\u0239\u023a\7 \2\2\u023a\u026b\5Z.\23")
        buf.write(u"\u023b\u023c\f\21\2\2\u023c\u023d\7!\2\2\u023d\u026b")
        buf.write(u"\5Z.\22\u023e\u023f\f\20\2\2\u023f\u0240\7\"\2\2\u0240")
        buf.write(u"\u026b\5Z.\21\u0241\u0242\f\17\2\2\u0242\u0243\7#\2\2")
        buf.write(u"\u0243\u026b\5Z.\20\u0244\u0245\f\16\2\2\u0245\u0246")
        buf.write(u"\7$\2\2\u0246\u026b\5Z.\17\u0247\u0248\f\r\2\2\u0248")
        buf.write(u"\u0249\7%\2\2\u0249\u026b\5Z.\16\u024a\u024b\f\f\2\2")
        buf.write(u"\u024b\u024c\7&\2\2\u024c\u026b\5Z.\r\u024d\u024e\f\13")
        buf.write(u"\2\2\u024e\u024f\7\'\2\2\u024f\u0250\5Z.\2\u0250\u0251")
        buf.write(u"\7\n\2\2\u0251\u0252\5Z.\f\u0252\u026b\3\2\2\2\u0253")
        buf.write(u"\u0254\f\61\2\2\u0254\u0255\7\13\2\2\u0255\u0256\5X-")
        buf.write(u"\2\u0256\u0257\7\f\2\2\u0257\u026b\3\2\2\2\u0258\u0259")
        buf.write(u"\f\60\2\2\u0259\u025a\7\r\2\2\u025a\u026b\5b\62\2\u025b")
        buf.write(u"\u025c\f/\2\2\u025c\u026b\5T+\2\u025d\u025e\f-\2\2\u025e")
        buf.write(u"\u025f\6.\36\2\u025f\u026b\7\16\2\2\u0260\u0261\f,\2")
        buf.write(u"\2\u0261\u0262\6. \2\u0262\u026b\7\17\2\2\u0263\u0264")
        buf.write(u"\f\n\2\2\u0264\u0265\7\6\2\2\u0265\u026b\5X-\2\u0266")
        buf.write(u"\u0267\f\t\2\2\u0267\u0268\5\\/\2\u0268\u0269\5X-\2\u0269")
        buf.write(u"\u026b\3\2\2\2\u026a\u0208\3\2\2\2\u026a\u020b\3\2\2")
        buf.write(u"\2\u026a\u020e\3\2\2\2\u026a\u0211\3\2\2\2\u026a\u0214")
        buf.write(u"\3\2\2\2\u026a\u0217\3\2\2\2\u026a\u021a\3\2\2\2\u026a")
        buf.write(u"\u021d\3\2\2\2\u026a\u0220\3\2\2\2\u026a\u0223\3\2\2")
        buf.write(u"\2\u026a\u0226\3\2\2\2\u026a\u0229\3\2\2\2\u026a\u022c")
        buf.write(u"\3\2\2\2\u026a\u022f\3\2\2\2\u026a\u0232\3\2\2\2\u026a")
        buf.write(u"\u0235\3\2\2\2\u026a\u0238\3\2\2\2\u026a\u023b\3\2\2")
        buf.write(u"\2\u026a\u023e\3\2\2\2\u026a\u0241\3\2\2\2\u026a\u0244")
        buf.write(u"\3\2\2\2\u026a\u0247\3\2\2\2\u026a\u024a\3\2\2\2\u026a")
        buf.write(u"\u024d\3\2\2\2\u026a\u0253\3\2\2\2\u026a\u0258\3\2\2")
        buf.write(u"\2\u026a\u025b\3\2\2\2\u026a\u025d\3\2\2\2\u026a\u0260")
        buf.write(u"\3\2\2\2\u026a\u0263\3\2\2\2\u026a\u0266\3\2\2\2\u026b")
        buf.write(u"\u026e\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2")
        buf.write(u"\2\u026d[\3\2\2\2\u026e\u026c\3\2\2\2\u026f\u0270\t\2")
        buf.write(u"\2\2\u0270]\3\2\2\2\u0271\u0277\5j\66\2\u0272\u0277\5")
        buf.write(u"l\67\2\u0273\u0277\7f\2\2\u0274\u0277\7\66\2\2\u0275")
        buf.write(u"\u0277\5`\61\2\u0276\u0271\3\2\2\2\u0276\u0272\3\2\2")
        buf.write(u"\2\u0276\u0273\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0275")
        buf.write(u"\3\2\2\2\u0277_\3\2\2\2\u0278\u0279\t\3\2\2\u0279a\3")
        buf.write(u"\2\2\2\u027a\u027d\5n8\2\u027b\u027d\5d\63\2\u027c\u027a")
        buf.write(u"\3\2\2\2\u027c\u027b\3\2\2\2\u027dc\3\2\2\2\u027e\u0283")
        buf.write(u"\5f\64\2\u027f\u0283\5h\65\2\u0280\u0283\5j\66\2\u0281")
        buf.write(u"\u0283\5l\67\2\u0282\u027e\3\2\2\2\u0282\u027f\3\2\2")
        buf.write(u"\2\u0282\u0280\3\2\2\2\u0282\u0281\3\2\2\2\u0283e\3\2")
        buf.write(u"\2\2\u0284\u0285\t\4\2\2\u0285g\3\2\2\2\u0286\u0287\t")
        buf.write(u"\5\2\2\u0287i\3\2\2\2\u0288\u0289\7\63\2\2\u0289k\3\2")
        buf.write(u"\2\2\u028a\u028b\t\6\2\2\u028bm\3\2\2\2\u028c\u028d\7")
        buf.write(u"e\2\2\u028do\3\2\2\2\u028e\u028f\69#\2\u028f\u0290\5")
        buf.write(u"n8\2\u0290q\3\2\2\2\u0291\u0292\6:$\2\u0292\u0293\5n")
        buf.write(u"8\2\u0293s\3\2\2\2\u0294\u0299\7\7\2\2\u0295\u0299\7")
        buf.write(u"\2\2\3\u0296\u0299\6;%\2\u0297\u0299\6;&\2\u0298\u0294")
        buf.write(u"\3\2\2\2\u0298\u0295\3\2\2\2\u0298\u0296\3\2\2\2\u0298")
        buf.write(u"\u0297\3\2\2\2\u0299u\3\2\2\2\66x}\u0081\u0092\u0096")
        buf.write(u"\u009d\u00a8\u00ad\u00bd\u00d0\u00d4\u00d8\u00e2\u00e6")
        buf.write(u"\u00fc\u0100\u0106\u010c\u011e\u0122\u0124\u012b\u0131")
        buf.write(u"\u0136\u014d\u015f\u016b\u017d\u0180\u0184\u0187\u018a")
        buf.write(u"\u018f\u0194\u0199\u019f\u01a3\u01a6\u01af\u01c5\u01ca")
        buf.write(u"\u01d0\u01d9\u01e1\u01fb\u0206\u026a\u026c\u0276\u027c")
        buf.write(u"\u0282\u0298")
        return buf.getvalue()
		

class ECMAScriptParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"','", u"'='", u"';'", 
                     u"'('", u"')'", u"':'", u"'['", u"']'", u"'.'", u"'++'", 
                     u"'--'", u"'+'", u"'-'", u"'~'", u"'!'", u"'*'", u"'/'", 
                     u"'%'", u"'<<'", u"'>>'", u"'>>>'", u"'<'", u"'>'", 
                     u"'<='", u"'>='", u"'=='", u"'!='", u"'==='", u"'!=='", 
                     u"'&'", u"'^'", u"'|'", u"'&&'", u"'||'", u"'?'", u"'*='", 
                     u"'/='", u"'%='", u"'+='", u"'-='", u"'<<='", u"'>>='", 
                     u"'>>>='", u"'&='", u"'^='", u"'|='", u"'null'", u"'true'", 
                     u"'false'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'break'", u"'do'", u"'instanceof'", 
                     u"'typeof'", u"'case'", u"'else'", u"'new'", u"'var'", 
                     u"'catch'", u"'finally'", u"'return'", u"'void'", u"'continue'", 
                     u"'for'", u"'switch'", u"'while'", u"'debugger'", u"'function'", 
                     u"'this'", u"'with'", u"'default'", u"'if'", u"'throw'", 
                     u"'delete'", u"'in'", u"'try'", u"'class'", u"'enum'", 
                     u"'extends'", u"'super'", u"'const'", u"'export'", 
                     u"'import'", u"'implements'", u"'let'", u"'private'", 
                     u"'public'", u"'interface'", u"'package'", u"'protected'", 
                     u"'static'", u"'yield'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"RegularExpressionLiteral", u"LineTerminator", u"DecimalLiteral", 
                      u"HexIntegerLiteral", u"OctalIntegerLiteral", u"Break", 
                      u"Do", u"Instanceof", u"Typeof", u"Case", u"Else", 
                      u"New", u"Var", u"Catch", u"Finally", u"Return", u"Void", 
                      u"Continue", u"For", u"Switch", u"While", u"Debugger", 
                      u"Function", u"This", u"With", u"Default", u"If", 
                      u"Throw", u"Delete", u"In", u"Try", u"Class", u"Enum", 
                      u"Extends", u"Super", u"Const", u"Export", u"Import", 
                      u"Implements", u"Let", u"Private", u"Public", u"Interface", 
                      u"Package", u"Protected", u"Static", u"Yield", u"Ident", 
                      u"StringLiteral", u"WhiteSpaces", u"MultiLineComment", 
                      u"SingleLineComment", u"UnexpectedCharacter" ]

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
    RULE_nullLiteral = 52
    RULE_booleanLiteral = 53
    RULE_identifier = 54
    RULE_getter = 55
    RULE_setter = 56
    RULE_eos = 57

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
                   u"keyword", u"futureReservedWord", u"nullLiteral", u"booleanLiteral", 
                   u"identifier", u"getter", u"setter", u"eos" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    RegularExpressionLiteral=52
    LineTerminator=53
    DecimalLiteral=54
    HexIntegerLiteral=55
    OctalIntegerLiteral=56
    Break=57
    Do=58
    Instanceof=59
    Typeof=60
    Case=61
    Else=62
    New=63
    Var=64
    Catch=65
    Finally=66
    Return=67
    Void=68
    Continue=69
    For=70
    Switch=71
    While=72
    Debugger=73
    Function=74
    This=75
    With=76
    Default=77
    If=78
    Throw=79
    Delete=80
    In=81
    Try=82
    Class=83
    Enum=84
    Extends=85
    Super=86
    Const=87
    Export=88
    Import=89
    Implements=90
    Let=91
    Private=92
    Public=93
    Interface=94
    Package=95
    Protected=96
    Static=97
    Yield=98
    Ident=99
    StringLiteral=100
    WhiteSpaces=101
    MultiLineComment=102
    SingleLineComment=103
    UnexpectedCharacter=104

    def __init__(self, input):
        super(ECMAScriptParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    def here(self, type) :

        possibleIndexEosToken = self.getCurrentToken().tokenIndex - 1;
        ahead = self._input.tokens[possibleIndexEosToken]

        return (ahead.channel == Lexer.HIDDEN) and (ahead.type == type);


    def lineTerminatorAhead(self) :

        possibleIndexEosToken = self.getCurrentToken().tokenIndex -1;
        ahead = self._input.tokens[possibleIndexEosToken]

        if (ahead.channel != Lexer.HIDDEN) :
            return False;
        

        text = ahead._text;
        type = ahead.type;

        return (type == self.MultiLineComment and (text.contains("\r") or text.contains("\n"))) or (type == self.LineTerminator)



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
            self.state = 118
            token = self._input.LA(1)
            if token in [ECMAScriptParser.T__0, ECMAScriptParser.T__4, ECMAScriptParser.T__5, ECMAScriptParser.T__8, ECMAScriptParser.T__11, ECMAScriptParser.T__12, ECMAScriptParser.T__13, ECMAScriptParser.T__14, ECMAScriptParser.T__15, ECMAScriptParser.T__16, ECMAScriptParser.T__48, ECMAScriptParser.T__49, ECMAScriptParser.T__50, ECMAScriptParser.RegularExpressionLiteral, ECMAScriptParser.DecimalLiteral, ECMAScriptParser.HexIntegerLiteral, ECMAScriptParser.OctalIntegerLiteral, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Typeof, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.Try, ECMAScriptParser.Ident, ECMAScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116 
                self.sourceElements()

            elif token in [ECMAScriptParser.EOF]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            pass
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
            self.state = 121 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120 
                self.sourceElement()
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__4) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Break) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.Void - 64)) | (1 << (ECMAScriptParser.Continue - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.Switch - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.Debugger - 64)) | (1 << (ECMAScriptParser.Function - 64)) | (1 << (ECMAScriptParser.This - 64)) | (1 << (ECMAScriptParser.With - 64)) | (1 << (ECMAScriptParser.If - 64)) | (1 << (ECMAScriptParser.Throw - 64)) | (1 << (ECMAScriptParser.Delete - 64)) | (1 << (ECMAScriptParser.Try - 64)) | (1 << (ECMAScriptParser.Ident - 64)) | (1 << (ECMAScriptParser.StringLiteral - 64)))) != 0)):
                    break

        except RecognitionException as re:
            raise Exception(self)
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
            self.state = 127
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125 
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126 
                self.functionDeclaration()
                pass


        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableStatementContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.EmptyStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IfStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.IterationStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ContinueStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.BreakStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReturnStatementContext,0)


        def withStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.WithStatementContext,0)


        def labelledStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.LabelledStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.SwitchStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.ThrowStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.TryStatementContext,0)


        def debuggerStatement(self):
            return self.getTypedRuleContext(ECMAScriptParser.DebuggerStatementContext,0)


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
            self.state = 144
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129 
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130 
                self.variableStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131 
                self.emptyStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132 
                self.expressionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133 
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 134 
                self.iterationStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 135 
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 136 
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 137 
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 138 
                self.withStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 139 
                self.labelledStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 140 
                self.switchStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 141 
                self.throwStatement()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 142 
                self.tryStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 143 
                self.debuggerStatement()
                pass


        except RecognitionException as re:
            pass
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
            self.state = 146
            self.match(ECMAScriptParser.T__0)
            self.state = 148
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__4) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Break) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.Void - 64)) | (1 << (ECMAScriptParser.Continue - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.Switch - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.Debugger - 64)) | (1 << (ECMAScriptParser.Function - 64)) | (1 << (ECMAScriptParser.This - 64)) | (1 << (ECMAScriptParser.With - 64)) | (1 << (ECMAScriptParser.If - 64)) | (1 << (ECMAScriptParser.Throw - 64)) | (1 << (ECMAScriptParser.Delete - 64)) | (1 << (ECMAScriptParser.Try - 64)) | (1 << (ECMAScriptParser.Ident - 64)) | (1 << (ECMAScriptParser.StringLiteral - 64)))) != 0):
                self.state = 147 
                self.statementList()


            self.state = 150
            self.match(ECMAScriptParser.T__1)
        except RecognitionException as re:
            pass
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
            self.state = 153 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152 
                self.statement()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__4) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Break) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.Void - 64)) | (1 << (ECMAScriptParser.Continue - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.Switch - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.Debugger - 64)) | (1 << (ECMAScriptParser.Function - 64)) | (1 << (ECMAScriptParser.This - 64)) | (1 << (ECMAScriptParser.With - 64)) | (1 << (ECMAScriptParser.If - 64)) | (1 << (ECMAScriptParser.Throw - 64)) | (1 << (ECMAScriptParser.Delete - 64)) | (1 << (ECMAScriptParser.Try - 64)) | (1 << (ECMAScriptParser.Ident - 64)) | (1 << (ECMAScriptParser.StringLiteral - 64)))) != 0)):
                    break

        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class VariableStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.VariableStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationListContext,0)


        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


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
            self.state = 157
            self.match(ECMAScriptParser.Var)
            self.state = 158 
            self.variableDeclarationList()
            self.state = 159 
            self.eos()
        except RecognitionException as re:
            pass
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161 
            self.variableDeclaration()
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 162
                    self.match(ECMAScriptParser.T__2)
                    self.state = 163 
                    self.variableDeclaration() 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.VariableDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def initialiser(self):
            return self.getTypedRuleContext(ECMAScriptParser.InitialiserContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169 
            self.identifier()
            self.state = 171
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 170 
                self.initialiser()


        except RecognitionException as re:
            pass
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
            self.state = 173
            self.match(ECMAScriptParser.T__3)
            self.state = 174 
            self.singleExpression(0)
        except RecognitionException as re:
            pass
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
            self.state = 176
            self.match(ECMAScriptParser.T__4)
        except RecognitionException as re:
            pass
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
            self.state = 178 
            self.expressionSequence()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.IfStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(ECMAScriptParser.If, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.StatementContext,i)


        def Else(self):
            return self.getToken(ECMAScriptParser.Else, 0)

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
            self.state = 180
            self.match(ECMAScriptParser.If)
            self.state = 181
            self.match(ECMAScriptParser.T__5)
            self.state = 182 
            self.expressionSequence()
            self.state = 183
            self.match(ECMAScriptParser.T__6)
            self.state = 184 
            self.statement()
            self.state = 187
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 185
                self.match(ECMAScriptParser.Else)
                self.state = 186 
                self.statement()


        except RecognitionException as re:
            pass
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

        def Do(self):
            return self.getToken(ECMAScriptParser.Do, 0)
        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


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

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)
        def variableDeclaration(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationContext,0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


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

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

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

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


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

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


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

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)
        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)
        def variableDeclarationList(self):
            return self.getTypedRuleContext(ECMAScriptParser.VariableDeclarationListContext,0)

        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)

        def expressionSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,i)


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
            self.state = 250
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(ECMAScriptParser.Do)
                self.state = 190 
                self.statement()
                self.state = 191
                self.match(ECMAScriptParser.While)
                self.state = 192
                self.match(ECMAScriptParser.T__5)
                self.state = 193 
                self.expressionSequence()
                self.state = 194
                self.match(ECMAScriptParser.T__6)
                self.state = 195 
                self.eos()
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(ECMAScriptParser.While)
                self.state = 198
                self.match(ECMAScriptParser.T__5)
                self.state = 199 
                self.expressionSequence()
                self.state = 200
                self.match(ECMAScriptParser.T__6)
                self.state = 201 
                self.statement()
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(ECMAScriptParser.For)
                self.state = 204
                self.match(ECMAScriptParser.T__5)
                self.state = 206
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (ECMAScriptParser.Void - 68)) | (1 << (ECMAScriptParser.Function - 68)) | (1 << (ECMAScriptParser.This - 68)) | (1 << (ECMAScriptParser.Delete - 68)) | (1 << (ECMAScriptParser.Ident - 68)) | (1 << (ECMAScriptParser.StringLiteral - 68)))) != 0):
                    self.state = 205 
                    self.expressionSequence()


                self.state = 208
                self.match(ECMAScriptParser.T__4)
                self.state = 210
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (ECMAScriptParser.Void - 68)) | (1 << (ECMAScriptParser.Function - 68)) | (1 << (ECMAScriptParser.This - 68)) | (1 << (ECMAScriptParser.Delete - 68)) | (1 << (ECMAScriptParser.Ident - 68)) | (1 << (ECMAScriptParser.StringLiteral - 68)))) != 0):
                    self.state = 209 
                    self.expressionSequence()


                self.state = 212
                self.match(ECMAScriptParser.T__4)
                self.state = 214
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (ECMAScriptParser.Void - 68)) | (1 << (ECMAScriptParser.Function - 68)) | (1 << (ECMAScriptParser.This - 68)) | (1 << (ECMAScriptParser.Delete - 68)) | (1 << (ECMAScriptParser.Ident - 68)) | (1 << (ECMAScriptParser.StringLiteral - 68)))) != 0):
                    self.state = 213 
                    self.expressionSequence()


                self.state = 216
                self.match(ECMAScriptParser.T__6)
                self.state = 217 
                self.statement()
                pass

            elif la_ == 4:
                localctx = ECMAScriptParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 218
                self.match(ECMAScriptParser.For)
                self.state = 219
                self.match(ECMAScriptParser.T__5)
                self.state = 220
                self.match(ECMAScriptParser.Var)
                self.state = 221 
                self.variableDeclarationList()
                self.state = 222
                self.match(ECMAScriptParser.T__4)
                self.state = 224
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (ECMAScriptParser.Void - 68)) | (1 << (ECMAScriptParser.Function - 68)) | (1 << (ECMAScriptParser.This - 68)) | (1 << (ECMAScriptParser.Delete - 68)) | (1 << (ECMAScriptParser.Ident - 68)) | (1 << (ECMAScriptParser.StringLiteral - 68)))) != 0):
                    self.state = 223 
                    self.expressionSequence()


                self.state = 226
                self.match(ECMAScriptParser.T__4)
                self.state = 228
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (ECMAScriptParser.Void - 68)) | (1 << (ECMAScriptParser.Function - 68)) | (1 << (ECMAScriptParser.This - 68)) | (1 << (ECMAScriptParser.Delete - 68)) | (1 << (ECMAScriptParser.Ident - 68)) | (1 << (ECMAScriptParser.StringLiteral - 68)))) != 0):
                    self.state = 227 
                    self.expressionSequence()


                self.state = 230
                self.match(ECMAScriptParser.T__6)
                self.state = 231 
                self.statement()
                pass

            elif la_ == 5:
                localctx = ECMAScriptParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 233
                self.match(ECMAScriptParser.For)
                self.state = 234
                self.match(ECMAScriptParser.T__5)
                self.state = 235 
                self.singleExpression(0)
                self.state = 236
                self.match(ECMAScriptParser.In)
                self.state = 237 
                self.expressionSequence()
                self.state = 238
                self.match(ECMAScriptParser.T__6)
                self.state = 239 
                self.statement()
                pass

            elif la_ == 6:
                localctx = ECMAScriptParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 241
                self.match(ECMAScriptParser.For)
                self.state = 242
                self.match(ECMAScriptParser.T__5)
                self.state = 243
                self.match(ECMAScriptParser.Var)
                self.state = 244 
                self.variableDeclaration()
                self.state = 245
                self.match(ECMAScriptParser.In)
                self.state = 246 
                self.expressionSequence()
                self.state = 247
                self.match(ECMAScriptParser.T__6)
                self.state = 248 
                self.statement()
                pass


        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ContinueStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(ECMAScriptParser.Continue, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(ECMAScriptParser.Continue)
            self.state = 254
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 253 
                self.identifier()


            self.state = 256 
            self.eos()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.BreakStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(ECMAScriptParser.Break, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ECMAScriptParser.Break)
            self.state = 260
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 259 
                self.identifier()


            self.state = 262 
            self.eos()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ReturnStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(ECMAScriptParser.Return, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ECMAScriptParser.Return)
            self.state = 266
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 265 
                self.expressionSequence()


            self.state = 268 
            self.eos()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class WithStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.WithStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def With(self):
            return self.getToken(ECMAScriptParser.With, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


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
            self.state = 270
            self.match(ECMAScriptParser.With)
            self.state = 271
            self.match(ECMAScriptParser.T__5)
            self.state = 272 
            self.expressionSequence()
            self.state = 273
            self.match(ECMAScriptParser.T__6)
            self.state = 274 
            self.statement()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class SwitchStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.SwitchStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Switch(self):
            return self.getToken(ECMAScriptParser.Switch, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


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
            self.state = 276
            self.match(ECMAScriptParser.Switch)
            self.state = 277
            self.match(ECMAScriptParser.T__5)
            self.state = 278 
            self.expressionSequence()
            self.state = 279
            self.match(ECMAScriptParser.T__6)
            self.state = 280 
            self.caseBlock()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class CaseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.CaseBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def caseClauses(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.CaseClausesContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.CaseClausesContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(ECMAScriptParser.DefaultClauseContext,0)


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
            self.state = 282
            self.match(ECMAScriptParser.T__0)
            self.state = 284
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Case:
                self.state = 283 
                self.caseClauses()


            self.state = 290
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Default:
                self.state = 286 
                self.defaultClause()
                self.state = 288
                _la = self._input.LA(1)
                if _la==ECMAScriptParser.Case:
                    self.state = 287 
                    self.caseClauses()




            self.state = 292
            self.match(ECMAScriptParser.T__1)
        except RecognitionException as re:
            pass
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
            self.state = 295 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 294 
                self.caseClause()
                self.state = 297 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.Case):
                    break

        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class CaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.CaseClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Case(self):
            return self.getToken(ECMAScriptParser.Case, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


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
            self.state = 299
            self.match(ECMAScriptParser.Case)
            self.state = 300 
            self.expressionSequence()
            self.state = 301
            self.match(ECMAScriptParser.T__7)
            self.state = 303
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__4) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Break) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.Void - 64)) | (1 << (ECMAScriptParser.Continue - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.Switch - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.Debugger - 64)) | (1 << (ECMAScriptParser.Function - 64)) | (1 << (ECMAScriptParser.This - 64)) | (1 << (ECMAScriptParser.With - 64)) | (1 << (ECMAScriptParser.If - 64)) | (1 << (ECMAScriptParser.Throw - 64)) | (1 << (ECMAScriptParser.Delete - 64)) | (1 << (ECMAScriptParser.Try - 64)) | (1 << (ECMAScriptParser.Ident - 64)) | (1 << (ECMAScriptParser.StringLiteral - 64)))) != 0):
                self.state = 302 
                self.statementList()


        except RecognitionException as re:
            pass
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
            self.state = 305
            self.match(ECMAScriptParser.Default)
            self.state = 306
            self.match(ECMAScriptParser.T__7)
            self.state = 308
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__4) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Break) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.Void - 64)) | (1 << (ECMAScriptParser.Continue - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.Switch - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.Debugger - 64)) | (1 << (ECMAScriptParser.Function - 64)) | (1 << (ECMAScriptParser.This - 64)) | (1 << (ECMAScriptParser.With - 64)) | (1 << (ECMAScriptParser.If - 64)) | (1 << (ECMAScriptParser.Throw - 64)) | (1 << (ECMAScriptParser.Delete - 64)) | (1 << (ECMAScriptParser.Try - 64)) | (1 << (ECMAScriptParser.Ident - 64)) | (1 << (ECMAScriptParser.StringLiteral - 64)))) != 0):
                self.state = 307 
                self.statementList()


        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class LabelledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.LabelledStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def statement(self):
            return self.getTypedRuleContext(ECMAScriptParser.StatementContext,0)


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
            self.state = 310 
            self.identifier()
            self.state = 311
            self.match(ECMAScriptParser.T__7)
            self.state = 312 
            self.statement()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class ThrowStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ThrowStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Throw(self):
            return self.getToken(ECMAScriptParser.Throw, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


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
            self.state = 314
            self.match(ECMAScriptParser.Throw)
            self.state = 315 
            self.expressionSequence()
            self.state = 316 
            self.eos()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class TryStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.TryStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(ECMAScriptParser.Try, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


        def catchProduction(self):
            return self.getTypedRuleContext(ECMAScriptParser.CatchProductionContext,0)


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
            self.state = 331
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(ECMAScriptParser.Try)
                self.state = 319 
                self.block()
                self.state = 320 
                self.catchProduction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(ECMAScriptParser.Try)
                self.state = 323 
                self.block()
                self.state = 324 
                self.finallyProduction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.match(ECMAScriptParser.Try)
                self.state = 327 
                self.block()
                self.state = 328 
                self.catchProduction()
                self.state = 329 
                self.finallyProduction()
                pass


        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class CatchProductionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.CatchProductionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(ECMAScriptParser.Catch, 0)

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


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
            self.state = 333
            self.match(ECMAScriptParser.Catch)
            self.state = 334
            self.match(ECMAScriptParser.T__5)
            self.state = 335 
            self.identifier()
            self.state = 336
            self.match(ECMAScriptParser.T__6)
            self.state = 337 
            self.block()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class FinallyProductionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FinallyProductionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Finally(self):
            return self.getToken(ECMAScriptParser.Finally, 0)

        def block(self):
            return self.getTypedRuleContext(ECMAScriptParser.BlockContext,0)


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
            self.state = 339
            self.match(ECMAScriptParser.Finally)
            self.state = 340 
            self.block()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class DebuggerStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.DebuggerStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Debugger(self):
            return self.getToken(ECMAScriptParser.Debugger, 0)

        def eos(self):
            return self.getTypedRuleContext(ECMAScriptParser.EosContext,0)


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
            self.state = 342
            self.match(ECMAScriptParser.Debugger)
            self.state = 343 
            self.eos()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FunctionDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.FormalParameterListContext,0)


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
            self.state = 345
            self.match(ECMAScriptParser.Function)
            self.state = 346 
            self.identifier()
            self.state = 347
            self.match(ECMAScriptParser.T__5)
            self.state = 349
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.Ident:
                self.state = 348 
                self.formalParameterList()


            self.state = 351
            self.match(ECMAScriptParser.T__6)
            self.state = 352
            self.match(ECMAScriptParser.T__0)
            self.state = 353 
            self.functionBody()
            self.state = 354
            self.match(ECMAScriptParser.T__1)
        except RecognitionException as re:
            pass
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
            self.state = 356 
            self.identifier()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.T__2:
                self.state = 357
                self.match(ECMAScriptParser.T__2)
                self.state = 358 
                self.identifier()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class FunctionExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FunctionExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.FormalParameterListContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


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
            self.state = 379
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(ECMAScriptParser.Function)
                self.state = 365
                self.match(ECMAScriptParser.T__5)
                self.state = 366 
                self.formalParameterList()
                self.state = 367
                self.match(ECMAScriptParser.T__6)
                self.state = 368
                self.match(ECMAScriptParser.T__0)
                self.state = 369 
                self.functionBody()
                self.state = 370
                self.match(ECMAScriptParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(ECMAScriptParser.Function)
                self.state = 373
                self.match(ECMAScriptParser.T__5)
                self.state = 374
                self.match(ECMAScriptParser.T__6)
                self.state = 375
                self.match(ECMAScriptParser.T__0)
                self.state = 376 
                self.functionBody()
                self.state = 377
                self.match(ECMAScriptParser.T__1)
                pass


        except RecognitionException as re:
            pass
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
            self.state = 382
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__4) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Break) | (1 << ECMAScriptParser.Do) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ECMAScriptParser.Var - 64)) | (1 << (ECMAScriptParser.Return - 64)) | (1 << (ECMAScriptParser.Void - 64)) | (1 << (ECMAScriptParser.Continue - 64)) | (1 << (ECMAScriptParser.For - 64)) | (1 << (ECMAScriptParser.Switch - 64)) | (1 << (ECMAScriptParser.While - 64)) | (1 << (ECMAScriptParser.Debugger - 64)) | (1 << (ECMAScriptParser.Function - 64)) | (1 << (ECMAScriptParser.This - 64)) | (1 << (ECMAScriptParser.With - 64)) | (1 << (ECMAScriptParser.If - 64)) | (1 << (ECMAScriptParser.Throw - 64)) | (1 << (ECMAScriptParser.Delete - 64)) | (1 << (ECMAScriptParser.Try - 64)) | (1 << (ECMAScriptParser.Ident - 64)) | (1 << (ECMAScriptParser.StringLiteral - 64)))) != 0):
                self.state = 381 
                self.sourceElements()


        except RecognitionException as re:
            pass
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
            self.state = 384
            self.match(ECMAScriptParser.T__8)
            self.state = 386
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 385 
                self.elementList()


            self.state = 389
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 388
                self.match(ECMAScriptParser.T__2)


            self.state = 392
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.T__2:
                self.state = 391 
                self.elision()


            self.state = 394
            self.match(ECMAScriptParser.T__9)
        except RecognitionException as re:
            pass
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
            self.state = 397
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.T__2:
                self.state = 396 
                self.elision()


            self.state = 399 
            self.singleExpression(0)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 400
                    self.match(ECMAScriptParser.T__2)
                    self.state = 402
                    _la = self._input.LA(1)
                    if _la==ECMAScriptParser.T__2:
                        self.state = 401 
                        self.elision()


                    self.state = 404 
                    self.singleExpression(0) 
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            pass
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
            self.state = 411 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 410
                self.match(ECMAScriptParser.T__2)
                self.state = 413 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECMAScriptParser.T__2):
                    break

        except RecognitionException as re:
            pass
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
            self.state = 415
            self.match(ECMAScriptParser.T__0)
            self.state = 417
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 416 
                self.propertyNameAndValueList()


            self.state = 420
            _la = self._input.LA(1)
            if _la==ECMAScriptParser.T__2:
                self.state = 419
                self.match(ECMAScriptParser.T__2)


            self.state = 422
            self.match(ECMAScriptParser.T__1)
        except RecognitionException as re:
            pass
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
            self.state = 424 
            self.propertyAssignment()
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 425
                    self.match(ECMAScriptParser.T__2)
                    self.state = 426 
                    self.propertyAssignment() 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            pass
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

        def getter(self):
            return self.getTypedRuleContext(ECMAScriptParser.GetterContext,0)

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

        def propertyName(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertyNameContext,0)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


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

        def setter(self):
            return self.getTypedRuleContext(ECMAScriptParser.SetterContext,0)

        def propertySetParameterList(self):
            return self.getTypedRuleContext(ECMAScriptParser.PropertySetParameterListContext,0)

        def functionBody(self):
            return self.getTypedRuleContext(ECMAScriptParser.FunctionBodyContext,0)


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
            self.state = 451
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = ECMAScriptParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 432 
                self.propertyName()
                self.state = 433
                self.match(ECMAScriptParser.T__7)
                self.state = 434 
                self.singleExpression(0)
                pass

            elif la_ == 2:
                localctx = ECMAScriptParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 436 
                self.getter()
                self.state = 437
                self.match(ECMAScriptParser.T__5)
                self.state = 438
                self.match(ECMAScriptParser.T__6)
                self.state = 439
                self.match(ECMAScriptParser.T__0)
                self.state = 440 
                self.functionBody()
                self.state = 441
                self.match(ECMAScriptParser.T__1)
                pass

            elif la_ == 3:
                localctx = ECMAScriptParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 443 
                self.setter()
                self.state = 444
                self.match(ECMAScriptParser.T__5)
                self.state = 445 
                self.propertySetParameterList()
                self.state = 446
                self.match(ECMAScriptParser.T__6)
                self.state = 447
                self.match(ECMAScriptParser.T__0)
                self.state = 448 
                self.functionBody()
                self.state = 449
                self.match(ECMAScriptParser.T__1)
                pass


        except RecognitionException as re:
            pass
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
            self.state = 456
            token = self._input.LA(1)
            if token in [ECMAScriptParser.T__48, ECMAScriptParser.T__49, ECMAScriptParser.T__50, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try, ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield, ECMAScriptParser.Ident]:
                self.enterOuterAlt(localctx, 1)
                self.state = 453 
                self.identifierName()

            elif token in [ECMAScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.match(ECMAScriptParser.StringLiteral)

            elif token in [ECMAScriptParser.DecimalLiteral, ECMAScriptParser.HexIntegerLiteral, ECMAScriptParser.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 455 
                self.numericLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            pass
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
            self.state = 458 
            self.identifier()
        except RecognitionException as re:
            pass
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
            self.state = 460
            self.match(ECMAScriptParser.T__5)
            self.state = 462
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__0) | (1 << ECMAScriptParser.T__5) | (1 << ECMAScriptParser.T__8) | (1 << ECMAScriptParser.T__11) | (1 << ECMAScriptParser.T__12) | (1 << ECMAScriptParser.T__13) | (1 << ECMAScriptParser.T__14) | (1 << ECMAScriptParser.T__15) | (1 << ECMAScriptParser.T__16) | (1 << ECMAScriptParser.T__48) | (1 << ECMAScriptParser.T__49) | (1 << ECMAScriptParser.T__50) | (1 << ECMAScriptParser.RegularExpressionLiteral) | (1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral) | (1 << ECMAScriptParser.Typeof) | (1 << ECMAScriptParser.New))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (ECMAScriptParser.Void - 68)) | (1 << (ECMAScriptParser.Function - 68)) | (1 << (ECMAScriptParser.This - 68)) | (1 << (ECMAScriptParser.Delete - 68)) | (1 << (ECMAScriptParser.Ident - 68)) | (1 << (ECMAScriptParser.StringLiteral - 68)))) != 0):
                self.state = 461 
                self.argumentList()


            self.state = 464
            self.match(ECMAScriptParser.T__6)
        except RecognitionException as re:
            pass
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
            self.state = 466 
            self.singleExpression(0)
            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ECMAScriptParser.T__2:
                self.state = 467
                self.match(ECMAScriptParser.T__2)
                self.state = 468 
                self.singleExpression(0)
                self.state = 473
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            pass
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
            self.state = 474 
            self.singleExpression(0)
            self.state = 479
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 475
                    self.match(ECMAScriptParser.T__2)
                    self.state = 476 
                    self.singleExpression(0) 
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            pass
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

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitAssignmentExpression(self)


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


    class InstanceofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.InstanceofExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ECMAScriptParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,i)

        def Instanceof(self):
            return self.getToken(ECMAScriptParser.Instanceof, 0)

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterInstanceofExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitInstanceofExpression(self)


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

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def identifierName(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierNameContext,0)


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

        def Delete(self):
            return self.getToken(ECMAScriptParser.Delete, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


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


    class VoidExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.VoidExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Void(self):
            return self.getToken(ECMAScriptParser.Void, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterVoidExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitVoidExpression(self)


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

        def Typeof(self):
            return self.getToken(ECMAScriptParser.Typeof, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)


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

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def assignmentOperator(self):
            return self.getTypedRuleContext(ECMAScriptParser.AssignmentOperatorContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


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


    class MemberIndexExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx): # actually a ECMAScriptParser.SingleExpressionContext)
            super(ECMAScriptParser.MemberIndexExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(ECMAScriptParser.SingleExpressionContext,0)

        def expressionSequence(self):
            return self.getTypedRuleContext(ECMAScriptParser.ExpressionSequenceContext,0)


        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterMemberIndexExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitMemberIndexExpression(self)


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
            self.state = 516
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Delete]:
                localctx = ECMAScriptParser.DeleteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 483
                self.match(ECMAScriptParser.Delete)
                self.state = 484 
                self.singleExpression(41)

            elif token in [ECMAScriptParser.Void]:
                localctx = ECMAScriptParser.VoidExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 485
                self.match(ECMAScriptParser.Void)
                self.state = 486 
                self.singleExpression(40)

            elif token in [ECMAScriptParser.Typeof]:
                localctx = ECMAScriptParser.TypeofExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 487
                self.match(ECMAScriptParser.Typeof)
                self.state = 488 
                self.singleExpression(39)

            elif token in [ECMAScriptParser.T__11]:
                localctx = ECMAScriptParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 489
                self.match(ECMAScriptParser.T__11)
                self.state = 490 
                self.singleExpression(38)

            elif token in [ECMAScriptParser.T__12]:
                localctx = ECMAScriptParser.PreDecreaseExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 491
                self.match(ECMAScriptParser.T__12)
                self.state = 492 
                self.singleExpression(37)

            elif token in [ECMAScriptParser.T__13]:
                localctx = ECMAScriptParser.UnaryPlusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 493
                self.match(ECMAScriptParser.T__13)
                self.state = 494 
                self.singleExpression(36)

            elif token in [ECMAScriptParser.T__14]:
                localctx = ECMAScriptParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 495
                self.match(ECMAScriptParser.T__14)
                self.state = 496 
                self.singleExpression(35)

            elif token in [ECMAScriptParser.T__15]:
                localctx = ECMAScriptParser.BitNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 497
                self.match(ECMAScriptParser.T__15)
                self.state = 498 
                self.singleExpression(34)

            elif token in [ECMAScriptParser.T__16]:
                localctx = ECMAScriptParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 499
                self.match(ECMAScriptParser.T__16)
                self.state = 500 
                self.singleExpression(33)

            elif token in [ECMAScriptParser.Function]:
                localctx = ECMAScriptParser.FnExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 501 
                self.functionExpression()

            elif token in [ECMAScriptParser.New]:
                localctx = ECMAScriptParser.NewExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 502
                self.match(ECMAScriptParser.New)
                self.state = 503 
                self.singleExpression(0)
                self.state = 505
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 504 
                    self.arguments()



            elif token in [ECMAScriptParser.This]:
                localctx = ECMAScriptParser.ThisExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 507
                self.match(ECMAScriptParser.This)

            elif token in [ECMAScriptParser.Ident]:
                localctx = ECMAScriptParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 508 
                self.identifier()

            elif token in [ECMAScriptParser.T__48, ECMAScriptParser.T__49, ECMAScriptParser.T__50, ECMAScriptParser.RegularExpressionLiteral, ECMAScriptParser.DecimalLiteral, ECMAScriptParser.HexIntegerLiteral, ECMAScriptParser.OctalIntegerLiteral, ECMAScriptParser.StringLiteral]:
                localctx = ECMAScriptParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 509 
                self.literal()

            elif token in [ECMAScriptParser.T__8]:
                localctx = ECMAScriptParser.ArrayLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 510 
                self.arrayLiteral()

            elif token in [ECMAScriptParser.T__0]:
                localctx = ECMAScriptParser.ObjectLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 511 
                self.objectLiteral()

            elif token in [ECMAScriptParser.T__5]:
                localctx = ECMAScriptParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 512
                self.match(ECMAScriptParser.T__5)
                self.state = 513 
                self.expressionSequence()
                self.state = 514
                self.match(ECMAScriptParser.T__6)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 618
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 616
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = ECMAScriptParser.MultiplyExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 518
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 519
                        self.match(ECMAScriptParser.T__17)
                        self.state = 520 
                        self.singleExpression(33)
                        pass

                    elif la_ == 2:
                        localctx = ECMAScriptParser.DivideExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 521
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 522
                        self.match(ECMAScriptParser.T__18)
                        self.state = 523 
                        self.singleExpression(32)
                        pass

                    elif la_ == 3:
                        localctx = ECMAScriptParser.ModulusExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 524
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 525
                        self.match(ECMAScriptParser.T__19)
                        self.state = 526 
                        self.singleExpression(31)
                        pass

                    elif la_ == 4:
                        localctx = ECMAScriptParser.AddExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 527
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 528
                        self.match(ECMAScriptParser.T__13)
                        self.state = 529 
                        self.singleExpression(30)
                        pass

                    elif la_ == 5:
                        localctx = ECMAScriptParser.SubtractExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 530
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 531
                        self.match(ECMAScriptParser.T__14)
                        self.state = 532 
                        self.singleExpression(29)
                        pass

                    elif la_ == 6:
                        localctx = ECMAScriptParser.LeftShiftArithmeticExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 533
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 534
                        self.match(ECMAScriptParser.T__20)
                        self.state = 535 
                        self.singleExpression(28)
                        pass

                    elif la_ == 7:
                        localctx = ECMAScriptParser.RightShiftArithmeticExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 536
                        if not self.precpred(self._ctx, 26):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 26)")
                        self.state = 537
                        self.match(ECMAScriptParser.T__21)
                        self.state = 538 
                        self.singleExpression(27)
                        pass

                    elif la_ == 8:
                        localctx = ECMAScriptParser.RightShiftLogicalExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 539
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 540
                        self.match(ECMAScriptParser.T__22)
                        self.state = 541 
                        self.singleExpression(26)
                        pass

                    elif la_ == 9:
                        localctx = ECMAScriptParser.LessThanExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 542
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 543
                        self.match(ECMAScriptParser.T__23)
                        self.state = 544 
                        self.singleExpression(25)
                        pass

                    elif la_ == 10:
                        localctx = ECMAScriptParser.GreaterThanExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 545
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 546
                        self.match(ECMAScriptParser.T__24)
                        self.state = 547 
                        self.singleExpression(24)
                        pass

                    elif la_ == 11:
                        localctx = ECMAScriptParser.LessThanEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 548
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 549
                        self.match(ECMAScriptParser.T__25)
                        self.state = 550 
                        self.singleExpression(23)
                        pass

                    elif la_ == 12:
                        localctx = ECMAScriptParser.GreaterThanEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 551
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 552
                        self.match(ECMAScriptParser.T__26)
                        self.state = 553 
                        self.singleExpression(22)
                        pass

                    elif la_ == 13:
                        localctx = ECMAScriptParser.InstanceofExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 554
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 555
                        self.match(ECMAScriptParser.Instanceof)
                        self.state = 556 
                        self.singleExpression(21)
                        pass

                    elif la_ == 14:
                        localctx = ECMAScriptParser.InExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 557
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 558
                        self.match(ECMAScriptParser.In)
                        self.state = 559 
                        self.singleExpression(20)
                        pass

                    elif la_ == 15:
                        localctx = ECMAScriptParser.EqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 560
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 561
                        self.match(ECMAScriptParser.T__27)
                        self.state = 562 
                        self.singleExpression(19)
                        pass

                    elif la_ == 16:
                        localctx = ECMAScriptParser.NotEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 563
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 564
                        self.match(ECMAScriptParser.T__28)
                        self.state = 565 
                        self.singleExpression(18)
                        pass

                    elif la_ == 17:
                        localctx = ECMAScriptParser.IdentityEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 566
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 567
                        self.match(ECMAScriptParser.T__29)
                        self.state = 568 
                        self.singleExpression(17)
                        pass

                    elif la_ == 18:
                        localctx = ECMAScriptParser.IdentityNotEqualsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 569
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 570
                        self.match(ECMAScriptParser.T__30)
                        self.state = 571 
                        self.singleExpression(16)
                        pass

                    elif la_ == 19:
                        localctx = ECMAScriptParser.BitAndExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 572
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 573
                        self.match(ECMAScriptParser.T__31)
                        self.state = 574 
                        self.singleExpression(15)
                        pass

                    elif la_ == 20:
                        localctx = ECMAScriptParser.BitXOrExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 575
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 576
                        self.match(ECMAScriptParser.T__32)
                        self.state = 577 
                        self.singleExpression(14)
                        pass

                    elif la_ == 21:
                        localctx = ECMAScriptParser.BitOrExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 578
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 579
                        self.match(ECMAScriptParser.T__33)
                        self.state = 580 
                        self.singleExpression(13)
                        pass

                    elif la_ == 22:
                        localctx = ECMAScriptParser.AndExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 581
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 582
                        self.match(ECMAScriptParser.T__34)
                        self.state = 583 
                        self.singleExpression(12)
                        pass

                    elif la_ == 23:
                        localctx = ECMAScriptParser.OrExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 584
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 585
                        self.match(ECMAScriptParser.T__35)
                        self.state = 586 
                        self.singleExpression(11)
                        pass

                    elif la_ == 24:
                        localctx = ECMAScriptParser.TernaryExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 587
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 588
                        self.match(ECMAScriptParser.T__36)
                        self.state = 589 
                        self.singleExpression(0)
                        self.state = 590
                        self.match(ECMAScriptParser.T__7)
                        self.state = 591 
                        self.singleExpression(10)
                        pass

                    elif la_ == 25:
                        localctx = ECMAScriptParser.MemberIndexExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 593
                        if not self.precpred(self._ctx, 47):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 47)")
                        self.state = 594
                        self.match(ECMAScriptParser.T__8)
                        self.state = 595 
                        self.expressionSequence()
                        self.state = 596
                        self.match(ECMAScriptParser.T__9)
                        pass

                    elif la_ == 26:
                        localctx = ECMAScriptParser.MemberDotExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 598
                        if not self.precpred(self._ctx, 46):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 46)")
                        self.state = 599
                        self.match(ECMAScriptParser.T__10)
                        self.state = 600 
                        self.identifierName()
                        pass

                    elif la_ == 27:
                        localctx = ECMAScriptParser.ArgumentsExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 601
                        if not self.precpred(self._ctx, 45):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 45)")
                        self.state = 602 
                        self.arguments()
                        pass

                    elif la_ == 28:
                        localctx = ECMAScriptParser.PostIncrementExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 603
                        if not self.precpred(self._ctx, 43):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 43)")
                        self.state = 604
                        if not  not self.here(self.LineTerminator):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, " not self.here(self.LineTerminator)")
                        self.state = 605
                        self.match(ECMAScriptParser.T__11)
                        pass

                    elif la_ == 29:
                        localctx = ECMAScriptParser.PostDecreaseExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 606
                        if not self.precpred(self._ctx, 42):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 42)")
                        self.state = 607
                        if not  not self.here(self.LineTerminator):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, " not self.here(self.LineTerminator)")
                        self.state = 608
                        self.match(ECMAScriptParser.T__12)
                        pass

                    elif la_ == 30:
                        localctx = ECMAScriptParser.AssignmentExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 609
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 610
                        self.match(ECMAScriptParser.T__3)
                        self.state = 611 
                        self.expressionSequence()
                        pass

                    elif la_ == 31:
                        localctx = ECMAScriptParser.AssignmentOperatorExpressionContext(self, ECMAScriptParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 612
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 613 
                        self.assignmentOperator()
                        self.state = 614 
                        self.expressionSequence()
                        pass

             
                self.state = 620
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            pass
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
            self.state = 621
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.T__37) | (1 << ECMAScriptParser.T__38) | (1 << ECMAScriptParser.T__39) | (1 << ECMAScriptParser.T__40) | (1 << ECMAScriptParser.T__41) | (1 << ECMAScriptParser.T__42) | (1 << ECMAScriptParser.T__43) | (1 << ECMAScriptParser.T__44) | (1 << ECMAScriptParser.T__45) | (1 << ECMAScriptParser.T__46) | (1 << ECMAScriptParser.T__47))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.LiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nullLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NullLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.BooleanLiteralContext,0)


        def StringLiteral(self):
            return self.getToken(ECMAScriptParser.StringLiteral, 0)

        def RegularExpressionLiteral(self):
            return self.getToken(ECMAScriptParser.RegularExpressionLiteral, 0)

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
            self.state = 628
            token = self._input.LA(1)
            if token in [ECMAScriptParser.T__48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 623 
                self.nullLiteral()

            elif token in [ECMAScriptParser.T__49, ECMAScriptParser.T__50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 624 
                self.booleanLiteral()

            elif token in [ECMAScriptParser.StringLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 625
                self.match(ECMAScriptParser.StringLiteral)

            elif token in [ECMAScriptParser.RegularExpressionLiteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 626
                self.match(ECMAScriptParser.RegularExpressionLiteral)

            elif token in [ECMAScriptParser.DecimalLiteral, ECMAScriptParser.HexIntegerLiteral, ECMAScriptParser.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 5)
                self.state = 627 
                self.numericLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.NumericLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(ECMAScriptParser.DecimalLiteral, 0)

        def HexIntegerLiteral(self):
            return self.getToken(ECMAScriptParser.HexIntegerLiteral, 0)

        def OctalIntegerLiteral(self):
            return self.getToken(ECMAScriptParser.OctalIntegerLiteral, 0)

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
            self.state = 630
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECMAScriptParser.DecimalLiteral) | (1 << ECMAScriptParser.HexIntegerLiteral) | (1 << ECMAScriptParser.OctalIntegerLiteral))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class IdentifierNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.IdentifierNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def reservedWord(self):
            return self.getTypedRuleContext(ECMAScriptParser.ReservedWordContext,0)


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
            self.state = 634
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Ident]:
                self.enterOuterAlt(localctx, 1)
                self.state = 632 
                self.identifier()

            elif token in [ECMAScriptParser.T__48, ECMAScriptParser.T__49, ECMAScriptParser.T__50, ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try, ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 633 
                self.reservedWord()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class ReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.ReservedWordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(ECMAScriptParser.KeywordContext,0)


        def futureReservedWord(self):
            return self.getTypedRuleContext(ECMAScriptParser.FutureReservedWordContext,0)


        def nullLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.NullLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(ECMAScriptParser.BooleanLiteralContext,0)


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
            self.state = 640
            token = self._input.LA(1)
            if token in [ECMAScriptParser.Break, ECMAScriptParser.Do, ECMAScriptParser.Instanceof, ECMAScriptParser.Typeof, ECMAScriptParser.Case, ECMAScriptParser.Else, ECMAScriptParser.New, ECMAScriptParser.Var, ECMAScriptParser.Catch, ECMAScriptParser.Finally, ECMAScriptParser.Return, ECMAScriptParser.Void, ECMAScriptParser.Continue, ECMAScriptParser.For, ECMAScriptParser.Switch, ECMAScriptParser.While, ECMAScriptParser.Debugger, ECMAScriptParser.Function, ECMAScriptParser.This, ECMAScriptParser.With, ECMAScriptParser.Default, ECMAScriptParser.If, ECMAScriptParser.Throw, ECMAScriptParser.Delete, ECMAScriptParser.In, ECMAScriptParser.Try]:
                self.enterOuterAlt(localctx, 1)
                self.state = 636 
                self.keyword()

            elif token in [ECMAScriptParser.Class, ECMAScriptParser.Enum, ECMAScriptParser.Extends, ECMAScriptParser.Super, ECMAScriptParser.Const, ECMAScriptParser.Export, ECMAScriptParser.Import, ECMAScriptParser.Implements, ECMAScriptParser.Let, ECMAScriptParser.Private, ECMAScriptParser.Public, ECMAScriptParser.Interface, ECMAScriptParser.Package, ECMAScriptParser.Protected, ECMAScriptParser.Static, ECMAScriptParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 637 
                self.futureReservedWord()

            elif token in [ECMAScriptParser.T__48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 638 
                self.nullLiteral()

            elif token in [ECMAScriptParser.T__49, ECMAScriptParser.T__50]:
                self.enterOuterAlt(localctx, 4)
                self.state = 639 
                self.booleanLiteral()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.KeywordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(ECMAScriptParser.Break, 0)

        def Do(self):
            return self.getToken(ECMAScriptParser.Do, 0)

        def Instanceof(self):
            return self.getToken(ECMAScriptParser.Instanceof, 0)

        def Typeof(self):
            return self.getToken(ECMAScriptParser.Typeof, 0)

        def Case(self):
            return self.getToken(ECMAScriptParser.Case, 0)

        def Else(self):
            return self.getToken(ECMAScriptParser.Else, 0)

        def New(self):
            return self.getToken(ECMAScriptParser.New, 0)

        def Var(self):
            return self.getToken(ECMAScriptParser.Var, 0)

        def Catch(self):
            return self.getToken(ECMAScriptParser.Catch, 0)

        def Finally(self):
            return self.getToken(ECMAScriptParser.Finally, 0)

        def Return(self):
            return self.getToken(ECMAScriptParser.Return, 0)

        def Void(self):
            return self.getToken(ECMAScriptParser.Void, 0)

        def Continue(self):
            return self.getToken(ECMAScriptParser.Continue, 0)

        def For(self):
            return self.getToken(ECMAScriptParser.For, 0)

        def Switch(self):
            return self.getToken(ECMAScriptParser.Switch, 0)

        def While(self):
            return self.getToken(ECMAScriptParser.While, 0)

        def Debugger(self):
            return self.getToken(ECMAScriptParser.Debugger, 0)

        def Function(self):
            return self.getToken(ECMAScriptParser.Function, 0)

        def This(self):
            return self.getToken(ECMAScriptParser.This, 0)

        def With(self):
            return self.getToken(ECMAScriptParser.With, 0)

        def Default(self):
            return self.getToken(ECMAScriptParser.Default, 0)

        def If(self):
            return self.getToken(ECMAScriptParser.If, 0)

        def Throw(self):
            return self.getToken(ECMAScriptParser.Throw, 0)

        def Delete(self):
            return self.getToken(ECMAScriptParser.Delete, 0)

        def In(self):
            return self.getToken(ECMAScriptParser.In, 0)

        def Try(self):
            return self.getToken(ECMAScriptParser.Try, 0)

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
            self.state = 642
            _la = self._input.LA(1)
            if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (ECMAScriptParser.Break - 57)) | (1 << (ECMAScriptParser.Do - 57)) | (1 << (ECMAScriptParser.Instanceof - 57)) | (1 << (ECMAScriptParser.Typeof - 57)) | (1 << (ECMAScriptParser.Case - 57)) | (1 << (ECMAScriptParser.Else - 57)) | (1 << (ECMAScriptParser.New - 57)) | (1 << (ECMAScriptParser.Var - 57)) | (1 << (ECMAScriptParser.Catch - 57)) | (1 << (ECMAScriptParser.Finally - 57)) | (1 << (ECMAScriptParser.Return - 57)) | (1 << (ECMAScriptParser.Void - 57)) | (1 << (ECMAScriptParser.Continue - 57)) | (1 << (ECMAScriptParser.For - 57)) | (1 << (ECMAScriptParser.Switch - 57)) | (1 << (ECMAScriptParser.While - 57)) | (1 << (ECMAScriptParser.Debugger - 57)) | (1 << (ECMAScriptParser.Function - 57)) | (1 << (ECMAScriptParser.This - 57)) | (1 << (ECMAScriptParser.With - 57)) | (1 << (ECMAScriptParser.Default - 57)) | (1 << (ECMAScriptParser.If - 57)) | (1 << (ECMAScriptParser.Throw - 57)) | (1 << (ECMAScriptParser.Delete - 57)) | (1 << (ECMAScriptParser.In - 57)) | (1 << (ECMAScriptParser.Try - 57)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class FutureReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.FutureReservedWordContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(ECMAScriptParser.Class, 0)

        def Enum(self):
            return self.getToken(ECMAScriptParser.Enum, 0)

        def Extends(self):
            return self.getToken(ECMAScriptParser.Extends, 0)

        def Super(self):
            return self.getToken(ECMAScriptParser.Super, 0)

        def Const(self):
            return self.getToken(ECMAScriptParser.Const, 0)

        def Export(self):
            return self.getToken(ECMAScriptParser.Export, 0)

        def Import(self):
            return self.getToken(ECMAScriptParser.Import, 0)

        def Implements(self):
            return self.getToken(ECMAScriptParser.Implements, 0)

        def Let(self):
            return self.getToken(ECMAScriptParser.Let, 0)

        def Private(self):
            return self.getToken(ECMAScriptParser.Private, 0)

        def Public(self):
            return self.getToken(ECMAScriptParser.Public, 0)

        def Interface(self):
            return self.getToken(ECMAScriptParser.Interface, 0)

        def Package(self):
            return self.getToken(ECMAScriptParser.Package, 0)

        def Protected(self):
            return self.getToken(ECMAScriptParser.Protected, 0)

        def Static(self):
            return self.getToken(ECMAScriptParser.Static, 0)

        def Yield(self):
            return self.getToken(ECMAScriptParser.Yield, 0)

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
            self.state = 644
            _la = self._input.LA(1)
            if not(((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & ((1 << (ECMAScriptParser.Class - 83)) | (1 << (ECMAScriptParser.Enum - 83)) | (1 << (ECMAScriptParser.Extends - 83)) | (1 << (ECMAScriptParser.Super - 83)) | (1 << (ECMAScriptParser.Const - 83)) | (1 << (ECMAScriptParser.Export - 83)) | (1 << (ECMAScriptParser.Import - 83)) | (1 << (ECMAScriptParser.Implements - 83)) | (1 << (ECMAScriptParser.Let - 83)) | (1 << (ECMAScriptParser.Private - 83)) | (1 << (ECMAScriptParser.Public - 83)) | (1 << (ECMAScriptParser.Interface - 83)) | (1 << (ECMAScriptParser.Package - 83)) | (1 << (ECMAScriptParser.Protected - 83)) | (1 << (ECMAScriptParser.Static - 83)) | (1 << (ECMAScriptParser.Yield - 83)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            pass
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
        self.enterRule(localctx, 104, self.RULE_nullLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.match(ECMAScriptParser.T__48)
        except RecognitionException as re:
            pass
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
        self.enterRule(localctx, 106, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            _la = self._input.LA(1)
            if not(_la==ECMAScriptParser.T__49 or _la==ECMAScriptParser.T__50):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            pass
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
        self.enterRule(localctx, 108, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            self.match(ECMAScriptParser.Ident)
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class GetterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.GetterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_getter

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterGetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitGetter(self)




    def getter(self):

        localctx = ECMAScriptParser.GetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_getter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            if not self._input.LT(1)._text.startsWith("get"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1)._text.startsWith(\"get\")")
            self.state = 653 
            self.identifier()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class SetterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.SetterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ECMAScriptParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ECMAScriptParser.RULE_setter

        def enterRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.enterSetter(self)

        def exitRule(self, listener):
            if isinstance( listener, ECMAScriptListener ):
                listener.exitSetter(self)




    def setter(self):

        localctx = ECMAScriptParser.SetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_setter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 655
            if not self._input.LT(1)._text.startsWith("set"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1)._text.startsWith(\"set\")")
            self.state = 656 
            self.identifier()
        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx

    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ECMAScriptParser.EosContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ECMAScriptParser.EOF, 0)

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
        self.enterRule(localctx, 114, self.RULE_eos)
        try:
            self.state = 662
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 658
                self.match(ECMAScriptParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 659
                self.match(ECMAScriptParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 660
                if not self.lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 661
                if not self._input.LT(1).type == '}':
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self._input.LT(1).type == '}'")
                pass


        except RecognitionException as re:
            pass
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[44] = self.singleExpression_sempred
        self._predicates[55] = self.getter_sempred
        self._predicates[56] = self.setter_sempred
        self._predicates[57] = self.eos_sempred
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
         

            if predIndex == 16:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 47)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 46)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 45)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 43)
         

            if predIndex == 28:
                return  not self.here(self.LineTerminator)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 42)
         

            if predIndex == 30:
                return  not self.here(self.LineTerminator)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 32:
                return self.precpred(self._ctx, 7)
         

    def getter_sempred(self, localctx, predIndex):
            if predIndex == 33:
                return self._input.LT(1)._text.startsWith("get")
         

    def setter_sempred(self, localctx, predIndex):
            if predIndex == 34:
                return self._input.LT(1)._text.startsWith("set")
         

    def eos_sempred(self, localctx, predIndex):
            if predIndex == 35:
                return self.lineTerminatorAhead()
         

            if predIndex == 36:
                return self._input.LT(1).type == '}'
         



