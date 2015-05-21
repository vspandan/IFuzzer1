// Generated from ECMAScript.g4 by ANTLR 4.5
package langparser;
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ECMAScriptParser}.
 */
public interface ECMAScriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(@NotNull ECMAScriptParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(@NotNull ECMAScriptParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#sourceElements}.
	 * @param ctx the parse tree
	 */
	void enterSourceElements(@NotNull ECMAScriptParser.SourceElementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#sourceElements}.
	 * @param ctx the parse tree
	 */
	void exitSourceElements(@NotNull ECMAScriptParser.SourceElementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#sourceElement}.
	 * @param ctx the parse tree
	 */
	void enterSourceElement(@NotNull ECMAScriptParser.SourceElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#sourceElement}.
	 * @param ctx the parse tree
	 */
	void exitSourceElement(@NotNull ECMAScriptParser.SourceElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#functionDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDeclaration(@NotNull ECMAScriptParser.FunctionDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#functionDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDeclaration(@NotNull ECMAScriptParser.FunctionDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(@NotNull ECMAScriptParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(@NotNull ECMAScriptParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#yieldExpression}.
	 * @param ctx the parse tree
	 */
	void enterYieldExpression(@NotNull ECMAScriptParser.YieldExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#yieldExpression}.
	 * @param ctx the parse tree
	 */
	void exitYieldExpression(@NotNull ECMAScriptParser.YieldExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(@NotNull ECMAScriptParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(@NotNull ECMAScriptParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#statementList}.
	 * @param ctx the parse tree
	 */
	void enterStatementList(@NotNull ECMAScriptParser.StatementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#statementList}.
	 * @param ctx the parse tree
	 */
	void exitStatementList(@NotNull ECMAScriptParser.StatementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#variableStatement}.
	 * @param ctx the parse tree
	 */
	void enterVariableStatement(@NotNull ECMAScriptParser.VariableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#variableStatement}.
	 * @param ctx the parse tree
	 */
	void exitVariableStatement(@NotNull ECMAScriptParser.VariableStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#variableDeclarationList}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclarationList(@NotNull ECMAScriptParser.VariableDeclarationListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#variableDeclarationList}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclarationList(@NotNull ECMAScriptParser.VariableDeclarationListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclaration(@NotNull ECMAScriptParser.VariableDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclaration(@NotNull ECMAScriptParser.VariableDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#initialiser}.
	 * @param ctx the parse tree
	 */
	void enterInitialiser(@NotNull ECMAScriptParser.InitialiserContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#initialiser}.
	 * @param ctx the parse tree
	 */
	void exitInitialiser(@NotNull ECMAScriptParser.InitialiserContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#emptyStatement}.
	 * @param ctx the parse tree
	 */
	void enterEmptyStatement(@NotNull ECMAScriptParser.EmptyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#emptyStatement}.
	 * @param ctx the parse tree
	 */
	void exitEmptyStatement(@NotNull ECMAScriptParser.EmptyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(@NotNull ECMAScriptParser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(@NotNull ECMAScriptParser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(@NotNull ECMAScriptParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(@NotNull ECMAScriptParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#elseStatement}.
	 * @param ctx the parse tree
	 */
	void enterElseStatement(@NotNull ECMAScriptParser.ElseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#elseStatement}.
	 * @param ctx the parse tree
	 */
	void exitElseStatement(@NotNull ECMAScriptParser.ElseStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DoStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterDoStatement(@NotNull ECMAScriptParser.DoStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DoStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitDoStatement(@NotNull ECMAScriptParser.DoStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code WhileStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(@NotNull ECMAScriptParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code WhileStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(@NotNull ECMAScriptParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(@NotNull ECMAScriptParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ForStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(@NotNull ECMAScriptParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarStatement(@NotNull ECMAScriptParser.ForVarStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarStatement(@NotNull ECMAScriptParser.ForVarStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForInStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForInStatement(@NotNull ECMAScriptParser.ForInStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ForInStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForInStatement(@NotNull ECMAScriptParser.ForInStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarInStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarInStatement(@NotNull ECMAScriptParser.ForVarInStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarInStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarInStatement(@NotNull ECMAScriptParser.ForVarInStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarInStatement2}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarInStatement2(@NotNull ECMAScriptParser.ForVarInStatement2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarInStatement2}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarInStatement2(@NotNull ECMAScriptParser.ForVarInStatement2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarInStatement3}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarInStatement3(@NotNull ECMAScriptParser.ForVarInStatement3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarInStatement3}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarInStatement3(@NotNull ECMAScriptParser.ForVarInStatement3Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarOfStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarOfStatement(@NotNull ECMAScriptParser.ForVarOfStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarOfStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarOfStatement(@NotNull ECMAScriptParser.ForVarOfStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarOfStatement2}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarOfStatement2(@NotNull ECMAScriptParser.ForVarOfStatement2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarOfStatement2}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarOfStatement2(@NotNull ECMAScriptParser.ForVarOfStatement2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarOfStatement3}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarOfStatement3(@NotNull ECMAScriptParser.ForVarOfStatement3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarOfStatement3}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarOfStatement3(@NotNull ECMAScriptParser.ForVarOfStatement3Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarOfStatement4}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarOfStatement4(@NotNull ECMAScriptParser.ForVarOfStatement4Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarOfStatement4}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarOfStatement4(@NotNull ECMAScriptParser.ForVarOfStatement4Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarOfStatement5}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarOfStatement5(@NotNull ECMAScriptParser.ForVarOfStatement5Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarOfStatement5}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarOfStatement5(@NotNull ECMAScriptParser.ForVarOfStatement5Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForVarOfStatement6}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForVarOfStatement6(@NotNull ECMAScriptParser.ForVarOfStatement6Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForVarOfStatement6}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForVarOfStatement6(@NotNull ECMAScriptParser.ForVarOfStatement6Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForEachStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForEachStatement(@NotNull ECMAScriptParser.ForEachStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ForEachStatement}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForEachStatement(@NotNull ECMAScriptParser.ForEachStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ForEachStatement2}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForEachStatement2(@NotNull ECMAScriptParser.ForEachStatement2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForEachStatement2}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForEachStatement2(@NotNull ECMAScriptParser.ForEachStatement2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForEachStatement3}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForEachStatement3(@NotNull ECMAScriptParser.ForEachStatement3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForEachStatement3}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForEachStatement3(@NotNull ECMAScriptParser.ForEachStatement3Context ctx);
	/**
	 * Enter a parse tree produced by the {@code ForEachStatement7}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterForEachStatement7(@NotNull ECMAScriptParser.ForEachStatement7Context ctx);
	/**
	 * Exit a parse tree produced by the {@code ForEachStatement7}
	 * labeled alternative in {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitForEachStatement7(@NotNull ECMAScriptParser.ForEachStatement7Context ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(@NotNull ECMAScriptParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(@NotNull ECMAScriptParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(@NotNull ECMAScriptParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(@NotNull ECMAScriptParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(@NotNull ECMAScriptParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(@NotNull ECMAScriptParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#withStatement}.
	 * @param ctx the parse tree
	 */
	void enterWithStatement(@NotNull ECMAScriptParser.WithStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#withStatement}.
	 * @param ctx the parse tree
	 */
	void exitWithStatement(@NotNull ECMAScriptParser.WithStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#switchStatement}.
	 * @param ctx the parse tree
	 */
	void enterSwitchStatement(@NotNull ECMAScriptParser.SwitchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#switchStatement}.
	 * @param ctx the parse tree
	 */
	void exitSwitchStatement(@NotNull ECMAScriptParser.SwitchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#caseBlock}.
	 * @param ctx the parse tree
	 */
	void enterCaseBlock(@NotNull ECMAScriptParser.CaseBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#caseBlock}.
	 * @param ctx the parse tree
	 */
	void exitCaseBlock(@NotNull ECMAScriptParser.CaseBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#caseClauses}.
	 * @param ctx the parse tree
	 */
	void enterCaseClauses(@NotNull ECMAScriptParser.CaseClausesContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#caseClauses}.
	 * @param ctx the parse tree
	 */
	void exitCaseClauses(@NotNull ECMAScriptParser.CaseClausesContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#caseClause}.
	 * @param ctx the parse tree
	 */
	void enterCaseClause(@NotNull ECMAScriptParser.CaseClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#caseClause}.
	 * @param ctx the parse tree
	 */
	void exitCaseClause(@NotNull ECMAScriptParser.CaseClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#defaultClause}.
	 * @param ctx the parse tree
	 */
	void enterDefaultClause(@NotNull ECMAScriptParser.DefaultClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#defaultClause}.
	 * @param ctx the parse tree
	 */
	void exitDefaultClause(@NotNull ECMAScriptParser.DefaultClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#labelledStatement}.
	 * @param ctx the parse tree
	 */
	void enterLabelledStatement(@NotNull ECMAScriptParser.LabelledStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#labelledStatement}.
	 * @param ctx the parse tree
	 */
	void exitLabelledStatement(@NotNull ECMAScriptParser.LabelledStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#throwStatement}.
	 * @param ctx the parse tree
	 */
	void enterThrowStatement(@NotNull ECMAScriptParser.ThrowStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#throwStatement}.
	 * @param ctx the parse tree
	 */
	void exitThrowStatement(@NotNull ECMAScriptParser.ThrowStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#tryStatement}.
	 * @param ctx the parse tree
	 */
	void enterTryStatement(@NotNull ECMAScriptParser.TryStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#tryStatement}.
	 * @param ctx the parse tree
	 */
	void exitTryStatement(@NotNull ECMAScriptParser.TryStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#catchProduction}.
	 * @param ctx the parse tree
	 */
	void enterCatchProduction(@NotNull ECMAScriptParser.CatchProductionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#catchProduction}.
	 * @param ctx the parse tree
	 */
	void exitCatchProduction(@NotNull ECMAScriptParser.CatchProductionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#finallyProduction}.
	 * @param ctx the parse tree
	 */
	void enterFinallyProduction(@NotNull ECMAScriptParser.FinallyProductionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#finallyProduction}.
	 * @param ctx the parse tree
	 */
	void exitFinallyProduction(@NotNull ECMAScriptParser.FinallyProductionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#debuggerStatement}.
	 * @param ctx the parse tree
	 */
	void enterDebuggerStatement(@NotNull ECMAScriptParser.DebuggerStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#debuggerStatement}.
	 * @param ctx the parse tree
	 */
	void exitDebuggerStatement(@NotNull ECMAScriptParser.DebuggerStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#formalParameterList}.
	 * @param ctx the parse tree
	 */
	void enterFormalParameterList(@NotNull ECMAScriptParser.FormalParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#formalParameterList}.
	 * @param ctx the parse tree
	 */
	void exitFormalParameterList(@NotNull ECMAScriptParser.FormalParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#formalParameter}.
	 * @param ctx the parse tree
	 */
	void enterFormalParameter(@NotNull ECMAScriptParser.FormalParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#formalParameter}.
	 * @param ctx the parse tree
	 */
	void exitFormalParameter(@NotNull ECMAScriptParser.FormalParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#functionBody}.
	 * @param ctx the parse tree
	 */
	void enterFunctionBody(@NotNull ECMAScriptParser.FunctionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#functionBody}.
	 * @param ctx the parse tree
	 */
	void exitFunctionBody(@NotNull ECMAScriptParser.FunctionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void enterArrayLiteral(@NotNull ECMAScriptParser.ArrayLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void exitArrayLiteral(@NotNull ECMAScriptParser.ArrayLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#elementList}.
	 * @param ctx the parse tree
	 */
	void enterElementList(@NotNull ECMAScriptParser.ElementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#elementList}.
	 * @param ctx the parse tree
	 */
	void exitElementList(@NotNull ECMAScriptParser.ElementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#elision}.
	 * @param ctx the parse tree
	 */
	void enterElision(@NotNull ECMAScriptParser.ElisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#elision}.
	 * @param ctx the parse tree
	 */
	void exitElision(@NotNull ECMAScriptParser.ElisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#objectLiteral}.
	 * @param ctx the parse tree
	 */
	void enterObjectLiteral(@NotNull ECMAScriptParser.ObjectLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#objectLiteral}.
	 * @param ctx the parse tree
	 */
	void exitObjectLiteral(@NotNull ECMAScriptParser.ObjectLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#propertyNameAndValueList}.
	 * @param ctx the parse tree
	 */
	void enterPropertyNameAndValueList(@NotNull ECMAScriptParser.PropertyNameAndValueListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#propertyNameAndValueList}.
	 * @param ctx the parse tree
	 */
	void exitPropertyNameAndValueList(@NotNull ECMAScriptParser.PropertyNameAndValueListContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PropertyExpressionAssignment1}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void enterPropertyExpressionAssignment1(@NotNull ECMAScriptParser.PropertyExpressionAssignment1Context ctx);
	/**
	 * Exit a parse tree produced by the {@code PropertyExpressionAssignment1}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void exitPropertyExpressionAssignment1(@NotNull ECMAScriptParser.PropertyExpressionAssignment1Context ctx);
	/**
	 * Enter a parse tree produced by the {@code PropertyExpressionAssignment}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void enterPropertyExpressionAssignment(@NotNull ECMAScriptParser.PropertyExpressionAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PropertyExpressionAssignment}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void exitPropertyExpressionAssignment(@NotNull ECMAScriptParser.PropertyExpressionAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PropertyGetter}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void enterPropertyGetter(@NotNull ECMAScriptParser.PropertyGetterContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PropertyGetter}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void exitPropertyGetter(@NotNull ECMAScriptParser.PropertyGetterContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PropertySetter}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void enterPropertySetter(@NotNull ECMAScriptParser.PropertySetterContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PropertySetter}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void exitPropertySetter(@NotNull ECMAScriptParser.PropertySetterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#propertyName}.
	 * @param ctx the parse tree
	 */
	void enterPropertyName(@NotNull ECMAScriptParser.PropertyNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#propertyName}.
	 * @param ctx the parse tree
	 */
	void exitPropertyName(@NotNull ECMAScriptParser.PropertyNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#propertySetParameterList}.
	 * @param ctx the parse tree
	 */
	void enterPropertySetParameterList(@NotNull ECMAScriptParser.PropertySetParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#propertySetParameterList}.
	 * @param ctx the parse tree
	 */
	void exitPropertySetParameterList(@NotNull ECMAScriptParser.PropertySetParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(@NotNull ECMAScriptParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(@NotNull ECMAScriptParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(@NotNull ECMAScriptParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(@NotNull ECMAScriptParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(@NotNull ECMAScriptParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(@NotNull ECMAScriptParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignmentExpression1}
	 * labeled alternative in {@link ECMAScriptParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression1(@NotNull ECMAScriptParser.AssignmentExpression1Context ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignmentExpression1}
	 * labeled alternative in {@link ECMAScriptParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression1(@NotNull ECMAScriptParser.AssignmentExpression1Context ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignmentExpression2}
	 * labeled alternative in {@link ECMAScriptParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression2(@NotNull ECMAScriptParser.AssignmentExpression2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignmentExpression2}
	 * labeled alternative in {@link ECMAScriptParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression2(@NotNull ECMAScriptParser.AssignmentExpression2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignmentExpression3}
	 * labeled alternative in {@link ECMAScriptParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression3(@NotNull ECMAScriptParser.AssignmentExpression3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignmentExpression3}
	 * labeled alternative in {@link ECMAScriptParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression3(@NotNull ECMAScriptParser.AssignmentExpression3Context ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#conditionalExpression}.
	 * @param ctx the parse tree
	 */
	void enterConditionalExpression(@NotNull ECMAScriptParser.ConditionalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#conditionalExpression}.
	 * @param ctx the parse tree
	 */
	void exitConditionalExpression(@NotNull ECMAScriptParser.ConditionalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#logicalORExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalORExpression(@NotNull ECMAScriptParser.LogicalORExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#logicalORExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalORExpression(@NotNull ECMAScriptParser.LogicalORExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#logicalANDExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalANDExpression(@NotNull ECMAScriptParser.LogicalANDExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#logicalANDExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalANDExpression(@NotNull ECMAScriptParser.LogicalANDExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bitwiseORExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseORExpression(@NotNull ECMAScriptParser.BitwiseORExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bitwiseORExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseORExpression(@NotNull ECMAScriptParser.BitwiseORExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bitwiseXORExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseXORExpression(@NotNull ECMAScriptParser.BitwiseXORExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bitwiseXORExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseXORExpression(@NotNull ECMAScriptParser.BitwiseXORExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bitwiseANDExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseANDExpression(@NotNull ECMAScriptParser.BitwiseANDExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bitwiseANDExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseANDExpression(@NotNull ECMAScriptParser.BitwiseANDExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpression(@NotNull ECMAScriptParser.EqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpression(@NotNull ECMAScriptParser.EqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpression(@NotNull ECMAScriptParser.RelationalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpression(@NotNull ECMAScriptParser.RelationalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void enterShiftExpression(@NotNull ECMAScriptParser.ShiftExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void exitShiftExpression(@NotNull ECMAScriptParser.ShiftExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(@NotNull ECMAScriptParser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(@NotNull ECMAScriptParser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(@NotNull ECMAScriptParser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(@NotNull ECMAScriptParser.MultiplicativeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpression(@NotNull ECMAScriptParser.UnaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpression(@NotNull ECMAScriptParser.UnaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#postfixExpression}.
	 * @param ctx the parse tree
	 */
	void enterPostfixExpression(@NotNull ECMAScriptParser.PostfixExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#postfixExpression}.
	 * @param ctx the parse tree
	 */
	void exitPostfixExpression(@NotNull ECMAScriptParser.PostfixExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#leftHandSideExpression}.
	 * @param ctx the parse tree
	 */
	void enterLeftHandSideExpression(@NotNull ECMAScriptParser.LeftHandSideExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#leftHandSideExpression}.
	 * @param ctx the parse tree
	 */
	void exitLeftHandSideExpression(@NotNull ECMAScriptParser.LeftHandSideExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#callExpression}.
	 * @param ctx the parse tree
	 */
	void enterCallExpression(@NotNull ECMAScriptParser.CallExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#callExpression}.
	 * @param ctx the parse tree
	 */
	void exitCallExpression(@NotNull ECMAScriptParser.CallExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#newExpression}.
	 * @param ctx the parse tree
	 */
	void enterNewExpression(@NotNull ECMAScriptParser.NewExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#newExpression}.
	 * @param ctx the parse tree
	 */
	void exitNewExpression(@NotNull ECMAScriptParser.NewExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#memberExpression}.
	 * @param ctx the parse tree
	 */
	void enterMemberExpression(@NotNull ECMAScriptParser.MemberExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#memberExpression}.
	 * @param ctx the parse tree
	 */
	void exitMemberExpression(@NotNull ECMAScriptParser.MemberExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#functionExpression}.
	 * @param ctx the parse tree
	 */
	void enterFunctionExpression(@NotNull ECMAScriptParser.FunctionExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#functionExpression}.
	 * @param ctx the parse tree
	 */
	void exitFunctionExpression(@NotNull ECMAScriptParser.FunctionExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpression(@NotNull ECMAScriptParser.PrimaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpression(@NotNull ECMAScriptParser.PrimaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentOperator(@NotNull ECMAScriptParser.AssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentOperator(@NotNull ECMAScriptParser.AssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(@NotNull ECMAScriptParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(@NotNull ECMAScriptParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#numericLiteral}.
	 * @param ctx the parse tree
	 */
	void enterNumericLiteral(@NotNull ECMAScriptParser.NumericLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#numericLiteral}.
	 * @param ctx the parse tree
	 */
	void exitNumericLiteral(@NotNull ECMAScriptParser.NumericLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#identifierName}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierName(@NotNull ECMAScriptParser.IdentifierNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#identifierName}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierName(@NotNull ECMAScriptParser.IdentifierNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#reservedWord}.
	 * @param ctx the parse tree
	 */
	void enterReservedWord(@NotNull ECMAScriptParser.ReservedWordContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#reservedWord}.
	 * @param ctx the parse tree
	 */
	void exitReservedWord(@NotNull ECMAScriptParser.ReservedWordContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#keyword}.
	 * @param ctx the parse tree
	 */
	void enterKeyword(@NotNull ECMAScriptParser.KeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#keyword}.
	 * @param ctx the parse tree
	 */
	void exitKeyword(@NotNull ECMAScriptParser.KeywordContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#futureReservedWord}.
	 * @param ctx the parse tree
	 */
	void enterFutureReservedWord(@NotNull ECMAScriptParser.FutureReservedWordContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#futureReservedWord}.
	 * @param ctx the parse tree
	 */
	void exitFutureReservedWord(@NotNull ECMAScriptParser.FutureReservedWordContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#eos}.
	 * @param ctx the parse tree
	 */
	void enterEos(@NotNull ECMAScriptParser.EosContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#eos}.
	 * @param ctx the parse tree
	 */
	void exitEos(@NotNull ECMAScriptParser.EosContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#eof}.
	 * @param ctx the parse tree
	 */
	void enterEof(@NotNull ECMAScriptParser.EofContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#eof}.
	 * @param ctx the parse tree
	 */
	void exitEof(@NotNull ECMAScriptParser.EofContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(@NotNull ECMAScriptParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(@NotNull ECMAScriptParser.VarContext ctx);
}