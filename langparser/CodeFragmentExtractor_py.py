#!/usr/bin/env python
""" generated source for module CodeFragmentExtractor """
from antlr4.tree import Tree
from antlr4 import *
from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptListener import ECMAScriptListener
from time import time

identifiers=[]
IR=[]
global_Objects=  ["Infinity", "NaN", "undefined", "null ", "eval", "uneval", "isFinite", "isNaN", "parseFloat", "parseInt", "decodeURI", "decodeURIComponent", "encodeURI", "encodeURIComponent", "escape", "unescape", "Object", "Function", "Boolean", "Symbol", "Error", "EvalError", "InternalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", "URIError", "Number", "Math", "Date", "String", "RegExp", "Array", "Int8Array", "Uint8Array", "Uint8ClampedArray", "Int16Array", "Uint16Array", "Int32Array", "Uint32Array", "Float32Array", "Float64Array", "Map", "Set", "WeakMap", "WeakSet", "Promise", "Generator", "GeneratorFunction", "ArrayBuffer", "DataView", "JSON", "Reflect", "Proxy", "Iterator", "ParallelArray", "StopIteration"]
hm={}
rules=ECMAScriptParser.ruleNames
    
class ECMAScriptBaseListener1(ECMAScriptListener):
        def enterEveryRule(self, ctx):
            pass
        def exitEveryRule(self, ctx):
            pass

        def enterIdentifier(self,ctx) :
            pass
        def visitTerminal(self,ctx) :
            pass

class ECMAScriptBaseListener2(ECMAScriptListener):
        def __init__(self,tokens):
            self.tokens=tokens
        def enterEveryRule(self, ctx):
            if ctx is not None:
                stmt = [];
                start = ctx.start.tokenIndex;
                stop = ctx.stop.tokenIndex;
                i = start;
                while( i <= stop):
                    tokenText=self.tokens.get(i).text
                    if self.tokens.get(i).type==98 and tokenText not in global_Objects:
                        tokenText = "_id_"+tokenText;
                    stmt.append(tokenText);
                    i+=1
                
                key=rules[ctx.getRuleIndex()];
                aL=None
                if (hm.has_key(key)):
                    aL = hm[key];
                else:
                    aL=[]
                aL.append(''.join(stmt));
                hm[key]=aL
            pass
        
def xmlEscapeText(t):
        """ generated source for method xmlEscapeText """
        sb=[]
        i = 0
        while i < len(t):
            c=t[i]
            if c=='<':
                sb.append("&lt;")
            elif c=='>':
                sb.append("&gt;")
            elif c=='\"':
                sb.append("&quot;")
            elif c=='&':
                sb.append("&amp;")
            elif c=='\'':
                sb.append("&apos;")
            else:
                sb.append(c)
            i += 1
        return ''.join(sb)


""" generated source for class CodeFragmentExtractor """
def XMLIRGenerator(fileStream):
    lexer = ECMAScriptLexer(fileStream)
    stream = CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    parser._listeners=[]
    tokens = parser.getTokenStream();
    listener=ECMAScriptBaseListener1()
    t=time()
    ParseTreeWalker.DEFAULT.walk(listener,parser.program())
    print time()-t
    return ''.join(IR), identifiers
    
def extractFrags(fileStream):
    lexer = ECMAScriptLexer(fileStream)
    stream = CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    parser._listeners=[]
    tokens = parser.getTokenStream();
    listener=ECMAScriptBaseListener2(tokens);
    
    ParseTreeWalker.DEFAULT.walk(listener,parser.program())
    return hm


if __name__=='__main__':
        """ generated source for method main """
        script = "/home/spandan/test.js"
        input = FileStream(script)
        hm1 = XMLIRGenerator(input)
        print hm1
        input = FileStream(script)
        hm1 = extractFrags(input)
        print hm1
