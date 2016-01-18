// Generated from ECMAScript.g4 by ANTLR 4.5
package langparser;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ECMAScriptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.5", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, RegularExpressionLiteral=34, LineTerminator=35, OpenBracket=36, 
		CloseBracket=37, OpenParen=38, CloseParen=39, OpenBrace=40, CloseBrace=41, 
		SemiColon=42, Comma=43, Assign=44, QuestionMark=45, Colon=46, Dot=47, 
		PlusPlus=48, MinusMinus=49, Plus=50, Minus=51, BitNot=52, Not=53, Multiply=54, 
		Divide=55, Modulus=56, RightShiftArithmetic=57, LeftShiftArithmetic=58, 
		RightShiftLogical=59, LessThan=60, MoreThan=61, LessThanEquals=62, GreaterThanEquals=63, 
		Equals=64, NotEquals=65, IdentityEquals=66, IdentityNotEquals=67, BitAnd=68, 
		BitXOr=69, BitOr=70, And=71, Or=72, MultiplyAssign=73, DivideAssign=74, 
		ModulusAssign=75, PlusAssign=76, MinusAssign=77, LeftShiftArithmeticAssign=78, 
		RightShiftArithmeticAssign=79, RightShiftLogicalAssign=80, BitAndAssign=81, 
		BitXorAssign=82, BitOrAssign=83, NullLiteral=84, BooleanLiteral=85, DecimalLiteral=86, 
		HexIntegerLiteral=87, OctalIntegerLiteral=88, BinaryLiteral=89, Break=90, 
		Do=91, Instanceof=92, Typeof=93, Case=94, Else=95, New=96, Var=97, Catch=98, 
		Finally=99, Return=100, Void=101, Continue=102, For=103, Switch=104, While=105, 
		Debugger=106, Function=107, This=108, With=109, Default=110, If=111, Throw=112, 
		Delete=113, In=114, Try=115, Of=116, Each=117, Class=118, Enum=119, Extends=120, 
		Super=121, Const=122, Export=123, Import=124, Implements=125, Let=126, 
		Private=127, Public=128, Interface=129, Package=130, Protected=131, Static=132, 
		Yield=133, Identifier=134, StringLiteral=135, WhiteSpaces=136, MultiLineComment=137, 
		SingleLineComment=138, UnexpectedCharacter=139;
	public static final int
		RULE_program = 0, RULE_statementListItem = 1, RULE_functionDeclaration = 2, 
		RULE_classDeclaration = 3, RULE_classTail = 4, RULE_classHeritage = 5, 
		RULE_classBody = 6, RULE_classElement = 7, RULE_statement = 8, RULE_yieldExpression = 9, 
		RULE_block = 10, RULE_statementList = 11, RULE_variableStatement = 12, 
		RULE_variableDeclarationList = 13, RULE_variableDeclaration = 14, RULE_identifierBinding = 15, 
		RULE_identifierReference = 16, RULE_identifierPattern = 17, RULE_arrayBindingPattern = 18, 
		RULE_restElement = 19, RULE_bindingElementList = 20, RULE_objectBindingPattern = 21, 
		RULE_argumentBindingPattern = 22, RULE_bindingPropertyList = 23, RULE_bindingProperty = 24, 
		RULE_initialiser = 25, RULE_emptyStatement = 26, RULE_expressionStatement = 27, 
		RULE_ifStatement = 28, RULE_elseStatement = 29, RULE_iterationStatement = 30, 
		RULE_continueStatement = 31, RULE_breakStatement = 32, RULE_returnStatement = 33, 
		RULE_withStatement = 34, RULE_switchStatement = 35, RULE_caseBlock = 36, 
		RULE_caseClauses = 37, RULE_caseClause = 38, RULE_defaultClause = 39, 
		RULE_labelledStatement = 40, RULE_throwStatement = 41, RULE_tryStatement = 42, 
		RULE_catchProduction = 43, RULE_finallyProduction = 44, RULE_debuggerStatement = 45, 
		RULE_formalParameterList = 46, RULE_formalParameters = 47, RULE_formalParameter = 48, 
		RULE_functionBody = 49, RULE_arrayLiteral = 50, RULE_elementList = 51, 
		RULE_elision = 52, RULE_objectLiteral = 53, RULE_propertyNameAndValueList = 54, 
		RULE_propertyAssignment = 55, RULE_methodDefinition = 56, RULE_propertyName = 57, 
		RULE_propertySetParameterList = 58, RULE_arguments = 59, RULE_argumentList = 60, 
		RULE_arrowFunction = 61, RULE_arrowParameters = 62, RULE_conciseBody = 63, 
		RULE_expression = 64, RULE_assignmentExpression = 65, RULE_conditionalExpression = 66, 
		RULE_leftHandSideExpression = 67, RULE_callExpression = 68, RULE_newExpression = 69, 
		RULE_memberExpression = 70, RULE_functionExpression = 71, RULE_primaryExpression = 72, 
		RULE_assignmentOperator = 73, RULE_literal = 74, RULE_numericLiteral = 75, 
		RULE_identifierName = 76, RULE_reservedWord = 77, RULE_eos = 78, RULE_eof = 79;
	public static final String[] ruleNames = {
		"program", "statementListItem", "functionDeclaration", "classDeclaration", 
		"classTail", "classHeritage", "classBody", "classElement", "statement", 
		"yieldExpression", "block", "statementList", "variableStatement", "variableDeclarationList", 
		"variableDeclaration", "identifierBinding", "identifierReference", "identifierPattern", 
		"arrayBindingPattern", "restElement", "bindingElementList", "objectBindingPattern", 
		"argumentBindingPattern", "bindingPropertyList", "bindingProperty", "initialiser", 
		"emptyStatement", "expressionStatement", "ifStatement", "elseStatement", 
		"iterationStatement", "continueStatement", "breakStatement", "returnStatement", 
		"withStatement", "switchStatement", "caseBlock", "caseClauses", "caseClause", 
		"defaultClause", "labelledStatement", "throwStatement", "tryStatement", 
		"catchProduction", "finallyProduction", "debuggerStatement", "formalParameterList", 
		"formalParameters", "formalParameter", "functionBody", "arrayLiteral", 
		"elementList", "elision", "objectLiteral", "propertyNameAndValueList", 
		"propertyAssignment", "methodDefinition", "propertyName", "propertySetParameterList", 
		"arguments", "argumentList", "arrowFunction", "arrowParameters", "conciseBody", 
		"expression", "assignmentExpression", "conditionalExpression", "leftHandSideExpression", 
		"callExpression", "newExpression", "memberExpression", "functionExpression", 
		"primaryExpression", "assignmentOperator", "literal", "numericLiteral", 
		"identifierName", "reservedWord", "eos", "eof"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'function'", "'static'", "'yield'", "'var'", "'let'", "'...'", 
		"'if'", "'else'", "'do'", "'while'", "'for'", "'each'", "'in'", "'of'", 
		"'continue'", "'break'", "'return'", "'with'", "'switch'", "'case'", "'default'", 
		"'throw'", "'try'", "'catch'", "'finally'", "'debugger'", "'=>'", "'instanceof'", 
		"'delete'", "'void'", "'typeof'", "'new'", "'this'", null, null, "'['", 
		"']'", "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'?'", "':'", 
		"'.'", "'++'", "'--'", "'+'", "'-'", "'~'", "'!'", "'*'", "'/'", "'%'", 
		"'>>'", "'<<'", "'>>>'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
		"'==='", "'!=='", "'&'", "'^'", "'|'", "'&&'", "'||'", "'*='", "'/='", 
		"'%='", "'+='", "'-='", "'<<='", "'>>='", "'>>>='", "'&='", "'^='", "'|='", 
		"'null'", null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, "'class'", 
		"'enum'", "'extends'", "'super'", "'const'", "'export'", "'import'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, "RegularExpressionLiteral", 
		"LineTerminator", "OpenBracket", "CloseBracket", "OpenParen", "CloseParen", 
		"OpenBrace", "CloseBrace", "SemiColon", "Comma", "Assign", "QuestionMark", 
		"Colon", "Dot", "PlusPlus", "MinusMinus", "Plus", "Minus", "BitNot", "Not", 
		"Multiply", "Divide", "Modulus", "RightShiftArithmetic", "LeftShiftArithmetic", 
		"RightShiftLogical", "LessThan", "MoreThan", "LessThanEquals", "GreaterThanEquals", 
		"Equals", "NotEquals", "IdentityEquals", "IdentityNotEquals", "BitAnd", 
		"BitXOr", "BitOr", "And", "Or", "MultiplyAssign", "DivideAssign", "ModulusAssign", 
		"PlusAssign", "MinusAssign", "LeftShiftArithmeticAssign", "RightShiftArithmeticAssign", 
		"RightShiftLogicalAssign", "BitAndAssign", "BitXorAssign", "BitOrAssign", 
		"NullLiteral", "BooleanLiteral", "DecimalLiteral", "HexIntegerLiteral", 
		"OctalIntegerLiteral", "BinaryLiteral", "Break", "Do", "Instanceof", "Typeof", 
		"Case", "Else", "New", "Var", "Catch", "Finally", "Return", "Void", "Continue", 
		"For", "Switch", "While", "Debugger", "Function", "This", "With", "Default", 
		"If", "Throw", "Delete", "In", "Try", "Of", "Each", "Class", "Enum", "Extends", 
		"Super", "Const", "Export", "Import", "Implements", "Let", "Private", 
		"Public", "Interface", "Package", "Protected", "Static", "Yield", "Identifier", 
		"StringLiteral", "WhiteSpaces", "MultiLineComment", "SingleLineComment", 
		"UnexpectedCharacter"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override
	@NotNull
	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ECMAScript.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


	  
	    private boolean here(final int type) {

	        int possibleIndexEosToken = this.getCurrentToken().getTokenIndex() - 1;
	        Token ahead = _input.get(possibleIndexEosToken);

	        return (ahead.getChannel() == Lexer.HIDDEN) && (ahead.getType() == type);
	    }

	    private boolean lineTerminatorAhead() {

	        int possibleIndexEosToken = this.getCurrentToken().getTokenIndex() - 1;
	        Token ahead = _input.get(possibleIndexEosToken);

	        if (ahead.getChannel() != Lexer.HIDDEN) {
	            return false;
	        }

	        String text = ahead.getText();
	        int type = ahead.getType();

	        return (type == MultiLineComment && (text.contains("\r") || text.contains("\n"))) ||
	                (type == LineTerminator);
	    }                                
	    private boolean functionAhead() {

	        int possibleIndexEosToken = this.getCurrentToken().getTokenIndex() - 1;
	        Token ahead = _input.get(possibleIndexEosToken);

	        if (ahead.getChannel() != Lexer.HIDDEN) {
	            return false;
	        }

	        String text = ahead.getText();
	        int type = ahead.getType();

	        return (type == Function);
	    }                                


	public ECMAScriptParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ECMAScriptParser.EOF, 0); }
		public List<StatementListItemContext> statementListItem() {
			return getRuleContexts(StatementListItemContext.class);
		}
		public StatementListItemContext statementListItem(int i) {
			return getRuleContext(StatementListItemContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(160); 
					statementListItem();
					}
					} 
				}
				setState(165);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(166); 
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementListItemContext extends ParserRuleContext {
		public FunctionDeclarationContext functionDeclaration() {
			return getRuleContext(FunctionDeclarationContext.class,0);
		}
		public ClassDeclarationContext classDeclaration() {
			return getRuleContext(ClassDeclarationContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public StatementListItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementListItem; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterStatementListItem(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitStatementListItem(this);
		}
	}

	public final StatementListItemContext statementListItem() throws RecognitionException {
		StatementListItemContext _localctx = new StatementListItemContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statementListItem);
		try {
			setState(171);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(168); 
				functionDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(169); 
				classDeclaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(170); 
				statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDeclarationContext extends ParserRuleContext {
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public FunctionBodyContext functionBody() {
			return getRuleContext(FunctionBodyContext.class,0);
		}
		public FormalParameterListContext formalParameterList() {
			return getRuleContext(FormalParameterListContext.class,0);
		}
		public FunctionDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterFunctionDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitFunctionDeclaration(this);
		}
	}

	public final FunctionDeclarationContext functionDeclaration() throws RecognitionException {
		FunctionDeclarationContext _localctx = new FunctionDeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_functionDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173); 
			match(T__0);
			setState(174); 
			identifierName();
			setState(175); 
			match(OpenParen);
			setState(177);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << OpenBracket) | (1L << OpenBrace))) != 0) || _la==Identifier) {
				{
				setState(176); 
				formalParameterList();
				}
			}

			setState(179); 
			match(CloseParen);
			setState(180); 
			match(OpenBrace);
			setState(181); 
			functionBody();
			setState(182); 
			match(CloseBrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassDeclarationContext extends ParserRuleContext {
		public ClassTailContext classTail() {
			return getRuleContext(ClassTailContext.class,0);
		}
		public IdentifierReferenceContext identifierReference() {
			return getRuleContext(IdentifierReferenceContext.class,0);
		}
		public ClassDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterClassDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitClassDeclaration(this);
		}
	}

	public final ClassDeclarationContext classDeclaration() throws RecognitionException {
		ClassDeclarationContext _localctx = new ClassDeclarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_classDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184); 
			match(Class);
			setState(186);
			_la = _input.LA(1);
			if (_la==T__2 || _la==Identifier) {
				{
				setState(185); 
				identifierReference();
				}
			}

			setState(188); 
			classTail();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassTailContext extends ParserRuleContext {
		public ClassHeritageContext classHeritage() {
			return getRuleContext(ClassHeritageContext.class,0);
		}
		public ClassBodyContext classBody() {
			return getRuleContext(ClassBodyContext.class,0);
		}
		public ClassTailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classTail; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterClassTail(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitClassTail(this);
		}
	}

	public final ClassTailContext classTail() throws RecognitionException {
		ClassTailContext _localctx = new ClassTailContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_classTail);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190); 
			classHeritage();
			setState(191); 
			match(OpenBrace);
			setState(192); 
			classBody();
			setState(193); 
			match(CloseBrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassHeritageContext extends ParserRuleContext {
		public TerminalNode Extends() { return getToken(ECMAScriptParser.Extends, 0); }
		public ConditionalExpressionContext conditionalExpression() {
			return getRuleContext(ConditionalExpressionContext.class,0);
		}
		public ClassHeritageContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classHeritage; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterClassHeritage(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitClassHeritage(this);
		}
	}

	public final ClassHeritageContext classHeritage() throws RecognitionException {
		ClassHeritageContext _localctx = new ClassHeritageContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_classHeritage);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195); 
			match(Extends);
			setState(196); 
			conditionalExpression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassBodyContext extends ParserRuleContext {
		public List<ClassElementContext> classElement() {
			return getRuleContexts(ClassElementContext.class);
		}
		public ClassElementContext classElement(int i) {
			return getRuleContext(ClassElementContext.class,i);
		}
		public ClassBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterClassBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitClassBody(this);
		}
	}

	public final ClassBodyContext classBody() throws RecognitionException {
		ClassBodyContext _localctx = new ClassBodyContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_classBody);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(199); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(198); 
					classElement();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(201); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassElementContext extends ParserRuleContext {
		public MethodDefinitionContext methodDefinition() {
			return getRuleContext(MethodDefinitionContext.class,0);
		}
		public ClassElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classElement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterClassElement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitClassElement(this);
		}
	}

	public final ClassElementContext classElement() throws RecognitionException {
		ClassElementContext _localctx = new ClassElementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_classElement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(203); 
				match(T__1);
				}
				break;
			}
			setState(206); 
			methodDefinition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public VariableStatementContext variableStatement() {
			return getRuleContext(VariableStatementContext.class,0);
		}
		public EmptyStatementContext emptyStatement() {
			return getRuleContext(EmptyStatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public ExpressionStatementContext expressionStatement() {
			return getRuleContext(ExpressionStatementContext.class,0);
		}
		public IterationStatementContext iterationStatement() {
			return getRuleContext(IterationStatementContext.class,0);
		}
		public ContinueStatementContext continueStatement() {
			return getRuleContext(ContinueStatementContext.class,0);
		}
		public BreakStatementContext breakStatement() {
			return getRuleContext(BreakStatementContext.class,0);
		}
		public ReturnStatementContext returnStatement() {
			return getRuleContext(ReturnStatementContext.class,0);
		}
		public WithStatementContext withStatement() {
			return getRuleContext(WithStatementContext.class,0);
		}
		public LabelledStatementContext labelledStatement() {
			return getRuleContext(LabelledStatementContext.class,0);
		}
		public SwitchStatementContext switchStatement() {
			return getRuleContext(SwitchStatementContext.class,0);
		}
		public ThrowStatementContext throwStatement() {
			return getRuleContext(ThrowStatementContext.class,0);
		}
		public TryStatementContext tryStatement() {
			return getRuleContext(TryStatementContext.class,0);
		}
		public DebuggerStatementContext debuggerStatement() {
			return getRuleContext(DebuggerStatementContext.class,0);
		}
		public YieldExpressionContext yieldExpression() {
			return getRuleContext(YieldExpressionContext.class,0);
		}
		public ElseStatementContext elseStatement() {
			return getRuleContext(ElseStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_statement);
		try {
			setState(225);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(208); 
				block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(209); 
				variableStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(210); 
				emptyStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(211); 
				ifStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(212); 
				expressionStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(213); 
				iterationStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(214); 
				continueStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(215); 
				breakStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(216); 
				returnStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(217); 
				withStatement();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(218); 
				labelledStatement();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(219); 
				switchStatement();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(220); 
				throwStatement();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(221); 
				tryStatement();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(222); 
				debuggerStatement();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(223); 
				yieldExpression();
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(224); 
				elseStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class YieldExpressionContext extends ParserRuleContext {
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public YieldExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_yieldExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterYieldExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitYieldExpression(this);
		}
	}

	public final YieldExpressionContext yieldExpression() throws RecognitionException {
		YieldExpressionContext _localctx = new YieldExpressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_yieldExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227); 
			match(T__2);
			setState(229);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(228); 
				match(Multiply);
				}
				break;
			}
			setState(232);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(231); 
				assignmentExpression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_block);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234); 
			match(OpenBrace);
			setState(236);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(235); 
				statementList(0);
				}
				break;
			}
			setState(238); 
			match(CloseBrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementListContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public StatementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterStatementList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitStatementList(this);
		}
	}

	public final StatementListContext statementList() throws RecognitionException {
		return statementList(0);
	}

	private StatementListContext statementList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		StatementListContext _localctx = new StatementListContext(_ctx, _parentState);
		StatementListContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_statementList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(241); 
			statement();
			}
			_ctx.stop = _input.LT(-1);
			setState(247);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new StatementListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_statementList);
					setState(243);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(244); 
					statement();
					}
					} 
				}
				setState(249);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class VariableStatementContext extends ParserRuleContext {
		public VariableDeclarationListContext variableDeclarationList() {
			return getRuleContext(VariableDeclarationListContext.class,0);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public VariableStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterVariableStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitVariableStatement(this);
		}
	}

	public final VariableStatementContext variableStatement() throws RecognitionException {
		VariableStatementContext _localctx = new VariableStatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_variableStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			_la = _input.LA(1);
			if ( !(_la==T__3 || _la==T__4 || _la==Const) ) {
			_errHandler.recoverInline(this);
			}
			consume();
			setState(251); 
			variableDeclarationList(0);
			setState(253);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(252); 
				eos();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableDeclarationListContext extends ParserRuleContext {
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
		}
		public VariableDeclarationListContext variableDeclarationList() {
			return getRuleContext(VariableDeclarationListContext.class,0);
		}
		public VariableDeclarationListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclarationList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterVariableDeclarationList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitVariableDeclarationList(this);
		}
	}

	public final VariableDeclarationListContext variableDeclarationList() throws RecognitionException {
		return variableDeclarationList(0);
	}

	private VariableDeclarationListContext variableDeclarationList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		VariableDeclarationListContext _localctx = new VariableDeclarationListContext(_ctx, _parentState);
		VariableDeclarationListContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_variableDeclarationList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(256); 
			variableDeclaration();
			}
			_ctx.stop = _input.LT(-1);
			setState(263);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new VariableDeclarationListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_variableDeclarationList);
					setState(258);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(259); 
					match(Comma);
					setState(260); 
					variableDeclaration();
					}
					} 
				}
				setState(265);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class VariableDeclarationContext extends ParserRuleContext {
		public IdentifierBindingContext identifierBinding() {
			return getRuleContext(IdentifierBindingContext.class,0);
		}
		public InitialiserContext initialiser() {
			return getRuleContext(InitialiserContext.class,0);
		}
		public VariableDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterVariableDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitVariableDeclaration(this);
		}
	}

	public final VariableDeclarationContext variableDeclaration() throws RecognitionException {
		VariableDeclarationContext _localctx = new VariableDeclarationContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_variableDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(266); 
			identifierBinding();
			setState(268);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(267); 
				initialiser();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierBindingContext extends ParserRuleContext {
		public IdentifierReferenceContext identifierReference() {
			return getRuleContext(IdentifierReferenceContext.class,0);
		}
		public IdentifierPatternContext identifierPattern() {
			return getRuleContext(IdentifierPatternContext.class,0);
		}
		public IdentifierBindingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierBinding; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterIdentifierBinding(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitIdentifierBinding(this);
		}
	}

	public final IdentifierBindingContext identifierBinding() throws RecognitionException {
		IdentifierBindingContext _localctx = new IdentifierBindingContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_identifierBinding);
		try {
			setState(272);
			switch (_input.LA(1)) {
			case T__2:
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(270); 
				identifierReference();
				}
				break;
			case OpenBracket:
			case OpenParen:
			case OpenBrace:
				enterOuterAlt(_localctx, 2);
				{
				setState(271); 
				identifierPattern();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierReferenceContext extends ParserRuleContext {
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public IdentifierReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierReference; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterIdentifierReference(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitIdentifierReference(this);
		}
	}

	public final IdentifierReferenceContext identifierReference() throws RecognitionException {
		IdentifierReferenceContext _localctx = new IdentifierReferenceContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_identifierReference);
		try {
			setState(276);
			switch (_input.LA(1)) {
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(274); 
				identifierName();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(275); 
				match(T__2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierPatternContext extends ParserRuleContext {
		public ArrayBindingPatternContext arrayBindingPattern() {
			return getRuleContext(ArrayBindingPatternContext.class,0);
		}
		public ObjectBindingPatternContext objectBindingPattern() {
			return getRuleContext(ObjectBindingPatternContext.class,0);
		}
		public ArgumentBindingPatternContext argumentBindingPattern() {
			return getRuleContext(ArgumentBindingPatternContext.class,0);
		}
		public IdentifierPatternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierPattern; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterIdentifierPattern(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitIdentifierPattern(this);
		}
	}

	public final IdentifierPatternContext identifierPattern() throws RecognitionException {
		IdentifierPatternContext _localctx = new IdentifierPatternContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_identifierPattern);
		try {
			setState(281);
			switch (_input.LA(1)) {
			case OpenBracket:
				enterOuterAlt(_localctx, 1);
				{
				setState(278); 
				arrayBindingPattern();
				}
				break;
			case OpenBrace:
				enterOuterAlt(_localctx, 2);
				{
				setState(279); 
				objectBindingPattern();
				}
				break;
			case OpenParen:
				enterOuterAlt(_localctx, 3);
				{
				setState(280); 
				argumentBindingPattern();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayBindingPatternContext extends ParserRuleContext {
		public RestElementContext restElement() {
			return getRuleContext(RestElementContext.class,0);
		}
		public ElisionContext elision() {
			return getRuleContext(ElisionContext.class,0);
		}
		public BindingElementListContext bindingElementList() {
			return getRuleContext(BindingElementListContext.class,0);
		}
		public ArrayBindingPatternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayBindingPattern; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterArrayBindingPattern(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitArrayBindingPattern(this);
		}
	}

	public final ArrayBindingPatternContext arrayBindingPattern() throws RecognitionException {
		ArrayBindingPatternContext _localctx = new ArrayBindingPatternContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_arrayBindingPattern);
		int _la;
		try {
			setState(303);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(283); 
				match(OpenBracket);
				setState(285);
				_la = _input.LA(1);
				if (_la==Comma) {
					{
					setState(284); 
					elision();
					}
				}

				setState(287); 
				restElement();
				setState(288); 
				match(CloseBracket);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(290); 
				match(OpenBracket);
				setState(291); 
				bindingElementList();
				setState(292); 
				match(CloseBracket);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(294); 
				match(OpenBracket);
				setState(295); 
				bindingElementList();
				setState(296); 
				match(Comma);
				setState(298);
				_la = _input.LA(1);
				if (_la==Comma) {
					{
					setState(297); 
					elision();
					}
				}

				setState(300); 
				restElement();
				setState(301); 
				match(CloseBracket);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RestElementContext extends ParserRuleContext {
		public IdentifierReferenceContext identifierReference() {
			return getRuleContext(IdentifierReferenceContext.class,0);
		}
		public RestElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_restElement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterRestElement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitRestElement(this);
		}
	}

	public final RestElementContext restElement() throws RecognitionException {
		RestElementContext _localctx = new RestElementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_restElement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(305); 
			match(T__5);
			setState(306); 
			identifierReference();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BindingElementListContext extends ParserRuleContext {
		public List<VariableDeclarationContext> variableDeclaration() {
			return getRuleContexts(VariableDeclarationContext.class);
		}
		public VariableDeclarationContext variableDeclaration(int i) {
			return getRuleContext(VariableDeclarationContext.class,i);
		}
		public List<ElisionContext> elision() {
			return getRuleContexts(ElisionContext.class);
		}
		public ElisionContext elision(int i) {
			return getRuleContext(ElisionContext.class,i);
		}
		public BindingElementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bindingElementList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterBindingElementList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitBindingElementList(this);
		}
	}

	public final BindingElementListContext bindingElementList() throws RecognitionException {
		BindingElementListContext _localctx = new BindingElementListContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_bindingElementList);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(312); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(309);
					_la = _input.LA(1);
					if (_la==Comma) {
						{
						setState(308); 
						elision();
						}
					}

					setState(311); 
					variableDeclaration();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(314); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ObjectBindingPatternContext extends ParserRuleContext {
		public BindingPropertyListContext bindingPropertyList() {
			return getRuleContext(BindingPropertyListContext.class,0);
		}
		public ObjectBindingPatternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objectBindingPattern; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterObjectBindingPattern(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitObjectBindingPattern(this);
		}
	}

	public final ObjectBindingPatternContext objectBindingPattern() throws RecognitionException {
		ObjectBindingPatternContext _localctx = new ObjectBindingPatternContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_objectBindingPattern);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(316); 
			match(OpenBrace);
			setState(318);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace))) != 0) || ((((_la - 86)) & ~0x3f) == 0 && ((1L << (_la - 86)) & ((1L << (DecimalLiteral - 86)) | (1L << (HexIntegerLiteral - 86)) | (1L << (OctalIntegerLiteral - 86)) | (1L << (BinaryLiteral - 86)) | (1L << (Identifier - 86)) | (1L << (StringLiteral - 86)))) != 0)) {
				{
				setState(317); 
				bindingPropertyList(0);
				}
			}

			setState(320); 
			match(CloseBrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentBindingPatternContext extends ParserRuleContext {
		public BindingPropertyListContext bindingPropertyList() {
			return getRuleContext(BindingPropertyListContext.class,0);
		}
		public ArgumentBindingPatternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentBindingPattern; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterArgumentBindingPattern(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitArgumentBindingPattern(this);
		}
	}

	public final ArgumentBindingPatternContext argumentBindingPattern() throws RecognitionException {
		ArgumentBindingPatternContext _localctx = new ArgumentBindingPatternContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_argumentBindingPattern);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322); 
			match(OpenParen);
			setState(324);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace))) != 0) || ((((_la - 86)) & ~0x3f) == 0 && ((1L << (_la - 86)) & ((1L << (DecimalLiteral - 86)) | (1L << (HexIntegerLiteral - 86)) | (1L << (OctalIntegerLiteral - 86)) | (1L << (BinaryLiteral - 86)) | (1L << (Identifier - 86)) | (1L << (StringLiteral - 86)))) != 0)) {
				{
				setState(323); 
				bindingPropertyList(0);
				}
			}

			setState(326); 
			match(CloseParen);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BindingPropertyListContext extends ParserRuleContext {
		public BindingPropertyContext bindingProperty() {
			return getRuleContext(BindingPropertyContext.class,0);
		}
		public BindingPropertyListContext bindingPropertyList() {
			return getRuleContext(BindingPropertyListContext.class,0);
		}
		public BindingPropertyListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bindingPropertyList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterBindingPropertyList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitBindingPropertyList(this);
		}
	}

	public final BindingPropertyListContext bindingPropertyList() throws RecognitionException {
		return bindingPropertyList(0);
	}

	private BindingPropertyListContext bindingPropertyList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BindingPropertyListContext _localctx = new BindingPropertyListContext(_ctx, _parentState);
		BindingPropertyListContext _prevctx = _localctx;
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_bindingPropertyList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(329); 
			bindingProperty();
			}
			_ctx.stop = _input.LT(-1);
			setState(336);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new BindingPropertyListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_bindingPropertyList);
					setState(331);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(332); 
					match(Comma);
					setState(333); 
					bindingProperty();
					}
					} 
				}
				setState(338);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BindingPropertyContext extends ParserRuleContext {
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
		}
		public PropertyNameContext propertyName() {
			return getRuleContext(PropertyNameContext.class,0);
		}
		public BindingPropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bindingProperty; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterBindingProperty(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitBindingProperty(this);
		}
	}

	public final BindingPropertyContext bindingProperty() throws RecognitionException {
		BindingPropertyContext _localctx = new BindingPropertyContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_bindingProperty);
		try {
			setState(344);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(339); 
				variableDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(340); 
				propertyName();
				setState(341); 
				match(Colon);
				setState(342); 
				variableDeclaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitialiserContext extends ParserRuleContext {
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public InitialiserContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initialiser; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterInitialiser(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitInitialiser(this);
		}
	}

	public final InitialiserContext initialiser() throws RecognitionException {
		InitialiserContext _localctx = new InitialiserContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_initialiser);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(346); 
			match(Assign);
			setState(347); 
			assignmentExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EmptyStatementContext extends ParserRuleContext {
		public TerminalNode SemiColon() { return getToken(ECMAScriptParser.SemiColon, 0); }
		public EmptyStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_emptyStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterEmptyStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitEmptyStatement(this);
		}
	}

	public final EmptyStatementContext emptyStatement() throws RecognitionException {
		EmptyStatementContext _localctx = new EmptyStatementContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_emptyStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349); 
			match(SemiColon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterExpressionStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitExpressionStatement(this);
		}
	}

	public final ExpressionStatementContext expressionStatement() throws RecognitionException {
		ExpressionStatementContext _localctx = new ExpressionStatementContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_expressionStatement);
		try {
			setState(355);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(351);
				if (!(!here(OpenBrace))) throw new FailedPredicateException(this, "!here(OpenBrace)");
				setState(352); 
				expression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(353);
				if (!(!here(Function))) throw new FailedPredicateException(this, "!here(Function)");
				setState(354); 
				expression(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ElseStatementContext elseStatement() {
			return getRuleContext(ElseStatementContext.class,0);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterIfStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitIfStatement(this);
		}
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(357); 
			match(T__6);
			setState(358); 
			match(OpenParen);
			setState(359); 
			expression(0);
			setState(360); 
			match(CloseParen);
			setState(361); 
			statement();
			setState(363);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(362); 
				elseStatement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElseStatementContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ElseStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterElseStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitElseStatement(this);
		}
	}

	public final ElseStatementContext elseStatement() throws RecognitionException {
		ElseStatementContext _localctx = new ElseStatementContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_elseStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(365); 
			match(T__7);
			setState(366); 
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IterationStatementContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public VariableDeclarationListContext variableDeclarationList() {
			return getRuleContext(VariableDeclarationListContext.class,0);
		}
		public IdentifierBindingContext identifierBinding() {
			return getRuleContext(IdentifierBindingContext.class,0);
		}
		public LeftHandSideExpressionContext leftHandSideExpression() {
			return getRuleContext(LeftHandSideExpressionContext.class,0);
		}
		public IterationStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iterationStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterIterationStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitIterationStatement(this);
		}
	}

	public final IterationStatementContext iterationStatement() throws RecognitionException {
		IterationStatementContext _localctx = new IterationStatementContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_iterationStatement);
		int _la;
		try {
			setState(427);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(368); 
				match(T__8);
				setState(369); 
				statement();
				setState(370); 
				match(T__9);
				setState(371); 
				match(OpenParen);
				setState(372); 
				expression(0);
				setState(373); 
				match(CloseParen);
				setState(374); 
				eos();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(376); 
				match(T__9);
				setState(377); 
				match(OpenParen);
				setState(378); 
				expression(0);
				setState(379); 
				match(CloseParen);
				setState(380); 
				statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(382); 
				match(T__10);
				setState(383); 
				match(OpenParen);
				setState(385);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__2) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (NullLiteral - 84)) | (1L << (BooleanLiteral - 84)) | (1L << (DecimalLiteral - 84)) | (1L << (HexIntegerLiteral - 84)) | (1L << (OctalIntegerLiteral - 84)) | (1L << (BinaryLiteral - 84)) | (1L << (Class - 84)) | (1L << (Identifier - 84)) | (1L << (StringLiteral - 84)))) != 0)) {
					{
					setState(384); 
					expression(0);
					}
				}

				setState(387); 
				match(SemiColon);
				setState(389);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__2) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (NullLiteral - 84)) | (1L << (BooleanLiteral - 84)) | (1L << (DecimalLiteral - 84)) | (1L << (HexIntegerLiteral - 84)) | (1L << (OctalIntegerLiteral - 84)) | (1L << (BinaryLiteral - 84)) | (1L << (Class - 84)) | (1L << (Identifier - 84)) | (1L << (StringLiteral - 84)))) != 0)) {
					{
					setState(388); 
					expression(0);
					}
				}

				setState(391); 
				match(SemiColon);
				setState(393);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__2) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (NullLiteral - 84)) | (1L << (BooleanLiteral - 84)) | (1L << (DecimalLiteral - 84)) | (1L << (HexIntegerLiteral - 84)) | (1L << (OctalIntegerLiteral - 84)) | (1L << (BinaryLiteral - 84)) | (1L << (Class - 84)) | (1L << (Identifier - 84)) | (1L << (StringLiteral - 84)))) != 0)) {
					{
					setState(392); 
					expression(0);
					}
				}

				setState(395); 
				match(CloseParen);
				setState(396); 
				statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(397); 
				match(T__10);
				setState(398); 
				match(OpenParen);
				setState(399);
				_la = _input.LA(1);
				if ( !(_la==T__3 || _la==T__4 || _la==Const) ) {
				_errHandler.recoverInline(this);
				}
				consume();
				setState(400); 
				variableDeclarationList(0);
				setState(401); 
				match(SemiColon);
				setState(403);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__2) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (NullLiteral - 84)) | (1L << (BooleanLiteral - 84)) | (1L << (DecimalLiteral - 84)) | (1L << (HexIntegerLiteral - 84)) | (1L << (OctalIntegerLiteral - 84)) | (1L << (BinaryLiteral - 84)) | (1L << (Class - 84)) | (1L << (Identifier - 84)) | (1L << (StringLiteral - 84)))) != 0)) {
					{
					setState(402); 
					expression(0);
					}
				}

				setState(405); 
				match(SemiColon);
				setState(407);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__2) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (NullLiteral - 84)) | (1L << (BooleanLiteral - 84)) | (1L << (DecimalLiteral - 84)) | (1L << (HexIntegerLiteral - 84)) | (1L << (OctalIntegerLiteral - 84)) | (1L << (BinaryLiteral - 84)) | (1L << (Class - 84)) | (1L << (Identifier - 84)) | (1L << (StringLiteral - 84)))) != 0)) {
					{
					setState(406); 
					expression(0);
					}
				}

				setState(409); 
				match(CloseParen);
				setState(410); 
				statement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(412); 
				match(T__10);
				setState(414);
				_la = _input.LA(1);
				if (_la==T__11) {
					{
					setState(413); 
					match(T__11);
					}
				}

				setState(416); 
				match(OpenParen);
				setState(420);
				switch (_input.LA(1)) {
				case T__3:
				case T__4:
				case Const:
					{
					setState(417);
					_la = _input.LA(1);
					if ( !(_la==T__3 || _la==T__4 || _la==Const) ) {
					_errHandler.recoverInline(this);
					}
					consume();
					setState(418); 
					identifierBinding();
					}
					break;
				case T__0:
				case T__31:
				case T__32:
				case RegularExpressionLiteral:
				case OpenBracket:
				case OpenParen:
				case OpenBrace:
				case NullLiteral:
				case BooleanLiteral:
				case DecimalLiteral:
				case HexIntegerLiteral:
				case OctalIntegerLiteral:
				case BinaryLiteral:
				case Class:
				case Identifier:
				case StringLiteral:
					{
					setState(419); 
					leftHandSideExpression();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(422);
				_la = _input.LA(1);
				if ( !(_la==T__12 || _la==T__13) ) {
				_errHandler.recoverInline(this);
				}
				consume();
				setState(423); 
				expression(0);
				setState(424); 
				match(CloseParen);
				setState(425); 
				statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ContinueStatementContext extends ParserRuleContext {
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public ContinueStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterContinueStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitContinueStatement(this);
		}
	}

	public final ContinueStatementContext continueStatement() throws RecognitionException {
		ContinueStatementContext _localctx = new ContinueStatementContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_continueStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(429); 
			match(T__14);
			setState(430);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(432);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(431); 
				identifierName();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BreakStatementContext extends ParserRuleContext {
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public BreakStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterBreakStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitBreakStatement(this);
		}
	}

	public final BreakStatementContext breakStatement() throws RecognitionException {
		BreakStatementContext _localctx = new BreakStatementContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_breakStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(434); 
			match(T__15);
			setState(435);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(437);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				{
				setState(436); 
				identifierName();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public ReturnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterReturnStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitReturnStatement(this);
		}
	}

	public final ReturnStatementContext returnStatement() throws RecognitionException {
		ReturnStatementContext _localctx = new ReturnStatementContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_returnStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(439); 
			match(T__16);
			setState(440);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(442);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				{
				setState(441); 
				expression(0);
				}
				break;
			}
			setState(445);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				{
				setState(444); 
				eos();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WithStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WithStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_withStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterWithStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitWithStatement(this);
		}
	}

	public final WithStatementContext withStatement() throws RecognitionException {
		WithStatementContext _localctx = new WithStatementContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_withStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(447); 
			match(T__17);
			setState(448); 
			match(OpenParen);
			setState(449); 
			expression(0);
			setState(450); 
			match(CloseParen);
			setState(451); 
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SwitchStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public CaseBlockContext caseBlock() {
			return getRuleContext(CaseBlockContext.class,0);
		}
		public SwitchStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterSwitchStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitSwitchStatement(this);
		}
	}

	public final SwitchStatementContext switchStatement() throws RecognitionException {
		SwitchStatementContext _localctx = new SwitchStatementContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_switchStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(453); 
			match(T__18);
			setState(454); 
			match(OpenParen);
			setState(455); 
			expression(0);
			setState(456); 
			match(CloseParen);
			setState(457); 
			caseBlock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CaseBlockContext extends ParserRuleContext {
		public List<CaseClausesContext> caseClauses() {
			return getRuleContexts(CaseClausesContext.class);
		}
		public CaseClausesContext caseClauses(int i) {
			return getRuleContext(CaseClausesContext.class,i);
		}
		public DefaultClauseContext defaultClause() {
			return getRuleContext(DefaultClauseContext.class,0);
		}
		public CaseBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseBlock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterCaseBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitCaseBlock(this);
		}
	}

	public final CaseBlockContext caseBlock() throws RecognitionException {
		CaseBlockContext _localctx = new CaseBlockContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_caseBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(459); 
			match(OpenBrace);
			setState(461);
			_la = _input.LA(1);
			if (_la==T__19) {
				{
				setState(460); 
				caseClauses();
				}
			}

			setState(467);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(463); 
				defaultClause();
				setState(465);
				_la = _input.LA(1);
				if (_la==T__19) {
					{
					setState(464); 
					caseClauses();
					}
				}

				}
			}

			setState(469); 
			match(CloseBrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CaseClausesContext extends ParserRuleContext {
		public List<CaseClauseContext> caseClause() {
			return getRuleContexts(CaseClauseContext.class);
		}
		public CaseClauseContext caseClause(int i) {
			return getRuleContext(CaseClauseContext.class,i);
		}
		public CaseClausesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseClauses; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterCaseClauses(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitCaseClauses(this);
		}
	}

	public final CaseClausesContext caseClauses() throws RecognitionException {
		CaseClausesContext _localctx = new CaseClausesContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_caseClauses);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(472); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(471); 
				caseClause();
				}
				}
				setState(474); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__19 );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CaseClauseContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public CaseClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterCaseClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitCaseClause(this);
		}
	}

	public final CaseClauseContext caseClause() throws RecognitionException {
		CaseClauseContext _localctx = new CaseClauseContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_caseClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(476); 
			match(T__19);
			setState(477); 
			expression(0);
			setState(478); 
			match(Colon);
			setState(480);
			switch ( getInterpreter().adaptivePredict(_input,44,_ctx) ) {
			case 1:
				{
				setState(479); 
				statementList(0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefaultClauseContext extends ParserRuleContext {
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public DefaultClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterDefaultClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitDefaultClause(this);
		}
	}

	public final DefaultClauseContext defaultClause() throws RecognitionException {
		DefaultClauseContext _localctx = new DefaultClauseContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_defaultClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(482); 
			match(T__20);
			setState(483); 
			match(Colon);
			setState(485);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				{
				setState(484); 
				statementList(0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LabelledStatementContext extends ParserRuleContext {
		public PropertyNameContext propertyName() {
			return getRuleContext(PropertyNameContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LabelledStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_labelledStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterLabelledStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitLabelledStatement(this);
		}
	}

	public final LabelledStatementContext labelledStatement() throws RecognitionException {
		LabelledStatementContext _localctx = new LabelledStatementContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_labelledStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(487); 
			propertyName();
			setState(488); 
			match(Colon);
			setState(491);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				{
				setState(489); 
				statement();
				}
				break;
			case 2:
				{
				setState(490); 
				expression(0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ThrowStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ThrowStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_throwStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterThrowStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitThrowStatement(this);
		}
	}

	public final ThrowStatementContext throwStatement() throws RecognitionException {
		ThrowStatementContext _localctx = new ThrowStatementContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_throwStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(493); 
			match(T__21);
			setState(494);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(495); 
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TryStatementContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<CatchProductionContext> catchProduction() {
			return getRuleContexts(CatchProductionContext.class);
		}
		public CatchProductionContext catchProduction(int i) {
			return getRuleContext(CatchProductionContext.class,i);
		}
		public FinallyProductionContext finallyProduction() {
			return getRuleContext(FinallyProductionContext.class,0);
		}
		public TryStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tryStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterTryStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitTryStatement(this);
		}
	}

	public final TryStatementContext tryStatement() throws RecognitionException {
		TryStatementContext _localctx = new TryStatementContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_tryStatement);
		int _la;
		try {
			int _alt;
			setState(519);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(497); 
				match(T__22);
				setState(498); 
				block();
				setState(502);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,47,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(499); 
						catchProduction();
						}
						} 
					}
					setState(504);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,47,_ctx);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(505); 
				match(T__22);
				setState(506); 
				block();
				setState(507); 
				finallyProduction();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(509); 
				match(T__22);
				setState(510); 
				block();
				setState(514);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__23) {
					{
					{
					setState(511); 
					catchProduction();
					}
					}
					setState(516);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(517); 
				finallyProduction();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CatchProductionContext extends ParserRuleContext {
		public IdentifierBindingContext identifierBinding() {
			return getRuleContext(IdentifierBindingContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public CatchProductionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_catchProduction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterCatchProduction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitCatchProduction(this);
		}
	}

	public final CatchProductionContext catchProduction() throws RecognitionException {
		CatchProductionContext _localctx = new CatchProductionContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_catchProduction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(521); 
			match(T__23);
			setState(522); 
			match(OpenParen);
			setState(523); 
			identifierBinding();
			setState(526);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(524); 
				match(T__6);
				setState(525); 
				expression(0);
				}
			}

			setState(528); 
			match(CloseParen);
			setState(529); 
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FinallyProductionContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FinallyProductionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_finallyProduction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterFinallyProduction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitFinallyProduction(this);
		}
	}

	public final FinallyProductionContext finallyProduction() throws RecognitionException {
		FinallyProductionContext _localctx = new FinallyProductionContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_finallyProduction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(531); 
			match(T__24);
			setState(532); 
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DebuggerStatementContext extends ParserRuleContext {
		public DebuggerStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_debuggerStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterDebuggerStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitDebuggerStatement(this);
		}
	}

	public final DebuggerStatementContext debuggerStatement() throws RecognitionException {
		DebuggerStatementContext _localctx = new DebuggerStatementContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_debuggerStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(534); 
			match(T__25);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalParameterListContext extends ParserRuleContext {
		public RestElementContext restElement() {
			return getRuleContext(RestElementContext.class,0);
		}
		public FormalParametersContext formalParameters() {
			return getRuleContext(FormalParametersContext.class,0);
		}
		public FormalParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formalParameterList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterFormalParameterList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitFormalParameterList(this);
		}
	}

	public final FormalParameterListContext formalParameterList() throws RecognitionException {
		FormalParameterListContext _localctx = new FormalParameterListContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_formalParameterList);
		try {
			setState(542);
			switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(536); 
				restElement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(537); 
				formalParameters();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(538); 
				formalParameters();
				setState(539); 
				match(Comma);
				setState(540); 
				restElement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalParametersContext extends ParserRuleContext {
		public List<FormalParameterContext> formalParameter() {
			return getRuleContexts(FormalParameterContext.class);
		}
		public FormalParameterContext formalParameter(int i) {
			return getRuleContext(FormalParameterContext.class,i);
		}
		public FormalParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formalParameters; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterFormalParameters(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitFormalParameters(this);
		}
	}

	public final FormalParametersContext formalParameters() throws RecognitionException {
		FormalParametersContext _localctx = new FormalParametersContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_formalParameters);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(544); 
			formalParameter();
			setState(549);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,52,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(545); 
					match(Comma);
					setState(546); 
					formalParameter();
					}
					} 
				}
				setState(551);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,52,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalParameterContext extends ParserRuleContext {
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public ArrayLiteralContext arrayLiteral() {
			return getRuleContext(ArrayLiteralContext.class,0);
		}
		public ObjectLiteralContext objectLiteral() {
			return getRuleContext(ObjectLiteralContext.class,0);
		}
		public FormalParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formalParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterFormalParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitFormalParameter(this);
		}
	}

	public final FormalParameterContext formalParameter() throws RecognitionException {
		FormalParameterContext _localctx = new FormalParameterContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_formalParameter);
		try {
			setState(555);
			switch (_input.LA(1)) {
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(552); 
				identifierName();
				}
				break;
			case OpenBracket:
				enterOuterAlt(_localctx, 2);
				{
				setState(553); 
				arrayLiteral();
				}
				break;
			case OpenBrace:
				enterOuterAlt(_localctx, 3);
				{
				setState(554); 
				objectLiteral();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionBodyContext extends ParserRuleContext {
		public StatementListItemContext statementListItem() {
			return getRuleContext(StatementListItemContext.class,0);
		}
		public FunctionBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterFunctionBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitFunctionBody(this);
		}
	}

	public final FunctionBodyContext functionBody() throws RecognitionException {
		FunctionBodyContext _localctx = new FunctionBodyContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_functionBody);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(558);
			switch ( getInterpreter().adaptivePredict(_input,54,_ctx) ) {
			case 1:
				{
				setState(557); 
				statementListItem();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayLiteralContext extends ParserRuleContext {
		public ElisionContext elision() {
			return getRuleContext(ElisionContext.class,0);
		}
		public ElementListContext elementList() {
			return getRuleContext(ElementListContext.class,0);
		}
		public ArrayLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayLiteral; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterArrayLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitArrayLiteral(this);
		}
	}

	public final ArrayLiteralContext arrayLiteral() throws RecognitionException {
		ArrayLiteralContext _localctx = new ArrayLiteralContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_arrayLiteral);
		int _la;
		try {
			setState(577);
			switch ( getInterpreter().adaptivePredict(_input,57,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(560); 
				match(OpenBracket);
				setState(562);
				_la = _input.LA(1);
				if (_la==Comma) {
					{
					setState(561); 
					elision();
					}
				}

				setState(564); 
				match(CloseBracket);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(565); 
				match(OpenBracket);
				setState(566); 
				elementList(0);
				setState(567); 
				match(CloseBracket);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(569); 
				match(OpenBracket);
				setState(570); 
				elementList(0);
				setState(571); 
				match(Comma);
				setState(573);
				_la = _input.LA(1);
				if (_la==Comma) {
					{
					setState(572); 
					elision();
					}
				}

				setState(575); 
				match(CloseBracket);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementListContext extends ParserRuleContext {
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public ElisionContext elision() {
			return getRuleContext(ElisionContext.class,0);
		}
		public ElementListContext elementList() {
			return getRuleContext(ElementListContext.class,0);
		}
		public ElementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elementList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterElementList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitElementList(this);
		}
	}

	public final ElementListContext elementList() throws RecognitionException {
		return elementList(0);
	}

	private ElementListContext elementList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ElementListContext _localctx = new ElementListContext(_ctx, _parentState);
		ElementListContext _prevctx = _localctx;
		int _startState = 102;
		enterRecursionRule(_localctx, 102, RULE_elementList, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(581);
			_la = _input.LA(1);
			if (_la==Comma) {
				{
				setState(580); 
				elision();
				}
			}

			setState(584);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(583); 
				match(T__5);
				}
			}

			setState(586); 
			assignmentExpression();
			}
			_ctx.stop = _input.LT(-1);
			setState(599);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,62,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ElementListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_elementList);
					setState(588);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(589); 
					match(Comma);
					setState(591);
					_la = _input.LA(1);
					if (_la==Comma) {
						{
						setState(590); 
						elision();
						}
					}

					setState(594);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(593); 
						match(T__5);
						}
					}

					setState(596); 
					assignmentExpression();
					}
					} 
				}
				setState(601);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,62,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ElisionContext extends ParserRuleContext {
		public ElisionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elision; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterElision(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitElision(this);
		}
	}

	public final ElisionContext elision() throws RecognitionException {
		ElisionContext _localctx = new ElisionContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_elision);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(603); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(602); 
				match(Comma);
				}
				}
				setState(605); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Comma );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ObjectLiteralContext extends ParserRuleContext {
		public PropertyNameAndValueListContext propertyNameAndValueList() {
			return getRuleContext(PropertyNameAndValueListContext.class,0);
		}
		public ObjectLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objectLiteral; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterObjectLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitObjectLiteral(this);
		}
	}

	public final ObjectLiteralContext objectLiteral() throws RecognitionException {
		ObjectLiteralContext _localctx = new ObjectLiteralContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_objectLiteral);
		try {
			setState(618);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(607); 
				match(OpenBrace);
				setState(608); 
				match(CloseBrace);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(609); 
				match(OpenBrace);
				setState(610); 
				propertyNameAndValueList(0);
				setState(611); 
				match(CloseBrace);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(613); 
				match(OpenBrace);
				setState(614); 
				propertyNameAndValueList(0);
				setState(615); 
				match(Comma);
				setState(616); 
				match(CloseBrace);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PropertyNameAndValueListContext extends ParserRuleContext {
		public PropertyAssignmentContext propertyAssignment() {
			return getRuleContext(PropertyAssignmentContext.class,0);
		}
		public PropertyNameAndValueListContext propertyNameAndValueList() {
			return getRuleContext(PropertyNameAndValueListContext.class,0);
		}
		public PropertyNameAndValueListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_propertyNameAndValueList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterPropertyNameAndValueList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitPropertyNameAndValueList(this);
		}
	}

	public final PropertyNameAndValueListContext propertyNameAndValueList() throws RecognitionException {
		return propertyNameAndValueList(0);
	}

	private PropertyNameAndValueListContext propertyNameAndValueList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PropertyNameAndValueListContext _localctx = new PropertyNameAndValueListContext(_ctx, _parentState);
		PropertyNameAndValueListContext _prevctx = _localctx;
		int _startState = 108;
		enterRecursionRule(_localctx, 108, RULE_propertyNameAndValueList, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(621); 
			propertyAssignment();
			}
			_ctx.stop = _input.LT(-1);
			setState(628);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,65,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new PropertyNameAndValueListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_propertyNameAndValueList);
					setState(623);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(624); 
					match(Comma);
					setState(625); 
					propertyAssignment();
					}
					} 
				}
				setState(630);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,65,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class PropertyAssignmentContext extends ParserRuleContext {
		public IdentifierReferenceContext identifierReference() {
			return getRuleContext(IdentifierReferenceContext.class,0);
		}
		public InitialiserContext initialiser() {
			return getRuleContext(InitialiserContext.class,0);
		}
		public PropertyNameContext propertyName() {
			return getRuleContext(PropertyNameContext.class,0);
		}
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public MethodDefinitionContext methodDefinition() {
			return getRuleContext(MethodDefinitionContext.class,0);
		}
		public PropertyAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_propertyAssignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterPropertyAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitPropertyAssignment(this);
		}
	}

	public final PropertyAssignmentContext propertyAssignment() throws RecognitionException {
		PropertyAssignmentContext _localctx = new PropertyAssignmentContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_propertyAssignment);
		try {
			setState(640);
			switch ( getInterpreter().adaptivePredict(_input,67,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(631); 
				identifierReference();
				setState(633);
				switch ( getInterpreter().adaptivePredict(_input,66,_ctx) ) {
				case 1:
					{
					setState(632); 
					initialiser();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(635); 
				propertyName();
				setState(636); 
				match(Colon);
				setState(637); 
				assignmentExpression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(639); 
				methodDefinition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodDefinitionContext extends ParserRuleContext {
		public PropertyNameContext propertyName() {
			return getRuleContext(PropertyNameContext.class,0);
		}
		public FunctionBodyContext functionBody() {
			return getRuleContext(FunctionBodyContext.class,0);
		}
		public FormalParameterListContext formalParameterList() {
			return getRuleContext(FormalParameterListContext.class,0);
		}
		public MethodDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDefinition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterMethodDefinition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitMethodDefinition(this);
		}
	}

	public final MethodDefinitionContext methodDefinition() throws RecognitionException {
		MethodDefinitionContext _localctx = new MethodDefinitionContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_methodDefinition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(642);
			if (!(!here(Function))) throw new FailedPredicateException(this, "!here(Function)");
			setState(643); 
			propertyName();
			setState(644); 
			match(OpenParen);
			setState(646);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << OpenBracket) | (1L << OpenBrace))) != 0) || _la==Identifier) {
				{
				setState(645); 
				formalParameterList();
				}
			}

			setState(648); 
			match(CloseParen);
			setState(649); 
			match(OpenBrace);
			setState(650); 
			functionBody();
			setState(651); 
			match(CloseBrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PropertyNameContext extends ParserRuleContext {
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public TerminalNode StringLiteral() { return getToken(ECMAScriptParser.StringLiteral, 0); }
		public NumericLiteralContext numericLiteral() {
			return getRuleContext(NumericLiteralContext.class,0);
		}
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public PropertyNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_propertyName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterPropertyName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitPropertyName(this);
		}
	}

	public final PropertyNameContext propertyName() throws RecognitionException {
		PropertyNameContext _localctx = new PropertyNameContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_propertyName);
		try {
			setState(660);
			switch (_input.LA(1)) {
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(653); 
				identifierName();
				}
				break;
			case StringLiteral:
				enterOuterAlt(_localctx, 2);
				{
				setState(654); 
				match(StringLiteral);
				}
				break;
			case DecimalLiteral:
			case HexIntegerLiteral:
			case OctalIntegerLiteral:
			case BinaryLiteral:
				enterOuterAlt(_localctx, 3);
				{
				setState(655); 
				numericLiteral();
				}
				break;
			case OpenBracket:
				enterOuterAlt(_localctx, 4);
				{
				setState(656); 
				match(OpenBracket);
				setState(657); 
				assignmentExpression();
				setState(658); 
				match(CloseBracket);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PropertySetParameterListContext extends ParserRuleContext {
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public PropertySetParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_propertySetParameterList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterPropertySetParameterList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitPropertySetParameterList(this);
		}
	}

	public final PropertySetParameterListContext propertySetParameterList() throws RecognitionException {
		PropertySetParameterListContext _localctx = new PropertySetParameterListContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_propertySetParameterList);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(662); 
			identifierName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentsContext extends ParserRuleContext {
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterArguments(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitArguments(this);
		}
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(664); 
			match(OpenParen);
			setState(666);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__2) | (1L << T__5) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (NullLiteral - 84)) | (1L << (BooleanLiteral - 84)) | (1L << (DecimalLiteral - 84)) | (1L << (HexIntegerLiteral - 84)) | (1L << (OctalIntegerLiteral - 84)) | (1L << (BinaryLiteral - 84)) | (1L << (Class - 84)) | (1L << (Identifier - 84)) | (1L << (StringLiteral - 84)))) != 0)) {
				{
				setState(665); 
				argumentList(0);
				}
			}

			setState(668); 
			match(CloseParen);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentListContext extends ParserRuleContext {
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterArgumentList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitArgumentList(this);
		}
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		return argumentList(0);
	}

	private ArgumentListContext argumentList(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, _parentState);
		ArgumentListContext _prevctx = _localctx;
		int _startState = 120;
		enterRecursionRule(_localctx, 120, RULE_argumentList, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(672);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(671); 
				match(T__5);
				}
			}

			setState(674); 
			assignmentExpression();
			}
			_ctx.stop = _input.LT(-1);
			setState(684);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,73,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ArgumentListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_argumentList);
					setState(676);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(677); 
					match(Comma);
					setState(679);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(678); 
						match(T__5);
						}
					}

					setState(681); 
					assignmentExpression();
					}
					} 
				}
				setState(686);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,73,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ArrowFunctionContext extends ParserRuleContext {
		public ArrowParametersContext arrowParameters() {
			return getRuleContext(ArrowParametersContext.class,0);
		}
		public ConciseBodyContext conciseBody() {
			return getRuleContext(ConciseBodyContext.class,0);
		}
		public ArrowFunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrowFunction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterArrowFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitArrowFunction(this);
		}
	}

	public final ArrowFunctionContext arrowFunction() throws RecognitionException {
		ArrowFunctionContext _localctx = new ArrowFunctionContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_arrowFunction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(687); 
			arrowParameters();
			setState(688);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(689); 
			match(T__26);
			setState(690); 
			conciseBody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrowParametersContext extends ParserRuleContext {
		public IdentifierReferenceContext identifierReference() {
			return getRuleContext(IdentifierReferenceContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public RestElementContext restElement() {
			return getRuleContext(RestElementContext.class,0);
		}
		public ArrowParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrowParameters; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterArrowParameters(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitArrowParameters(this);
		}
	}

	public final ArrowParametersContext arrowParameters() throws RecognitionException {
		ArrowParametersContext _localctx = new ArrowParametersContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_arrowParameters);
		int _la;
		try {
			setState(701);
			switch (_input.LA(1)) {
			case T__2:
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(692); 
				identifierReference();
				}
				break;
			case OpenParen:
				enterOuterAlt(_localctx, 2);
				{
				setState(693); 
				match(OpenParen);
				setState(695);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__2) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (NullLiteral - 84)) | (1L << (BooleanLiteral - 84)) | (1L << (DecimalLiteral - 84)) | (1L << (HexIntegerLiteral - 84)) | (1L << (OctalIntegerLiteral - 84)) | (1L << (BinaryLiteral - 84)) | (1L << (Class - 84)) | (1L << (Identifier - 84)) | (1L << (StringLiteral - 84)))) != 0)) {
					{
					setState(694); 
					expression(0);
					}
				}

				setState(698);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(697); 
					restElement();
					}
				}

				setState(700); 
				match(CloseParen);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConciseBodyContext extends ParserRuleContext {
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public FunctionBodyContext functionBody() {
			return getRuleContext(FunctionBodyContext.class,0);
		}
		public ConciseBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conciseBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterConciseBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitConciseBody(this);
		}
	}

	public final ConciseBodyContext conciseBody() throws RecognitionException {
		ConciseBodyContext _localctx = new ConciseBodyContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_conciseBody);
		try {
			setState(709);
			switch ( getInterpreter().adaptivePredict(_input,77,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(703);
				if (!(!here(OpenBrace))) throw new FailedPredicateException(this, "!here(OpenBrace)");
				setState(704); 
				assignmentExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(705); 
				match(OpenBrace);
				setState(706); 
				functionBody();
				setState(707); 
				match(CloseBrace);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 128;
		enterRecursionRule(_localctx, 128, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(712); 
			assignmentExpression();
			}
			_ctx.stop = _input.LT(-1);
			setState(719);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,78,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(714);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(715); 
					match(Comma);
					setState(716); 
					assignmentExpression();
					}
					} 
				}
				setState(721);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,78,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class AssignmentExpressionContext extends ParserRuleContext {
		public ConditionalExpressionContext conditionalExpression() {
			return getRuleContext(ConditionalExpressionContext.class,0);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public YieldExpressionContext yieldExpression() {
			return getRuleContext(YieldExpressionContext.class,0);
		}
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public AssignmentOperatorContext assignmentOperator() {
			return getRuleContext(AssignmentOperatorContext.class,0);
		}
		public ArrowFunctionContext arrowFunction() {
			return getRuleContext(ArrowFunctionContext.class,0);
		}
		public AssignmentExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterAssignmentExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitAssignmentExpression(this);
		}
	}

	public final AssignmentExpressionContext assignmentExpression() throws RecognitionException {
		AssignmentExpressionContext _localctx = new AssignmentExpressionContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_assignmentExpression);
		try {
			setState(738);
			switch ( getInterpreter().adaptivePredict(_input,81,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(722); 
				conditionalExpression(0);
				setState(724);
				switch ( getInterpreter().adaptivePredict(_input,79,_ctx) ) {
				case 1:
					{
					setState(723); 
					eos();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(726); 
				yieldExpression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(727); 
				conditionalExpression(0);
				setState(728); 
				match(Assign);
				setState(729); 
				assignmentExpression();
				setState(731);
				switch ( getInterpreter().adaptivePredict(_input,80,_ctx) ) {
				case 1:
					{
					setState(730); 
					eos();
					}
					break;
				}
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(733); 
				conditionalExpression(0);
				setState(734); 
				assignmentOperator();
				setState(735); 
				assignmentExpression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(737); 
				arrowFunction();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionalExpressionContext extends ParserRuleContext {
		public List<ConditionalExpressionContext> conditionalExpression() {
			return getRuleContexts(ConditionalExpressionContext.class);
		}
		public ConditionalExpressionContext conditionalExpression(int i) {
			return getRuleContext(ConditionalExpressionContext.class,i);
		}
		public LeftHandSideExpressionContext leftHandSideExpression() {
			return getRuleContext(LeftHandSideExpressionContext.class,0);
		}
		public List<AssignmentExpressionContext> assignmentExpression() {
			return getRuleContexts(AssignmentExpressionContext.class);
		}
		public AssignmentExpressionContext assignmentExpression(int i) {
			return getRuleContext(AssignmentExpressionContext.class,i);
		}
		public ConditionalExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditionalExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterConditionalExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitConditionalExpression(this);
		}
	}

	public final ConditionalExpressionContext conditionalExpression() throws RecognitionException {
		return conditionalExpression(0);
	}

	private ConditionalExpressionContext conditionalExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ConditionalExpressionContext _localctx = new ConditionalExpressionContext(_ctx, _parentState);
		ConditionalExpressionContext _prevctx = _localctx;
		int _startState = 132;
		enterRecursionRule(_localctx, 132, RULE_conditionalExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(760);
			switch (_input.LA(1)) {
			case T__28:
				{
				setState(741); 
				match(T__28);
				setState(742); 
				conditionalExpression(12);
				}
				break;
			case T__29:
				{
				setState(743); 
				match(T__29);
				setState(744); 
				conditionalExpression(11);
				}
				break;
			case T__30:
				{
				setState(745); 
				match(T__30);
				setState(746); 
				conditionalExpression(10);
				}
				break;
			case PlusPlus:
				{
				setState(747); 
				match(PlusPlus);
				setState(748); 
				conditionalExpression(9);
				}
				break;
			case MinusMinus:
				{
				setState(749); 
				match(MinusMinus);
				setState(750); 
				conditionalExpression(8);
				}
				break;
			case Plus:
				{
				setState(751); 
				match(Plus);
				setState(752); 
				conditionalExpression(7);
				}
				break;
			case Minus:
				{
				setState(753); 
				match(Minus);
				setState(754); 
				conditionalExpression(6);
				}
				break;
			case BitNot:
				{
				setState(755); 
				match(BitNot);
				setState(756); 
				conditionalExpression(5);
				}
				break;
			case Not:
				{
				setState(757); 
				match(Not);
				setState(758); 
				conditionalExpression(4);
				}
				break;
			case T__0:
			case T__31:
			case T__32:
			case RegularExpressionLiteral:
			case OpenBracket:
			case OpenParen:
			case OpenBrace:
			case NullLiteral:
			case BooleanLiteral:
			case DecimalLiteral:
			case HexIntegerLiteral:
			case OctalIntegerLiteral:
			case BinaryLiteral:
			case Class:
			case Identifier:
			case StringLiteral:
				{
				setState(759); 
				leftHandSideExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(845);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,84,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(843);
					switch ( getInterpreter().adaptivePredict(_input,83,_ctx) ) {
					case 1:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(762);
						if (!(precpred(_ctx, 35))) throw new FailedPredicateException(this, "precpred(_ctx, 35)");
						setState(763); 
						match(Or);
						setState(764); 
						conditionalExpression(36);
						}
						break;
					case 2:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(765);
						if (!(precpred(_ctx, 34))) throw new FailedPredicateException(this, "precpred(_ctx, 34)");
						setState(766); 
						match(And);
						setState(767); 
						conditionalExpression(35);
						}
						break;
					case 3:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(768);
						if (!(precpred(_ctx, 33))) throw new FailedPredicateException(this, "precpred(_ctx, 33)");
						setState(769); 
						match(BitOr);
						setState(770); 
						conditionalExpression(34);
						}
						break;
					case 4:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(771);
						if (!(precpred(_ctx, 32))) throw new FailedPredicateException(this, "precpred(_ctx, 32)");
						setState(772); 
						match(BitXOr);
						setState(773); 
						conditionalExpression(33);
						}
						break;
					case 5:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(774);
						if (!(precpred(_ctx, 31))) throw new FailedPredicateException(this, "precpred(_ctx, 31)");
						setState(775); 
						match(BitAnd);
						setState(776); 
						conditionalExpression(32);
						}
						break;
					case 6:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(777);
						if (!(precpred(_ctx, 30))) throw new FailedPredicateException(this, "precpred(_ctx, 30)");
						setState(778); 
						match(Equals);
						setState(779); 
						conditionalExpression(31);
						}
						break;
					case 7:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(780);
						if (!(precpred(_ctx, 29))) throw new FailedPredicateException(this, "precpred(_ctx, 29)");
						setState(781); 
						match(NotEquals);
						setState(782); 
						conditionalExpression(30);
						}
						break;
					case 8:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(783);
						if (!(precpred(_ctx, 28))) throw new FailedPredicateException(this, "precpred(_ctx, 28)");
						setState(784); 
						match(IdentityEquals);
						setState(785); 
						conditionalExpression(29);
						}
						break;
					case 9:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(786);
						if (!(precpred(_ctx, 27))) throw new FailedPredicateException(this, "precpred(_ctx, 27)");
						setState(787); 
						match(IdentityNotEquals);
						setState(788); 
						conditionalExpression(28);
						}
						break;
					case 10:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(789);
						if (!(precpred(_ctx, 26))) throw new FailedPredicateException(this, "precpred(_ctx, 26)");
						setState(790); 
						match(LessThan);
						setState(791); 
						conditionalExpression(27);
						}
						break;
					case 11:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(792);
						if (!(precpred(_ctx, 25))) throw new FailedPredicateException(this, "precpred(_ctx, 25)");
						setState(793); 
						match(MoreThan);
						setState(794); 
						conditionalExpression(26);
						}
						break;
					case 12:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(795);
						if (!(precpred(_ctx, 24))) throw new FailedPredicateException(this, "precpred(_ctx, 24)");
						setState(796); 
						match(LessThanEquals);
						setState(797); 
						conditionalExpression(25);
						}
						break;
					case 13:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(798);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(799); 
						match(GreaterThanEquals);
						setState(800); 
						conditionalExpression(24);
						}
						break;
					case 14:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(801);
						if (!(precpred(_ctx, 22))) throw new FailedPredicateException(this, "precpred(_ctx, 22)");
						setState(802); 
						match(T__27);
						setState(803); 
						conditionalExpression(23);
						}
						break;
					case 15:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(804);
						if (!(precpred(_ctx, 21))) throw new FailedPredicateException(this, "precpred(_ctx, 21)");
						setState(805); 
						match(T__12);
						setState(806); 
						conditionalExpression(22);
						}
						break;
					case 16:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(807);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(808); 
						match(LeftShiftArithmetic);
						setState(809); 
						conditionalExpression(21);
						}
						break;
					case 17:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(810);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(811); 
						match(RightShiftArithmetic);
						setState(812); 
						conditionalExpression(20);
						}
						break;
					case 18:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(813);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(814); 
						match(RightShiftLogical);
						setState(815); 
						conditionalExpression(19);
						}
						break;
					case 19:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(816);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(817); 
						match(Plus);
						setState(818); 
						conditionalExpression(18);
						}
						break;
					case 20:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(819);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(820); 
						match(Minus);
						setState(821); 
						conditionalExpression(17);
						}
						break;
					case 21:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(822);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(823); 
						match(Multiply);
						setState(824); 
						conditionalExpression(16);
						}
						break;
					case 22:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(825);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(826); 
						match(Divide);
						setState(827); 
						conditionalExpression(15);
						}
						break;
					case 23:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(828);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(829); 
						match(Modulus);
						setState(830); 
						conditionalExpression(14);
						}
						break;
					case 24:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(831);
						if (!(precpred(_ctx, 36))) throw new FailedPredicateException(this, "precpred(_ctx, 36)");
						setState(832); 
						match(QuestionMark);
						setState(833); 
						assignmentExpression();
						setState(834); 
						match(Colon);
						setState(835); 
						assignmentExpression();
						}
						break;
					case 25:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(837);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(838);
						if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
						setState(839); 
						match(PlusPlus);
						}
						break;
					case 26:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(840);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(841);
						if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
						setState(842); 
						match(MinusMinus);
						}
						break;
					}
					} 
				}
				setState(847);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,84,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class LeftHandSideExpressionContext extends ParserRuleContext {
		public CallExpressionContext callExpression() {
			return getRuleContext(CallExpressionContext.class,0);
		}
		public NewExpressionContext newExpression() {
			return getRuleContext(NewExpressionContext.class,0);
		}
		public LeftHandSideExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_leftHandSideExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterLeftHandSideExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitLeftHandSideExpression(this);
		}
	}

	public final LeftHandSideExpressionContext leftHandSideExpression() throws RecognitionException {
		LeftHandSideExpressionContext _localctx = new LeftHandSideExpressionContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_leftHandSideExpression);
		try {
			setState(850);
			switch ( getInterpreter().adaptivePredict(_input,85,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(848); 
				callExpression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(849); 
				newExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallExpressionContext extends ParserRuleContext {
		public MemberExpressionContext memberExpression() {
			return getRuleContext(MemberExpressionContext.class,0);
		}
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public CallExpressionContext callExpression() {
			return getRuleContext(CallExpressionContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public CallExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterCallExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitCallExpression(this);
		}
	}

	public final CallExpressionContext callExpression() throws RecognitionException {
		return callExpression(0);
	}

	private CallExpressionContext callExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CallExpressionContext _localctx = new CallExpressionContext(_ctx, _parentState);
		CallExpressionContext _prevctx = _localctx;
		int _startState = 136;
		enterRecursionRule(_localctx, 136, RULE_callExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(853); 
			memberExpression(0);
			setState(854); 
			arguments();
			setState(856);
			switch ( getInterpreter().adaptivePredict(_input,86,_ctx) ) {
			case 1:
				{
				setState(855); 
				eos();
				}
				break;
			}
			}
			_ctx.stop = _input.LT(-1);
			setState(878);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,91,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(876);
					switch ( getInterpreter().adaptivePredict(_input,90,_ctx) ) {
					case 1:
						{
						_localctx = new CallExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_callExpression);
						setState(858);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(859); 
						arguments();
						setState(861);
						switch ( getInterpreter().adaptivePredict(_input,87,_ctx) ) {
						case 1:
							{
							setState(860); 
							eos();
							}
							break;
						}
						}
						break;
					case 2:
						{
						_localctx = new CallExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_callExpression);
						setState(863);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(864); 
						match(OpenBracket);
						setState(865); 
						expression(0);
						setState(866); 
						match(CloseBracket);
						setState(868);
						switch ( getInterpreter().adaptivePredict(_input,88,_ctx) ) {
						case 1:
							{
							setState(867); 
							eos();
							}
							break;
						}
						}
						break;
					case 3:
						{
						_localctx = new CallExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_callExpression);
						setState(870);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(871); 
						match(Dot);
						setState(872); 
						identifierName();
						setState(874);
						switch ( getInterpreter().adaptivePredict(_input,89,_ctx) ) {
						case 1:
							{
							setState(873); 
							eos();
							}
							break;
						}
						}
						break;
					}
					} 
				}
				setState(880);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,91,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class NewExpressionContext extends ParserRuleContext {
		public MemberExpressionContext memberExpression() {
			return getRuleContext(MemberExpressionContext.class,0);
		}
		public NewExpressionContext newExpression() {
			return getRuleContext(NewExpressionContext.class,0);
		}
		public NewExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_newExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterNewExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitNewExpression(this);
		}
	}

	public final NewExpressionContext newExpression() throws RecognitionException {
		NewExpressionContext _localctx = new NewExpressionContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_newExpression);
		try {
			setState(884);
			switch ( getInterpreter().adaptivePredict(_input,92,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(881); 
				memberExpression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(882); 
				match(T__31);
				setState(883); 
				newExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MemberExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public MemberExpressionContext memberExpression() {
			return getRuleContext(MemberExpressionContext.class,0);
		}
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public MemberExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_memberExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterMemberExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitMemberExpression(this);
		}
	}

	public final MemberExpressionContext memberExpression() throws RecognitionException {
		return memberExpression(0);
	}

	private MemberExpressionContext memberExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MemberExpressionContext _localctx = new MemberExpressionContext(_ctx, _parentState);
		MemberExpressionContext _prevctx = _localctx;
		int _startState = 140;
		enterRecursionRule(_localctx, 140, RULE_memberExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(892);
			switch (_input.LA(1)) {
			case T__0:
			case T__32:
			case RegularExpressionLiteral:
			case OpenBracket:
			case OpenParen:
			case OpenBrace:
			case NullLiteral:
			case BooleanLiteral:
			case DecimalLiteral:
			case HexIntegerLiteral:
			case OctalIntegerLiteral:
			case BinaryLiteral:
			case Class:
			case Identifier:
			case StringLiteral:
				{
				setState(887); 
				primaryExpression();
				}
				break;
			case T__31:
				{
				setState(888); 
				match(T__31);
				setState(889); 
				memberExpression(0);
				setState(890); 
				arguments();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(904);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,95,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(902);
					switch ( getInterpreter().adaptivePredict(_input,94,_ctx) ) {
					case 1:
						{
						_localctx = new MemberExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_memberExpression);
						setState(894);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(895); 
						match(OpenBracket);
						setState(896); 
						expression(0);
						setState(897); 
						match(CloseBracket);
						}
						break;
					case 2:
						{
						_localctx = new MemberExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_memberExpression);
						setState(899);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(900); 
						match(Dot);
						setState(901); 
						identifierName();
						}
						break;
					}
					} 
				}
				setState(906);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,95,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class FunctionExpressionContext extends ParserRuleContext {
		public FunctionBodyContext functionBody() {
			return getRuleContext(FunctionBodyContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public FormalParameterListContext formalParameterList() {
			return getRuleContext(FormalParameterListContext.class,0);
		}
		public FunctionExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterFunctionExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitFunctionExpression(this);
		}
	}

	public final FunctionExpressionContext functionExpression() throws RecognitionException {
		FunctionExpressionContext _localctx = new FunctionExpressionContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_functionExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(907); 
			match(T__0);
			setState(909);
			_la = _input.LA(1);
			if (_la==Multiply) {
				{
				setState(908); 
				match(Multiply);
				}
			}

			setState(912);
			_la = _input.LA(1);
			if (_la==Identifier) {
				{
				setState(911); 
				identifierName();
				}
			}

			setState(914); 
			match(OpenParen);
			setState(916);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << OpenBracket) | (1L << OpenBrace))) != 0) || _la==Identifier) {
				{
				setState(915); 
				formalParameterList();
				}
			}

			setState(918); 
			match(CloseParen);
			setState(924);
			switch ( getInterpreter().adaptivePredict(_input,99,_ctx) ) {
			case 1:
				{
				setState(919); 
				match(OpenBrace);
				setState(920); 
				functionBody();
				setState(921); 
				match(CloseBrace);
				}
				break;
			case 2:
				{
				setState(923); 
				statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrimaryExpressionContext extends ParserRuleContext {
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public FunctionExpressionContext functionExpression() {
			return getRuleContext(FunctionExpressionContext.class,0);
		}
		public ClassDeclarationContext classDeclaration() {
			return getRuleContext(ClassDeclarationContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public ObjectLiteralContext objectLiteral() {
			return getRuleContext(ObjectLiteralContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ArrayLiteralContext arrayLiteral() {
			return getRuleContext(ArrayLiteralContext.class,0);
		}
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterPrimaryExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitPrimaryExpression(this);
		}
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_primaryExpression);
		try {
			setState(937);
			switch (_input.LA(1)) {
			case T__32:
				enterOuterAlt(_localctx, 1);
				{
				setState(926); 
				match(T__32);
				}
				break;
			case Identifier:
				enterOuterAlt(_localctx, 2);
				{
				setState(927); 
				identifierName();
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 3);
				{
				setState(928); 
				functionExpression();
				}
				break;
			case Class:
				enterOuterAlt(_localctx, 4);
				{
				setState(929); 
				classDeclaration();
				}
				break;
			case RegularExpressionLiteral:
			case NullLiteral:
			case BooleanLiteral:
			case DecimalLiteral:
			case HexIntegerLiteral:
			case OctalIntegerLiteral:
			case BinaryLiteral:
			case StringLiteral:
				enterOuterAlt(_localctx, 5);
				{
				setState(930); 
				literal();
				}
				break;
			case OpenBrace:
				enterOuterAlt(_localctx, 6);
				{
				setState(931); 
				objectLiteral();
				}
				break;
			case OpenParen:
				enterOuterAlt(_localctx, 7);
				{
				setState(932); 
				match(OpenParen);
				setState(933); 
				expression(0);
				setState(934); 
				match(CloseParen);
				}
				break;
			case OpenBracket:
				enterOuterAlt(_localctx, 8);
				{
				setState(936); 
				arrayLiteral();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentOperatorContext extends ParserRuleContext {
		public AssignmentOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterAssignmentOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitAssignmentOperator(this);
		}
	}

	public final AssignmentOperatorContext assignmentOperator() throws RecognitionException {
		AssignmentOperatorContext _localctx = new AssignmentOperatorContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_assignmentOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(939);
			_la = _input.LA(1);
			if ( !(((((_la - 73)) & ~0x3f) == 0 && ((1L << (_la - 73)) & ((1L << (MultiplyAssign - 73)) | (1L << (DivideAssign - 73)) | (1L << (ModulusAssign - 73)) | (1L << (PlusAssign - 73)) | (1L << (MinusAssign - 73)) | (1L << (LeftShiftArithmeticAssign - 73)) | (1L << (RightShiftArithmeticAssign - 73)) | (1L << (RightShiftLogicalAssign - 73)) | (1L << (BitAndAssign - 73)) | (1L << (BitXorAssign - 73)) | (1L << (BitOrAssign - 73)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			consume();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode NullLiteral() { return getToken(ECMAScriptParser.NullLiteral, 0); }
		public TerminalNode BooleanLiteral() { return getToken(ECMAScriptParser.BooleanLiteral, 0); }
		public TerminalNode StringLiteral() { return getToken(ECMAScriptParser.StringLiteral, 0); }
		public TerminalNode RegularExpressionLiteral() { return getToken(ECMAScriptParser.RegularExpressionLiteral, 0); }
		public NumericLiteralContext numericLiteral() {
			return getRuleContext(NumericLiteralContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 148, RULE_literal);
		int _la;
		try {
			setState(943);
			switch (_input.LA(1)) {
			case RegularExpressionLiteral:
			case NullLiteral:
			case BooleanLiteral:
			case StringLiteral:
				enterOuterAlt(_localctx, 1);
				{
				setState(941);
				_la = _input.LA(1);
				if ( !(_la==RegularExpressionLiteral || ((((_la - 84)) & ~0x3f) == 0 && ((1L << (_la - 84)) & ((1L << (NullLiteral - 84)) | (1L << (BooleanLiteral - 84)) | (1L << (StringLiteral - 84)))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				consume();
				}
				break;
			case DecimalLiteral:
			case HexIntegerLiteral:
			case OctalIntegerLiteral:
			case BinaryLiteral:
				enterOuterAlt(_localctx, 2);
				{
				setState(942); 
				numericLiteral();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumericLiteralContext extends ParserRuleContext {
		public TerminalNode DecimalLiteral() { return getToken(ECMAScriptParser.DecimalLiteral, 0); }
		public TerminalNode HexIntegerLiteral() { return getToken(ECMAScriptParser.HexIntegerLiteral, 0); }
		public TerminalNode OctalIntegerLiteral() { return getToken(ECMAScriptParser.OctalIntegerLiteral, 0); }
		public TerminalNode BinaryLiteral() { return getToken(ECMAScriptParser.BinaryLiteral, 0); }
		public NumericLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numericLiteral; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterNumericLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitNumericLiteral(this);
		}
	}

	public final NumericLiteralContext numericLiteral() throws RecognitionException {
		NumericLiteralContext _localctx = new NumericLiteralContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_numericLiteral);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(945);
			_la = _input.LA(1);
			if ( !(((((_la - 86)) & ~0x3f) == 0 && ((1L << (_la - 86)) & ((1L << (DecimalLiteral - 86)) | (1L << (HexIntegerLiteral - 86)) | (1L << (OctalIntegerLiteral - 86)) | (1L << (BinaryLiteral - 86)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			consume();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierNameContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(ECMAScriptParser.Identifier, 0); }
		public IdentifierNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterIdentifierName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitIdentifierName(this);
		}
	}

	public final IdentifierNameContext identifierName() throws RecognitionException {
		IdentifierNameContext _localctx = new IdentifierNameContext(_ctx, getState());
		enterRule(_localctx, 152, RULE_identifierName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(947); 
			match(Identifier);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReservedWordContext extends ParserRuleContext {
		public TerminalNode NullLiteral() { return getToken(ECMAScriptParser.NullLiteral, 0); }
		public TerminalNode BooleanLiteral() { return getToken(ECMAScriptParser.BooleanLiteral, 0); }
		public ReservedWordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reservedWord; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterReservedWord(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitReservedWord(this);
		}
	}

	public final ReservedWordContext reservedWord() throws RecognitionException {
		ReservedWordContext _localctx = new ReservedWordContext(_ctx, getState());
		enterRule(_localctx, 154, RULE_reservedWord);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(949);
			_la = _input.LA(1);
			if ( !(_la==NullLiteral || _la==BooleanLiteral) ) {
			_errHandler.recoverInline(this);
			}
			consume();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EosContext extends ParserRuleContext {
		public TerminalNode SemiColon() { return getToken(ECMAScriptParser.SemiColon, 0); }
		public TerminalNode EOF() { return getToken(ECMAScriptParser.EOF, 0); }
		public EosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterEos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitEos(this);
		}
	}

	public final EosContext eos() throws RecognitionException {
		EosContext _localctx = new EosContext(_ctx, getState());
		enterRule(_localctx, 156, RULE_eos);
		try {
			setState(955);
			switch ( getInterpreter().adaptivePredict(_input,102,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(951); 
				match(SemiColon);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(952); 
				match(EOF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(953);
				if (!(lineTerminatorAhead())) throw new FailedPredicateException(this, "lineTerminatorAhead()");
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(954);
				if (!(_input.LT(1).getType() == CloseBrace)) throw new FailedPredicateException(this, "_input.LT(1).getType() == CloseBrace");
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EofContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ECMAScriptParser.EOF, 0); }
		public EofContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eof; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterEof(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitEof(this);
		}
	}

	public final EofContext eof() throws RecognitionException {
		EofContext _localctx = new EofContext(_ctx, getState());
		enterRule(_localctx, 158, RULE_eof);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(957); 
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 11: 
			return statementList_sempred((StatementListContext)_localctx, predIndex);
		case 13: 
			return variableDeclarationList_sempred((VariableDeclarationListContext)_localctx, predIndex);
		case 23: 
			return bindingPropertyList_sempred((BindingPropertyListContext)_localctx, predIndex);
		case 27: 
			return expressionStatement_sempred((ExpressionStatementContext)_localctx, predIndex);
		case 31: 
			return continueStatement_sempred((ContinueStatementContext)_localctx, predIndex);
		case 32: 
			return breakStatement_sempred((BreakStatementContext)_localctx, predIndex);
		case 33: 
			return returnStatement_sempred((ReturnStatementContext)_localctx, predIndex);
		case 41: 
			return throwStatement_sempred((ThrowStatementContext)_localctx, predIndex);
		case 51: 
			return elementList_sempred((ElementListContext)_localctx, predIndex);
		case 54: 
			return propertyNameAndValueList_sempred((PropertyNameAndValueListContext)_localctx, predIndex);
		case 56: 
			return methodDefinition_sempred((MethodDefinitionContext)_localctx, predIndex);
		case 60: 
			return argumentList_sempred((ArgumentListContext)_localctx, predIndex);
		case 61: 
			return arrowFunction_sempred((ArrowFunctionContext)_localctx, predIndex);
		case 63: 
			return conciseBody_sempred((ConciseBodyContext)_localctx, predIndex);
		case 64: 
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 66: 
			return conditionalExpression_sempred((ConditionalExpressionContext)_localctx, predIndex);
		case 68: 
			return callExpression_sempred((CallExpressionContext)_localctx, predIndex);
		case 70: 
			return memberExpression_sempred((MemberExpressionContext)_localctx, predIndex);
		case 78: 
			return eos_sempred((EosContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean statementList_sempred(StatementListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean variableDeclarationList_sempred(VariableDeclarationListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean bindingPropertyList_sempred(BindingPropertyListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean expressionStatement_sempred(ExpressionStatementContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3: 
			return !here(OpenBrace);
		case 4: 
			return !here(Function);
		}
		return true;
	}
	private boolean continueStatement_sempred(ContinueStatementContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5: 
			return !here(LineTerminator);
		}
		return true;
	}
	private boolean breakStatement_sempred(BreakStatementContext _localctx, int predIndex) {
		switch (predIndex) {
		case 6: 
			return !here(LineTerminator);
		}
		return true;
	}
	private boolean returnStatement_sempred(ReturnStatementContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7: 
			return !here(LineTerminator);
		}
		return true;
	}
	private boolean throwStatement_sempred(ThrowStatementContext _localctx, int predIndex) {
		switch (predIndex) {
		case 8: 
			return !here(LineTerminator);
		}
		return true;
	}
	private boolean elementList_sempred(ElementListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 9: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean propertyNameAndValueList_sempred(PropertyNameAndValueListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 10: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean methodDefinition_sempred(MethodDefinitionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 11: 
			return !here(Function);
		}
		return true;
	}
	private boolean argumentList_sempred(ArgumentListContext _localctx, int predIndex) {
		switch (predIndex) {
		case 12: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean arrowFunction_sempred(ArrowFunctionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 13: 
			return !here(LineTerminator);
		}
		return true;
	}
	private boolean conciseBody_sempred(ConciseBodyContext _localctx, int predIndex) {
		switch (predIndex) {
		case 14: 
			return !here(OpenBrace);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 15: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean conditionalExpression_sempred(ConditionalExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 16: 
			return precpred(_ctx, 35);
		case 17: 
			return precpred(_ctx, 34);
		case 18: 
			return precpred(_ctx, 33);
		case 19: 
			return precpred(_ctx, 32);
		case 20: 
			return precpred(_ctx, 31);
		case 21: 
			return precpred(_ctx, 30);
		case 22: 
			return precpred(_ctx, 29);
		case 23: 
			return precpred(_ctx, 28);
		case 24: 
			return precpred(_ctx, 27);
		case 25: 
			return precpred(_ctx, 26);
		case 26: 
			return precpred(_ctx, 25);
		case 27: 
			return precpred(_ctx, 24);
		case 28: 
			return precpred(_ctx, 23);
		case 29: 
			return precpred(_ctx, 22);
		case 30: 
			return precpred(_ctx, 21);
		case 31: 
			return precpred(_ctx, 20);
		case 32: 
			return precpred(_ctx, 19);
		case 33: 
			return precpred(_ctx, 18);
		case 34: 
			return precpred(_ctx, 17);
		case 35: 
			return precpred(_ctx, 16);
		case 36: 
			return precpred(_ctx, 15);
		case 37: 
			return precpred(_ctx, 14);
		case 38: 
			return precpred(_ctx, 13);
		case 39: 
			return precpred(_ctx, 36);
		case 40: 
			return precpred(_ctx, 3);
		case 41: 
			return !here(LineTerminator);
		case 42: 
			return precpred(_ctx, 2);
		case 43: 
			return !here(LineTerminator);
		}
		return true;
	}
	private boolean callExpression_sempred(CallExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 44: 
			return precpred(_ctx, 3);
		case 45: 
			return precpred(_ctx, 2);
		case 46: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean memberExpression_sempred(MemberExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 47: 
			return precpred(_ctx, 3);
		case 48: 
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean eos_sempred(EosContext _localctx, int predIndex) {
		switch (predIndex) {
		case 49: 
			return lineTerminatorAhead();
		case 50: 
			return _input.LT(1).getType() == CloseBrace;
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u008d\u03c2\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\7\2\u00a4\n\2"+
		"\f\2\16\2\u00a7\13\2\3\2\3\2\3\3\3\3\3\3\5\3\u00ae\n\3\3\4\3\4\3\4\3\4"+
		"\5\4\u00b4\n\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5\u00bd\n\5\3\5\3\5\3\6\3"+
		"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\6\b\u00ca\n\b\r\b\16\b\u00cb\3\t\5\t\u00cf"+
		"\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\5\n\u00e4\n\n\3\13\3\13\5\13\u00e8\n\13\3\13\5\13\u00eb\n\13"+
		"\3\f\3\f\5\f\u00ef\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\7\r\u00f8\n\r\f\r\16"+
		"\r\u00fb\13\r\3\16\3\16\3\16\5\16\u0100\n\16\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\7\17\u0108\n\17\f\17\16\17\u010b\13\17\3\20\3\20\5\20\u010f\n\20"+
		"\3\21\3\21\5\21\u0113\n\21\3\22\3\22\5\22\u0117\n\22\3\23\3\23\3\23\5"+
		"\23\u011c\n\23\3\24\3\24\5\24\u0120\n\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\5\24\u012d\n\24\3\24\3\24\3\24\5\24\u0132\n"+
		"\24\3\25\3\25\3\25\3\26\5\26\u0138\n\26\3\26\6\26\u013b\n\26\r\26\16\26"+
		"\u013c\3\27\3\27\5\27\u0141\n\27\3\27\3\27\3\30\3\30\5\30\u0147\n\30\3"+
		"\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0151\n\31\f\31\16\31\u0154"+
		"\13\31\3\32\3\32\3\32\3\32\3\32\5\32\u015b\n\32\3\33\3\33\3\33\3\34\3"+
		"\34\3\35\3\35\3\35\3\35\5\35\u0166\n\35\3\36\3\36\3\36\3\36\3\36\3\36"+
		"\5\36\u016e\n\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3"+
		" \3 \3 \3 \3 \5 \u0184\n \3 \3 \5 \u0188\n \3 \3 \5 \u018c\n \3 \3 \3"+
		" \3 \3 \3 \3 \3 \5 \u0196\n \3 \3 \5 \u019a\n \3 \3 \3 \3 \3 \5 \u01a1"+
		"\n \3 \3 \3 \3 \5 \u01a7\n \3 \3 \3 \3 \3 \5 \u01ae\n \3!\3!\3!\5!\u01b3"+
		"\n!\3\"\3\"\3\"\5\"\u01b8\n\"\3#\3#\3#\5#\u01bd\n#\3#\5#\u01c0\n#\3$\3"+
		"$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\5&\u01d0\n&\3&\3&\5&\u01d4\n&\5"+
		"&\u01d6\n&\3&\3&\3\'\6\'\u01db\n\'\r\'\16\'\u01dc\3(\3(\3(\3(\5(\u01e3"+
		"\n(\3)\3)\3)\5)\u01e8\n)\3*\3*\3*\3*\5*\u01ee\n*\3+\3+\3+\3+\3,\3,\3,"+
		"\7,\u01f7\n,\f,\16,\u01fa\13,\3,\3,\3,\3,\3,\3,\3,\7,\u0203\n,\f,\16,"+
		"\u0206\13,\3,\3,\5,\u020a\n,\3-\3-\3-\3-\3-\5-\u0211\n-\3-\3-\3-\3.\3"+
		".\3.\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0221\n\60\3\61\3\61\3\61"+
		"\7\61\u0226\n\61\f\61\16\61\u0229\13\61\3\62\3\62\3\62\5\62\u022e\n\62"+
		"\3\63\5\63\u0231\n\63\3\64\3\64\5\64\u0235\n\64\3\64\3\64\3\64\3\64\3"+
		"\64\3\64\3\64\3\64\3\64\5\64\u0240\n\64\3\64\3\64\5\64\u0244\n\64\3\65"+
		"\3\65\5\65\u0248\n\65\3\65\5\65\u024b\n\65\3\65\3\65\3\65\3\65\3\65\5"+
		"\65\u0252\n\65\3\65\5\65\u0255\n\65\3\65\7\65\u0258\n\65\f\65\16\65\u025b"+
		"\13\65\3\66\6\66\u025e\n\66\r\66\16\66\u025f\3\67\3\67\3\67\3\67\3\67"+
		"\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u026d\n\67\38\38\38\38\38\38\78\u0275"+
		"\n8\f8\168\u0278\138\39\39\59\u027c\n9\39\39\39\39\39\59\u0283\n9\3:\3"+
		":\3:\3:\5:\u0289\n:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\5;\u0297\n;\3"+
		"<\3<\3=\3=\5=\u029d\n=\3=\3=\3>\3>\5>\u02a3\n>\3>\3>\3>\3>\3>\5>\u02aa"+
		"\n>\3>\7>\u02ad\n>\f>\16>\u02b0\13>\3?\3?\3?\3?\3?\3@\3@\3@\5@\u02ba\n"+
		"@\3@\5@\u02bd\n@\3@\5@\u02c0\n@\3A\3A\3A\3A\3A\3A\5A\u02c8\nA\3B\3B\3"+
		"B\3B\3B\3B\7B\u02d0\nB\fB\16B\u02d3\13B\3C\3C\5C\u02d7\nC\3C\3C\3C\3C"+
		"\3C\5C\u02de\nC\3C\3C\3C\3C\3C\5C\u02e5\nC\3D\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\5D\u02fb\nD\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\3D\3D\7D\u034e\nD\fD\16D\u0351\13D\3E\3E\5E\u0355\nE\3F\3F\3F\3"+
		"F\5F\u035b\nF\3F\3F\3F\5F\u0360\nF\3F\3F\3F\3F\3F\5F\u0367\nF\3F\3F\3"+
		"F\3F\5F\u036d\nF\7F\u036f\nF\fF\16F\u0372\13F\3G\3G\3G\5G\u0377\nG\3H"+
		"\3H\3H\3H\3H\3H\5H\u037f\nH\3H\3H\3H\3H\3H\3H\3H\3H\7H\u0389\nH\fH\16"+
		"H\u038c\13H\3I\3I\5I\u0390\nI\3I\5I\u0393\nI\3I\3I\5I\u0397\nI\3I\3I\3"+
		"I\3I\3I\3I\5I\u039f\nI\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u03ac\nJ\3"+
		"K\3K\3L\3L\5L\u03b2\nL\3M\3M\3N\3N\3O\3O\3P\3P\3P\3P\5P\u03be\nP\3Q\3"+
		"Q\3Q\2\f\30\34\60hnz\u0082\u0086\u008a\u008eR\2\4\6\b\n\f\16\20\22\24"+
		"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv"+
		"xz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094"+
		"\u0096\u0098\u009a\u009c\u009e\u00a0\2\b\4\2\6\7||\3\2\17\20\3\2KU\5\2"+
		"$$VW\u0089\u0089\3\2X[\3\2VW\u0421\2\u00a5\3\2\2\2\4\u00ad\3\2\2\2\6\u00af"+
		"\3\2\2\2\b\u00ba\3\2\2\2\n\u00c0\3\2\2\2\f\u00c5\3\2\2\2\16\u00c9\3\2"+
		"\2\2\20\u00ce\3\2\2\2\22\u00e3\3\2\2\2\24\u00e5\3\2\2\2\26\u00ec\3\2\2"+
		"\2\30\u00f2\3\2\2\2\32\u00fc\3\2\2\2\34\u0101\3\2\2\2\36\u010c\3\2\2\2"+
		" \u0112\3\2\2\2\"\u0116\3\2\2\2$\u011b\3\2\2\2&\u0131\3\2\2\2(\u0133\3"+
		"\2\2\2*\u013a\3\2\2\2,\u013e\3\2\2\2.\u0144\3\2\2\2\60\u014a\3\2\2\2\62"+
		"\u015a\3\2\2\2\64\u015c\3\2\2\2\66\u015f\3\2\2\28\u0165\3\2\2\2:\u0167"+
		"\3\2\2\2<\u016f\3\2\2\2>\u01ad\3\2\2\2@\u01af\3\2\2\2B\u01b4\3\2\2\2D"+
		"\u01b9\3\2\2\2F\u01c1\3\2\2\2H\u01c7\3\2\2\2J\u01cd\3\2\2\2L\u01da\3\2"+
		"\2\2N\u01de\3\2\2\2P\u01e4\3\2\2\2R\u01e9\3\2\2\2T\u01ef\3\2\2\2V\u0209"+
		"\3\2\2\2X\u020b\3\2\2\2Z\u0215\3\2\2\2\\\u0218\3\2\2\2^\u0220\3\2\2\2"+
		"`\u0222\3\2\2\2b\u022d\3\2\2\2d\u0230\3\2\2\2f\u0243\3\2\2\2h\u0245\3"+
		"\2\2\2j\u025d\3\2\2\2l\u026c\3\2\2\2n\u026e\3\2\2\2p\u0282\3\2\2\2r\u0284"+
		"\3\2\2\2t\u0296\3\2\2\2v\u0298\3\2\2\2x\u029a\3\2\2\2z\u02a0\3\2\2\2|"+
		"\u02b1\3\2\2\2~\u02bf\3\2\2\2\u0080\u02c7\3\2\2\2\u0082\u02c9\3\2\2\2"+
		"\u0084\u02e4\3\2\2\2\u0086\u02fa\3\2\2\2\u0088\u0354\3\2\2\2\u008a\u0356"+
		"\3\2\2\2\u008c\u0376\3\2\2\2\u008e\u037e\3\2\2\2\u0090\u038d\3\2\2\2\u0092"+
		"\u03ab\3\2\2\2\u0094\u03ad\3\2\2\2\u0096\u03b1\3\2\2\2\u0098\u03b3\3\2"+
		"\2\2\u009a\u03b5\3\2\2\2\u009c\u03b7\3\2\2\2\u009e\u03bd\3\2\2\2\u00a0"+
		"\u03bf\3\2\2\2\u00a2\u00a4\5\4\3\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2"+
		"\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7"+
		"\u00a5\3\2\2\2\u00a8\u00a9\7\2\2\3\u00a9\3\3\2\2\2\u00aa\u00ae\5\6\4\2"+
		"\u00ab\u00ae\5\b\5\2\u00ac\u00ae\5\22\n\2\u00ad\u00aa\3\2\2\2\u00ad\u00ab"+
		"\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\5\3\2\2\2\u00af\u00b0\7\3\2\2\u00b0"+
		"\u00b1\5\u009aN\2\u00b1\u00b3\7(\2\2\u00b2\u00b4\5^\60\2\u00b3\u00b2\3"+
		"\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\7)\2\2\u00b6"+
		"\u00b7\7*\2\2\u00b7\u00b8\5d\63\2\u00b8\u00b9\7+\2\2\u00b9\7\3\2\2\2\u00ba"+
		"\u00bc\7x\2\2\u00bb\u00bd\5\"\22\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2"+
		"\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\5\n\6\2\u00bf\t\3\2\2\2\u00c0\u00c1"+
		"\5\f\7\2\u00c1\u00c2\7*\2\2\u00c2\u00c3\5\16\b\2\u00c3\u00c4\7+\2\2\u00c4"+
		"\13\3\2\2\2\u00c5\u00c6\7z\2\2\u00c6\u00c7\5\u0086D\2\u00c7\r\3\2\2\2"+
		"\u00c8\u00ca\5\20\t\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9"+
		"\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\17\3\2\2\2\u00cd\u00cf\7\4\2\2\u00ce"+
		"\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\5r"+
		":\2\u00d1\21\3\2\2\2\u00d2\u00e4\5\26\f\2\u00d3\u00e4\5\32\16\2\u00d4"+
		"\u00e4\5\66\34\2\u00d5\u00e4\5:\36\2\u00d6\u00e4\58\35\2\u00d7\u00e4\5"+
		"> \2\u00d8\u00e4\5@!\2\u00d9\u00e4\5B\"\2\u00da\u00e4\5D#\2\u00db\u00e4"+
		"\5F$\2\u00dc\u00e4\5R*\2\u00dd\u00e4\5H%\2\u00de\u00e4\5T+\2\u00df\u00e4"+
		"\5V,\2\u00e0\u00e4\5\\/\2\u00e1\u00e4\5\24\13\2\u00e2\u00e4\5<\37\2\u00e3"+
		"\u00d2\3\2\2\2\u00e3\u00d3\3\2\2\2\u00e3\u00d4\3\2\2\2\u00e3\u00d5\3\2"+
		"\2\2\u00e3\u00d6\3\2\2\2\u00e3\u00d7\3\2\2\2\u00e3\u00d8\3\2\2\2\u00e3"+
		"\u00d9\3\2\2\2\u00e3\u00da\3\2\2\2\u00e3\u00db\3\2\2\2\u00e3\u00dc\3\2"+
		"\2\2\u00e3\u00dd\3\2\2\2\u00e3\u00de\3\2\2\2\u00e3\u00df\3\2\2\2\u00e3"+
		"\u00e0\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\23\3\2\2"+
		"\2\u00e5\u00e7\7\5\2\2\u00e6\u00e8\78\2\2\u00e7\u00e6\3\2\2\2\u00e7\u00e8"+
		"\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00eb\5\u0084C\2\u00ea\u00e9\3\2\2"+
		"\2\u00ea\u00eb\3\2\2\2\u00eb\25\3\2\2\2\u00ec\u00ee\7*\2\2\u00ed\u00ef"+
		"\5\30\r\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2"+
		"\u00f0\u00f1\7+\2\2\u00f1\27\3\2\2\2\u00f2\u00f3\b\r\1\2\u00f3\u00f4\5"+
		"\22\n\2\u00f4\u00f9\3\2\2\2\u00f5\u00f6\f\3\2\2\u00f6\u00f8\5\22\n\2\u00f7"+
		"\u00f5\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2"+
		"\2\2\u00fa\31\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\t\2\2\2\u00fd\u00ff"+
		"\5\34\17\2\u00fe\u0100\5\u009eP\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2"+
		"\2\2\u0100\33\3\2\2\2\u0101\u0102\b\17\1\2\u0102\u0103\5\36\20\2\u0103"+
		"\u0109\3\2\2\2\u0104\u0105\f\3\2\2\u0105\u0106\7-\2\2\u0106\u0108\5\36"+
		"\20\2\u0107\u0104\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109"+
		"\u010a\3\2\2\2\u010a\35\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010e\5 \21"+
		"\2\u010d\u010f\5\64\33\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f"+
		"\37\3\2\2\2\u0110\u0113\5\"\22\2\u0111\u0113\5$\23\2\u0112\u0110\3\2\2"+
		"\2\u0112\u0111\3\2\2\2\u0113!\3\2\2\2\u0114\u0117\5\u009aN\2\u0115\u0117"+
		"\7\5\2\2\u0116\u0114\3\2\2\2\u0116\u0115\3\2\2\2\u0117#\3\2\2\2\u0118"+
		"\u011c\5&\24\2\u0119\u011c\5,\27\2\u011a\u011c\5.\30\2\u011b\u0118\3\2"+
		"\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2\u011c%\3\2\2\2\u011d\u011f"+
		"\7&\2\2\u011e\u0120\5j\66\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120"+
		"\u0121\3\2\2\2\u0121\u0122\5(\25\2\u0122\u0123\7\'\2\2\u0123\u0132\3\2"+
		"\2\2\u0124\u0125\7&\2\2\u0125\u0126\5*\26\2\u0126\u0127\7\'\2\2\u0127"+
		"\u0132\3\2\2\2\u0128\u0129\7&\2\2\u0129\u012a\5*\26\2\u012a\u012c\7-\2"+
		"\2\u012b\u012d\5j\66\2\u012c\u012b\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e"+
		"\3\2\2\2\u012e\u012f\5(\25\2\u012f\u0130\7\'\2\2\u0130\u0132\3\2\2\2\u0131"+
		"\u011d\3\2\2\2\u0131\u0124\3\2\2\2\u0131\u0128\3\2\2\2\u0132\'\3\2\2\2"+
		"\u0133\u0134\7\b\2\2\u0134\u0135\5\"\22\2\u0135)\3\2\2\2\u0136\u0138\5"+
		"j\66\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139\3\2\2\2\u0139"+
		"\u013b\5\36\20\2\u013a\u0137\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013a\3"+
		"\2\2\2\u013c\u013d\3\2\2\2\u013d+\3\2\2\2\u013e\u0140\7*\2\2\u013f\u0141"+
		"\5\60\31\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2"+
		"\u0142\u0143\7+\2\2\u0143-\3\2\2\2\u0144\u0146\7(\2\2\u0145\u0147\5\60"+
		"\31\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\3\2\2\2\u0148"+
		"\u0149\7)\2\2\u0149/\3\2\2\2\u014a\u014b\b\31\1\2\u014b\u014c\5\62\32"+
		"\2\u014c\u0152\3\2\2\2\u014d\u014e\f\3\2\2\u014e\u014f\7-\2\2\u014f\u0151"+
		"\5\62\32\2\u0150\u014d\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2"+
		"\u0152\u0153\3\2\2\2\u0153\61\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u015b"+
		"\5\36\20\2\u0156\u0157\5t;\2\u0157\u0158\7\60\2\2\u0158\u0159\5\36\20"+
		"\2\u0159\u015b\3\2\2\2\u015a\u0155\3\2\2\2\u015a\u0156\3\2\2\2\u015b\63"+
		"\3\2\2\2\u015c\u015d\7.\2\2\u015d\u015e\5\u0084C\2\u015e\65\3\2\2\2\u015f"+
		"\u0160\7,\2\2\u0160\67\3\2\2\2\u0161\u0162\6\35\5\2\u0162\u0166\5\u0082"+
		"B\2\u0163\u0164\6\35\6\2\u0164\u0166\5\u0082B\2\u0165\u0161\3\2\2\2\u0165"+
		"\u0163\3\2\2\2\u01669\3\2\2\2\u0167\u0168\7\t\2\2\u0168\u0169\7(\2\2\u0169"+
		"\u016a\5\u0082B\2\u016a\u016b\7)\2\2\u016b\u016d\5\22\n\2\u016c\u016e"+
		"\5<\37\2\u016d\u016c\3\2\2\2\u016d\u016e\3\2\2\2\u016e;\3\2\2\2\u016f"+
		"\u0170\7\n\2\2\u0170\u0171\5\22\n\2\u0171=\3\2\2\2\u0172\u0173\7\13\2"+
		"\2\u0173\u0174\5\22\n\2\u0174\u0175\7\f\2\2\u0175\u0176\7(\2\2\u0176\u0177"+
		"\5\u0082B\2\u0177\u0178\7)\2\2\u0178\u0179\5\u009eP\2\u0179\u01ae\3\2"+
		"\2\2\u017a\u017b\7\f\2\2\u017b\u017c\7(\2\2\u017c\u017d\5\u0082B\2\u017d"+
		"\u017e\7)\2\2\u017e\u017f\5\22\n\2\u017f\u01ae\3\2\2\2\u0180\u0181\7\r"+
		"\2\2\u0181\u0183\7(\2\2\u0182\u0184\5\u0082B\2\u0183\u0182\3\2\2\2\u0183"+
		"\u0184\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\7,\2\2\u0186\u0188\5\u0082"+
		"B\2\u0187\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189"+
		"\u018b\7,\2\2\u018a\u018c\5\u0082B\2\u018b\u018a\3\2\2\2\u018b\u018c\3"+
		"\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e\7)\2\2\u018e\u01ae\5\22\n\2\u018f"+
		"\u0190\7\r\2\2\u0190\u0191\7(\2\2\u0191\u0192\t\2\2\2\u0192\u0193\5\34"+
		"\17\2\u0193\u0195\7,\2\2\u0194\u0196\5\u0082B\2\u0195\u0194\3\2\2\2\u0195"+
		"\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0199\7,\2\2\u0198\u019a\5\u0082"+
		"B\2\u0199\u0198\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\3\2\2\2\u019b"+
		"\u019c\7)\2\2\u019c\u019d\5\22\n\2\u019d\u01ae\3\2\2\2\u019e\u01a0\7\r"+
		"\2\2\u019f\u01a1\7\16\2\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1"+
		"\u01a2\3\2\2\2\u01a2\u01a6\7(\2\2\u01a3\u01a4\t\2\2\2\u01a4\u01a7\5 \21"+
		"\2\u01a5\u01a7\5\u0088E\2\u01a6\u01a3\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7"+
		"\u01a8\3\2\2\2\u01a8\u01a9\t\3\2\2\u01a9\u01aa\5\u0082B\2\u01aa\u01ab"+
		"\7)\2\2\u01ab\u01ac\5\22\n\2\u01ac\u01ae\3\2\2\2\u01ad\u0172\3\2\2\2\u01ad"+
		"\u017a\3\2\2\2\u01ad\u0180\3\2\2\2\u01ad\u018f\3\2\2\2\u01ad\u019e\3\2"+
		"\2\2\u01ae?\3\2\2\2\u01af\u01b0\7\21\2\2\u01b0\u01b2\6!\7\2\u01b1\u01b3"+
		"\5\u009aN\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3A\3\2\2\2\u01b4"+
		"\u01b5\7\22\2\2\u01b5\u01b7\6\"\b\2\u01b6\u01b8\5\u009aN\2\u01b7\u01b6"+
		"\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8C\3\2\2\2\u01b9\u01ba\7\23\2\2\u01ba"+
		"\u01bc\6#\t\2\u01bb\u01bd\5\u0082B\2\u01bc\u01bb\3\2\2\2\u01bc\u01bd\3"+
		"\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01c0\5\u009eP\2\u01bf\u01be\3\2\2\2"+
		"\u01bf\u01c0\3\2\2\2\u01c0E\3\2\2\2\u01c1\u01c2\7\24\2\2\u01c2\u01c3\7"+
		"(\2\2\u01c3\u01c4\5\u0082B\2\u01c4\u01c5\7)\2\2\u01c5\u01c6\5\22\n\2\u01c6"+
		"G\3\2\2\2\u01c7\u01c8\7\25\2\2\u01c8\u01c9\7(\2\2\u01c9\u01ca\5\u0082"+
		"B\2\u01ca\u01cb\7)\2\2\u01cb\u01cc\5J&\2\u01ccI\3\2\2\2\u01cd\u01cf\7"+
		"*\2\2\u01ce\u01d0\5L\'\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0"+
		"\u01d5\3\2\2\2\u01d1\u01d3\5P)\2\u01d2\u01d4\5L\'\2\u01d3\u01d2\3\2\2"+
		"\2\u01d3\u01d4\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d1\3\2\2\2\u01d5\u01d6"+
		"\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\7+\2\2\u01d8K\3\2\2\2\u01d9\u01db"+
		"\5N(\2\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc"+
		"\u01dd\3\2\2\2\u01ddM\3\2\2\2\u01de\u01df\7\26\2\2\u01df\u01e0\5\u0082"+
		"B\2\u01e0\u01e2\7\60\2\2\u01e1\u01e3\5\30\r\2\u01e2\u01e1\3\2\2\2\u01e2"+
		"\u01e3\3\2\2\2\u01e3O\3\2\2\2\u01e4\u01e5\7\27\2\2\u01e5\u01e7\7\60\2"+
		"\2\u01e6\u01e8\5\30\r\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8"+
		"Q\3\2\2\2\u01e9\u01ea\5t;\2\u01ea\u01ed\7\60\2\2\u01eb\u01ee\5\22\n\2"+
		"\u01ec\u01ee\5\u0082B\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee"+
		"S\3\2\2\2\u01ef\u01f0\7\30\2\2\u01f0\u01f1\6+\n\2\u01f1\u01f2\5\u0082"+
		"B\2\u01f2U\3\2\2\2\u01f3\u01f4\7\31\2\2\u01f4\u01f8\5\26\f\2\u01f5\u01f7"+
		"\5X-\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8"+
		"\u01f9\3\2\2\2\u01f9\u020a\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fc\7\31"+
		"\2\2\u01fc\u01fd\5\26\f\2\u01fd\u01fe\5Z.\2\u01fe\u020a\3\2\2\2\u01ff"+
		"\u0200\7\31\2\2\u0200\u0204\5\26\f\2\u0201\u0203\5X-\2\u0202\u0201\3\2"+
		"\2\2\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205"+
		"\u0207\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0208\5Z.\2\u0208\u020a\3\2\2"+
		"\2\u0209\u01f3\3\2\2\2\u0209\u01fb\3\2\2\2\u0209\u01ff\3\2\2\2\u020aW"+
		"\3\2\2\2\u020b\u020c\7\32\2\2\u020c\u020d\7(\2\2\u020d\u0210\5 \21\2\u020e"+
		"\u020f\7\t\2\2\u020f\u0211\5\u0082B\2\u0210\u020e\3\2\2\2\u0210\u0211"+
		"\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213\7)\2\2\u0213\u0214\5\26\f\2\u0214"+
		"Y\3\2\2\2\u0215\u0216\7\33\2\2\u0216\u0217\5\26\f\2\u0217[\3\2\2\2\u0218"+
		"\u0219\7\34\2\2\u0219]\3\2\2\2\u021a\u0221\5(\25\2\u021b\u0221\5`\61\2"+
		"\u021c\u021d\5`\61\2\u021d\u021e\7-\2\2\u021e\u021f\5(\25\2\u021f\u0221"+
		"\3\2\2\2\u0220\u021a\3\2\2\2\u0220\u021b\3\2\2\2\u0220\u021c\3\2\2\2\u0221"+
		"_\3\2\2\2\u0222\u0227\5b\62\2\u0223\u0224\7-\2\2\u0224\u0226\5b\62\2\u0225"+
		"\u0223\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2"+
		"\2\2\u0228a\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022e\5\u009aN\2\u022b\u022e"+
		"\5f\64\2\u022c\u022e\5l\67\2\u022d\u022a\3\2\2\2\u022d\u022b\3\2\2\2\u022d"+
		"\u022c\3\2\2\2\u022ec\3\2\2\2\u022f\u0231\5\4\3\2\u0230\u022f\3\2\2\2"+
		"\u0230\u0231\3\2\2\2\u0231e\3\2\2\2\u0232\u0234\7&\2\2\u0233\u0235\5j"+
		"\66\2\u0234\u0233\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0236\3\2\2\2\u0236"+
		"\u0244\7\'\2\2\u0237\u0238\7&\2\2\u0238\u0239\5h\65\2\u0239\u023a\7\'"+
		"\2\2\u023a\u0244\3\2\2\2\u023b\u023c\7&\2\2\u023c\u023d\5h\65\2\u023d"+
		"\u023f\7-\2\2\u023e\u0240\5j\66\2\u023f\u023e\3\2\2\2\u023f\u0240\3\2"+
		"\2\2\u0240\u0241\3\2\2\2\u0241\u0242\7\'\2\2\u0242\u0244\3\2\2\2\u0243"+
		"\u0232\3\2\2\2\u0243\u0237\3\2\2\2\u0243\u023b\3\2\2\2\u0244g\3\2\2\2"+
		"\u0245\u0247\b\65\1\2\u0246\u0248\5j\66\2\u0247\u0246\3\2\2\2\u0247\u0248"+
		"\3\2\2\2\u0248\u024a\3\2\2\2\u0249\u024b\7\b\2\2\u024a\u0249\3\2\2\2\u024a"+
		"\u024b\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d\5\u0084C\2\u024d\u0259"+
		"\3\2\2\2\u024e\u024f\f\3\2\2\u024f\u0251\7-\2\2\u0250\u0252\5j\66\2\u0251"+
		"\u0250\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0254\3\2\2\2\u0253\u0255\7\b"+
		"\2\2\u0254\u0253\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0256\3\2\2\2\u0256"+
		"\u0258\5\u0084C\2\u0257\u024e\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257"+
		"\3\2\2\2\u0259\u025a\3\2\2\2\u025ai\3\2\2\2\u025b\u0259\3\2\2\2\u025c"+
		"\u025e\7-\2\2\u025d\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u025d\3\2"+
		"\2\2\u025f\u0260\3\2\2\2\u0260k\3\2\2\2\u0261\u0262\7*\2\2\u0262\u026d"+
		"\7+\2\2\u0263\u0264\7*\2\2\u0264\u0265\5n8\2\u0265\u0266\7+\2\2\u0266"+
		"\u026d\3\2\2\2\u0267\u0268\7*\2\2\u0268\u0269\5n8\2\u0269\u026a\7-\2\2"+
		"\u026a\u026b\7+\2\2\u026b\u026d\3\2\2\2\u026c\u0261\3\2\2\2\u026c\u0263"+
		"\3\2\2\2\u026c\u0267\3\2\2\2\u026dm\3\2\2\2\u026e\u026f\b8\1\2\u026f\u0270"+
		"\5p9\2\u0270\u0276\3\2\2\2\u0271\u0272\f\3\2\2\u0272\u0273\7-\2\2\u0273"+
		"\u0275\5p9\2\u0274\u0271\3\2\2\2\u0275\u0278\3\2\2\2\u0276\u0274\3\2\2"+
		"\2\u0276\u0277\3\2\2\2\u0277o\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u027b"+
		"\5\"\22\2\u027a\u027c\5\64\33\2\u027b\u027a\3\2\2\2\u027b\u027c\3\2\2"+
		"\2\u027c\u0283\3\2\2\2\u027d\u027e\5t;\2\u027e\u027f\7\60\2\2\u027f\u0280"+
		"\5\u0084C\2\u0280\u0283\3\2\2\2\u0281\u0283\5r:\2\u0282\u0279\3\2\2\2"+
		"\u0282\u027d\3\2\2\2\u0282\u0281\3\2\2\2\u0283q\3\2\2\2\u0284\u0285\6"+
		":\r\2\u0285\u0286\5t;\2\u0286\u0288\7(\2\2\u0287\u0289\5^\60\2\u0288\u0287"+
		"\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u028b\7)\2\2\u028b"+
		"\u028c\7*\2\2\u028c\u028d\5d\63\2\u028d\u028e\7+\2\2\u028es\3\2\2\2\u028f"+
		"\u0297\5\u009aN\2\u0290\u0297\7\u0089\2\2\u0291\u0297\5\u0098M\2\u0292"+
		"\u0293\7&\2\2\u0293\u0294\5\u0084C\2\u0294\u0295\7\'\2\2\u0295\u0297\3"+
		"\2\2\2\u0296\u028f\3\2\2\2\u0296\u0290\3\2\2\2\u0296\u0291\3\2\2\2\u0296"+
		"\u0292\3\2\2\2\u0297u\3\2\2\2\u0298\u0299\5\u009aN\2\u0299w\3\2\2\2\u029a"+
		"\u029c\7(\2\2\u029b\u029d\5z>\2\u029c\u029b\3\2\2\2\u029c\u029d\3\2\2"+
		"\2\u029d\u029e\3\2\2\2\u029e\u029f\7)\2\2\u029fy\3\2\2\2\u02a0\u02a2\b"+
		">\1\2\u02a1\u02a3\7\b\2\2\u02a2\u02a1\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3"+
		"\u02a4\3\2\2\2\u02a4\u02a5\5\u0084C\2\u02a5\u02ae\3\2\2\2\u02a6\u02a7"+
		"\f\3\2\2\u02a7\u02a9\7-\2\2\u02a8\u02aa\7\b\2\2\u02a9\u02a8\3\2\2\2\u02a9"+
		"\u02aa\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab\u02ad\5\u0084C\2\u02ac\u02a6"+
		"\3\2\2\2\u02ad\u02b0\3\2\2\2\u02ae\u02ac\3\2\2\2\u02ae\u02af\3\2\2\2\u02af"+
		"{\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b1\u02b2\5~@\2\u02b2\u02b3\6?\17\2\u02b3"+
		"\u02b4\7\35\2\2\u02b4\u02b5\5\u0080A\2\u02b5}\3\2\2\2\u02b6\u02c0\5\""+
		"\22\2\u02b7\u02b9\7(\2\2\u02b8\u02ba\5\u0082B\2\u02b9\u02b8\3\2\2\2\u02b9"+
		"\u02ba\3\2\2\2\u02ba\u02bc\3\2\2\2\u02bb\u02bd\5(\25\2\u02bc\u02bb\3\2"+
		"\2\2\u02bc\u02bd\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02c0\7)\2\2\u02bf"+
		"\u02b6\3\2\2\2\u02bf\u02b7\3\2\2\2\u02c0\177\3\2\2\2\u02c1\u02c2\6A\20"+
		"\2\u02c2\u02c8\5\u0084C\2\u02c3\u02c4\7*\2\2\u02c4\u02c5\5d\63\2\u02c5"+
		"\u02c6\7+\2\2\u02c6\u02c8\3\2\2\2\u02c7\u02c1\3\2\2\2\u02c7\u02c3\3\2"+
		"\2\2\u02c8\u0081\3\2\2\2\u02c9\u02ca\bB\1\2\u02ca\u02cb\5\u0084C\2\u02cb"+
		"\u02d1\3\2\2\2\u02cc\u02cd\f\3\2\2\u02cd\u02ce\7-\2\2\u02ce\u02d0\5\u0084"+
		"C\2\u02cf\u02cc\3\2\2\2\u02d0\u02d3\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d1"+
		"\u02d2\3\2\2\2\u02d2\u0083\3\2\2\2\u02d3\u02d1\3\2\2\2\u02d4\u02d6\5\u0086"+
		"D\2\u02d5\u02d7\5\u009eP\2\u02d6\u02d5\3\2\2\2\u02d6\u02d7\3\2\2\2\u02d7"+
		"\u02e5\3\2\2\2\u02d8\u02e5\5\24\13\2\u02d9\u02da\5\u0086D\2\u02da\u02db"+
		"\7.\2\2\u02db\u02dd\5\u0084C\2\u02dc\u02de\5\u009eP\2\u02dd\u02dc\3\2"+
		"\2\2\u02dd\u02de\3\2\2\2\u02de\u02e5\3\2\2\2\u02df\u02e0\5\u0086D\2\u02e0"+
		"\u02e1\5\u0094K\2\u02e1\u02e2\5\u0084C\2\u02e2\u02e5\3\2\2\2\u02e3\u02e5"+
		"\5|?\2\u02e4\u02d4\3\2\2\2\u02e4\u02d8\3\2\2\2\u02e4\u02d9\3\2\2\2\u02e4"+
		"\u02df\3\2\2\2\u02e4\u02e3\3\2\2\2\u02e5\u0085\3\2\2\2\u02e6\u02e7\bD"+
		"\1\2\u02e7\u02e8\7\37\2\2\u02e8\u02fb\5\u0086D\16\u02e9\u02ea\7 \2\2\u02ea"+
		"\u02fb\5\u0086D\r\u02eb\u02ec\7!\2\2\u02ec\u02fb\5\u0086D\f\u02ed\u02ee"+
		"\7\62\2\2\u02ee\u02fb\5\u0086D\13\u02ef\u02f0\7\63\2\2\u02f0\u02fb\5\u0086"+
		"D\n\u02f1\u02f2\7\64\2\2\u02f2\u02fb\5\u0086D\t\u02f3\u02f4\7\65\2\2\u02f4"+
		"\u02fb\5\u0086D\b\u02f5\u02f6\7\66\2\2\u02f6\u02fb\5\u0086D\7\u02f7\u02f8"+
		"\7\67\2\2\u02f8\u02fb\5\u0086D\6\u02f9\u02fb\5\u0088E\2\u02fa\u02e6\3"+
		"\2\2\2\u02fa\u02e9\3\2\2\2\u02fa\u02eb\3\2\2\2\u02fa\u02ed\3\2\2\2\u02fa"+
		"\u02ef\3\2\2\2\u02fa\u02f1\3\2\2\2\u02fa\u02f3\3\2\2\2\u02fa\u02f5\3\2"+
		"\2\2\u02fa\u02f7\3\2\2\2\u02fa\u02f9\3\2\2\2\u02fb\u034f\3\2\2\2\u02fc"+
		"\u02fd\f%\2\2\u02fd\u02fe\7J\2\2\u02fe\u034e\5\u0086D&\u02ff\u0300\f$"+
		"\2\2\u0300\u0301\7I\2\2\u0301\u034e\5\u0086D%\u0302\u0303\f#\2\2\u0303"+
		"\u0304\7H\2\2\u0304\u034e\5\u0086D$\u0305\u0306\f\"\2\2\u0306\u0307\7"+
		"G\2\2\u0307\u034e\5\u0086D#\u0308\u0309\f!\2\2\u0309\u030a\7F\2\2\u030a"+
		"\u034e\5\u0086D\"\u030b\u030c\f \2\2\u030c\u030d\7B\2\2\u030d\u034e\5"+
		"\u0086D!\u030e\u030f\f\37\2\2\u030f\u0310\7C\2\2\u0310\u034e\5\u0086D"+
		" \u0311\u0312\f\36\2\2\u0312\u0313\7D\2\2\u0313\u034e\5\u0086D\37\u0314"+
		"\u0315\f\35\2\2\u0315\u0316\7E\2\2\u0316\u034e\5\u0086D\36\u0317\u0318"+
		"\f\34\2\2\u0318\u0319\7>\2\2\u0319\u034e\5\u0086D\35\u031a\u031b\f\33"+
		"\2\2\u031b\u031c\7?\2\2\u031c\u034e\5\u0086D\34\u031d\u031e\f\32\2\2\u031e"+
		"\u031f\7@\2\2\u031f\u034e\5\u0086D\33\u0320\u0321\f\31\2\2\u0321\u0322"+
		"\7A\2\2\u0322\u034e\5\u0086D\32\u0323\u0324\f\30\2\2\u0324\u0325\7\36"+
		"\2\2\u0325\u034e\5\u0086D\31\u0326\u0327\f\27\2\2\u0327\u0328\7\17\2\2"+
		"\u0328\u034e\5\u0086D\30\u0329\u032a\f\26\2\2\u032a\u032b\7<\2\2\u032b"+
		"\u034e\5\u0086D\27\u032c\u032d\f\25\2\2\u032d\u032e\7;\2\2\u032e\u034e"+
		"\5\u0086D\26\u032f\u0330\f\24\2\2\u0330\u0331\7=\2\2\u0331\u034e\5\u0086"+
		"D\25\u0332\u0333\f\23\2\2\u0333\u0334\7\64\2\2\u0334\u034e\5\u0086D\24"+
		"\u0335\u0336\f\22\2\2\u0336\u0337\7\65\2\2\u0337\u034e\5\u0086D\23\u0338"+
		"\u0339\f\21\2\2\u0339\u033a\78\2\2\u033a\u034e\5\u0086D\22\u033b\u033c"+
		"\f\20\2\2\u033c\u033d\79\2\2\u033d\u034e\5\u0086D\21\u033e\u033f\f\17"+
		"\2\2\u033f\u0340\7:\2\2\u0340\u034e\5\u0086D\20\u0341\u0342\f&\2\2\u0342"+
		"\u0343\7/\2\2\u0343\u0344\5\u0084C\2\u0344\u0345\7\60\2\2\u0345\u0346"+
		"\5\u0084C\2\u0346\u034e\3\2\2\2\u0347\u0348\f\5\2\2\u0348\u0349\6D+\2"+
		"\u0349\u034e\7\62\2\2\u034a\u034b\f\4\2\2\u034b\u034c\6D-\2\u034c\u034e"+
		"\7\63\2\2\u034d\u02fc\3\2\2\2\u034d\u02ff\3\2\2\2\u034d\u0302\3\2\2\2"+
		"\u034d\u0305\3\2\2\2\u034d\u0308\3\2\2\2\u034d\u030b\3\2\2\2\u034d\u030e"+
		"\3\2\2\2\u034d\u0311\3\2\2\2\u034d\u0314\3\2\2\2\u034d\u0317\3\2\2\2\u034d"+
		"\u031a\3\2\2\2\u034d\u031d\3\2\2\2\u034d\u0320\3\2\2\2\u034d\u0323\3\2"+
		"\2\2\u034d\u0326\3\2\2\2\u034d\u0329\3\2\2\2\u034d\u032c\3\2\2\2\u034d"+
		"\u032f\3\2\2\2\u034d\u0332\3\2\2\2\u034d\u0335\3\2\2\2\u034d\u0338\3\2"+
		"\2\2\u034d\u033b\3\2\2\2\u034d\u033e\3\2\2\2\u034d\u0341\3\2\2\2\u034d"+
		"\u0347\3\2\2\2\u034d\u034a\3\2\2\2\u034e\u0351\3\2\2\2\u034f\u034d\3\2"+
		"\2\2\u034f\u0350\3\2\2\2\u0350\u0087\3\2\2\2\u0351\u034f\3\2\2\2\u0352"+
		"\u0355\5\u008aF\2\u0353\u0355\5\u008cG\2\u0354\u0352\3\2\2\2\u0354\u0353"+
		"\3\2\2\2\u0355\u0089\3\2\2\2\u0356\u0357\bF\1\2\u0357\u0358\5\u008eH\2"+
		"\u0358\u035a\5x=\2\u0359\u035b\5\u009eP\2\u035a\u0359\3\2\2\2\u035a\u035b"+
		"\3\2\2\2\u035b\u0370\3\2\2\2\u035c\u035d\f\5\2\2\u035d\u035f\5x=\2\u035e"+
		"\u0360\5\u009eP\2\u035f\u035e\3\2\2\2\u035f\u0360\3\2\2\2\u0360\u036f"+
		"\3\2\2\2\u0361\u0362\f\4\2\2\u0362\u0363\7&\2\2\u0363\u0364\5\u0082B\2"+
		"\u0364\u0366\7\'\2\2\u0365\u0367\5\u009eP\2\u0366\u0365\3\2\2\2\u0366"+
		"\u0367\3\2\2\2\u0367\u036f\3\2\2\2\u0368\u0369\f\3\2\2\u0369\u036a\7\61"+
		"\2\2\u036a\u036c\5\u009aN\2\u036b\u036d\5\u009eP\2\u036c\u036b\3\2\2\2"+
		"\u036c\u036d\3\2\2\2\u036d\u036f\3\2\2\2\u036e\u035c\3\2\2\2\u036e\u0361"+
		"\3\2\2\2\u036e\u0368\3\2\2\2\u036f\u0372\3\2\2\2\u0370\u036e\3\2\2\2\u0370"+
		"\u0371\3\2\2\2\u0371\u008b\3\2\2\2\u0372\u0370\3\2\2\2\u0373\u0377\5\u008e"+
		"H\2\u0374\u0375\7\"\2\2\u0375\u0377\5\u008cG\2\u0376\u0373\3\2\2\2\u0376"+
		"\u0374\3\2\2\2\u0377\u008d\3\2\2\2\u0378\u0379\bH\1\2\u0379\u037f\5\u0092"+
		"J\2\u037a\u037b\7\"\2\2\u037b\u037c\5\u008eH\2\u037c\u037d\5x=\2\u037d"+
		"\u037f\3\2\2\2\u037e\u0378\3\2\2\2\u037e\u037a\3\2\2\2\u037f\u038a\3\2"+
		"\2\2\u0380\u0381\f\5\2\2\u0381\u0382\7&\2\2\u0382\u0383\5\u0082B\2\u0383"+
		"\u0384\7\'\2\2\u0384\u0389\3\2\2\2\u0385\u0386\f\4\2\2\u0386\u0387\7\61"+
		"\2\2\u0387\u0389\5\u009aN\2\u0388\u0380\3\2\2\2\u0388\u0385\3\2\2\2\u0389"+
		"\u038c\3\2\2\2\u038a\u0388\3\2\2\2\u038a\u038b\3\2\2\2\u038b\u008f\3\2"+
		"\2\2\u038c\u038a\3\2\2\2\u038d\u038f\7\3\2\2\u038e\u0390\78\2\2\u038f"+
		"\u038e\3\2\2\2\u038f\u0390\3\2\2\2\u0390\u0392\3\2\2\2\u0391\u0393\5\u009a"+
		"N\2\u0392\u0391\3\2\2\2\u0392\u0393\3\2\2\2\u0393\u0394\3\2\2\2\u0394"+
		"\u0396\7(\2\2\u0395\u0397\5^\60\2\u0396\u0395\3\2\2\2\u0396\u0397\3\2"+
		"\2\2\u0397\u0398\3\2\2\2\u0398\u039e\7)\2\2\u0399\u039a\7*\2\2\u039a\u039b"+
		"\5d\63\2\u039b\u039c\7+\2\2\u039c\u039f\3\2\2\2\u039d\u039f\5\22\n\2\u039e"+
		"\u0399\3\2\2\2\u039e\u039d\3\2\2\2\u039f\u0091\3\2\2\2\u03a0\u03ac\7#"+
		"\2\2\u03a1\u03ac\5\u009aN\2\u03a2\u03ac\5\u0090I\2\u03a3\u03ac\5\b\5\2"+
		"\u03a4\u03ac\5\u0096L\2\u03a5\u03ac\5l\67\2\u03a6\u03a7\7(\2\2\u03a7\u03a8"+
		"\5\u0082B\2\u03a8\u03a9\7)\2\2\u03a9\u03ac\3\2\2\2\u03aa\u03ac\5f\64\2"+
		"\u03ab\u03a0\3\2\2\2\u03ab\u03a1\3\2\2\2\u03ab\u03a2\3\2\2\2\u03ab\u03a3"+
		"\3\2\2\2\u03ab\u03a4\3\2\2\2\u03ab\u03a5\3\2\2\2\u03ab\u03a6\3\2\2\2\u03ab"+
		"\u03aa\3\2\2\2\u03ac\u0093\3\2\2\2\u03ad\u03ae\t\4\2\2\u03ae\u0095\3\2"+
		"\2\2\u03af\u03b2\t\5\2\2\u03b0\u03b2\5\u0098M\2\u03b1\u03af\3\2\2\2\u03b1"+
		"\u03b0\3\2\2\2\u03b2\u0097\3\2\2\2\u03b3\u03b4\t\6\2\2\u03b4\u0099\3\2"+
		"\2\2\u03b5\u03b6\7\u0088\2\2\u03b6\u009b\3\2\2\2\u03b7\u03b8\t\7\2\2\u03b8"+
		"\u009d\3\2\2\2\u03b9\u03be\7,\2\2\u03ba\u03be\7\2\2\3\u03bb\u03be\6P\63"+
		"\2\u03bc\u03be\6P\64\2\u03bd\u03b9\3\2\2\2\u03bd\u03ba\3\2\2\2\u03bd\u03bb"+
		"\3\2\2\2\u03bd\u03bc\3\2\2\2\u03be\u009f\3\2\2\2\u03bf\u03c0\7\2\2\3\u03c0"+
		"\u00a1\3\2\2\2i\u00a5\u00ad\u00b3\u00bc\u00cb\u00ce\u00e3\u00e7\u00ea"+
		"\u00ee\u00f9\u00ff\u0109\u010e\u0112\u0116\u011b\u011f\u012c\u0131\u0137"+
		"\u013c\u0140\u0146\u0152\u015a\u0165\u016d\u0183\u0187\u018b\u0195\u0199"+
		"\u01a0\u01a6\u01ad\u01b2\u01b7\u01bc\u01bf\u01cf\u01d3\u01d5\u01dc\u01e2"+
		"\u01e7\u01ed\u01f8\u0204\u0209\u0210\u0220\u0227\u022d\u0230\u0234\u023f"+
		"\u0243\u0247\u024a\u0251\u0254\u0259\u025f\u026c\u0276\u027b\u0282\u0288"+
		"\u0296\u029c\u02a2\u02a9\u02ae\u02b9\u02bc\u02bf\u02c7\u02d1\u02d6\u02dd"+
		"\u02e4\u02fa\u034d\u034f\u0354\u035a\u035f\u0366\u036c\u036e\u0370\u0376"+
		"\u037e\u0388\u038a\u038f\u0392\u0396\u039e\u03ab\u03b1\u03bd";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}