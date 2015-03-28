import java.io.FileInputStream;
import java.io.IOException;
import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.TerminalNode;
import java.util.HashMap;
import java.util.ArrayList;

public class CodeFragmentExtractor {

    public String XMLIRGenerator(String script, boolean isPrg) throws IOException {
        
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
        ParseTreeWalker.DEFAULT.walk(new ECMAScriptBaseListener(){
            

            @Override 
            
            public void enterProgram(@NotNull ECMAScriptParser.ProgramContext ctx) {
            }
            
            @Override 
            public void exitProgram(@NotNull ECMAScriptParser.ProgramContext ctx) {
            }
            
            @Override 
            public void enterSourceElements(@NotNull ECMAScriptParser.SourceElementsContext ctx) {
            }
            
            @Override 
            public void exitSourceElements(@NotNull ECMAScriptParser.SourceElementsContext ctx) {
            }
            
            @Override 
            public void enterSourceElement(@NotNull ECMAScriptParser.SourceElementContext ctx) {
                
            }
            
            @Override 
            public void exitSourceElement(@NotNull ECMAScriptParser.SourceElementContext ctx) {
                
            }
            
            @Override 
            public void enterStatement(@NotNull ECMAScriptParser.StatementContext ctx) {
                
            }
            
            @Override 
            public void exitStatement(@NotNull ECMAScriptParser.StatementContext ctx) {
                
            }
            
            @Override 
            public void enterBlock(@NotNull ECMAScriptParser.BlockContext ctx) {
                
            }
            
            @Override 
            public void exitBlock(@NotNull ECMAScriptParser.BlockContext ctx) {
                
            }
            
            @Override 
            public void enterStatementList(@NotNull ECMAScriptParser.StatementListContext ctx) {
                
            }
            
            @Override 
            public void exitStatementList(@NotNull ECMAScriptParser.StatementListContext ctx) {
                
            }
            
            @Override 
            public void enterVariableStatement(@NotNull ECMAScriptParser.VariableStatementContext ctx) {
                
            }
            
            @Override 
            public void exitVariableStatement(@NotNull ECMAScriptParser.VariableStatementContext ctx) {
                
            }
            
            @Override 
            public void enterVariableDeclarationList(@NotNull ECMAScriptParser.VariableDeclarationListContext ctx) {
                
            }
            
            @Override 
            public void exitVariableDeclarationList(@NotNull ECMAScriptParser.VariableDeclarationListContext ctx) {
                
            }
            
            @Override 
            public void enterVariableDeclaration(@NotNull ECMAScriptParser.VariableDeclarationContext ctx) {
                
            }
            
            @Override 
            public void exitVariableDeclaration(@NotNull ECMAScriptParser.VariableDeclarationContext ctx) {
                
            }
            
            @Override 
            public void enterInitialiser(@NotNull ECMAScriptParser.InitialiserContext ctx) {
                
            }
            
            @Override 
            public void exitInitialiser(@NotNull ECMAScriptParser.InitialiserContext ctx) {
                
            }
            
            @Override 
            public void enterEmptyStatement(@NotNull ECMAScriptParser.EmptyStatementContext ctx) {
                
            }
            
            @Override 
            public void exitEmptyStatement(@NotNull ECMAScriptParser.EmptyStatementContext ctx) {
                
            }
            
            @Override 
            public void enterExpressionStatement(@NotNull ECMAScriptParser.ExpressionStatementContext ctx) {
                
            }
            
            @Override 
            public void exitExpressionStatement(@NotNull ECMAScriptParser.ExpressionStatementContext ctx) {
                
            }
            
            @Override 
            public void enterIfStatement(@NotNull ECMAScriptParser.IfStatementContext ctx) {
                
            }
            
            @Override 
            public void exitIfStatement(@NotNull ECMAScriptParser.IfStatementContext ctx) {
                
            }
            
            @Override 
            public void enterDoStatement(@NotNull ECMAScriptParser.DoStatementContext ctx) {
                
            }
            
            @Override 
            public void exitDoStatement(@NotNull ECMAScriptParser.DoStatementContext ctx) {
                
            }
            
            @Override 
            public void enterWhileStatement(@NotNull ECMAScriptParser.WhileStatementContext ctx) {
                
            }
            
            @Override 
            public void exitWhileStatement(@NotNull ECMAScriptParser.WhileStatementContext ctx) {
                
            }
            
            @Override 
            public void enterForStatement(@NotNull ECMAScriptParser.ForStatementContext ctx) {
                
            }
            
            @Override 
            public void exitForStatement(@NotNull ECMAScriptParser.ForStatementContext ctx) {
                
            }
            
            @Override 
            public void enterForVarStatement(@NotNull ECMAScriptParser.ForVarStatementContext ctx) {
                
            }
            
            @Override 
            public void exitForVarStatement(@NotNull ECMAScriptParser.ForVarStatementContext ctx) {
                
            }
            
            @Override 
            public void enterForInStatement(@NotNull ECMAScriptParser.ForInStatementContext ctx) {
                
            }
            
            @Override 
            public void exitForInStatement(@NotNull ECMAScriptParser.ForInStatementContext ctx) {
                
            }
            
            @Override 
            public void enterForVarInStatement(@NotNull ECMAScriptParser.ForVarInStatementContext ctx) {
                
            }
            
            @Override 
            public void exitForVarInStatement(@NotNull ECMAScriptParser.ForVarInStatementContext ctx) {
                
            }
            
            @Override 
            public void enterContinueStatement(@NotNull ECMAScriptParser.ContinueStatementContext ctx) {
                
            }
            
            @Override 
            public void exitContinueStatement(@NotNull ECMAScriptParser.ContinueStatementContext ctx) {
                
            }
            
            @Override 
            public void enterBreakStatement(@NotNull ECMAScriptParser.BreakStatementContext ctx) {
                
            }
            
            @Override 
            public void exitBreakStatement(@NotNull ECMAScriptParser.BreakStatementContext ctx) {
                
            }
            
            @Override 
            public void enterReturnStatement(@NotNull ECMAScriptParser.ReturnStatementContext ctx) {
                
            }
            
            @Override 
            public void exitReturnStatement(@NotNull ECMAScriptParser.ReturnStatementContext ctx) {
                
            }
            
            @Override 
            public void enterWithStatement(@NotNull ECMAScriptParser.WithStatementContext ctx) {
                
            }
            
            @Override 
            public void exitWithStatement(@NotNull ECMAScriptParser.WithStatementContext ctx) {
                
            }
            
            @Override 
            public void enterSwitchStatement(@NotNull ECMAScriptParser.SwitchStatementContext ctx) {
                
            }
            
            @Override 
            public void exitSwitchStatement(@NotNull ECMAScriptParser.SwitchStatementContext ctx) {
                
            }
            
            @Override 
            public void enterCaseBlock(@NotNull ECMAScriptParser.CaseBlockContext ctx) {
                
            }
            
            @Override 
            public void exitCaseBlock(@NotNull ECMAScriptParser.CaseBlockContext ctx) {
                
            }
            
            @Override 
            public void enterCaseClauses(@NotNull ECMAScriptParser.CaseClausesContext ctx) {
                
            }
            
            @Override 
            public void exitCaseClauses(@NotNull ECMAScriptParser.CaseClausesContext ctx) {
                
            }
            
            @Override 
            public void enterCaseClause(@NotNull ECMAScriptParser.CaseClauseContext ctx) {
                
            }
            
            @Override 
            public void exitCaseClause(@NotNull ECMAScriptParser.CaseClauseContext ctx) {
                
            }
            
            @Override 
            public void enterDefaultClause(@NotNull ECMAScriptParser.DefaultClauseContext ctx) {
                
            }
            
            @Override 
            public void exitDefaultClause(@NotNull ECMAScriptParser.DefaultClauseContext ctx) {
                
            }
            
            @Override 
            public void enterLabelledStatement(@NotNull ECMAScriptParser.LabelledStatementContext ctx) {
                
            }
            
            @Override 
            public void exitLabelledStatement(@NotNull ECMAScriptParser.LabelledStatementContext ctx) {
                
            }
            
            @Override 
            public void enterThrowStatement(@NotNull ECMAScriptParser.ThrowStatementContext ctx) {
                
            }
            
            @Override 
            public void exitThrowStatement(@NotNull ECMAScriptParser.ThrowStatementContext ctx) {
                
            }
            
            @Override 
            public void enterTryStatement(@NotNull ECMAScriptParser.TryStatementContext ctx) {
                
            }
            
            @Override 
            public void exitTryStatement(@NotNull ECMAScriptParser.TryStatementContext ctx) {
                
            }
            
            @Override 
            public void enterCatchProduction(@NotNull ECMAScriptParser.CatchProductionContext ctx) {
                
            }
            
            @Override 
            public void exitCatchProduction(@NotNull ECMAScriptParser.CatchProductionContext ctx) {
                
            }
            
            @Override 
            public void enterFinallyProduction(@NotNull ECMAScriptParser.FinallyProductionContext ctx) {
                
            }
            
            @Override 
            public void exitFinallyProduction(@NotNull ECMAScriptParser.FinallyProductionContext ctx) {
                
            }
            
            @Override 
            public void enterDebuggerStatement(@NotNull ECMAScriptParser.DebuggerStatementContext ctx) {
                
            }
            
            @Override 
            public void exitDebuggerStatement(@NotNull ECMAScriptParser.DebuggerStatementContext ctx) {
                
            }
            
            @Override 
            public void enterFunctionDeclaration(@NotNull ECMAScriptParser.FunctionDeclarationContext ctx) {
                
            }
            
            @Override 
            public void exitFunctionDeclaration(@NotNull ECMAScriptParser.FunctionDeclarationContext ctx) {
                
            }
            
            @Override 
            public void enterFormalParameterList(@NotNull ECMAScriptParser.FormalParameterListContext ctx) {
                
            }
            
            @Override 
            public void exitFormalParameterList(@NotNull ECMAScriptParser.FormalParameterListContext ctx) {
                
            }
            
            @Override 
            public void enterFunctionBody(@NotNull ECMAScriptParser.FunctionBodyContext ctx) {
                
            }
            
            @Override 
            public void exitFunctionBody(@NotNull ECMAScriptParser.FunctionBodyContext ctx) {
                
            }
            
            @Override 
            public void enterArrayLiteral(@NotNull ECMAScriptParser.ArrayLiteralContext ctx) {
                
            }
            
            @Override 
            public void exitArrayLiteral(@NotNull ECMAScriptParser.ArrayLiteralContext ctx) {
                
            }
            
            @Override 
            public void enterElementList(@NotNull ECMAScriptParser.ElementListContext ctx) {
                
            }
            
            @Override 
            public void exitElementList(@NotNull ECMAScriptParser.ElementListContext ctx) {
                
            }
            
            @Override 
            public void enterElision(@NotNull ECMAScriptParser.ElisionContext ctx) {
                
            }
            
            @Override 
            public void exitElision(@NotNull ECMAScriptParser.ElisionContext ctx) {
                
            }
            
            @Override 
            public void enterObjectLiteral(@NotNull ECMAScriptParser.ObjectLiteralContext ctx) {
                
            }
            
            @Override 
            public void exitObjectLiteral(@NotNull ECMAScriptParser.ObjectLiteralContext ctx) {
                
            }
            
            @Override 
            public void enterPropertyNameAndValueList(@NotNull ECMAScriptParser.PropertyNameAndValueListContext ctx) {
                
            }
            
            @Override 
            public void exitPropertyNameAndValueList(@NotNull ECMAScriptParser.PropertyNameAndValueListContext ctx) {
                
            }
            
            @Override 
            public void enterPropertyExpressionAssignment(@NotNull ECMAScriptParser.PropertyExpressionAssignmentContext ctx) {
                
            }
            
            @Override 
            public void exitPropertyExpressionAssignment(@NotNull ECMAScriptParser.PropertyExpressionAssignmentContext ctx) {
                
            }
            
            @Override 
            public void enterPropertyGetter(@NotNull ECMAScriptParser.PropertyGetterContext ctx) {
                
            }
            
            @Override 
            public void exitPropertyGetter(@NotNull ECMAScriptParser.PropertyGetterContext ctx) {
                
            }
            
            @Override 
            public void enterPropertySetter(@NotNull ECMAScriptParser.PropertySetterContext ctx) {
                
            }
            
            @Override 
            public void exitPropertySetter(@NotNull ECMAScriptParser.PropertySetterContext ctx) {
                
            }
            
            @Override 
            public void enterPropertyName(@NotNull ECMAScriptParser.PropertyNameContext ctx) {
                
            }
            
            @Override 
            public void exitPropertyName(@NotNull ECMAScriptParser.PropertyNameContext ctx) {
                
            }
            
            @Override 
            public void enterPropertySetParameterList(@NotNull ECMAScriptParser.PropertySetParameterListContext ctx) {
                
            }
            
            @Override 
            public void exitPropertySetParameterList(@NotNull ECMAScriptParser.PropertySetParameterListContext ctx) {
                
            }
            
            @Override 
            public void enterArguments(@NotNull ECMAScriptParser.ArgumentsContext ctx) {
                
            }
            
            @Override 
            public void exitArguments(@NotNull ECMAScriptParser.ArgumentsContext ctx) {
                
            }
            
            @Override 
            public void enterArgumentList(@NotNull ECMAScriptParser.ArgumentListContext ctx) {
                
            }
            
            @Override 
            public void exitArgumentList(@NotNull ECMAScriptParser.ArgumentListContext ctx) {
                
            }
            
            @Override 
            public void enterExpressionSequence(@NotNull ECMAScriptParser.ExpressionSequenceContext ctx) {
                
            }
            
            @Override 
            public void exitExpressionSequence(@NotNull ECMAScriptParser.ExpressionSequenceContext ctx) {
                
            }
            
            @Override 
            public void enterTernaryExpression(@NotNull ECMAScriptParser.TernaryExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitTernaryExpression(@NotNull ECMAScriptParser.TernaryExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterBitOrExpression(@NotNull ECMAScriptParser.BitOrExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitBitOrExpression(@NotNull ECMAScriptParser.BitOrExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterAssignmentExpression(@NotNull ECMAScriptParser.AssignmentExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitAssignmentExpression(@NotNull ECMAScriptParser.AssignmentExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterLogicalAndExpression(@NotNull ECMAScriptParser.LogicalAndExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitLogicalAndExpression(@NotNull ECMAScriptParser.LogicalAndExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterInstanceofExpression(@NotNull ECMAScriptParser.InstanceofExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitInstanceofExpression(@NotNull ECMAScriptParser.InstanceofExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterObjectLiteralExpression(@NotNull ECMAScriptParser.ObjectLiteralExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitObjectLiteralExpression(@NotNull ECMAScriptParser.ObjectLiteralExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterPreDecreaseExpression(@NotNull ECMAScriptParser.PreDecreaseExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitPreDecreaseExpression(@NotNull ECMAScriptParser.PreDecreaseExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterArrayLiteralExpression(@NotNull ECMAScriptParser.ArrayLiteralExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitArrayLiteralExpression(@NotNull ECMAScriptParser.ArrayLiteralExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterInExpression(@NotNull ECMAScriptParser.InExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitInExpression(@NotNull ECMAScriptParser.InExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterArgumentsExpression(@NotNull ECMAScriptParser.ArgumentsExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitArgumentsExpression(@NotNull ECMAScriptParser.ArgumentsExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterMemberDotExpression(@NotNull ECMAScriptParser.MemberDotExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitMemberDotExpression(@NotNull ECMAScriptParser.MemberDotExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterNotExpression(@NotNull ECMAScriptParser.NotExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitNotExpression(@NotNull ECMAScriptParser.NotExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterDeleteExpression(@NotNull ECMAScriptParser.DeleteExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitDeleteExpression(@NotNull ECMAScriptParser.DeleteExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterIdentifierExpression(@NotNull ECMAScriptParser.IdentifierExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitIdentifierExpression(@NotNull ECMAScriptParser.IdentifierExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterBitAndExpression(@NotNull ECMAScriptParser.BitAndExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitBitAndExpression(@NotNull ECMAScriptParser.BitAndExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterUnaryMinusExpression(@NotNull ECMAScriptParser.UnaryMinusExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitUnaryMinusExpression(@NotNull ECMAScriptParser.UnaryMinusExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterPreIncrementExpression(@NotNull ECMAScriptParser.PreIncrementExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitPreIncrementExpression(@NotNull ECMAScriptParser.PreIncrementExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterFunctionExpression(@NotNull ECMAScriptParser.FunctionExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitFunctionExpression(@NotNull ECMAScriptParser.FunctionExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterBitShiftExpression(@NotNull ECMAScriptParser.BitShiftExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitBitShiftExpression(@NotNull ECMAScriptParser.BitShiftExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterLogicalOrExpression(@NotNull ECMAScriptParser.LogicalOrExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitLogicalOrExpression(@NotNull ECMAScriptParser.LogicalOrExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterVoidExpression(@NotNull ECMAScriptParser.VoidExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitVoidExpression(@NotNull ECMAScriptParser.VoidExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterParenthesizedExpression(@NotNull ECMAScriptParser.ParenthesizedExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitParenthesizedExpression(@NotNull ECMAScriptParser.ParenthesizedExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterUnaryPlusExpression(@NotNull ECMAScriptParser.UnaryPlusExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitUnaryPlusExpression(@NotNull ECMAScriptParser.UnaryPlusExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterLiteralExpression(@NotNull ECMAScriptParser.LiteralExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitLiteralExpression(@NotNull ECMAScriptParser.LiteralExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterBitNotExpression(@NotNull ECMAScriptParser.BitNotExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitBitNotExpression(@NotNull ECMAScriptParser.BitNotExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterPostIncrementExpression(@NotNull ECMAScriptParser.PostIncrementExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitPostIncrementExpression(@NotNull ECMAScriptParser.PostIncrementExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterTypeofExpression(@NotNull ECMAScriptParser.TypeofExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitTypeofExpression(@NotNull ECMAScriptParser.TypeofExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterAssignmentOperatorExpression(@NotNull ECMAScriptParser.AssignmentOperatorExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitAssignmentOperatorExpression(@NotNull ECMAScriptParser.AssignmentOperatorExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterNewExpression(@NotNull ECMAScriptParser.NewExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitNewExpression(@NotNull ECMAScriptParser.NewExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterPostDecreaseExpression(@NotNull ECMAScriptParser.PostDecreaseExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitPostDecreaseExpression(@NotNull ECMAScriptParser.PostDecreaseExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterRelationalExpression(@NotNull ECMAScriptParser.RelationalExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitRelationalExpression(@NotNull ECMAScriptParser.RelationalExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterEqualityExpression(@NotNull ECMAScriptParser.EqualityExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitEqualityExpression(@NotNull ECMAScriptParser.EqualityExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterBitXOrExpression(@NotNull ECMAScriptParser.BitXOrExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitBitXOrExpression(@NotNull ECMAScriptParser.BitXOrExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterAdditiveExpression(@NotNull ECMAScriptParser.AdditiveExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitAdditiveExpression(@NotNull ECMAScriptParser.AdditiveExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterMemberIndexExpression(@NotNull ECMAScriptParser.MemberIndexExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitMemberIndexExpression(@NotNull ECMAScriptParser.MemberIndexExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterThisExpression(@NotNull ECMAScriptParser.ThisExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitThisExpression(@NotNull ECMAScriptParser.ThisExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterMultiplicativeExpression(@NotNull ECMAScriptParser.MultiplicativeExpressionContext ctx) {
                
            }
            
            @Override 
            public void exitMultiplicativeExpression(@NotNull ECMAScriptParser.MultiplicativeExpressionContext ctx) {
                
            }
            
            @Override 
            public void enterAssignmentOperator(@NotNull ECMAScriptParser.AssignmentOperatorContext ctx) {
                
            }
            
            @Override 
            public void exitAssignmentOperator(@NotNull ECMAScriptParser.AssignmentOperatorContext ctx) {
                
            }
            
            @Override 
            public void enterLiteral(@NotNull ECMAScriptParser.LiteralContext ctx) {
                if(ctx != null) {}
            }
            
            @Override 
            public void exitLiteral(@NotNull ECMAScriptParser.LiteralContext ctx) {
                
            }
            
            @Override 
            public void enterNumericLiteral(@NotNull ECMAScriptParser.NumericLiteralContext ctx) {
                if(ctx != null) {    ;   
                    
                }
            }
            
            @Override 
            public void exitNumericLiteral(@NotNull ECMAScriptParser.NumericLiteralContext ctx) {
                
            }
            
            @Override 
            public void enterIdentifierName(@NotNull ECMAScriptParser.IdentifierNameContext ctx) {
                if(ctx != null) {}
            }
            
            @Override 
            public void exitIdentifierName(@NotNull ECMAScriptParser.IdentifierNameContext ctx) {
                
            }
            
            @Override 
            public void enterReservedWord(@NotNull ECMAScriptParser.ReservedWordContext ctx) {
            }
            
            @Override 
            public void exitReservedWord(@NotNull ECMAScriptParser.ReservedWordContext ctx) {
                
            }
            
            @Override 
            public void enterKeyword(@NotNull ECMAScriptParser.KeywordContext ctx) {
            }
            
            @Override 
            public void exitKeyword(@NotNull ECMAScriptParser.KeywordContext ctx) {
                
            }
            
            @Override 
            public void enterFutureReservedWord(@NotNull ECMAScriptParser.FutureReservedWordContext ctx) {
            }
            
            @Override 
            public void exitFutureReservedWord(@NotNull ECMAScriptParser.FutureReservedWordContext ctx) {
                
            }
            
            @Override 
            public void enterGetter(@NotNull ECMAScriptParser.GetterContext ctx) {
            }
            
            @Override 
            public void exitGetter(@NotNull ECMAScriptParser.GetterContext ctx) {
            }
            
            @Override 
            public void enterSetter(@NotNull ECMAScriptParser.SetterContext ctx) {
            }
            
            @Override 
            public void exitSetter(@NotNull ECMAScriptParser.SetterContext ctx) {
                
            }
            
            @Override 
            public void enterEos(@NotNull ECMAScriptParser.EosContext ctx) {
            }
            
            @Override 
            public void exitEos(@NotNull ECMAScriptParser.EosContext ctx) {
                
            }
            
            @Override 
            public void enterEof(@NotNull ECMAScriptParser.EofContext ctx) {
            }
            
            @Override 
            public void exitEof(@NotNull ECMAScriptParser.EofContext ctx) {
                
            }

            
            @Override 
            public void enterEveryRule(@NotNull ParserRuleContext ctx) {
                if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    sb.append("<"+key+">");
                }
            }
            
            @Override 
            public void exitEveryRule(@NotNull ParserRuleContext ctx) {
                if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
                    String key=ruleNames[ctx.getRuleIndex()];
                    sb.append("</"+key+">");
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
        
        return sb.toString();
    }

    public static void main(String[] args) throws Exception {
        CodeFragmentExtractor c=new CodeFragmentExtractor();
        String script = "/home/spandan/Desktop/test.js";
        System.out.println(c.XMLIRGenerator(script,false));
    }

    public HashMap<String,ArrayList> extractFrags(String script, boolean isFile) throws IOException {
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
            public void enterProgram(@NotNull ECMAScriptParser.ProgramContext ctx) {
                if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterSourceElements(@NotNull ECMAScriptParser.SourceElementsContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterSourceElement(@NotNull ECMAScriptParser.SourceElementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterStatement(@NotNull ECMAScriptParser.StatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterBlock(@NotNull ECMAScriptParser.BlockContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterStatementList(@NotNull ECMAScriptParser.StatementListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterVariableStatement(@NotNull ECMAScriptParser.VariableStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterVariableDeclarationList(@NotNull ECMAScriptParser.VariableDeclarationListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterVariableDeclaration(@NotNull ECMAScriptParser.VariableDeclarationContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterInitialiser(@NotNull ECMAScriptParser.InitialiserContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterEmptyStatement(@NotNull ECMAScriptParser.EmptyStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterExpressionStatement(@NotNull ECMAScriptParser.ExpressionStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterIfStatement(@NotNull ECMAScriptParser.IfStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterDoStatement(@NotNull ECMAScriptParser.DoStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterWhileStatement(@NotNull ECMAScriptParser.WhileStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterForStatement(@NotNull ECMAScriptParser.ForStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterForVarStatement(@NotNull ECMAScriptParser.ForVarStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterForInStatement(@NotNull ECMAScriptParser.ForInStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterForVarInStatement(@NotNull ECMAScriptParser.ForVarInStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterContinueStatement(@NotNull ECMAScriptParser.ContinueStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterBreakStatement(@NotNull ECMAScriptParser.BreakStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterReturnStatement(@NotNull ECMAScriptParser.ReturnStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterWithStatement(@NotNull ECMAScriptParser.WithStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterSwitchStatement(@NotNull ECMAScriptParser.SwitchStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterCaseBlock(@NotNull ECMAScriptParser.CaseBlockContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterCaseClauses(@NotNull ECMAScriptParser.CaseClausesContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterCaseClause(@NotNull ECMAScriptParser.CaseClauseContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterDefaultClause(@NotNull ECMAScriptParser.DefaultClauseContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterLabelledStatement(@NotNull ECMAScriptParser.LabelledStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterThrowStatement(@NotNull ECMAScriptParser.ThrowStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterTryStatement(@NotNull ECMAScriptParser.TryStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterCatchProduction(@NotNull ECMAScriptParser.CatchProductionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterFinallyProduction(@NotNull ECMAScriptParser.FinallyProductionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterDebuggerStatement(@NotNull ECMAScriptParser.DebuggerStatementContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterFunctionDeclaration(@NotNull ECMAScriptParser.FunctionDeclarationContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterFormalParameterList(@NotNull ECMAScriptParser.FormalParameterListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterFunctionBody(@NotNull ECMAScriptParser.FunctionBodyContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterArrayLiteral(@NotNull ECMAScriptParser.ArrayLiteralContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterElementList(@NotNull ECMAScriptParser.ElementListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterElision(@NotNull ECMAScriptParser.ElisionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterObjectLiteral(@NotNull ECMAScriptParser.ObjectLiteralContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPropertyNameAndValueList(@NotNull ECMAScriptParser.PropertyNameAndValueListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPropertyExpressionAssignment(@NotNull ECMAScriptParser.PropertyExpressionAssignmentContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPropertyGetter(@NotNull ECMAScriptParser.PropertyGetterContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPropertySetter(@NotNull ECMAScriptParser.PropertySetterContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPropertyName(@NotNull ECMAScriptParser.PropertyNameContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPropertySetParameterList(@NotNull ECMAScriptParser.PropertySetParameterListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterArguments(@NotNull ECMAScriptParser.ArgumentsContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterArgumentList(@NotNull ECMAScriptParser.ArgumentListContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterExpressionSequence(@NotNull ECMAScriptParser.ExpressionSequenceContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterTernaryExpression(@NotNull ECMAScriptParser.TernaryExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterBitOrExpression(@NotNull ECMAScriptParser.BitOrExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterAssignmentExpression(@NotNull ECMAScriptParser.AssignmentExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterLogicalAndExpression(@NotNull ECMAScriptParser.LogicalAndExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterInstanceofExpression(@NotNull ECMAScriptParser.InstanceofExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterObjectLiteralExpression(@NotNull ECMAScriptParser.ObjectLiteralExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPreDecreaseExpression(@NotNull ECMAScriptParser.PreDecreaseExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterArrayLiteralExpression(@NotNull ECMAScriptParser.ArrayLiteralExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterInExpression(@NotNull ECMAScriptParser.InExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterArgumentsExpression(@NotNull ECMAScriptParser.ArgumentsExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterMemberDotExpression(@NotNull ECMAScriptParser.MemberDotExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterNotExpression(@NotNull ECMAScriptParser.NotExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterDeleteExpression(@NotNull ECMAScriptParser.DeleteExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterIdentifierExpression(@NotNull ECMAScriptParser.IdentifierExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterBitAndExpression(@NotNull ECMAScriptParser.BitAndExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterUnaryMinusExpression(@NotNull ECMAScriptParser.UnaryMinusExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPreIncrementExpression(@NotNull ECMAScriptParser.PreIncrementExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterFunctionExpression(@NotNull ECMAScriptParser.FunctionExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterBitShiftExpression(@NotNull ECMAScriptParser.BitShiftExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterLogicalOrExpression(@NotNull ECMAScriptParser.LogicalOrExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterVoidExpression(@NotNull ECMAScriptParser.VoidExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterParenthesizedExpression(@NotNull ECMAScriptParser.ParenthesizedExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterUnaryPlusExpression(@NotNull ECMAScriptParser.UnaryPlusExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterLiteralExpression(@NotNull ECMAScriptParser.LiteralExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterBitNotExpression(@NotNull ECMAScriptParser.BitNotExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPostIncrementExpression(@NotNull ECMAScriptParser.PostIncrementExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterTypeofExpression(@NotNull ECMAScriptParser.TypeofExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterAssignmentOperatorExpression(@NotNull ECMAScriptParser.AssignmentOperatorExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterNewExpression(@NotNull ECMAScriptParser.NewExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterPostDecreaseExpression(@NotNull ECMAScriptParser.PostDecreaseExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterRelationalExpression(@NotNull ECMAScriptParser.RelationalExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterEqualityExpression(@NotNull ECMAScriptParser.EqualityExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterBitXOrExpression(@NotNull ECMAScriptParser.BitXOrExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterAdditiveExpression(@NotNull ECMAScriptParser.AdditiveExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterMemberIndexExpression(@NotNull ECMAScriptParser.MemberIndexExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterThisExpression(@NotNull ECMAScriptParser.ThisExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterMultiplicativeExpression(@NotNull ECMAScriptParser.MultiplicativeExpressionContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterAssignmentOperator(@NotNull ECMAScriptParser.AssignmentOperatorContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterLiteral(@NotNull ECMAScriptParser.LiteralContext ctx) {
                /*if (ctx.numericLiteral() != null) {
                    System.out.println(ctx.numericLiteral().getText());
                }*/
            }
            
            @Override 
            public void enterNumericLiteral(@NotNull ECMAScriptParser.NumericLiteralContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterIdentifierName(@NotNull ECMAScriptParser.IdentifierNameContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterReservedWord(@NotNull ECMAScriptParser.ReservedWordContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterKeyword(@NotNull ECMAScriptParser.KeywordContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterFutureReservedWord(@NotNull ECMAScriptParser.FutureReservedWordContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterGetter(@NotNull ECMAScriptParser.GetterContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterSetter(@NotNull ECMAScriptParser.SetterContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterEos(@NotNull ECMAScriptParser.EosContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterEof(@NotNull ECMAScriptParser.EofContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
            
            
            @Override 
            public void enterEveryRule(@NotNull ParserRuleContext ctx) {
                  if(ctx != null) {
                    
                    String Stmt = null;
                    Stmt = tokens.getText(ctx);
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
