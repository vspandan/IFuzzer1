// Generated from ../grammarFiles/ECMAScript1.g4 by ANTLR 4.5
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ECMAScript1Parser}.
 */
public interface ECMAScript1Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(@NotNull ECMAScript1Parser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(@NotNull ECMAScript1Parser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#sourceElements}.
	 * @param ctx the parse tree
	 */
	void enterSourceElements(@NotNull ECMAScript1Parser.SourceElementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#sourceElements}.
	 * @param ctx the parse tree
	 */
	void exitSourceElements(@NotNull ECMAScript1Parser.SourceElementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#sourceElement}.
	 * @param ctx the parse tree
	 */
	void enterSourceElement(@NotNull ECMAScript1Parser.SourceElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#sourceElement}.
	 * @param ctx the parse tree
	 */
	void exitSourceElement(@NotNull ECMAScript1Parser.SourceElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#functionDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDeclaration(@NotNull ECMAScript1Parser.FunctionDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#functionDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDeclaration(@NotNull ECMAScript1Parser.FunctionDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#functionExpression}.
	 * @param ctx the parse tree
	 */
	void enterFunctionExpression(@NotNull ECMAScript1Parser.FunctionExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#functionExpression}.
	 * @param ctx the parse tree
	 */
	void exitFunctionExpression(@NotNull ECMAScript1Parser.FunctionExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#formalParameterList}.
	 * @param ctx the parse tree
	 */
	void enterFormalParameterList(@NotNull ECMAScript1Parser.FormalParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#formalParameterList}.
	 * @param ctx the parse tree
	 */
	void exitFormalParameterList(@NotNull ECMAScript1Parser.FormalParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#functionBody}.
	 * @param ctx the parse tree
	 */
	void enterFunctionBody(@NotNull ECMAScript1Parser.FunctionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#functionBody}.
	 * @param ctx the parse tree
	 */
	void exitFunctionBody(@NotNull ECMAScript1Parser.FunctionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(@NotNull ECMAScript1Parser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(@NotNull ECMAScript1Parser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#statementBlock}.
	 * @param ctx the parse tree
	 */
	void enterStatementBlock(@NotNull ECMAScript1Parser.StatementBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#statementBlock}.
	 * @param ctx the parse tree
	 */
	void exitStatementBlock(@NotNull ECMAScript1Parser.StatementBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#statementList}.
	 * @param ctx the parse tree
	 */
	void enterStatementList(@NotNull ECMAScript1Parser.StatementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#statementList}.
	 * @param ctx the parse tree
	 */
	void exitStatementList(@NotNull ECMAScript1Parser.StatementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#variableStatement}.
	 * @param ctx the parse tree
	 */
	void enterVariableStatement(@NotNull ECMAScript1Parser.VariableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#variableStatement}.
	 * @param ctx the parse tree
	 */
	void exitVariableStatement(@NotNull ECMAScript1Parser.VariableStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#variableDeclarationList}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclarationList(@NotNull ECMAScript1Parser.VariableDeclarationListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#variableDeclarationList}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclarationList(@NotNull ECMAScript1Parser.VariableDeclarationListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#variableDeclarationListNoIn}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclarationListNoIn(@NotNull ECMAScript1Parser.VariableDeclarationListNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#variableDeclarationListNoIn}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclarationListNoIn(@NotNull ECMAScript1Parser.VariableDeclarationListNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclaration(@NotNull ECMAScript1Parser.VariableDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclaration(@NotNull ECMAScript1Parser.VariableDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#variableDeclarationNoIn}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclarationNoIn(@NotNull ECMAScript1Parser.VariableDeclarationNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#variableDeclarationNoIn}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclarationNoIn(@NotNull ECMAScript1Parser.VariableDeclarationNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#initialiser}.
	 * @param ctx the parse tree
	 */
	void enterInitialiser(@NotNull ECMAScript1Parser.InitialiserContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#initialiser}.
	 * @param ctx the parse tree
	 */
	void exitInitialiser(@NotNull ECMAScript1Parser.InitialiserContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#initialiserNoIn}.
	 * @param ctx the parse tree
	 */
	void enterInitialiserNoIn(@NotNull ECMAScript1Parser.InitialiserNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#initialiserNoIn}.
	 * @param ctx the parse tree
	 */
	void exitInitialiserNoIn(@NotNull ECMAScript1Parser.InitialiserNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#emptyStatement}.
	 * @param ctx the parse tree
	 */
	void enterEmptyStatement(@NotNull ECMAScript1Parser.EmptyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#emptyStatement}.
	 * @param ctx the parse tree
	 */
	void exitEmptyStatement(@NotNull ECMAScript1Parser.EmptyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(@NotNull ECMAScript1Parser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(@NotNull ECMAScript1Parser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(@NotNull ECMAScript1Parser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(@NotNull ECMAScript1Parser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterIterationStatement(@NotNull ECMAScript1Parser.IterationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitIterationStatement(@NotNull ECMAScript1Parser.IterationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(@NotNull ECMAScript1Parser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(@NotNull ECMAScript1Parser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(@NotNull ECMAScript1Parser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(@NotNull ECMAScript1Parser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(@NotNull ECMAScript1Parser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(@NotNull ECMAScript1Parser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#withStatement}.
	 * @param ctx the parse tree
	 */
	void enterWithStatement(@NotNull ECMAScript1Parser.WithStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#withStatement}.
	 * @param ctx the parse tree
	 */
	void exitWithStatement(@NotNull ECMAScript1Parser.WithStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#labelledStatement}.
	 * @param ctx the parse tree
	 */
	void enterLabelledStatement(@NotNull ECMAScript1Parser.LabelledStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#labelledStatement}.
	 * @param ctx the parse tree
	 */
	void exitLabelledStatement(@NotNull ECMAScript1Parser.LabelledStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#switchStatement}.
	 * @param ctx the parse tree
	 */
	void enterSwitchStatement(@NotNull ECMAScript1Parser.SwitchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#switchStatement}.
	 * @param ctx the parse tree
	 */
	void exitSwitchStatement(@NotNull ECMAScript1Parser.SwitchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#caseBlock}.
	 * @param ctx the parse tree
	 */
	void enterCaseBlock(@NotNull ECMAScript1Parser.CaseBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#caseBlock}.
	 * @param ctx the parse tree
	 */
	void exitCaseBlock(@NotNull ECMAScript1Parser.CaseBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#caseClauses}.
	 * @param ctx the parse tree
	 */
	void enterCaseClauses(@NotNull ECMAScript1Parser.CaseClausesContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#caseClauses}.
	 * @param ctx the parse tree
	 */
	void exitCaseClauses(@NotNull ECMAScript1Parser.CaseClausesContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#caseClause}.
	 * @param ctx the parse tree
	 */
	void enterCaseClause(@NotNull ECMAScript1Parser.CaseClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#caseClause}.
	 * @param ctx the parse tree
	 */
	void exitCaseClause(@NotNull ECMAScript1Parser.CaseClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#defaultClause}.
	 * @param ctx the parse tree
	 */
	void enterDefaultClause(@NotNull ECMAScript1Parser.DefaultClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#defaultClause}.
	 * @param ctx the parse tree
	 */
	void exitDefaultClause(@NotNull ECMAScript1Parser.DefaultClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#throwStatement}.
	 * @param ctx the parse tree
	 */
	void enterThrowStatement(@NotNull ECMAScript1Parser.ThrowStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#throwStatement}.
	 * @param ctx the parse tree
	 */
	void exitThrowStatement(@NotNull ECMAScript1Parser.ThrowStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#tryStatement}.
	 * @param ctx the parse tree
	 */
	void enterTryStatement(@NotNull ECMAScript1Parser.TryStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#tryStatement}.
	 * @param ctx the parse tree
	 */
	void exitTryStatement(@NotNull ECMAScript1Parser.TryStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#catchClause}.
	 * @param ctx the parse tree
	 */
	void enterCatchClause(@NotNull ECMAScript1Parser.CatchClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#catchClause}.
	 * @param ctx the parse tree
	 */
	void exitCatchClause(@NotNull ECMAScript1Parser.CatchClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#finallyClause}.
	 * @param ctx the parse tree
	 */
	void enterFinallyClause(@NotNull ECMAScript1Parser.FinallyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#finallyClause}.
	 * @param ctx the parse tree
	 */
	void exitFinallyClause(@NotNull ECMAScript1Parser.FinallyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(@NotNull ECMAScript1Parser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(@NotNull ECMAScript1Parser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#expressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterExpressionNoIn(@NotNull ECMAScript1Parser.ExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#expressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitExpressionNoIn(@NotNull ECMAScript1Parser.ExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression(@NotNull ECMAScript1Parser.AssignmentExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression(@NotNull ECMAScript1Parser.AssignmentExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#assignmentExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpressionNoIn(@NotNull ECMAScript1Parser.AssignmentExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#assignmentExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpressionNoIn(@NotNull ECMAScript1Parser.AssignmentExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#newExpression}.
	 * @param ctx the parse tree
	 */
	void enterNewExpression(@NotNull ECMAScript1Parser.NewExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#newExpression}.
	 * @param ctx the parse tree
	 */
	void exitNewExpression(@NotNull ECMAScript1Parser.NewExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#memberExpression}.
	 * @param ctx the parse tree
	 */
	void enterMemberExpression(@NotNull ECMAScript1Parser.MemberExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#memberExpression}.
	 * @param ctx the parse tree
	 */
	void exitMemberExpression(@NotNull ECMAScript1Parser.MemberExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#callExpression}.
	 * @param ctx the parse tree
	 */
	void enterCallExpression(@NotNull ECMAScript1Parser.CallExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#callExpression}.
	 * @param ctx the parse tree
	 */
	void exitCallExpression(@NotNull ECMAScript1Parser.CallExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(@NotNull ECMAScript1Parser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(@NotNull ECMAScript1Parser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(@NotNull ECMAScript1Parser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(@NotNull ECMAScript1Parser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#leftHandSideExpression}.
	 * @param ctx the parse tree
	 */
	void enterLeftHandSideExpression(@NotNull ECMAScript1Parser.LeftHandSideExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#leftHandSideExpression}.
	 * @param ctx the parse tree
	 */
	void exitLeftHandSideExpression(@NotNull ECMAScript1Parser.LeftHandSideExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#indexSuffix}.
	 * @param ctx the parse tree
	 */
	void enterIndexSuffix(@NotNull ECMAScript1Parser.IndexSuffixContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#indexSuffix}.
	 * @param ctx the parse tree
	 */
	void exitIndexSuffix(@NotNull ECMAScript1Parser.IndexSuffixContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#propertyReferenceSuffix}.
	 * @param ctx the parse tree
	 */
	void enterPropertyReferenceSuffix(@NotNull ECMAScript1Parser.PropertyReferenceSuffixContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#propertyReferenceSuffix}.
	 * @param ctx the parse tree
	 */
	void exitPropertyReferenceSuffix(@NotNull ECMAScript1Parser.PropertyReferenceSuffixContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentOperator(@NotNull ECMAScript1Parser.AssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentOperator(@NotNull ECMAScript1Parser.AssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#conditionalExpression}.
	 * @param ctx the parse tree
	 */
	void enterConditionalExpression(@NotNull ECMAScript1Parser.ConditionalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#conditionalExpression}.
	 * @param ctx the parse tree
	 */
	void exitConditionalExpression(@NotNull ECMAScript1Parser.ConditionalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#conditionalExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterConditionalExpressionNoIn(@NotNull ECMAScript1Parser.ConditionalExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#conditionalExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitConditionalExpressionNoIn(@NotNull ECMAScript1Parser.ConditionalExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#logicalORExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalORExpression(@NotNull ECMAScript1Parser.LogicalORExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#logicalORExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalORExpression(@NotNull ECMAScript1Parser.LogicalORExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#logicalORExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterLogicalORExpressionNoIn(@NotNull ECMAScript1Parser.LogicalORExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#logicalORExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitLogicalORExpressionNoIn(@NotNull ECMAScript1Parser.LogicalORExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#logicalANDExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalANDExpression(@NotNull ECMAScript1Parser.LogicalANDExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#logicalANDExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalANDExpression(@NotNull ECMAScript1Parser.LogicalANDExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#logicalANDExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterLogicalANDExpressionNoIn(@NotNull ECMAScript1Parser.LogicalANDExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#logicalANDExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitLogicalANDExpressionNoIn(@NotNull ECMAScript1Parser.LogicalANDExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#bitwiseORExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseORExpression(@NotNull ECMAScript1Parser.BitwiseORExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#bitwiseORExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseORExpression(@NotNull ECMAScript1Parser.BitwiseORExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#bitwiseORExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseORExpressionNoIn(@NotNull ECMAScript1Parser.BitwiseORExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#bitwiseORExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseORExpressionNoIn(@NotNull ECMAScript1Parser.BitwiseORExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#bitwiseXORExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseXORExpression(@NotNull ECMAScript1Parser.BitwiseXORExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#bitwiseXORExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseXORExpression(@NotNull ECMAScript1Parser.BitwiseXORExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#bitwiseXORExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseXORExpressionNoIn(@NotNull ECMAScript1Parser.BitwiseXORExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#bitwiseXORExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseXORExpressionNoIn(@NotNull ECMAScript1Parser.BitwiseXORExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#bitwiseANDExpression}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseANDExpression(@NotNull ECMAScript1Parser.BitwiseANDExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#bitwiseANDExpression}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseANDExpression(@NotNull ECMAScript1Parser.BitwiseANDExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#bitwiseANDExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseANDExpressionNoIn(@NotNull ECMAScript1Parser.BitwiseANDExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#bitwiseANDExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseANDExpressionNoIn(@NotNull ECMAScript1Parser.BitwiseANDExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpression(@NotNull ECMAScript1Parser.EqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpression(@NotNull ECMAScript1Parser.EqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#equalityExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpressionNoIn(@NotNull ECMAScript1Parser.EqualityExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#equalityExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpressionNoIn(@NotNull ECMAScript1Parser.EqualityExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpression(@NotNull ECMAScript1Parser.RelationalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpression(@NotNull ECMAScript1Parser.RelationalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#relationalExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpressionNoIn(@NotNull ECMAScript1Parser.RelationalExpressionNoInContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#relationalExpressionNoIn}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpressionNoIn(@NotNull ECMAScript1Parser.RelationalExpressionNoInContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void enterShiftExpression(@NotNull ECMAScript1Parser.ShiftExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#shiftExpression}.
	 * @param ctx the parse tree
	 */
	void exitShiftExpression(@NotNull ECMAScript1Parser.ShiftExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(@NotNull ECMAScript1Parser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(@NotNull ECMAScript1Parser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(@NotNull ECMAScript1Parser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(@NotNull ECMAScript1Parser.MultiplicativeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpression(@NotNull ECMAScript1Parser.UnaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpression(@NotNull ECMAScript1Parser.UnaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#postfixExpression}.
	 * @param ctx the parse tree
	 */
	void enterPostfixExpression(@NotNull ECMAScript1Parser.PostfixExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#postfixExpression}.
	 * @param ctx the parse tree
	 */
	void exitPostfixExpression(@NotNull ECMAScript1Parser.PostfixExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpression(@NotNull ECMAScript1Parser.PrimaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpression(@NotNull ECMAScript1Parser.PrimaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void enterArrayLiteral(@NotNull ECMAScript1Parser.ArrayLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void exitArrayLiteral(@NotNull ECMAScript1Parser.ArrayLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#elementList}.
	 * @param ctx the parse tree
	 */
	void enterElementList(@NotNull ECMAScript1Parser.ElementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#elementList}.
	 * @param ctx the parse tree
	 */
	void exitElementList(@NotNull ECMAScript1Parser.ElementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#elision}.
	 * @param ctx the parse tree
	 */
	void enterElision(@NotNull ECMAScript1Parser.ElisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#elision}.
	 * @param ctx the parse tree
	 */
	void exitElision(@NotNull ECMAScript1Parser.ElisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#objectLiteral}.
	 * @param ctx the parse tree
	 */
	void enterObjectLiteral(@NotNull ECMAScript1Parser.ObjectLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#objectLiteral}.
	 * @param ctx the parse tree
	 */
	void exitObjectLiteral(@NotNull ECMAScript1Parser.ObjectLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#propertyNameAndValueList}.
	 * @param ctx the parse tree
	 */
	void enterPropertyNameAndValueList(@NotNull ECMAScript1Parser.PropertyNameAndValueListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#propertyNameAndValueList}.
	 * @param ctx the parse tree
	 */
	void exitPropertyNameAndValueList(@NotNull ECMAScript1Parser.PropertyNameAndValueListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#propertyName}.
	 * @param ctx the parse tree
	 */
	void enterPropertyName(@NotNull ECMAScript1Parser.PropertyNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#propertyName}.
	 * @param ctx the parse tree
	 */
	void exitPropertyName(@NotNull ECMAScript1Parser.PropertyNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void enterPropertyAssignment(@NotNull ECMAScript1Parser.PropertyAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void exitPropertyAssignment(@NotNull ECMAScript1Parser.PropertyAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(@NotNull ECMAScript1Parser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(@NotNull ECMAScript1Parser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScript1Parser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(@NotNull ECMAScript1Parser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScript1Parser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(@NotNull ECMAScript1Parser.IdentifierContext ctx);
}