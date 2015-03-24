import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.TerminalNode;
import java.util.HashMap;
import java.util.HashSet;

public class CodeFragmentExtractor {

    private static HashMap<String,HashSet> printRegexLiteralsDemo(String script) {
        
        final HashMap<String,HashSet> hm=new HashMap<String,HashSet>();    
        final ECMAScriptParser parser = new Builder.Parser(script).build();
        final TokenStream tokens = parser.getTokenStream();
        final String[] ruleNames = parser.ruleNames;
        ParseTreeWalker.DEFAULT.walk(new ECMAScriptBaseListener(){
        
            @Override 
            public void enterProgram(@NotNull ECMAScriptParser.ProgramContext ctx) {
                if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterSourceElements(@NotNull ECMAScriptParser.SourceElementsContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterSourceElement(@NotNull ECMAScriptParser.SourceElementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterStatement(@NotNull ECMAScriptParser.StatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterBlock(@NotNull ECMAScriptParser.BlockContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterStatementList(@NotNull ECMAScriptParser.StatementListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterVariableStatement(@NotNull ECMAScriptParser.VariableStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterVariableDeclarationList(@NotNull ECMAScriptParser.VariableDeclarationListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterVariableDeclaration(@NotNull ECMAScriptParser.VariableDeclarationContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterInitialiser(@NotNull ECMAScriptParser.InitialiserContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterEmptyStatement(@NotNull ECMAScriptParser.EmptyStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterExpressionStatement(@NotNull ECMAScriptParser.ExpressionStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterIfStatement(@NotNull ECMAScriptParser.IfStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterDoStatement(@NotNull ECMAScriptParser.DoStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterWhileStatement(@NotNull ECMAScriptParser.WhileStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterForStatement(@NotNull ECMAScriptParser.ForStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterForVarStatement(@NotNull ECMAScriptParser.ForVarStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterForInStatement(@NotNull ECMAScriptParser.ForInStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterForVarInStatement(@NotNull ECMAScriptParser.ForVarInStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterContinueStatement(@NotNull ECMAScriptParser.ContinueStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterBreakStatement(@NotNull ECMAScriptParser.BreakStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterReturnStatement(@NotNull ECMAScriptParser.ReturnStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterWithStatement(@NotNull ECMAScriptParser.WithStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterSwitchStatement(@NotNull ECMAScriptParser.SwitchStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterCaseBlock(@NotNull ECMAScriptParser.CaseBlockContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterCaseClauses(@NotNull ECMAScriptParser.CaseClausesContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterCaseClause(@NotNull ECMAScriptParser.CaseClauseContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterDefaultClause(@NotNull ECMAScriptParser.DefaultClauseContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterLabelledStatement(@NotNull ECMAScriptParser.LabelledStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterThrowStatement(@NotNull ECMAScriptParser.ThrowStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterTryStatement(@NotNull ECMAScriptParser.TryStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterCatchProduction(@NotNull ECMAScriptParser.CatchProductionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterFinallyProduction(@NotNull ECMAScriptParser.FinallyProductionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterDebuggerStatement(@NotNull ECMAScriptParser.DebuggerStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterFunctionDeclaration(@NotNull ECMAScriptParser.FunctionDeclarationContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterFormalParameterList(@NotNull ECMAScriptParser.FormalParameterListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterFunctionBody(@NotNull ECMAScriptParser.FunctionBodyContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterArrayLiteral(@NotNull ECMAScriptParser.ArrayLiteralContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterElementList(@NotNull ECMAScriptParser.ElementListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterElision(@NotNull ECMAScriptParser.ElisionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterObjectLiteral(@NotNull ECMAScriptParser.ObjectLiteralContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPropertyNameAndValueList(@NotNull ECMAScriptParser.PropertyNameAndValueListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPropertyExpressionAssignment(@NotNull ECMAScriptParser.PropertyExpressionAssignmentContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPropertyGetter(@NotNull ECMAScriptParser.PropertyGetterContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPropertySetter(@NotNull ECMAScriptParser.PropertySetterContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPropertyName(@NotNull ECMAScriptParser.PropertyNameContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPropertySetParameterList(@NotNull ECMAScriptParser.PropertySetParameterListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterArguments(@NotNull ECMAScriptParser.ArgumentsContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterArgumentList(@NotNull ECMAScriptParser.ArgumentListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterExpressionSequence(@NotNull ECMAScriptParser.ExpressionSequenceContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterTernaryExpression(@NotNull ECMAScriptParser.TernaryExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterBitOrExpression(@NotNull ECMAScriptParser.BitOrExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterAssignmentExpression(@NotNull ECMAScriptParser.AssignmentExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterLogicalAndExpression(@NotNull ECMAScriptParser.LogicalAndExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterInstanceofExpression(@NotNull ECMAScriptParser.InstanceofExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterObjectLiteralExpression(@NotNull ECMAScriptParser.ObjectLiteralExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPreDecreaseExpression(@NotNull ECMAScriptParser.PreDecreaseExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterArrayLiteralExpression(@NotNull ECMAScriptParser.ArrayLiteralExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterInExpression(@NotNull ECMAScriptParser.InExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterArgumentsExpression(@NotNull ECMAScriptParser.ArgumentsExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterMemberDotExpression(@NotNull ECMAScriptParser.MemberDotExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterNotExpression(@NotNull ECMAScriptParser.NotExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterDeleteExpression(@NotNull ECMAScriptParser.DeleteExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterIdentifierExpression(@NotNull ECMAScriptParser.IdentifierExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterBitAndExpression(@NotNull ECMAScriptParser.BitAndExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterUnaryMinusExpression(@NotNull ECMAScriptParser.UnaryMinusExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPreIncrementExpression(@NotNull ECMAScriptParser.PreIncrementExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterFunctionExpression(@NotNull ECMAScriptParser.FunctionExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterBitShiftExpression(@NotNull ECMAScriptParser.BitShiftExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterLogicalOrExpression(@NotNull ECMAScriptParser.LogicalOrExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterVoidExpression(@NotNull ECMAScriptParser.VoidExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterParenthesizedExpression(@NotNull ECMAScriptParser.ParenthesizedExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterUnaryPlusExpression(@NotNull ECMAScriptParser.UnaryPlusExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterLiteralExpression(@NotNull ECMAScriptParser.LiteralExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterBitNotExpression(@NotNull ECMAScriptParser.BitNotExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPostIncrementExpression(@NotNull ECMAScriptParser.PostIncrementExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterTypeofExpression(@NotNull ECMAScriptParser.TypeofExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterAssignmentOperatorExpression(@NotNull ECMAScriptParser.AssignmentOperatorExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterNewExpression(@NotNull ECMAScriptParser.NewExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterPostDecreaseExpression(@NotNull ECMAScriptParser.PostDecreaseExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterRelationalExpression(@NotNull ECMAScriptParser.RelationalExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterEqualityExpression(@NotNull ECMAScriptParser.EqualityExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterBitXOrExpression(@NotNull ECMAScriptParser.BitXOrExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterAdditiveExpression(@NotNull ECMAScriptParser.AdditiveExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterMemberIndexExpression(@NotNull ECMAScriptParser.MemberIndexExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterThisExpression(@NotNull ECMAScriptParser.ThisExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterMultiplicativeExpression(@NotNull ECMAScriptParser.MultiplicativeExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterAssignmentOperator(@NotNull ECMAScriptParser.AssignmentOperatorContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterLiteral(@NotNull ECMAScriptParser.LiteralContext ctx) {
                if (ctx.numericLiteral() != null) {
                    System.out.println(ctx.numericLiteral().getText());
                }
            }
            
            @Override 
            public void enterNumericLiteral(@NotNull ECMAScriptParser.NumericLiteralContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterIdentifierName(@NotNull ECMAScriptParser.IdentifierNameContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterReservedWord(@NotNull ECMAScriptParser.ReservedWordContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterKeyword(@NotNull ECMAScriptParser.KeywordContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterFutureReservedWord(@NotNull ECMAScriptParser.FutureReservedWordContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterGetter(@NotNull ECMAScriptParser.GetterContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterSetter(@NotNull ECMAScriptParser.SetterContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterEos(@NotNull ECMAScriptParser.EosContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterEof(@NotNull ECMAScriptParser.EofContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void enterEveryRule(@NotNull ParserRuleContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    HashSet<String> aL = null;
                    if (!hm.containsKey(key)){
                        aL = new HashSet<String>();
                        aL.add(Stmt);
                    }
                    else{
                        aL=hm.get(key);
                        aL.add(Stmt);
                    }
                    hm.put(key,aL);
                }
            }
            
            
            @Override 
            public void visitTerminal(@NotNull TerminalNode node) {
            }
            
            
            @Override 
            public void visitErrorNode(@NotNull ErrorNode node) {
            }
            

        }, parser.program());
        ECMAScriptParser.ProgramContext prg = parser.program();
        return hm;
    }

    public static void main(String[] args) throws Exception {
        String script = "var s = 100;";
        System.out.println(printRegexLiteralsDemo(script));
    }
}
