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
	 * Enter a parse tree produced by {@link ECMAScriptParser#identifierReference}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierReference(@NotNull ECMAScriptParser.IdentifierReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#identifierReference}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierReference(@NotNull ECMAScriptParser.IdentifierReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingIdentifier}.
	 * @param ctx the parse tree
	 */
	void enterBindingIdentifier(@NotNull ECMAScriptParser.BindingIdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingIdentifier}.
	 * @param ctx the parse tree
	 */
	void exitBindingIdentifier(@NotNull ECMAScriptParser.BindingIdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#labelIdentifier}.
	 * @param ctx the parse tree
	 */
	void enterLabelIdentifier(@NotNull ECMAScriptParser.LabelIdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#labelIdentifier}.
	 * @param ctx the parse tree
	 */
	void exitLabelIdentifier(@NotNull ECMAScriptParser.LabelIdentifierContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#coverParenthesizedExpressionAndArrowParameterList}.
	 * @param ctx the parse tree
	 */
	void enterCoverParenthesizedExpressionAndArrowParameterList(@NotNull ECMAScriptParser.CoverParenthesizedExpressionAndArrowParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#coverParenthesizedExpressionAndArrowParameterList}.
	 * @param ctx the parse tree
	 */
	void exitCoverParenthesizedExpressionAndArrowParameterList(@NotNull ECMAScriptParser.CoverParenthesizedExpressionAndArrowParameterListContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#spreadElement}.
	 * @param ctx the parse tree
	 */
	void enterSpreadElement(@NotNull ECMAScriptParser.SpreadElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#spreadElement}.
	 * @param ctx the parse tree
	 */
	void exitSpreadElement(@NotNull ECMAScriptParser.SpreadElementContext ctx);
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
	 * Enter a parse tree produced by the {@code PropertyExpressionAssignment2}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void enterPropertyExpressionAssignment2(@NotNull ECMAScriptParser.PropertyExpressionAssignment2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code PropertyExpressionAssignment2}
	 * labeled alternative in {@link ECMAScriptParser#propertyAssignment}.
	 * @param ctx the parse tree
	 */
	void exitPropertyExpressionAssignment2(@NotNull ECMAScriptParser.PropertyExpressionAssignment2Context ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#literalPropertyName}.
	 * @param ctx the parse tree
	 */
	void enterLiteralPropertyName(@NotNull ECMAScriptParser.LiteralPropertyNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#literalPropertyName}.
	 * @param ctx the parse tree
	 */
	void exitLiteralPropertyName(@NotNull ECMAScriptParser.LiteralPropertyNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#computedPropertyName}.
	 * @param ctx the parse tree
	 */
	void enterComputedPropertyName(@NotNull ECMAScriptParser.ComputedPropertyNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#computedPropertyName}.
	 * @param ctx the parse tree
	 */
	void exitComputedPropertyName(@NotNull ECMAScriptParser.ComputedPropertyNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#coverInitializedName}.
	 * @param ctx the parse tree
	 */
	void enterCoverInitializedName(@NotNull ECMAScriptParser.CoverInitializedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#coverInitializedName}.
	 * @param ctx the parse tree
	 */
	void exitCoverInitializedName(@NotNull ECMAScriptParser.CoverInitializedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#initializer}.
	 * @param ctx the parse tree
	 */
	void enterInitializer(@NotNull ECMAScriptParser.InitializerContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#initializer}.
	 * @param ctx the parse tree
	 */
	void exitInitializer(@NotNull ECMAScriptParser.InitializerContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#templateLiteral}.
	 * @param ctx the parse tree
	 */
	void enterTemplateLiteral(@NotNull ECMAScriptParser.TemplateLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#templateLiteral}.
	 * @param ctx the parse tree
	 */
	void exitTemplateLiteral(@NotNull ECMAScriptParser.TemplateLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#templateSpans}.
	 * @param ctx the parse tree
	 */
	void enterTemplateSpans(@NotNull ECMAScriptParser.TemplateSpansContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#templateSpans}.
	 * @param ctx the parse tree
	 */
	void exitTemplateSpans(@NotNull ECMAScriptParser.TemplateSpansContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#templateMiddleList}.
	 * @param ctx the parse tree
	 */
	void enterTemplateMiddleList(@NotNull ECMAScriptParser.TemplateMiddleListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#templateMiddleList}.
	 * @param ctx the parse tree
	 */
	void exitTemplateMiddleList(@NotNull ECMAScriptParser.TemplateMiddleListContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#superProperty}.
	 * @param ctx the parse tree
	 */
	void enterSuperProperty(@NotNull ECMAScriptParser.SuperPropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#superProperty}.
	 * @param ctx the parse tree
	 */
	void exitSuperProperty(@NotNull ECMAScriptParser.SuperPropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#metaProperty}.
	 * @param ctx the parse tree
	 */
	void enterMetaProperty(@NotNull ECMAScriptParser.MetaPropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#metaProperty}.
	 * @param ctx the parse tree
	 */
	void exitMetaProperty(@NotNull ECMAScriptParser.MetaPropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#newTarget}.
	 * @param ctx the parse tree
	 */
	void enterNewTarget(@NotNull ECMAScriptParser.NewTargetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#newTarget}.
	 * @param ctx the parse tree
	 */
	void exitNewTarget(@NotNull ECMAScriptParser.NewTargetContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#superCall}.
	 * @param ctx the parse tree
	 */
	void enterSuperCall(@NotNull ECMAScriptParser.SuperCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#superCall}.
	 * @param ctx the parse tree
	 */
	void exitSuperCall(@NotNull ECMAScriptParser.SuperCallContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression(@NotNull ECMAScriptParser.AssignmentExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression(@NotNull ECMAScriptParser.AssignmentExpressionContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(@NotNull ECMAScriptParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(@NotNull ECMAScriptParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#hoistableStatement}.
	 * @param ctx the parse tree
	 */
	void enterHoistableStatement(@NotNull ECMAScriptParser.HoistableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#hoistableStatement}.
	 * @param ctx the parse tree
	 */
	void exitHoistableStatement(@NotNull ECMAScriptParser.HoistableStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#breakableStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakableStatement(@NotNull ECMAScriptParser.BreakableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#breakableStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakableStatement(@NotNull ECMAScriptParser.BreakableStatementContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#statementListItem}.
	 * @param ctx the parse tree
	 */
	void enterStatementListItem(@NotNull ECMAScriptParser.StatementListItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#statementListItem}.
	 * @param ctx the parse tree
	 */
	void exitStatementListItem(@NotNull ECMAScriptParser.StatementListItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#lexicalDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterLexicalDeclaration(@NotNull ECMAScriptParser.LexicalDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#lexicalDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitLexicalDeclaration(@NotNull ECMAScriptParser.LexicalDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#letOrConst}.
	 * @param ctx the parse tree
	 */
	void enterLetOrConst(@NotNull ECMAScriptParser.LetOrConstContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#letOrConst}.
	 * @param ctx the parse tree
	 */
	void exitLetOrConst(@NotNull ECMAScriptParser.LetOrConstContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingList}.
	 * @param ctx the parse tree
	 */
	void enterBindingList(@NotNull ECMAScriptParser.BindingListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingList}.
	 * @param ctx the parse tree
	 */
	void exitBindingList(@NotNull ECMAScriptParser.BindingListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#lexicalBinding}.
	 * @param ctx the parse tree
	 */
	void enterLexicalBinding(@NotNull ECMAScriptParser.LexicalBindingContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#lexicalBinding}.
	 * @param ctx the parse tree
	 */
	void exitLexicalBinding(@NotNull ECMAScriptParser.LexicalBindingContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingPattern}.
	 * @param ctx the parse tree
	 */
	void enterBindingPattern(@NotNull ECMAScriptParser.BindingPatternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingPattern}.
	 * @param ctx the parse tree
	 */
	void exitBindingPattern(@NotNull ECMAScriptParser.BindingPatternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#objectBindingPattern}.
	 * @param ctx the parse tree
	 */
	void enterObjectBindingPattern(@NotNull ECMAScriptParser.ObjectBindingPatternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#objectBindingPattern}.
	 * @param ctx the parse tree
	 */
	void exitObjectBindingPattern(@NotNull ECMAScriptParser.ObjectBindingPatternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#arrayBindingPattern}.
	 * @param ctx the parse tree
	 */
	void enterArrayBindingPattern(@NotNull ECMAScriptParser.ArrayBindingPatternContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#arrayBindingPattern}.
	 * @param ctx the parse tree
	 */
	void exitArrayBindingPattern(@NotNull ECMAScriptParser.ArrayBindingPatternContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingPropertyList}.
	 * @param ctx the parse tree
	 */
	void enterBindingPropertyList(@NotNull ECMAScriptParser.BindingPropertyListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingPropertyList}.
	 * @param ctx the parse tree
	 */
	void exitBindingPropertyList(@NotNull ECMAScriptParser.BindingPropertyListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingElementList}.
	 * @param ctx the parse tree
	 */
	void enterBindingElementList(@NotNull ECMAScriptParser.BindingElementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingElementList}.
	 * @param ctx the parse tree
	 */
	void exitBindingElementList(@NotNull ECMAScriptParser.BindingElementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingElisionElement}.
	 * @param ctx the parse tree
	 */
	void enterBindingElisionElement(@NotNull ECMAScriptParser.BindingElisionElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingElisionElement}.
	 * @param ctx the parse tree
	 */
	void exitBindingElisionElement(@NotNull ECMAScriptParser.BindingElisionElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingProperty}.
	 * @param ctx the parse tree
	 */
	void enterBindingProperty(@NotNull ECMAScriptParser.BindingPropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingProperty}.
	 * @param ctx the parse tree
	 */
	void exitBindingProperty(@NotNull ECMAScriptParser.BindingPropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingElement}.
	 * @param ctx the parse tree
	 */
	void enterBindingElement(@NotNull ECMAScriptParser.BindingElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingElement}.
	 * @param ctx the parse tree
	 */
	void exitBindingElement(@NotNull ECMAScriptParser.BindingElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#singleNameBinding}.
	 * @param ctx the parse tree
	 */
	void enterSingleNameBinding(@NotNull ECMAScriptParser.SingleNameBindingContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#singleNameBinding}.
	 * @param ctx the parse tree
	 */
	void exitSingleNameBinding(@NotNull ECMAScriptParser.SingleNameBindingContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#bindingRestElement}.
	 * @param ctx the parse tree
	 */
	void enterBindingRestElement(@NotNull ECMAScriptParser.BindingRestElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#bindingRestElement}.
	 * @param ctx the parse tree
	 */
	void exitBindingRestElement(@NotNull ECMAScriptParser.BindingRestElementContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void enterIterationStatement(@NotNull ECMAScriptParser.IterationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#iterationStatement}.
	 * @param ctx the parse tree
	 */
	void exitIterationStatement(@NotNull ECMAScriptParser.IterationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#forDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterForDeclaration(@NotNull ECMAScriptParser.ForDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#forDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitForDeclaration(@NotNull ECMAScriptParser.ForDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#forBinding}.
	 * @param ctx the parse tree
	 */
	void enterForBinding(@NotNull ECMAScriptParser.ForBindingContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#forBinding}.
	 * @param ctx the parse tree
	 */
	void exitForBinding(@NotNull ECMAScriptParser.ForBindingContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#labelledItem}.
	 * @param ctx the parse tree
	 */
	void enterLabelledItem(@NotNull ECMAScriptParser.LabelledItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#labelledItem}.
	 * @param ctx the parse tree
	 */
	void exitLabelledItem(@NotNull ECMAScriptParser.LabelledItemContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#catchParameter}.
	 * @param ctx the parse tree
	 */
	void enterCatchParameter(@NotNull ECMAScriptParser.CatchParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#catchParameter}.
	 * @param ctx the parse tree
	 */
	void exitCatchParameter(@NotNull ECMAScriptParser.CatchParameterContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#strictFormalParameters}.
	 * @param ctx the parse tree
	 */
	void enterStrictFormalParameters(@NotNull ECMAScriptParser.StrictFormalParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#strictFormalParameters}.
	 * @param ctx the parse tree
	 */
	void exitStrictFormalParameters(@NotNull ECMAScriptParser.StrictFormalParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#formalParameters}.
	 * @param ctx the parse tree
	 */
	void enterFormalParameters(@NotNull ECMAScriptParser.FormalParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#formalParameters}.
	 * @param ctx the parse tree
	 */
	void exitFormalParameters(@NotNull ECMAScriptParser.FormalParametersContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#formalsList}.
	 * @param ctx the parse tree
	 */
	void enterFormalsList(@NotNull ECMAScriptParser.FormalsListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#formalsList}.
	 * @param ctx the parse tree
	 */
	void exitFormalsList(@NotNull ECMAScriptParser.FormalsListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#functionRestParameter}.
	 * @param ctx the parse tree
	 */
	void enterFunctionRestParameter(@NotNull ECMAScriptParser.FunctionRestParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#functionRestParameter}.
	 * @param ctx the parse tree
	 */
	void exitFunctionRestParameter(@NotNull ECMAScriptParser.FunctionRestParameterContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#functionStatementList}.
	 * @param ctx the parse tree
	 */
	void enterFunctionStatementList(@NotNull ECMAScriptParser.FunctionStatementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#functionStatementList}.
	 * @param ctx the parse tree
	 */
	void exitFunctionStatementList(@NotNull ECMAScriptParser.FunctionStatementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#arrowFunction}.
	 * @param ctx the parse tree
	 */
	void enterArrowFunction(@NotNull ECMAScriptParser.ArrowFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#arrowFunction}.
	 * @param ctx the parse tree
	 */
	void exitArrowFunction(@NotNull ECMAScriptParser.ArrowFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#arrowParameters}.
	 * @param ctx the parse tree
	 */
	void enterArrowParameters(@NotNull ECMAScriptParser.ArrowParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#arrowParameters}.
	 * @param ctx the parse tree
	 */
	void exitArrowParameters(@NotNull ECMAScriptParser.ArrowParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#conciseBody}.
	 * @param ctx the parse tree
	 */
	void enterConciseBody(@NotNull ECMAScriptParser.ConciseBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#conciseBody}.
	 * @param ctx the parse tree
	 */
	void exitConciseBody(@NotNull ECMAScriptParser.ConciseBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#arrowFormalParameters}.
	 * @param ctx the parse tree
	 */
	void enterArrowFormalParameters(@NotNull ECMAScriptParser.ArrowFormalParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#arrowFormalParameters}.
	 * @param ctx the parse tree
	 */
	void exitArrowFormalParameters(@NotNull ECMAScriptParser.ArrowFormalParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#methodDefinition}.
	 * @param ctx the parse tree
	 */
	void enterMethodDefinition(@NotNull ECMAScriptParser.MethodDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#methodDefinition}.
	 * @param ctx the parse tree
	 */
	void exitMethodDefinition(@NotNull ECMAScriptParser.MethodDefinitionContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#generatorMethod}.
	 * @param ctx the parse tree
	 */
	void enterGeneratorMethod(@NotNull ECMAScriptParser.GeneratorMethodContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#generatorMethod}.
	 * @param ctx the parse tree
	 */
	void exitGeneratorMethod(@NotNull ECMAScriptParser.GeneratorMethodContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#generatorDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterGeneratorDeclaration(@NotNull ECMAScriptParser.GeneratorDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#generatorDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitGeneratorDeclaration(@NotNull ECMAScriptParser.GeneratorDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#generatorExpression}.
	 * @param ctx the parse tree
	 */
	void enterGeneratorExpression(@NotNull ECMAScriptParser.GeneratorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#generatorExpression}.
	 * @param ctx the parse tree
	 */
	void exitGeneratorExpression(@NotNull ECMAScriptParser.GeneratorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#generatorBody}.
	 * @param ctx the parse tree
	 */
	void enterGeneratorBody(@NotNull ECMAScriptParser.GeneratorBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#generatorBody}.
	 * @param ctx the parse tree
	 */
	void exitGeneratorBody(@NotNull ECMAScriptParser.GeneratorBodyContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#classDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterClassDeclaration(@NotNull ECMAScriptParser.ClassDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#classDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitClassDeclaration(@NotNull ECMAScriptParser.ClassDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#classExpression}.
	 * @param ctx the parse tree
	 */
	void enterClassExpression(@NotNull ECMAScriptParser.ClassExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#classExpression}.
	 * @param ctx the parse tree
	 */
	void exitClassExpression(@NotNull ECMAScriptParser.ClassExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#classTail}.
	 * @param ctx the parse tree
	 */
	void enterClassTail(@NotNull ECMAScriptParser.ClassTailContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#classTail}.
	 * @param ctx the parse tree
	 */
	void exitClassTail(@NotNull ECMAScriptParser.ClassTailContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#classHeritage}.
	 * @param ctx the parse tree
	 */
	void enterClassHeritage(@NotNull ECMAScriptParser.ClassHeritageContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#classHeritage}.
	 * @param ctx the parse tree
	 */
	void exitClassHeritage(@NotNull ECMAScriptParser.ClassHeritageContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#classBody}.
	 * @param ctx the parse tree
	 */
	void enterClassBody(@NotNull ECMAScriptParser.ClassBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#classBody}.
	 * @param ctx the parse tree
	 */
	void exitClassBody(@NotNull ECMAScriptParser.ClassBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#classElementList}.
	 * @param ctx the parse tree
	 */
	void enterClassElementList(@NotNull ECMAScriptParser.ClassElementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#classElementList}.
	 * @param ctx the parse tree
	 */
	void exitClassElementList(@NotNull ECMAScriptParser.ClassElementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ECMAScriptParser#classElement}.
	 * @param ctx the parse tree
	 */
	void enterClassElement(@NotNull ECMAScriptParser.ClassElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#classElement}.
	 * @param ctx the parse tree
	 */
	void exitClassElement(@NotNull ECMAScriptParser.ClassElementContext ctx);
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
	 * Enter a parse tree produced by {@link ECMAScriptParser#commonToken}.
	 * @param ctx the parse tree
	 */
	void enterCommonToken(@NotNull ECMAScriptParser.CommonTokenContext ctx);
	/**
	 * Exit a parse tree produced by {@link ECMAScriptParser#commonToken}.
	 * @param ctx the parse tree
	 */
	void exitCommonToken(@NotNull ECMAScriptParser.CommonTokenContext ctx);
}