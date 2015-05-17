package langparser;
import java.io.FileInputStream;
import java.io.IOException;
import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.RuleContext;
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.antlr.v4.runtime.tree.ParseTree;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

public class CodeFragmentExtractor {
    
    public HashMap XMLIRGenerator(String script, boolean isPrg) throws IOException {
        
        final List<String> nonTermWithIdentifiers=  Arrays.asList("variableDeclaration","continueStatement","breakStatement","labelledStatement","catchProduction","functionDeclaration","formalParameterList","propertySetParameterList","getter","setter","primaryExpression");
        
        final List<String> global_Objects=  Arrays.asList("Infinity", "NaN", "undefined", "null ", "eval", "uneval", "isFinite", "isNaN", "parseFloat", "parseInt", "decodeURI", "decodeURIComponent", "encodeURI", "encodeURIComponent", "escape", "unescape", "Object", "Function", "Boolean", "Symbol", "Error", "EvalError", "InternalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", "URIError", "Number", "Math", "Date", "String", "RegExp", "Array", "Int8Array", "Uint8Array", "Uint8ClampedArray", "Int16Array", "Uint16Array", "Int32Array", "Uint32Array", "Float32Array", "Float64Array", "Map", "Set", "WeakMap", "WeakSet", "Promise", "Generator", "GeneratorFunction", "ArrayBuffer", "DataView", "JSON", "Reflect", "Proxy", "Iterator", "ParallelArray", "StopIteration");
        
        ECMAScriptParser parser = null;
        if (isPrg){
            parser = new Builder.Parser(script).build();
        }
        else{
            FileInputStream fis = new FileInputStream(script);
            parser = new Builder.Parser(new ANTLRInputStream(fis)).build();
            fis.close();
        }
        final TokenStream tokens = parser.getTokenStream();
        final String[] ruleNames = parser.ruleNames;
        final StringBuffer sb = new StringBuffer();
        final HashMap hm = new HashMap();
        final HashSet identifiers = new HashSet();
        final ArrayList nonTerminals = new ArrayList();
        ParseTreeWalker.DEFAULT.walk(new ECMAScriptBaseListener(){
            private boolean eosInd=false;
            
            @Override
            public void enterEveryRule(@NotNull ParserRuleContext ctx) {
                java.util.List<ParseTree> childs=ctx.children;
                boolean ind=false;
                if (childs!=null){
                    
                    if (childs.size()>1){
                            ind = true;
                    }
                    else 
                        if (childs.size()>0){
                            for (ParseTree p : childs){
                                if (p.getChildCount()==0){
                                    ind=true;
                                    break;
                                }
                            }
                        }
                    if (ind){
                        ind=false;
                        String Stmt = null;
                        Stmt = tokens.getText(ctx);
                        String key=ruleNames[ctx.getRuleIndex()];
                        
                        if(key.equals("eos")){
                            eosInd=false;
                        }
                        sb.append("<"+key+">");
                    }
                }
            }
            
            @Override
            public void exitEveryRule(@NotNull ParserRuleContext ctx) {
                if(ctx != null) {
                    java.util.List<ParseTree> childs=ctx.children;
                    boolean ind=false;
                    if (childs!=null){
                        if (childs.size()>1){
                            ind = true;
                        }
                        else 
                            if (childs.size()>0){
                                for (ParseTree p : childs){
                                    if (p.getChildCount()==0){
                                        ind=true;
                                        break;
                                    }
                                    
                                }
                            }
                        
                        if (ind){
                            ind=false;
                            String Stmt = null;
                            Stmt = tokens.getText(ctx);
                            String key=ruleNames[ctx.getRuleIndex()];
                            
                            if(key.equals("eos")){
                                eosInd=false;
                            }
                            sb.append("</"+key+">");
                        }
                    }
                }
            }
            
            @Override
            public void visitTerminal(@NotNull TerminalNode ctx) {
                if(ctx != null) {
                    try{
                        String token=ctx.getText();
                        if (!eosInd){
                            if(!token.equals("<EOF>"))
                            sb.append(xmlEscapeText(token)+" ");
                        }
                        else{
                            if (!token.trim().equals(";"))
                            sb.append(";");
                            
                        }
                    }
                    catch (Exception e){
                        System.out.println(e.getMessage());
                    }
                    
                }
            }
            
            @Override
            public void visitErrorNode(@NotNull ErrorNode ctx) {
                if(ctx != null) {
                }
            }
            @Override
            public void enterIdentifier(@NotNull ECMAScriptParser.IdentifierContext ctx) {
                if (ctx != null){
                    RuleContext parentCtx=ctx.parent;
                    String key = ruleNames[parentCtx.getRuleIndex()];
                    if(nonTermWithIdentifiers.contains(key)){
                      String id=ctx.getText();
                      if (!global_Objects.contains(id))
                        identifiers.add(id);  
                      //System.out.println(id);
                    }
                    
                }
            }
            @Override
            public void exitIdentifier(@NotNull ECMAScriptParser.IdentifierContext ctx) {
            }
            
        }, parser.program());
        hm.put("parsecode",sb.toString());
        hm.put("identifiers",new ArrayList(identifiers));
        return hm;
    }
    
    public static void main(String[] args) throws Exception {
        CodeFragmentExtractor c=new CodeFragmentExtractor();
        String script = "/home/spandan/test.js";
        HashMap hm=c.XMLIRGenerator(script,false);
        System.out.println(hm);
        hm=c.extractFrags(script,true);
        System.out.println(hm);
    }
    
    public HashMap<String,ArrayList> extractFrags(String script, boolean isFile) throws IOException {
        final List<String> global_Objects=  Arrays.asList("Infinity", "NaN", "undefined", "null ", "eval", "uneval", "isFinite", "isNaN", "parseFloat", "parseInt", "decodeURI", "decodeURIComponent", "encodeURI", "encodeURIComponent", "escape", "unescape", "Object", "Function", "Boolean", "Symbol", "Error", "EvalError", "InternalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", "URIError", "Number", "Math", "Date", "String", "RegExp", "Array", "Int8Array", "Uint8Array", "Uint8ClampedArray", "Int16Array", "Uint16Array", "Int32Array", "Uint32Array", "Float32Array", "Float64Array", "Map", "Set", "WeakMap", "WeakSet", "Promise", "Generator", "GeneratorFunction", "ArrayBuffer", "DataView", "JSON", "Reflect", "Proxy", "Iterator", "ParallelArray", "StopIteration");
        ECMAScriptParser parser = null;
        final HashMap<String,ArrayList> hm=new HashMap<String,ArrayList>();
        if (!isFile){
            parser = new Builder.Parser(script).build();
        }
        else{
            FileInputStream fis = new FileInputStream(script);
            parser = new Builder.Parser(new ANTLRInputStream(fis)).build();
            fis.close();
        }
        
        final TokenStream tokens = parser.getTokenStream();
        final String[] ruleNames = parser.ruleNames;
        
        
        ParseTreeWalker.DEFAULT.walk(new ECMAScriptBaseListener(){
            
            
            @Override
            public void enterEveryRule(@NotNull ParserRuleContext ctx) {
                try{
                    if(ctx != null) {
                        java.util.List<ParseTree> childs=ctx.children;
                        boolean ind=false;
                        if (childs.size()>1){
                            ind = true;
                        }
                        else 
                            if (childs.size()>0){
                                for (ParseTree p : childs){
                                    if (p.getChildCount()==0){
                                        ind=true;
                                        break;
                                    }
                                    
                                }
                            }
                        
                        if (ind){
                            String Stmt = "";
                            /*Stmt = tokens.getText(ctx);*/
                            int start = ctx.start.getTokenIndex();
                            int stop = ctx.stop.getTokenIndex();
                            for (int i = start; i <= stop; i++) {
                                String tokenText=tokens.get(i).getText();
                                if (tokens.get(i).getType()==100 && !global_Objects.contains(tokenText))
                                    tokenText = "_id_"+tokenText;
                                Stmt += tokenText;
                            }
                            //System.out.println(ctx.start);
                            
                            String key=ruleNames[ctx.getRuleIndex()];
                            ArrayList<String> aL = null;
                            if (!hm.containsKey(key)){
                                aL = new ArrayList<String>();
                                aL.add(Stmt);
                            }
                            else{
                                aL=hm.get(key);
                                aL.add(Stmt);
                            }
                            hm.put(key,aL);
                        }
                    }
                    
                }
                catch(Exception e){
                    
                }
            }
            
            
            @Override
            public void visitTerminal(@NotNull TerminalNode node) {
            }
            
            
            @Override
            public void visitErrorNode(@NotNull ErrorNode node) {
            }
            
            
        }, parser.program());
        return hm;
    }
    
    private String xmlEscapeText(String t) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < t.length(); i++){
            char c = t.charAt(i);
            switch(c){
                case '<': sb.append("&lt;"); break;
                case '>': sb.append("&gt;"); break;
                case '\"': sb.append("&quot;"); break;
                case '&': sb.append("&amp;"); break;
                case '\'': sb.append("&apos;"); break;
                default:
                if(c>0x7e) {
                    sb.append("&#"+((int)c)+";");
                }else
                    sb.append(c);
            }
        }
        return sb.toString();
    }
}
