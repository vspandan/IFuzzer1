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
	 * Enter a parse tree produced by {@link ECMAScriptParser#expressionSequence}.
	 * @param ctx the parse tree
	 */
	void enterExpressionSequence(@NotNull ECMAScriptParser.ExpressionSequenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#expressionSequence}.
	 * @param ctx the parse tree
	 */
	void exitExpressionSequence(@NotNull ECMAScriptParser.ExpressionSequenceContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TernaryExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterTernaryExpression(@NotNull ECMAScriptParser.TernaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TernaryExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitTernaryExpression(@NotNull ECMAScriptParser.TernaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitOrExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitOrExpression(@NotNull ECMAScriptParser.BitOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitOrExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitOrExpression(@NotNull ECMAScriptParser.BitOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignmentExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression(@NotNull ECMAScriptParser.AssignmentExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignmentExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression(@NotNull ECMAScriptParser.AssignmentExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogicalAndExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpression(@NotNull ECMAScriptParser.LogicalAndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogicalAndExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpression(@NotNull ECMAScriptParser.LogicalAndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InstanceofExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterInstanceofExpression(@NotNull ECMAScriptParser.InstanceofExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InstanceofExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitInstanceofExpression(@NotNull ECMAScriptParser.InstanceofExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ObjectLiteralExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterObjectLiteralExpression(@NotNull ECMAScriptParser.ObjectLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ObjectLiteralExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitObjectLiteralExpression(@NotNull ECMAScriptParser.ObjectLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PreDecreaseExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterPreDecreaseExpression(@NotNull ECMAScriptParser.PreDecreaseExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PreDecreaseExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitPreDecreaseExpression(@NotNull ECMAScriptParser.PreDecreaseExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArrayLiteralExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterArrayLiteralExpression(@NotNull ECMAScriptParser.ArrayLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArrayLiteralExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitArrayLiteralExpression(@NotNull ECMAScriptParser.ArrayLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code InExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterInExpression(@NotNull ECMAScriptParser.InExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code InExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitInExpression(@NotNull ECMAScriptParser.InExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArgumentsExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterArgumentsExpression(@NotNull ECMAScriptParser.ArgumentsExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArgumentsExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitArgumentsExpression(@NotNull ECMAScriptParser.ArgumentsExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MemberDotExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterMemberDotExpression(@NotNull ECMAScriptParser.MemberDotExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MemberDotExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitMemberDotExpression(@NotNull ECMAScriptParser.MemberDotExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterNotExpression(@NotNull ECMAScriptParser.NotExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitNotExpression(@NotNull ECMAScriptParser.NotExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DeleteExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterDeleteExpression(@NotNull ECMAScriptParser.DeleteExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DeleteExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitDeleteExpression(@NotNull ECMAScriptParser.DeleteExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IdentifierExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierExpression(@NotNull ECMAScriptParser.IdentifierExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IdentifierExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierExpression(@NotNull ECMAScriptParser.IdentifierExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitAndExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitAndExpression(@NotNull ECMAScriptParser.BitAndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitAndExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitAndExpression(@NotNull ECMAScriptParser.BitAndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryMinusExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinusExpression(@NotNull ECMAScriptParser.UnaryMinusExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryMinusExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinusExpression(@NotNull ECMAScriptParser.UnaryMinusExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PreIncrementExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterPreIncrementExpression(@NotNull ECMAScriptParser.PreIncrementExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PreIncrementExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitPreIncrementExpression(@NotNull ECMAScriptParser.PreIncrementExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FunctionExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterFunctionExpression(@NotNull ECMAScriptParser.FunctionExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FunctionExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitFunctionExpression(@NotNull ECMAScriptParser.FunctionExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitShiftExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitShiftExpression(@NotNull ECMAScriptParser.BitShiftExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitShiftExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitShiftExpression(@NotNull ECMAScriptParser.BitShiftExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogicalOrExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpression(@NotNull ECMAScriptParser.LogicalOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogicalOrExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpression(@NotNull ECMAScriptParser.LogicalOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code VoidExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterVoidExpression(@NotNull ECMAScriptParser.VoidExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VoidExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitVoidExpression(@NotNull ECMAScriptParser.VoidExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenthesizedExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterParenthesizedExpression(@NotNull ECMAScriptParser.ParenthesizedExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenthesizedExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitParenthesizedExpression(@NotNull ECMAScriptParser.ParenthesizedExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryPlusExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryPlusExpression(@NotNull ECMAScriptParser.UnaryPlusExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryPlusExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryPlusExpression(@NotNull ECMAScriptParser.UnaryPlusExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LiteralExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterLiteralExpression(@NotNull ECMAScriptParser.LiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LiteralExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitLiteralExpression(@NotNull ECMAScriptParser.LiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitNotExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitNotExpression(@NotNull ECMAScriptParser.BitNotExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitNotExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitNotExpression(@NotNull ECMAScriptParser.BitNotExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PostIncrementExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterPostIncrementExpression(@NotNull ECMAScriptParser.PostIncrementExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PostIncrementExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitPostIncrementExpression(@NotNull ECMAScriptParser.PostIncrementExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TypeofExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterTypeofExpression(@NotNull ECMAScriptParser.TypeofExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TypeofExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitTypeofExpression(@NotNull ECMAScriptParser.TypeofExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignmentOperatorExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentOperatorExpression(@NotNull ECMAScriptParser.AssignmentOperatorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignmentOperatorExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentOperatorExpression(@NotNull ECMAScriptParser.AssignmentOperatorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NewExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterNewExpression(@NotNull ECMAScriptParser.NewExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NewExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitNewExpression(@NotNull ECMAScriptParser.NewExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PostDecreaseExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterPostDecreaseExpression(@NotNull ECMAScriptParser.PostDecreaseExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PostDecreaseExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitPostDecreaseExpression(@NotNull ECMAScriptParser.PostDecreaseExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RelationalExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpression(@NotNull ECMAScriptParser.RelationalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RelationalExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpression(@NotNull ECMAScriptParser.RelationalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EqualityExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpression(@NotNull ECMAScriptParser.EqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EqualityExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpression(@NotNull ECMAScriptParser.EqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitXOrExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitXOrExpression(@NotNull ECMAScriptParser.BitXOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitXOrExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitXOrExpression(@NotNull ECMAScriptParser.BitXOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AdditiveExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(@NotNull ECMAScriptParser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AdditiveExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(@NotNull ECMAScriptParser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MemberIndexExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterMemberIndexExpression(@NotNull ECMAScriptParser.MemberIndexExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MemberIndexExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitMemberIndexExpression(@NotNull ECMAScriptParser.MemberIndexExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ThisExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterThisExpression(@NotNull ECMAScriptParser.ThisExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ThisExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitThisExpression(@NotNull ECMAScriptParser.ThisExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MultiplicativeExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(@NotNull ECMAScriptParser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MultiplicativeExpression}
	 * labeled alternative in {@link ECMAScriptParser#singleExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(@NotNull ECMAScriptParser.MultiplicativeExpressionContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#getter}.
	 * @param ctx the parse tree
	 */
	void enterGetter(@NotNull ECMAScriptParser.GetterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#getter}.
	 * @param ctx the parse tree
	 */
	void exitGetter(@NotNull ECMAScriptParser.GetterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#setter}.
	 * @param ctx the parse tree
	 */
	void enterSetter(@NotNull ECMAScriptParser.SetterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#setter}.
	 * @param ctx the parse tree
	 */
	void exitSetter(@NotNull ECMAScriptParser.SetterContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(@NotNull ECMAScriptParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(@NotNull ECMAScriptParser.IdentifierContext ctx);
}