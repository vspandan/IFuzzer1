package langparser;
import java.util.*;
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
import org.antlr.v4.runtime.Token;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

public class CodeFragmentExtractor {
    
    public HashMap XMLIRGenerator(String script, boolean isPrg) throws IOException {
        long startTime = System.currentTimeMillis();
        
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
            private boolean escape=true;
            @Override
            public void enterEveryRule(@NotNull ParserRuleContext ctx) {
                java.util.List<ParseTree> childs=ctx.children;
                boolean ind=true;
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
                        ind=true;
                        String key=ruleNames[ctx.getRuleIndex()];
                            sb.append("<"+key+">");
                    }
                }
            }
            
            @Override
            public void exitEveryRule(@NotNull ParserRuleContext ctx) {
                if(ctx != null) {
                    java.util.List<ParseTree> childs=ctx.children;
                    boolean ind=true;
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
                            ind=true;
                            String Stmt = null;
                            Stmt = tokens.getText(ctx);
                            String key=ruleNames[ctx.getRuleIndex()];

                            /*if(key.equals("eos")){
                                sb.append(";");
                            }*/
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
                        
                        if(!token.equals("<EOF>"))
                            sb.append(xmlEscapeText(token)+" ");
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
            
            
        }, parser.program());
        long endTime = System.currentTimeMillis();
        hm.put("parsecode",sb.toString());
        hm.put("identifiers",new ArrayList(identifiers));
        hm.put("exec_time",endTime-startTime);
        return hm;
    }
    
    public static void main(String[] args) throws Exception {
        CodeFragmentExtractor c=new CodeFragmentExtractor();
        String script = "/home/spandan/test.js";
        HashMap hm=c.XMLIRGenerator(script,false);
        System.out.println(hm);
        hm=c.extractFrags(script,true);
        System.out.println(hm);
		System.out.println(c.extractAST(script,true));
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
                        boolean ind=true;
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
                            ind=true;
                            String Stmt = "";
                            /*Stmt = tokens.getText(ctx);*/
                            int start = ctx.start.getTokenIndex();
                            int stop = ctx.stop.getTokenIndex();
                            for (int i = start; i <= stop; i++) {
                                String tokenText=tokens.get(i).getText();
                                if (!global_Objects.contains(tokenText))
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

	public String extractAST(String script, boolean isFile) throws IOException {
        ECMAScriptParser parser = null;
        if (!isFile){
            parser = new Builder.Parser(script).build();
        }
        else{
            FileInputStream fis = new FileInputStream(script);
            parser = new Builder.Parser(new ANTLRInputStream(fis)).build();
            fis.close();
        }
		AST ast = new AST(parser.program());
        return ast.toString();
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



class AST {

    private final Object payload;

    private final List<AST> children;

    public AST(ParseTree tree) {
        this(null, tree);
    }

    private AST(AST ast, ParseTree tree) {
        this(ast, tree, new ArrayList<AST>());
    }

    private AST(AST parent, ParseTree tree, List<AST> children) {

        this.payload = getPayload(tree);
        this.children = children;

        if (parent == null) {
            walk(tree, this);
        }
        else {
            parent.children.add(this);
        }
    }

    public Object getPayload() {
        return payload;
    }

    public List<AST> getChildren() {
        return new ArrayList<>(children);
    }

    private Object getPayload(ParseTree tree) {
        if (tree.getChildCount() == 0) {
            return tree.getPayload();
        }
        else {
            String ruleName = tree.getClass().getSimpleName().replace("Context", "");
            return Character.toLowerCase(ruleName.charAt(0)) + ruleName.substring(1);
        }
    }

    private static void walk(ParseTree tree, AST ast) {

        if (tree.getChildCount() == 0) {
            new AST(ast, tree);
        }
        else if (tree.getChildCount() == 1) {
            walk(tree.getChild(0), ast);
        }
        else if (tree.getChildCount() > 1) {

            for (int i = 0; i < tree.getChildCount(); i++) {

                AST temp = new AST(ast, tree.getChild(i));

                if (!(temp.payload instanceof Token)) {
                    walk(tree.getChild(i), temp);
                }
            }
        }
    }

    @Override
    public String toString() {

        StringBuilder builder = new StringBuilder();

        AST ast = this;
        List<AST> firstStack = new ArrayList<>();
        firstStack.add(ast);

        List<List<AST>> childListStack = new ArrayList<>();
        childListStack.add(firstStack);

        while (!childListStack.isEmpty()) {

            List<AST> childStack = childListStack.get(childListStack.size() - 1);

            if (childStack.isEmpty()) {
                childListStack.remove(childListStack.size() - 1);
            }
            else {
                ast = childStack.remove(0);
                String caption;

                if (ast.payload instanceof Token) {
                    Token token = (Token) ast.payload;
                    caption = String.format("TOKEN[type: %s, text: %s]",
                            token.getType(), token.getText().replace("\n", "\\n"));
                }
                else {
                    caption = String.valueOf(ast.payload);
                }

                String indent = "";

                for (int i = 0; i < childListStack.size() - 1; i++) {
                    indent += (childListStack.get(i).size() > 0) ? "|  " : "   ";
                }

                builder.append(indent)
                        .append(childStack.isEmpty() ? "'- " : "|- ")
                        .append(caption)
                        .append("\n");

                if (ast.children.size() > 0) {
                    List<AST> children = new ArrayList<>();
                    for (int i = 0; i < ast.children.size(); i++) {
                        children.add(ast.children.get(i));
                    }
                    childListStack.add(children);
                }
            }
        }

        return builder.toString();
    }
}