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
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, RegularExpressionLiteral=42, LineTerminator=43, 
		OpenBracket=44, CloseBracket=45, OpenParen=46, CloseParen=47, OpenBrace=48, 
		CloseBrace=49, SemiColon=50, Comma=51, Assign=52, QuestionMark=53, Colon=54, 
		Dot=55, PlusPlus=56, MinusMinus=57, Plus=58, Minus=59, BitNot=60, Not=61, 
		Multiply=62, Divide=63, Modulus=64, RightShiftArithmetic=65, LeftShiftArithmetic=66, 
		RightShiftLogical=67, LessThan=68, MoreThan=69, LessThanEquals=70, GreaterThanEquals=71, 
		Equals=72, NotEquals=73, IdentityEquals=74, IdentityNotEquals=75, BitAnd=76, 
		BitXOr=77, BitOr=78, And=79, Or=80, MultiplyAssign=81, DivideAssign=82, 
		ModulusAssign=83, PlusAssign=84, MinusAssign=85, LeftShiftArithmeticAssign=86, 
		RightShiftArithmeticAssign=87, RightShiftLogicalAssign=88, BitAndAssign=89, 
		BitXorAssign=90, BitOrAssign=91, NullLiteral=92, BooleanLiteral=93, DecimalLiteral=94, 
		HexIntegerLiteral=95, OctalIntegerLiteral=96, BinaryLiteral=97, Break=98, 
		Do=99, Instanceof=100, Typeof=101, Case=102, Else=103, New=104, Var=105, 
		Catch=106, Finally=107, Return=108, Void=109, Continue=110, For=111, Switch=112, 
		While=113, Debugger=114, Function=115, This=116, With=117, Default=118, 
		If=119, Throw=120, Delete=121, In=122, Try=123, Of=124, Get=125, Set=126, 
		Each=127, Class=128, Enum=129, Extends=130, Super=131, Const=132, Export=133, 
		Import=134, Implements=135, Let=136, Private=137, Public=138, Interface=139, 
		Package=140, Protected=141, Static=142, Yield=143, Identifier=144, StringLiteral=145, 
		WhiteSpaces=146, MultiLineComment=147, SingleLineComment=148, UnexpectedCharacter=149;
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
		RULE_leftHandSideExpression = 67, RULE_callExpression = 68, RULE_superCall = 69, 
		RULE_newExpression = 70, RULE_memberExpression = 71, RULE_superPropery = 72, 
		RULE_functionExpression = 73, RULE_primaryExpression = 74, RULE_assignmentOperator = 75, 
		RULE_literal = 76, RULE_numericLiteral = 77, RULE_identifierName = 78, 
		RULE_reservedWord = 79, RULE_keyword = 80, RULE_futureReservedWord = 81, 
		RULE_eos = 82, RULE_eof = 83;
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
		"callExpression", "superCall", "newExpression", "memberExpression", "superPropery", 
		"functionExpression", "primaryExpression", "assignmentOperator", "literal", 
		"numericLiteral", "identifierName", "reservedWord", "keyword", "futureReservedWord", 
		"eos", "eof"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'function'", "'static'", "'yield'", "'var'", "'let'", "'...'", 
		"'if'", "'else'", "'do'", "'while'", "'for'", "'each'", "'in'", "'of'", 
		"'continue'", "'break'", "'return'", "'with'", "'switch'", "'case'", "'default'", 
		"'throw'", "'try'", "'catch'", "'finally'", "'debugger'", "'get'", "'set'", 
		"'=>'", "'instanceof'", "'delete'", "'void'", "'typeof'", "'new'", "'this'", 
		"'implements'", "'private'", "'public'", "'interface'", "'package'", "'protected'", 
		null, null, "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','", "'='", 
		"'?'", "':'", "'.'", "'++'", "'--'", "'+'", "'-'", "'~'", "'!'", "'*'", 
		"'/'", "'%'", "'>>'", "'<<'", "'>>>'", "'<'", "'>'", "'<='", "'>='", "'=='", 
		"'!='", "'==='", "'!=='", "'&'", "'^'", "'|'", "'&&'", "'||'", "'*='", 
		"'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", "'>>>='", "'&='", "'^='", 
		"'|='", "'null'", null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, "'class'", "'enum'", "'extends'", "'super'", "'const'", "'export'", 
		"'import'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, "RegularExpressionLiteral", "LineTerminator", 
		"OpenBracket", "CloseBracket", "OpenParen", "CloseParen", "OpenBrace", 
		"CloseBrace", "SemiColon", "Comma", "Assign", "QuestionMark", "Colon", 
		"Dot", "PlusPlus", "MinusMinus", "Plus", "Minus", "BitNot", "Not", "Multiply", 
		"Divide", "Modulus", "RightShiftArithmetic", "LeftShiftArithmetic", "RightShiftLogical", 
		"LessThan", "MoreThan", "LessThanEquals", "GreaterThanEquals", "Equals", 
		"NotEquals", "IdentityEquals", "IdentityNotEquals", "BitAnd", "BitXOr", 
		"BitOr", "And", "Or", "MultiplyAssign", "DivideAssign", "ModulusAssign", 
		"PlusAssign", "MinusAssign", "LeftShiftArithmeticAssign", "RightShiftArithmeticAssign", 
		"RightShiftLogicalAssign", "BitAndAssign", "BitXorAssign", "BitOrAssign", 
		"NullLiteral", "BooleanLiteral", "DecimalLiteral", "HexIntegerLiteral", 
		"OctalIntegerLiteral", "BinaryLiteral", "Break", "Do", "Instanceof", "Typeof", 
		"Case", "Else", "New", "Var", "Catch", "Finally", "Return", "Void", "Continue", 
		"For", "Switch", "While", "Debugger", "Function", "This", "With", "Default", 
		"If", "Throw", "Delete", "In", "Try", "Of", "Get", "Set", "Each", "Class", 
		"Enum", "Extends", "Super", "Const", "Export", "Import", "Implements", 
		"Let", "Private", "Public", "Interface", "Package", "Protected", "Static", 
		"Yield", "Identifier", "StringLiteral", "WhiteSpaces", "MultiLineComment", 
		"SingleLineComment", "UnexpectedCharacter"
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
			setState(171);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(168); 
					statementListItem();
					}
					} 
				}
				setState(173);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(174); 
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
			setState(179);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(176); 
				functionDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(177); 
				classDeclaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(178); 
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
			setState(181); 
			match(T__0);
			setState(182); 
			identifierName();
			setState(183); 
			match(OpenParen);
			setState(185);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << OpenBracket) | (1L << OpenBrace))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)))) != 0)) {
				{
				setState(184); 
				formalParameterList();
				}
			}

			setState(187); 
			match(CloseParen);
			setState(188); 
			match(OpenBrace);
			setState(189); 
			functionBody();
			setState(190); 
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
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192); 
			match(Class);
			setState(194);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(193); 
				identifierReference();
				}
				break;
			}
			setState(196); 
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
			setState(198); 
			classHeritage();
			setState(199); 
			match(OpenBrace);
			setState(200); 
			classBody();
			setState(201); 
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
			setState(203); 
			match(Extends);
			setState(204); 
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
			setState(207); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(206); 
					classElement();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(209); 
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
			setState(212);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(211); 
				match(T__1);
				}
				break;
			}
			setState(214); 
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
		public ExpressionStatementContext expressionStatement() {
			return getRuleContext(ExpressionStatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
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
			setState(233);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(216); 
				block();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(217); 
				variableStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(218); 
				emptyStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(219); 
				expressionStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(220); 
				ifStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(221); 
				iterationStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(222); 
				continueStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(223); 
				breakStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(224); 
				returnStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(225); 
				withStatement();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(226); 
				labelledStatement();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(227); 
				switchStatement();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(228); 
				throwStatement();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(229); 
				tryStatement();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(230); 
				debuggerStatement();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(231); 
				yieldExpression();
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(232); 
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
			setState(235); 
			match(T__2);
			setState(237);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(236); 
				match(Multiply);
				}
				break;
			}
			setState(240);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(239); 
				assignmentExpression(0);
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
			setState(242); 
			match(OpenBrace);
			setState(244);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(243); 
				statementList(0);
				}
				break;
			}
			setState(246); 
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
			setState(249); 
			statement();
			}
			_ctx.stop = _input.LT(-1);
			setState(255);
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
					setState(251);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(252); 
					statement();
					}
					} 
				}
				setState(257);
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
			setState(258);
			_la = _input.LA(1);
			if ( !(_la==T__3 || _la==T__4 || _la==Const) ) {
			_errHandler.recoverInline(this);
			}
			consume();
			setState(259); 
			variableDeclarationList(0);
			setState(261);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(260); 
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
			setState(264); 
			variableDeclaration();
			}
			_ctx.stop = _input.LT(-1);
			setState(271);
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
					setState(266);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(267); 
					match(Comma);
					setState(268); 
					variableDeclaration();
					}
					} 
				}
				setState(273);
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
			setState(274); 
			identifierBinding();
			setState(276);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(275); 
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
			setState(280);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case NullLiteral:
			case BooleanLiteral:
			case Class:
			case Enum:
			case Extends:
			case Super:
			case Const:
			case Export:
			case Import:
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(278); 
				identifierReference();
				}
				break;
			case OpenBracket:
			case OpenParen:
			case OpenBrace:
				enterOuterAlt(_localctx, 2);
				{
				setState(279); 
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
			setState(284);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(282); 
				identifierName();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(283); 
				match(T__2);
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
			setState(289);
			switch (_input.LA(1)) {
			case OpenBracket:
				enterOuterAlt(_localctx, 1);
				{
				setState(286); 
				arrayBindingPattern();
				}
				break;
			case OpenBrace:
				enterOuterAlt(_localctx, 2);
				{
				setState(287); 
				objectBindingPattern();
				}
				break;
			case OpenParen:
				enterOuterAlt(_localctx, 3);
				{
				setState(288); 
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
			setState(311);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(291); 
				match(OpenBracket);
				setState(293);
				_la = _input.LA(1);
				if (_la==Comma) {
					{
					setState(292); 
					elision();
					}
				}

				setState(295); 
				restElement();
				setState(296); 
				match(CloseBracket);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(298); 
				match(OpenBracket);
				setState(299); 
				bindingElementList();
				setState(300); 
				match(CloseBracket);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(302); 
				match(OpenBracket);
				setState(303); 
				bindingElementList();
				setState(304); 
				match(Comma);
				setState(306);
				_la = _input.LA(1);
				if (_la==Comma) {
					{
					setState(305); 
					elision();
					}
				}

				setState(308); 
				restElement();
				setState(309); 
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
			setState(313); 
			match(T__5);
			setState(314); 
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
			setState(320); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(317);
					_la = _input.LA(1);
					if (_la==Comma) {
						{
						setState(316); 
						elision();
						}
					}

					setState(319); 
					variableDeclaration();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(322); 
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
			setState(324); 
			match(OpenBrace);
			setState(326);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
				{
				setState(325); 
				bindingPropertyList(0);
				}
			}

			setState(328); 
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
			setState(330); 
			match(OpenParen);
			setState(332);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
				{
				setState(331); 
				bindingPropertyList(0);
				}
			}

			setState(334); 
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
			setState(337); 
			bindingProperty();
			}
			_ctx.stop = _input.LT(-1);
			setState(344);
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
					setState(339);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(340); 
					match(Comma);
					setState(341); 
					bindingProperty();
					}
					} 
				}
				setState(346);
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
			setState(352);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(347); 
				variableDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(348); 
				propertyName();
				setState(349); 
				match(Colon);
				setState(350); 
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
			setState(354); 
			match(Assign);
			setState(355); 
			assignmentExpression(0);
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
			setState(357); 
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
			setState(363);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(359);
				if (!(!here(OpenBrace))) throw new FailedPredicateException(this, "!here(OpenBrace)");
				setState(360); 
				expression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(361);
				if (!(!here(Function))) throw new FailedPredicateException(this, "!here(Function)");
				setState(362); 
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
			setState(365); 
			match(T__6);
			setState(366); 
			match(OpenParen);
			setState(367); 
			expression(0);
			setState(368); 
			match(CloseParen);
			setState(369); 
			statement();
			setState(371);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(370); 
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
			setState(373); 
			match(T__7);
			setState(374); 
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
			setState(435);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(376); 
				match(T__8);
				setState(377); 
				statement();
				setState(378); 
				match(T__9);
				setState(379); 
				match(OpenParen);
				setState(380); 
				expression(0);
				setState(381); 
				match(CloseParen);
				setState(382); 
				eos();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(384); 
				match(T__9);
				setState(385); 
				match(OpenParen);
				setState(386); 
				expression(0);
				setState(387); 
				match(CloseParen);
				setState(388); 
				statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(390); 
				match(T__10);
				setState(391); 
				match(OpenParen);
				setState(393);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
					{
					setState(392); 
					expression(0);
					}
				}

				setState(395); 
				match(SemiColon);
				setState(397);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
					{
					setState(396); 
					expression(0);
					}
				}

				setState(399); 
				match(SemiColon);
				setState(401);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
					{
					setState(400); 
					expression(0);
					}
				}

				setState(403); 
				match(CloseParen);
				setState(404); 
				statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(405); 
				match(T__10);
				setState(406); 
				match(OpenParen);
				setState(407);
				_la = _input.LA(1);
				if ( !(_la==T__3 || _la==T__4 || _la==Const) ) {
				_errHandler.recoverInline(this);
				}
				consume();
				setState(408); 
				variableDeclarationList(0);
				setState(409); 
				match(SemiColon);
				setState(411);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
					{
					setState(410); 
					expression(0);
					}
				}

				setState(413); 
				match(SemiColon);
				setState(415);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
					{
					setState(414); 
					expression(0);
					}
				}

				setState(417); 
				match(CloseParen);
				setState(418); 
				statement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(420); 
				match(T__10);
				setState(422);
				_la = _input.LA(1);
				if (_la==T__11) {
					{
					setState(421); 
					match(T__11);
					}
				}

				setState(424); 
				match(OpenParen);
				setState(428);
				switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
				case 1:
					{
					setState(425);
					_la = _input.LA(1);
					if ( !(_la==T__3 || _la==T__4 || _la==Const) ) {
					_errHandler.recoverInline(this);
					}
					consume();
					setState(426); 
					identifierBinding();
					}
					break;
				case 2:
					{
					setState(427); 
					leftHandSideExpression();
					}
					break;
				}
				setState(430);
				_la = _input.LA(1);
				if ( !(_la==T__12 || _la==T__13) ) {
				_errHandler.recoverInline(this);
				}
				consume();
				setState(431); 
				expression(0);
				setState(432); 
				match(CloseParen);
				setState(433); 
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
			setState(437); 
			match(T__14);
			setState(438);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(440);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(439); 
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
			setState(442); 
			match(T__15);
			setState(443);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(445);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				{
				setState(444); 
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
			setState(447); 
			match(T__16);
			setState(448);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(450);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				{
				setState(449); 
				expression(0);
				}
				break;
			}
			setState(453);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				{
				setState(452); 
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
			setState(455); 
			match(T__17);
			setState(456); 
			match(OpenParen);
			setState(457); 
			expression(0);
			setState(458); 
			match(CloseParen);
			setState(459); 
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
			setState(461); 
			match(T__18);
			setState(462); 
			match(OpenParen);
			setState(463); 
			expression(0);
			setState(464); 
			match(CloseParen);
			setState(465); 
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
			setState(467); 
			match(OpenBrace);
			setState(469);
			_la = _input.LA(1);
			if (_la==T__19) {
				{
				setState(468); 
				caseClauses();
				}
			}

			setState(475);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(471); 
				defaultClause();
				setState(473);
				_la = _input.LA(1);
				if (_la==T__19) {
					{
					setState(472); 
					caseClauses();
					}
				}

				}
			}

			setState(477); 
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
			setState(480); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(479); 
				caseClause();
				}
				}
				setState(482); 
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
			setState(484); 
			match(T__19);
			setState(485); 
			expression(0);
			setState(486); 
			match(Colon);
			setState(488);
			switch ( getInterpreter().adaptivePredict(_input,44,_ctx) ) {
			case 1:
				{
				setState(487); 
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
			setState(490); 
			match(T__20);
			setState(491); 
			match(Colon);
			setState(493);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				{
				setState(492); 
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
			setState(495); 
			propertyName();
			setState(496); 
			match(Colon);
			setState(499);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				{
				setState(497); 
				statement();
				}
				break;
			case 2:
				{
				setState(498); 
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
			setState(501); 
			match(T__21);
			setState(502);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(503); 
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
			setState(527);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(505); 
				match(T__22);
				setState(506); 
				block();
				setState(510);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,47,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(507); 
						catchProduction();
						}
						} 
					}
					setState(512);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,47,_ctx);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(513); 
				match(T__22);
				setState(514); 
				block();
				setState(515); 
				finallyProduction();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(517); 
				match(T__22);
				setState(518); 
				block();
				setState(522);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__23) {
					{
					{
					setState(519); 
					catchProduction();
					}
					}
					setState(524);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(525); 
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
			setState(529); 
			match(T__23);
			setState(530); 
			match(OpenParen);
			setState(531); 
			identifierBinding();
			setState(534);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(532); 
				match(T__6);
				setState(533); 
				expression(0);
				}
			}

			setState(536); 
			match(CloseParen);
			setState(537); 
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
			setState(539); 
			match(T__24);
			setState(540); 
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
			setState(542); 
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
			setState(550);
			switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(544); 
				restElement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(545); 
				formalParameters();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(546); 
				formalParameters();
				setState(547); 
				match(Comma);
				setState(548); 
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
			setState(552); 
			formalParameter();
			setState(557);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,52,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(553); 
					match(Comma);
					setState(554); 
					formalParameter();
					}
					} 
				}
				setState(559);
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
			setState(563);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case NullLiteral:
			case BooleanLiteral:
			case Class:
			case Enum:
			case Extends:
			case Super:
			case Const:
			case Export:
			case Import:
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(560); 
				identifierName();
				}
				break;
			case OpenBracket:
				enterOuterAlt(_localctx, 2);
				{
				setState(561); 
				arrayLiteral();
				}
				break;
			case OpenBrace:
				enterOuterAlt(_localctx, 3);
				{
				setState(562); 
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
			setState(566);
			switch ( getInterpreter().adaptivePredict(_input,54,_ctx) ) {
			case 1:
				{
				setState(565); 
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
			setState(585);
			switch ( getInterpreter().adaptivePredict(_input,57,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(568); 
				match(OpenBracket);
				setState(570);
				_la = _input.LA(1);
				if (_la==Comma) {
					{
					setState(569); 
					elision();
					}
				}

				setState(572); 
				match(CloseBracket);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(573); 
				match(OpenBracket);
				setState(574); 
				elementList(0);
				setState(575); 
				match(CloseBracket);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(577); 
				match(OpenBracket);
				setState(578); 
				elementList(0);
				setState(579); 
				match(Comma);
				setState(581);
				_la = _input.LA(1);
				if (_la==Comma) {
					{
					setState(580); 
					elision();
					}
				}

				setState(583); 
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
			setState(589);
			_la = _input.LA(1);
			if (_la==Comma) {
				{
				setState(588); 
				elision();
				}
			}

			setState(592);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(591); 
				match(T__5);
				}
			}

			setState(594); 
			assignmentExpression(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(607);
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
					setState(596);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(597); 
					match(Comma);
					setState(599);
					_la = _input.LA(1);
					if (_la==Comma) {
						{
						setState(598); 
						elision();
						}
					}

					setState(602);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(601); 
						match(T__5);
						}
					}

					setState(604); 
					assignmentExpression(0);
					}
					} 
				}
				setState(609);
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
			setState(611); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(610); 
				match(Comma);
				}
				}
				setState(613); 
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
			setState(626);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(615); 
				match(OpenBrace);
				setState(616); 
				match(CloseBrace);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(617); 
				match(OpenBrace);
				setState(618); 
				propertyNameAndValueList(0);
				setState(619); 
				match(CloseBrace);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(621); 
				match(OpenBrace);
				setState(622); 
				propertyNameAndValueList(0);
				setState(623); 
				match(Comma);
				setState(624); 
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
			setState(629); 
			propertyAssignment();
			}
			_ctx.stop = _input.LT(-1);
			setState(636);
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
					setState(631);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(632); 
					match(Comma);
					setState(633); 
					propertyAssignment();
					}
					} 
				}
				setState(638);
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
			setState(648);
			switch ( getInterpreter().adaptivePredict(_input,67,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(639); 
				identifierReference();
				setState(641);
				switch ( getInterpreter().adaptivePredict(_input,66,_ctx) ) {
				case 1:
					{
					setState(640); 
					initialiser();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(643); 
				propertyName();
				setState(644); 
				match(Colon);
				setState(645); 
				assignmentExpression(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(647); 
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
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
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
			setState(678);
			switch ( getInterpreter().adaptivePredict(_input,69,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(650);
				if (!(!here(Function))) throw new FailedPredicateException(this, "!here(Function)");
				setState(651); 
				propertyName();
				setState(652); 
				match(OpenParen);
				setState(654);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << OpenBracket) | (1L << OpenBrace))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)))) != 0)) {
					{
					setState(653); 
					formalParameterList();
					}
				}

				setState(656); 
				match(CloseParen);
				setState(657); 
				match(OpenBrace);
				setState(658); 
				functionBody();
				setState(659); 
				match(CloseBrace);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(661); 
				match(T__26);
				setState(662); 
				propertyName();
				setState(663); 
				match(OpenParen);
				setState(664); 
				match(CloseParen);
				setState(665); 
				match(OpenBrace);
				setState(666); 
				functionBody();
				setState(667); 
				match(CloseBrace);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(669); 
				match(T__27);
				setState(670); 
				propertyName();
				setState(671); 
				match(OpenParen);
				setState(672); 
				variableDeclaration();
				setState(673); 
				match(CloseParen);
				setState(674); 
				match(OpenBrace);
				setState(675); 
				functionBody();
				setState(676); 
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
			setState(687);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case NullLiteral:
			case BooleanLiteral:
			case Class:
			case Enum:
			case Extends:
			case Super:
			case Const:
			case Export:
			case Import:
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(680); 
				identifierName();
				}
				break;
			case StringLiteral:
				enterOuterAlt(_localctx, 2);
				{
				setState(681); 
				match(StringLiteral);
				}
				break;
			case DecimalLiteral:
			case HexIntegerLiteral:
			case OctalIntegerLiteral:
			case BinaryLiteral:
				enterOuterAlt(_localctx, 3);
				{
				setState(682); 
				numericLiteral();
				}
				break;
			case OpenBracket:
				enterOuterAlt(_localctx, 4);
				{
				setState(683); 
				match(OpenBracket);
				setState(684); 
				assignmentExpression(0);
				setState(685); 
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
			setState(689); 
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
			setState(691); 
			match(OpenParen);
			setState(693);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
				{
				setState(692); 
				argumentList(0);
				}
			}

			setState(695); 
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
			setState(699);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(698); 
				match(T__5);
				}
			}

			setState(701); 
			assignmentExpression(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(711);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,74,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ArgumentListContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_argumentList);
					setState(703);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(704); 
					match(Comma);
					setState(706);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(705); 
						match(T__5);
						}
					}

					setState(708); 
					assignmentExpression(0);
					}
					} 
				}
				setState(713);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,74,_ctx);
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
			setState(714); 
			arrowParameters();
			setState(715);
			if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
			setState(716); 
			match(T__28);
			setState(717); 
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
			setState(728);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case NullLiteral:
			case BooleanLiteral:
			case Class:
			case Enum:
			case Extends:
			case Super:
			case Const:
			case Export:
			case Import:
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(719); 
				identifierReference();
				}
				break;
			case OpenParen:
				enterOuterAlt(_localctx, 2);
				{
				setState(720); 
				match(OpenParen);
				setState(722);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << RegularExpressionLiteral) | (1L << OpenBracket) | (1L << OpenParen) | (1L << OpenBrace) | (1L << PlusPlus) | (1L << MinusMinus) | (1L << Plus) | (1L << Minus) | (1L << BitNot) | (1L << Not))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (DecimalLiteral - 92)) | (1L << (HexIntegerLiteral - 92)) | (1L << (OctalIntegerLiteral - 92)) | (1L << (BinaryLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)) | (1L << (StringLiteral - 92)))) != 0)) {
					{
					setState(721); 
					expression(0);
					}
				}

				setState(725);
				_la = _input.LA(1);
				if (_la==T__5) {
					{
					setState(724); 
					restElement();
					}
				}

				setState(727); 
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
			setState(736);
			switch ( getInterpreter().adaptivePredict(_input,78,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(730);
				if (!(!here(OpenBrace))) throw new FailedPredicateException(this, "!here(OpenBrace)");
				setState(731); 
				assignmentExpression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(732); 
				match(OpenBrace);
				setState(733); 
				functionBody();
				setState(734); 
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
			setState(739); 
			assignmentExpression(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(746);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,79,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(741);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(742); 
					match(Comma);
					setState(743); 
					assignmentExpression(0);
					}
					} 
				}
				setState(748);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,79,_ctx);
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
		public AssignmentOperatorContext assignmentOperator() {
			return getRuleContext(AssignmentOperatorContext.class,0);
		}
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public YieldExpressionContext yieldExpression() {
			return getRuleContext(YieldExpressionContext.class,0);
		}
		public EosContext eos() {
			return getRuleContext(EosContext.class,0);
		}
		public ArrowFunctionContext arrowFunction() {
			return getRuleContext(ArrowFunctionContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IdentifierBindingContext identifierBinding() {
			return getRuleContext(IdentifierBindingContext.class,0);
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
		return assignmentExpression(0);
	}

	private AssignmentExpressionContext assignmentExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		AssignmentExpressionContext _localctx = new AssignmentExpressionContext(_ctx, _parentState);
		AssignmentExpressionContext _prevctx = _localctx;
		int _startState = 130;
		enterRecursionRule(_localctx, 130, RULE_assignmentExpression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(763);
			switch ( getInterpreter().adaptivePredict(_input,81,_ctx) ) {
			case 1:
				{
				setState(750); 
				conditionalExpression(0);
				setState(751); 
				assignmentOperator();
				setState(752); 
				assignmentExpression(4);
				}
				break;
			case 2:
				{
				setState(754); 
				conditionalExpression(0);
				}
				break;
			case 3:
				{
				setState(755); 
				yieldExpression();
				}
				break;
			case 4:
				{
				setState(756); 
				conditionalExpression(0);
				setState(757); 
				match(Assign);
				setState(758); 
				assignmentExpression(0);
				setState(760);
				switch ( getInterpreter().adaptivePredict(_input,80,_ctx) ) {
				case 1:
					{
					setState(759); 
					eos();
					}
					break;
				}
				}
				break;
			case 5:
				{
				setState(762); 
				arrowFunction();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(788);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,85,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(786);
					switch ( getInterpreter().adaptivePredict(_input,84,_ctx) ) {
					case 1:
						{
						_localctx = new AssignmentExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_assignmentExpression);
						setState(765);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(766); 
						match(T__10);
						setState(768);
						_la = _input.LA(1);
						if (_la==T__11) {
							{
							setState(767); 
							match(T__11);
							}
						}

						setState(770); 
						match(OpenParen);
						setState(774);
						switch ( getInterpreter().adaptivePredict(_input,83,_ctx) ) {
						case 1:
							{
							setState(771);
							_la = _input.LA(1);
							if ( !(_la==T__3 || _la==T__4 || _la==Const) ) {
							_errHandler.recoverInline(this);
							}
							consume();
							setState(772); 
							identifierBinding();
							}
							break;
						case 2:
							{
							setState(773); 
							conditionalExpression(0);
							}
							break;
						}
						setState(776);
						_la = _input.LA(1);
						if ( !(_la==T__12 || _la==T__13) ) {
						_errHandler.recoverInline(this);
						}
						consume();
						setState(777); 
						expression(0);
						setState(778); 
						match(CloseParen);
						}
						break;
					case 2:
						{
						_localctx = new AssignmentExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_assignmentExpression);
						setState(780);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(781); 
						match(T__6);
						setState(782); 
						match(OpenParen);
						setState(783); 
						expression(0);
						setState(784); 
						match(CloseParen);
						}
						break;
					}
					} 
				}
				setState(790);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,85,_ctx);
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
			setState(811);
			switch ( getInterpreter().adaptivePredict(_input,86,_ctx) ) {
			case 1:
				{
				setState(792); 
				match(T__30);
				setState(793); 
				conditionalExpression(12);
				}
				break;
			case 2:
				{
				setState(794); 
				match(T__31);
				setState(795); 
				conditionalExpression(11);
				}
				break;
			case 3:
				{
				setState(796); 
				match(T__32);
				setState(797); 
				conditionalExpression(10);
				}
				break;
			case 4:
				{
				setState(798); 
				match(PlusPlus);
				setState(799); 
				conditionalExpression(9);
				}
				break;
			case 5:
				{
				setState(800); 
				match(MinusMinus);
				setState(801); 
				conditionalExpression(8);
				}
				break;
			case 6:
				{
				setState(802); 
				match(Plus);
				setState(803); 
				conditionalExpression(7);
				}
				break;
			case 7:
				{
				setState(804); 
				match(Minus);
				setState(805); 
				conditionalExpression(6);
				}
				break;
			case 8:
				{
				setState(806); 
				match(BitNot);
				setState(807); 
				conditionalExpression(5);
				}
				break;
			case 9:
				{
				setState(808); 
				match(Not);
				setState(809); 
				conditionalExpression(4);
				}
				break;
			case 10:
				{
				setState(810); 
				leftHandSideExpression();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(896);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,88,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(894);
					switch ( getInterpreter().adaptivePredict(_input,87,_ctx) ) {
					case 1:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(813);
						if (!(precpred(_ctx, 35))) throw new FailedPredicateException(this, "precpred(_ctx, 35)");
						setState(814); 
						match(Or);
						setState(815); 
						conditionalExpression(36);
						}
						break;
					case 2:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(816);
						if (!(precpred(_ctx, 34))) throw new FailedPredicateException(this, "precpred(_ctx, 34)");
						setState(817); 
						match(And);
						setState(818); 
						conditionalExpression(35);
						}
						break;
					case 3:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(819);
						if (!(precpred(_ctx, 33))) throw new FailedPredicateException(this, "precpred(_ctx, 33)");
						setState(820); 
						match(BitOr);
						setState(821); 
						conditionalExpression(34);
						}
						break;
					case 4:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(822);
						if (!(precpred(_ctx, 32))) throw new FailedPredicateException(this, "precpred(_ctx, 32)");
						setState(823); 
						match(BitXOr);
						setState(824); 
						conditionalExpression(33);
						}
						break;
					case 5:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(825);
						if (!(precpred(_ctx, 31))) throw new FailedPredicateException(this, "precpred(_ctx, 31)");
						setState(826); 
						match(BitAnd);
						setState(827); 
						conditionalExpression(32);
						}
						break;
					case 6:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(828);
						if (!(precpred(_ctx, 30))) throw new FailedPredicateException(this, "precpred(_ctx, 30)");
						setState(829); 
						match(Equals);
						setState(830); 
						conditionalExpression(31);
						}
						break;
					case 7:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(831);
						if (!(precpred(_ctx, 29))) throw new FailedPredicateException(this, "precpred(_ctx, 29)");
						setState(832); 
						match(NotEquals);
						setState(833); 
						conditionalExpression(30);
						}
						break;
					case 8:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(834);
						if (!(precpred(_ctx, 28))) throw new FailedPredicateException(this, "precpred(_ctx, 28)");
						setState(835); 
						match(IdentityEquals);
						setState(836); 
						conditionalExpression(29);
						}
						break;
					case 9:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(837);
						if (!(precpred(_ctx, 27))) throw new FailedPredicateException(this, "precpred(_ctx, 27)");
						setState(838); 
						match(IdentityNotEquals);
						setState(839); 
						conditionalExpression(28);
						}
						break;
					case 10:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(840);
						if (!(precpred(_ctx, 26))) throw new FailedPredicateException(this, "precpred(_ctx, 26)");
						setState(841); 
						match(LessThan);
						setState(842); 
						conditionalExpression(27);
						}
						break;
					case 11:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(843);
						if (!(precpred(_ctx, 25))) throw new FailedPredicateException(this, "precpred(_ctx, 25)");
						setState(844); 
						match(MoreThan);
						setState(845); 
						conditionalExpression(26);
						}
						break;
					case 12:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(846);
						if (!(precpred(_ctx, 24))) throw new FailedPredicateException(this, "precpred(_ctx, 24)");
						setState(847); 
						match(LessThanEquals);
						setState(848); 
						conditionalExpression(25);
						}
						break;
					case 13:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(849);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(850); 
						match(GreaterThanEquals);
						setState(851); 
						conditionalExpression(24);
						}
						break;
					case 14:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(852);
						if (!(precpred(_ctx, 22))) throw new FailedPredicateException(this, "precpred(_ctx, 22)");
						setState(853); 
						match(T__29);
						setState(854); 
						conditionalExpression(23);
						}
						break;
					case 15:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(855);
						if (!(precpred(_ctx, 21))) throw new FailedPredicateException(this, "precpred(_ctx, 21)");
						setState(856); 
						match(T__12);
						setState(857); 
						conditionalExpression(22);
						}
						break;
					case 16:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(858);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(859); 
						match(LeftShiftArithmetic);
						setState(860); 
						conditionalExpression(21);
						}
						break;
					case 17:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(861);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(862); 
						match(RightShiftArithmetic);
						setState(863); 
						conditionalExpression(20);
						}
						break;
					case 18:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(864);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(865); 
						match(RightShiftLogical);
						setState(866); 
						conditionalExpression(19);
						}
						break;
					case 19:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(867);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(868); 
						match(Plus);
						setState(869); 
						conditionalExpression(18);
						}
						break;
					case 20:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(870);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(871); 
						match(Minus);
						setState(872); 
						conditionalExpression(17);
						}
						break;
					case 21:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(873);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(874); 
						match(Multiply);
						setState(875); 
						conditionalExpression(16);
						}
						break;
					case 22:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(876);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(877); 
						match(Divide);
						setState(878); 
						conditionalExpression(15);
						}
						break;
					case 23:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(879);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(880); 
						match(Modulus);
						setState(881); 
						conditionalExpression(14);
						}
						break;
					case 24:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(882);
						if (!(precpred(_ctx, 36))) throw new FailedPredicateException(this, "precpred(_ctx, 36)");
						setState(883); 
						match(QuestionMark);
						setState(884); 
						assignmentExpression(0);
						setState(885); 
						match(Colon);
						setState(886); 
						assignmentExpression(0);
						}
						break;
					case 25:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(888);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(889);
						if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
						setState(890); 
						match(PlusPlus);
						}
						break;
					case 26:
						{
						_localctx = new ConditionalExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditionalExpression);
						setState(891);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(892);
						if (!(!here(LineTerminator))) throw new FailedPredicateException(this, "!here(LineTerminator)");
						setState(893); 
						match(MinusMinus);
						}
						break;
					}
					} 
				}
				setState(898);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,88,_ctx);
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
			setState(901);
			switch ( getInterpreter().adaptivePredict(_input,89,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(899); 
				callExpression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(900); 
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
		public SuperCallContext superCall() {
			return getRuleContext(SuperCallContext.class,0);
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
			setState(913);
			switch ( getInterpreter().adaptivePredict(_input,92,_ctx) ) {
			case 1:
				{
				setState(904); 
				memberExpression(0);
				setState(905); 
				arguments();
				setState(907);
				switch ( getInterpreter().adaptivePredict(_input,90,_ctx) ) {
				case 1:
					{
					setState(906); 
					eos();
					}
					break;
				}
				}
				break;
			case 2:
				{
				setState(909); 
				superCall();
				setState(911);
				switch ( getInterpreter().adaptivePredict(_input,91,_ctx) ) {
				case 1:
					{
					setState(910); 
					eos();
					}
					break;
				}
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(935);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,97,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(933);
					switch ( getInterpreter().adaptivePredict(_input,96,_ctx) ) {
					case 1:
						{
						_localctx = new CallExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_callExpression);
						setState(915);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(916); 
						arguments();
						setState(918);
						switch ( getInterpreter().adaptivePredict(_input,93,_ctx) ) {
						case 1:
							{
							setState(917); 
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
						setState(920);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(921); 
						match(OpenBracket);
						setState(922); 
						expression(0);
						setState(923); 
						match(CloseBracket);
						setState(925);
						switch ( getInterpreter().adaptivePredict(_input,94,_ctx) ) {
						case 1:
							{
							setState(924); 
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
						setState(927);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(928); 
						match(Dot);
						setState(929); 
						identifierName();
						setState(931);
						switch ( getInterpreter().adaptivePredict(_input,95,_ctx) ) {
						case 1:
							{
							setState(930); 
							eos();
							}
							break;
						}
						}
						break;
					}
					} 
				}
				setState(937);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,97,_ctx);
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

	public static class SuperCallContext extends ParserRuleContext {
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public SuperCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_superCall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterSuperCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitSuperCall(this);
		}
	}

	public final SuperCallContext superCall() throws RecognitionException {
		SuperCallContext _localctx = new SuperCallContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_superCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(938); 
			match(Super);
			setState(939); 
			arguments();
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
		enterRule(_localctx, 140, RULE_newExpression);
		try {
			setState(944);
			switch ( getInterpreter().adaptivePredict(_input,98,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(941); 
				memberExpression(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(942); 
				match(T__33);
				setState(943); 
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
		public SuperProperyContext superPropery() {
			return getRuleContext(SuperProperyContext.class,0);
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
		int _startState = 142;
		enterRecursionRule(_localctx, 142, RULE_memberExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(953);
			switch ( getInterpreter().adaptivePredict(_input,99,_ctx) ) {
			case 1:
				{
				setState(947); 
				primaryExpression();
				}
				break;
			case 2:
				{
				setState(948); 
				superPropery();
				}
				break;
			case 3:
				{
				setState(949); 
				match(T__33);
				setState(950); 
				memberExpression(0);
				setState(951); 
				arguments();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(965);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,101,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(963);
					switch ( getInterpreter().adaptivePredict(_input,100,_ctx) ) {
					case 1:
						{
						_localctx = new MemberExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_memberExpression);
						setState(955);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(956); 
						match(OpenBracket);
						setState(957); 
						expression(0);
						setState(958); 
						match(CloseBracket);
						}
						break;
					case 2:
						{
						_localctx = new MemberExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_memberExpression);
						setState(960);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(961); 
						match(Dot);
						setState(962); 
						identifierName();
						}
						break;
					}
					} 
				}
				setState(967);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,101,_ctx);
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

	public static class SuperProperyContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public SuperProperyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_superPropery; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterSuperPropery(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitSuperPropery(this);
		}
	}

	public final SuperProperyContext superPropery() throws RecognitionException {
		SuperProperyContext _localctx = new SuperProperyContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_superPropery);
		try {
			setState(976);
			switch ( getInterpreter().adaptivePredict(_input,102,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(968); 
				match(Super);
				setState(969); 
				match(OpenBracket);
				setState(970); 
				expression(0);
				setState(971); 
				match(CloseBracket);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(973); 
				match(Super);
				setState(974); 
				match(Dot);
				setState(975); 
				identifierName();
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
		enterRule(_localctx, 146, RULE_functionExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(978); 
			match(T__0);
			setState(980);
			_la = _input.LA(1);
			if (_la==Multiply) {
				{
				setState(979); 
				match(Multiply);
				}
			}

			setState(983);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)))) != 0)) {
				{
				setState(982); 
				identifierName();
				}
			}

			setState(985); 
			match(OpenParen);
			setState(987);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << OpenBracket) | (1L << OpenBrace))) != 0) || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (Class - 92)) | (1L << (Enum - 92)) | (1L << (Extends - 92)) | (1L << (Super - 92)) | (1L << (Const - 92)) | (1L << (Export - 92)) | (1L << (Import - 92)) | (1L << (Identifier - 92)))) != 0)) {
				{
				setState(986); 
				formalParameterList();
				}
			}

			setState(989); 
			match(CloseParen);
			setState(995);
			switch ( getInterpreter().adaptivePredict(_input,106,_ctx) ) {
			case 1:
				{
				setState(990); 
				match(OpenBrace);
				setState(991); 
				functionBody();
				setState(992); 
				match(CloseBrace);
				}
				break;
			case 2:
				{
				setState(994); 
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
		enterRule(_localctx, 148, RULE_primaryExpression);
		try {
			setState(1008);
			switch ( getInterpreter().adaptivePredict(_input,107,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(997); 
				match(T__34);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(998); 
				identifierName();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(999); 
				functionExpression();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(1000); 
				classDeclaration();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(1001); 
				literal();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(1002); 
				objectLiteral();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(1003); 
				match(OpenParen);
				setState(1004); 
				expression(0);
				setState(1005); 
				match(CloseParen);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(1007); 
				arrayLiteral();
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
		enterRule(_localctx, 150, RULE_assignmentOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1010);
			_la = _input.LA(1);
			if ( !(((((_la - 81)) & ~0x3f) == 0 && ((1L << (_la - 81)) & ((1L << (MultiplyAssign - 81)) | (1L << (DivideAssign - 81)) | (1L << (ModulusAssign - 81)) | (1L << (PlusAssign - 81)) | (1L << (MinusAssign - 81)) | (1L << (LeftShiftArithmeticAssign - 81)) | (1L << (RightShiftArithmeticAssign - 81)) | (1L << (RightShiftLogicalAssign - 81)) | (1L << (BitAndAssign - 81)) | (1L << (BitXorAssign - 81)) | (1L << (BitOrAssign - 81)))) != 0)) ) {
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
		enterRule(_localctx, 152, RULE_literal);
		int _la;
		try {
			setState(1014);
			switch (_input.LA(1)) {
			case RegularExpressionLiteral:
			case NullLiteral:
			case BooleanLiteral:
			case StringLiteral:
				enterOuterAlt(_localctx, 1);
				{
				setState(1012);
				_la = _input.LA(1);
				if ( !(_la==RegularExpressionLiteral || ((((_la - 92)) & ~0x3f) == 0 && ((1L << (_la - 92)) & ((1L << (NullLiteral - 92)) | (1L << (BooleanLiteral - 92)) | (1L << (StringLiteral - 92)))) != 0)) ) {
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
				setState(1013); 
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
		enterRule(_localctx, 154, RULE_numericLiteral);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1016);
			_la = _input.LA(1);
			if ( !(((((_la - 94)) & ~0x3f) == 0 && ((1L << (_la - 94)) & ((1L << (DecimalLiteral - 94)) | (1L << (HexIntegerLiteral - 94)) | (1L << (OctalIntegerLiteral - 94)) | (1L << (BinaryLiteral - 94)))) != 0)) ) {
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
		public ReservedWordContext reservedWord() {
			return getRuleContext(ReservedWordContext.class,0);
		}
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
		enterRule(_localctx, 156, RULE_identifierName);
		try {
			setState(1020);
			switch (_input.LA(1)) {
			case Identifier:
				enterOuterAlt(_localctx, 1);
				{
				setState(1018); 
				match(Identifier);
				}
				break;
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case NullLiteral:
			case BooleanLiteral:
			case Class:
			case Enum:
			case Extends:
			case Super:
			case Const:
			case Export:
			case Import:
				enterOuterAlt(_localctx, 2);
				{
				setState(1019); 
				reservedWord();
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

	public static class ReservedWordContext extends ParserRuleContext {
		public KeywordContext keyword() {
			return getRuleContext(KeywordContext.class,0);
		}
		public FutureReservedWordContext futureReservedWord() {
			return getRuleContext(FutureReservedWordContext.class,0);
		}
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
		enterRule(_localctx, 158, RULE_reservedWord);
		int _la;
		try {
			setState(1025);
			switch (_input.LA(1)) {
			case T__0:
			case T__3:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
				enterOuterAlt(_localctx, 1);
				{
				setState(1022); 
				keyword();
				}
				break;
			case T__1:
			case T__2:
			case T__4:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case Class:
			case Enum:
			case Extends:
			case Super:
			case Const:
			case Export:
			case Import:
				enterOuterAlt(_localctx, 2);
				{
				setState(1023); 
				futureReservedWord();
				}
				break;
			case NullLiteral:
			case BooleanLiteral:
				enterOuterAlt(_localctx, 3);
				{
				setState(1024);
				_la = _input.LA(1);
				if ( !(_la==NullLiteral || _la==BooleanLiteral) ) {
				_errHandler.recoverInline(this);
				}
				consume();
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

	public static class KeywordContext extends ParserRuleContext {
		public KeywordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyword; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterKeyword(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitKeyword(this);
		}
	}

	public final KeywordContext keyword() throws RecognitionException {
		KeywordContext _localctx = new KeywordContext(_ctx, getState());
		enterRule(_localctx, 160, RULE_keyword);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1027);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__3) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19) | (1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34))) != 0)) ) {
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

	public static class FutureReservedWordContext extends ParserRuleContext {
		public FutureReservedWordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_futureReservedWord; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).enterFutureReservedWord(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ECMAScriptListener ) ((ECMAScriptListener)listener).exitFutureReservedWord(this);
		}
	}

	public final FutureReservedWordContext futureReservedWord() throws RecognitionException {
		FutureReservedWordContext _localctx = new FutureReservedWordContext(_ctx, getState());
		enterRule(_localctx, 162, RULE_futureReservedWord);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1029);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__2) | (1L << T__4) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40))) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & ((1L << (Class - 128)) | (1L << (Enum - 128)) | (1L << (Extends - 128)) | (1L << (Super - 128)) | (1L << (Const - 128)) | (1L << (Export - 128)) | (1L << (Import - 128)))) != 0)) ) {
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
		enterRule(_localctx, 164, RULE_eos);
		try {
			setState(1035);
			switch ( getInterpreter().adaptivePredict(_input,111,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1031); 
				match(SemiColon);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1032); 
				match(EOF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1033);
				if (!(lineTerminatorAhead())) throw new FailedPredicateException(this, "lineTerminatorAhead()");
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(1034);
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
		enterRule(_localctx, 166, RULE_eof);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1037); 
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
		case 65: 
			return assignmentExpression_sempred((AssignmentExpressionContext)_localctx, predIndex);
		case 66: 
			return conditionalExpression_sempred((ConditionalExpressionContext)_localctx, predIndex);
		case 68: 
			return callExpression_sempred((CallExpressionContext)_localctx, predIndex);
		case 71: 
			return memberExpression_sempred((MemberExpressionContext)_localctx, predIndex);
		case 82: 
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
	private boolean assignmentExpression_sempred(AssignmentExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 16: 
			return precpred(_ctx, 2);
		case 17: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean conditionalExpression_sempred(ConditionalExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 18: 
			return precpred(_ctx, 35);
		case 19: 
			return precpred(_ctx, 34);
		case 20: 
			return precpred(_ctx, 33);
		case 21: 
			return precpred(_ctx, 32);
		case 22: 
			return precpred(_ctx, 31);
		case 23: 
			return precpred(_ctx, 30);
		case 24: 
			return precpred(_ctx, 29);
		case 25: 
			return precpred(_ctx, 28);
		case 26: 
			return precpred(_ctx, 27);
		case 27: 
			return precpred(_ctx, 26);
		case 28: 
			return precpred(_ctx, 25);
		case 29: 
			return precpred(_ctx, 24);
		case 30: 
			return precpred(_ctx, 23);
		case 31: 
			return precpred(_ctx, 22);
		case 32: 
			return precpred(_ctx, 21);
		case 33: 
			return precpred(_ctx, 20);
		case 34: 
			return precpred(_ctx, 19);
		case 35: 
			return precpred(_ctx, 18);
		case 36: 
			return precpred(_ctx, 17);
		case 37: 
			return precpred(_ctx, 16);
		case 38: 
			return precpred(_ctx, 15);
		case 39: 
			return precpred(_ctx, 14);
		case 40: 
			return precpred(_ctx, 13);
		case 41: 
			return precpred(_ctx, 36);
		case 42: 
			return precpred(_ctx, 3);
		case 43: 
			return !here(LineTerminator);
		case 44: 
			return precpred(_ctx, 2);
		case 45: 
			return !here(LineTerminator);
		}
		return true;
	}
	private boolean callExpression_sempred(CallExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 46: 
			return precpred(_ctx, 3);
		case 47: 
			return precpred(_ctx, 2);
		case 48: 
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean memberExpression_sempred(MemberExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 49: 
			return precpred(_ctx, 4);
		case 50: 
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean eos_sempred(EosContext _localctx, int predIndex) {
		switch (predIndex) {
		case 51: 
			return lineTerminatorAhead();
		case 52: 
			return _input.LT(1).getType() == CloseBrace;
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0097\u0412\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\3\2\7\2\u00ac\n\2\f\2\16\2\u00af\13\2\3\2\3\2\3\3\3\3\3\3\5\3\u00b6"+
		"\n\3\3\4\3\4\3\4\3\4\5\4\u00bc\n\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5\u00c5"+
		"\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\6\b\u00d2\n\b\r\b\16"+
		"\b\u00d3\3\t\5\t\u00d7\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00ec\n\n\3\13\3\13\5\13\u00f0\n"+
		"\13\3\13\5\13\u00f3\n\13\3\f\3\f\5\f\u00f7\n\f\3\f\3\f\3\r\3\r\3\r\3\r"+
		"\3\r\7\r\u0100\n\r\f\r\16\r\u0103\13\r\3\16\3\16\3\16\5\16\u0108\n\16"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u0110\n\17\f\17\16\17\u0113\13\17"+
		"\3\20\3\20\5\20\u0117\n\20\3\21\3\21\5\21\u011b\n\21\3\22\3\22\5\22\u011f"+
		"\n\22\3\23\3\23\3\23\5\23\u0124\n\23\3\24\3\24\5\24\u0128\n\24\3\24\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0135\n\24\3\24"+
		"\3\24\3\24\5\24\u013a\n\24\3\25\3\25\3\25\3\26\5\26\u0140\n\26\3\26\6"+
		"\26\u0143\n\26\r\26\16\26\u0144\3\27\3\27\5\27\u0149\n\27\3\27\3\27\3"+
		"\30\3\30\5\30\u014f\n\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31"+
		"\u0159\n\31\f\31\16\31\u015c\13\31\3\32\3\32\3\32\3\32\3\32\5\32\u0163"+
		"\n\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u016e\n\35\3\36"+
		"\3\36\3\36\3\36\3\36\3\36\5\36\u0176\n\36\3\37\3\37\3\37\3 \3 \3 \3 \3"+
		" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u018c\n \3 \3 \5 \u0190\n \3"+
		" \3 \5 \u0194\n \3 \3 \3 \3 \3 \3 \3 \3 \5 \u019e\n \3 \3 \5 \u01a2\n"+
		" \3 \3 \3 \3 \3 \5 \u01a9\n \3 \3 \3 \3 \5 \u01af\n \3 \3 \3 \3 \3 \5"+
		" \u01b6\n \3!\3!\3!\5!\u01bb\n!\3\"\3\"\3\"\5\"\u01c0\n\"\3#\3#\3#\5#"+
		"\u01c5\n#\3#\5#\u01c8\n#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\5&"+
		"\u01d8\n&\3&\3&\5&\u01dc\n&\5&\u01de\n&\3&\3&\3\'\6\'\u01e3\n\'\r\'\16"+
		"\'\u01e4\3(\3(\3(\3(\5(\u01eb\n(\3)\3)\3)\5)\u01f0\n)\3*\3*\3*\3*\5*\u01f6"+
		"\n*\3+\3+\3+\3+\3,\3,\3,\7,\u01ff\n,\f,\16,\u0202\13,\3,\3,\3,\3,\3,\3"+
		",\3,\7,\u020b\n,\f,\16,\u020e\13,\3,\3,\5,\u0212\n,\3-\3-\3-\3-\3-\5-"+
		"\u0219\n-\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0229"+
		"\n\60\3\61\3\61\3\61\7\61\u022e\n\61\f\61\16\61\u0231\13\61\3\62\3\62"+
		"\3\62\5\62\u0236\n\62\3\63\5\63\u0239\n\63\3\64\3\64\5\64\u023d\n\64\3"+
		"\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0248\n\64\3\64\3\64"+
		"\5\64\u024c\n\64\3\65\3\65\5\65\u0250\n\65\3\65\5\65\u0253\n\65\3\65\3"+
		"\65\3\65\3\65\3\65\5\65\u025a\n\65\3\65\5\65\u025d\n\65\3\65\7\65\u0260"+
		"\n\65\f\65\16\65\u0263\13\65\3\66\6\66\u0266\n\66\r\66\16\66\u0267\3\67"+
		"\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0275\n\67\38"+
		"\38\38\38\38\38\78\u027d\n8\f8\168\u0280\138\39\39\59\u0284\n9\39\39\3"+
		"9\39\39\59\u028b\n9\3:\3:\3:\3:\5:\u0291\n:\3:\3:\3:\3:\3:\3:\3:\3:\3"+
		":\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u02a9\n:\3;\3;\3;\3;\3;\3"+
		";\3;\5;\u02b2\n;\3<\3<\3=\3=\5=\u02b8\n=\3=\3=\3>\3>\5>\u02be\n>\3>\3"+
		">\3>\3>\3>\5>\u02c5\n>\3>\7>\u02c8\n>\f>\16>\u02cb\13>\3?\3?\3?\3?\3?"+
		"\3@\3@\3@\5@\u02d5\n@\3@\5@\u02d8\n@\3@\5@\u02db\n@\3A\3A\3A\3A\3A\3A"+
		"\5A\u02e3\nA\3B\3B\3B\3B\3B\3B\7B\u02eb\nB\fB\16B\u02ee\13B\3C\3C\3C\3"+
		"C\3C\3C\3C\3C\3C\3C\3C\5C\u02fb\nC\3C\5C\u02fe\nC\3C\3C\3C\5C\u0303\n"+
		"C\3C\3C\3C\3C\5C\u0309\nC\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\7C\u0315\nC\f"+
		"C\16C\u0318\13C\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\5D\u032e\nD\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D"+
		"\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\7D\u0381\nD\fD"+
		"\16D\u0384\13D\3E\3E\5E\u0388\nE\3F\3F\3F\3F\5F\u038e\nF\3F\3F\5F\u0392"+
		"\nF\5F\u0394\nF\3F\3F\3F\5F\u0399\nF\3F\3F\3F\3F\3F\5F\u03a0\nF\3F\3F"+
		"\3F\3F\5F\u03a6\nF\7F\u03a8\nF\fF\16F\u03ab\13F\3G\3G\3G\3H\3H\3H\5H\u03b3"+
		"\nH\3I\3I\3I\3I\3I\3I\3I\5I\u03bc\nI\3I\3I\3I\3I\3I\3I\3I\3I\7I\u03c6"+
		"\nI\fI\16I\u03c9\13I\3J\3J\3J\3J\3J\3J\3J\3J\5J\u03d3\nJ\3K\3K\5K\u03d7"+
		"\nK\3K\5K\u03da\nK\3K\3K\5K\u03de\nK\3K\3K\3K\3K\3K\3K\5K\u03e6\nK\3L"+
		"\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u03f3\nL\3M\3M\3N\3N\5N\u03f9\nN\3O"+
		"\3O\3P\3P\5P\u03ff\nP\3Q\3Q\3Q\5Q\u0404\nQ\3R\3R\3S\3S\3T\3T\3T\3T\5T"+
		"\u040e\nT\3U\3U\3U\2\r\30\34\60hnz\u0082\u0084\u0086\u008a\u0090V\2\4"+
		"\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNP"+
		"RTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e"+
		"\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6"+
		"\u00a8\2\n\4\2\6\7\u0086\u0086\3\2\17\20\3\2S]\5\2,,^_\u0093\u0093\3\2"+
		"`c\3\2^_\6\2\3\3\6\6\t\36 %\6\2\4\5\7\7&+\u0082\u0088\u0479\2\u00ad\3"+
		"\2\2\2\4\u00b5\3\2\2\2\6\u00b7\3\2\2\2\b\u00c2\3\2\2\2\n\u00c8\3\2\2\2"+
		"\f\u00cd\3\2\2\2\16\u00d1\3\2\2\2\20\u00d6\3\2\2\2\22\u00eb\3\2\2\2\24"+
		"\u00ed\3\2\2\2\26\u00f4\3\2\2\2\30\u00fa\3\2\2\2\32\u0104\3\2\2\2\34\u0109"+
		"\3\2\2\2\36\u0114\3\2\2\2 \u011a\3\2\2\2\"\u011e\3\2\2\2$\u0123\3\2\2"+
		"\2&\u0139\3\2\2\2(\u013b\3\2\2\2*\u0142\3\2\2\2,\u0146\3\2\2\2.\u014c"+
		"\3\2\2\2\60\u0152\3\2\2\2\62\u0162\3\2\2\2\64\u0164\3\2\2\2\66\u0167\3"+
		"\2\2\28\u016d\3\2\2\2:\u016f\3\2\2\2<\u0177\3\2\2\2>\u01b5\3\2\2\2@\u01b7"+
		"\3\2\2\2B\u01bc\3\2\2\2D\u01c1\3\2\2\2F\u01c9\3\2\2\2H\u01cf\3\2\2\2J"+
		"\u01d5\3\2\2\2L\u01e2\3\2\2\2N\u01e6\3\2\2\2P\u01ec\3\2\2\2R\u01f1\3\2"+
		"\2\2T\u01f7\3\2\2\2V\u0211\3\2\2\2X\u0213\3\2\2\2Z\u021d\3\2\2\2\\\u0220"+
		"\3\2\2\2^\u0228\3\2\2\2`\u022a\3\2\2\2b\u0235\3\2\2\2d\u0238\3\2\2\2f"+
		"\u024b\3\2\2\2h\u024d\3\2\2\2j\u0265\3\2\2\2l\u0274\3\2\2\2n\u0276\3\2"+
		"\2\2p\u028a\3\2\2\2r\u02a8\3\2\2\2t\u02b1\3\2\2\2v\u02b3\3\2\2\2x\u02b5"+
		"\3\2\2\2z\u02bb\3\2\2\2|\u02cc\3\2\2\2~\u02da\3\2\2\2\u0080\u02e2\3\2"+
		"\2\2\u0082\u02e4\3\2\2\2\u0084\u02fd\3\2\2\2\u0086\u032d\3\2\2\2\u0088"+
		"\u0387\3\2\2\2\u008a\u0393\3\2\2\2\u008c\u03ac\3\2\2\2\u008e\u03b2\3\2"+
		"\2\2\u0090\u03bb\3\2\2\2\u0092\u03d2\3\2\2\2\u0094\u03d4\3\2\2\2\u0096"+
		"\u03f2\3\2\2\2\u0098\u03f4\3\2\2\2\u009a\u03f8\3\2\2\2\u009c\u03fa\3\2"+
		"\2\2\u009e\u03fe\3\2\2\2\u00a0\u0403\3\2\2\2\u00a2\u0405\3\2\2\2\u00a4"+
		"\u0407\3\2\2\2\u00a6\u040d\3\2\2\2\u00a8\u040f\3\2\2\2\u00aa\u00ac\5\4"+
		"\3\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad"+
		"\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\7\2"+
		"\2\3\u00b1\3\3\2\2\2\u00b2\u00b6\5\6\4\2\u00b3\u00b6\5\b\5\2\u00b4\u00b6"+
		"\5\22\n\2\u00b5\u00b2\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2"+
		"\u00b6\5\3\2\2\2\u00b7\u00b8\7\3\2\2\u00b8\u00b9\5\u009eP\2\u00b9\u00bb"+
		"\7\60\2\2\u00ba\u00bc\5^\60\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2"+
		"\u00bc\u00bd\3\2\2\2\u00bd\u00be\7\61\2\2\u00be\u00bf\7\62\2\2\u00bf\u00c0"+
		"\5d\63\2\u00c0\u00c1\7\63\2\2\u00c1\7\3\2\2\2\u00c2\u00c4\7\u0082\2\2"+
		"\u00c3\u00c5\5\"\22\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6"+
		"\3\2\2\2\u00c6\u00c7\5\n\6\2\u00c7\t\3\2\2\2\u00c8\u00c9\5\f\7\2\u00c9"+
		"\u00ca\7\62\2\2\u00ca\u00cb\5\16\b\2\u00cb\u00cc\7\63\2\2\u00cc\13\3\2"+
		"\2\2\u00cd\u00ce\7\u0084\2\2\u00ce\u00cf\5\u0086D\2\u00cf\r\3\2\2\2\u00d0"+
		"\u00d2\5\20\t\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1\3"+
		"\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\17\3\2\2\2\u00d5\u00d7\7\4\2\2\u00d6"+
		"\u00d5\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\5r"+
		":\2\u00d9\21\3\2\2\2\u00da\u00ec\5\26\f\2\u00db\u00ec\5\32\16\2\u00dc"+
		"\u00ec\5\66\34\2\u00dd\u00ec\58\35\2\u00de\u00ec\5:\36\2\u00df\u00ec\5"+
		"> \2\u00e0\u00ec\5@!\2\u00e1\u00ec\5B\"\2\u00e2\u00ec\5D#\2\u00e3\u00ec"+
		"\5F$\2\u00e4\u00ec\5R*\2\u00e5\u00ec\5H%\2\u00e6\u00ec\5T+\2\u00e7\u00ec"+
		"\5V,\2\u00e8\u00ec\5\\/\2\u00e9\u00ec\5\24\13\2\u00ea\u00ec\5<\37\2\u00eb"+
		"\u00da\3\2\2\2\u00eb\u00db\3\2\2\2\u00eb\u00dc\3\2\2\2\u00eb\u00dd\3\2"+
		"\2\2\u00eb\u00de\3\2\2\2\u00eb\u00df\3\2\2\2\u00eb\u00e0\3\2\2\2\u00eb"+
		"\u00e1\3\2\2\2\u00eb\u00e2\3\2\2\2\u00eb\u00e3\3\2\2\2\u00eb\u00e4\3\2"+
		"\2\2\u00eb\u00e5\3\2\2\2\u00eb\u00e6\3\2\2\2\u00eb\u00e7\3\2\2\2\u00eb"+
		"\u00e8\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\23\3\2\2"+
		"\2\u00ed\u00ef\7\5\2\2\u00ee\u00f0\7@\2\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0"+
		"\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00f3\5\u0084C\2\u00f2\u00f1\3\2\2"+
		"\2\u00f2\u00f3\3\2\2\2\u00f3\25\3\2\2\2\u00f4\u00f6\7\62\2\2\u00f5\u00f7"+
		"\5\30\r\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2"+
		"\u00f8\u00f9\7\63\2\2\u00f9\27\3\2\2\2\u00fa\u00fb\b\r\1\2\u00fb\u00fc"+
		"\5\22\n\2\u00fc\u0101\3\2\2\2\u00fd\u00fe\f\3\2\2\u00fe\u0100\5\22\n\2"+
		"\u00ff\u00fd\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102"+
		"\3\2\2\2\u0102\31\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\t\2\2\2\u0105"+
		"\u0107\5\34\17\2\u0106\u0108\5\u00a6T\2\u0107\u0106\3\2\2\2\u0107\u0108"+
		"\3\2\2\2\u0108\33\3\2\2\2\u0109\u010a\b\17\1\2\u010a\u010b\5\36\20\2\u010b"+
		"\u0111\3\2\2\2\u010c\u010d\f\3\2\2\u010d\u010e\7\65\2\2\u010e\u0110\5"+
		"\36\20\2\u010f\u010c\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111"+
		"\u0112\3\2\2\2\u0112\35\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0116\5 \21"+
		"\2\u0115\u0117\5\64\33\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2\u0117"+
		"\37\3\2\2\2\u0118\u011b\5\"\22\2\u0119\u011b\5$\23\2\u011a\u0118\3\2\2"+
		"\2\u011a\u0119\3\2\2\2\u011b!\3\2\2\2\u011c\u011f\5\u009eP\2\u011d\u011f"+
		"\7\5\2\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f#\3\2\2\2\u0120"+
		"\u0124\5&\24\2\u0121\u0124\5,\27\2\u0122\u0124\5.\30\2\u0123\u0120\3\2"+
		"\2\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124%\3\2\2\2\u0125\u0127"+
		"\7.\2\2\u0126\u0128\5j\66\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128"+
		"\u0129\3\2\2\2\u0129\u012a\5(\25\2\u012a\u012b\7/\2\2\u012b\u013a\3\2"+
		"\2\2\u012c\u012d\7.\2\2\u012d\u012e\5*\26\2\u012e\u012f\7/\2\2\u012f\u013a"+
		"\3\2\2\2\u0130\u0131\7.\2\2\u0131\u0132\5*\26\2\u0132\u0134\7\65\2\2\u0133"+
		"\u0135\5j\66\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3\2"+
		"\2\2\u0136\u0137\5(\25\2\u0137\u0138\7/\2\2\u0138\u013a\3\2\2\2\u0139"+
		"\u0125\3\2\2\2\u0139\u012c\3\2\2\2\u0139\u0130\3\2\2\2\u013a\'\3\2\2\2"+
		"\u013b\u013c\7\b\2\2\u013c\u013d\5\"\22\2\u013d)\3\2\2\2\u013e\u0140\5"+
		"j\66\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141"+
		"\u0143\5\36\20\2\u0142\u013f\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0142\3"+
		"\2\2\2\u0144\u0145\3\2\2\2\u0145+\3\2\2\2\u0146\u0148\7\62\2\2\u0147\u0149"+
		"\5\60\31\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2"+
		"\u014a\u014b\7\63\2\2\u014b-\3\2\2\2\u014c\u014e\7\60\2\2\u014d\u014f"+
		"\5\60\31\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2"+
		"\u0150\u0151\7\61\2\2\u0151/\3\2\2\2\u0152\u0153\b\31\1\2\u0153\u0154"+
		"\5\62\32\2\u0154\u015a\3\2\2\2\u0155\u0156\f\3\2\2\u0156\u0157\7\65\2"+
		"\2\u0157\u0159\5\62\32\2\u0158\u0155\3\2\2\2\u0159\u015c\3\2\2\2\u015a"+
		"\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\61\3\2\2\2\u015c\u015a\3\2\2"+
		"\2\u015d\u0163\5\36\20\2\u015e\u015f\5t;\2\u015f\u0160\78\2\2\u0160\u0161"+
		"\5\36\20\2\u0161\u0163\3\2\2\2\u0162\u015d\3\2\2\2\u0162\u015e\3\2\2\2"+
		"\u0163\63\3\2\2\2\u0164\u0165\7\66\2\2\u0165\u0166\5\u0084C\2\u0166\65"+
		"\3\2\2\2\u0167\u0168\7\64\2\2\u0168\67\3\2\2\2\u0169\u016a\6\35\5\2\u016a"+
		"\u016e\5\u0082B\2\u016b\u016c\6\35\6\2\u016c\u016e\5\u0082B\2\u016d\u0169"+
		"\3\2\2\2\u016d\u016b\3\2\2\2\u016e9\3\2\2\2\u016f\u0170\7\t\2\2\u0170"+
		"\u0171\7\60\2\2\u0171\u0172\5\u0082B\2\u0172\u0173\7\61\2\2\u0173\u0175"+
		"\5\22\n\2\u0174\u0176\5<\37\2\u0175\u0174\3\2\2\2\u0175\u0176\3\2\2\2"+
		"\u0176;\3\2\2\2\u0177\u0178\7\n\2\2\u0178\u0179\5\22\n\2\u0179=\3\2\2"+
		"\2\u017a\u017b\7\13\2\2\u017b\u017c\5\22\n\2\u017c\u017d\7\f\2\2\u017d"+
		"\u017e\7\60\2\2\u017e\u017f\5\u0082B\2\u017f\u0180\7\61\2\2\u0180\u0181"+
		"\5\u00a6T\2\u0181\u01b6\3\2\2\2\u0182\u0183\7\f\2\2\u0183\u0184\7\60\2"+
		"\2\u0184\u0185\5\u0082B\2\u0185\u0186\7\61\2\2\u0186\u0187\5\22\n\2\u0187"+
		"\u01b6\3\2\2\2\u0188\u0189\7\r\2\2\u0189\u018b\7\60\2\2\u018a\u018c\5"+
		"\u0082B\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\3\2\2\2"+
		"\u018d\u018f\7\64\2\2\u018e\u0190\5\u0082B\2\u018f\u018e\3\2\2\2\u018f"+
		"\u0190\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193\7\64\2\2\u0192\u0194\5"+
		"\u0082B\2\u0193\u0192\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195\3\2\2\2"+
		"\u0195\u0196\7\61\2\2\u0196\u01b6\5\22\n\2\u0197\u0198\7\r\2\2\u0198\u0199"+
		"\7\60\2\2\u0199\u019a\t\2\2\2\u019a\u019b\5\34\17\2\u019b\u019d\7\64\2"+
		"\2\u019c\u019e\5\u0082B\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e"+
		"\u019f\3\2\2\2\u019f\u01a1\7\64\2\2\u01a0\u01a2\5\u0082B\2\u01a1\u01a0"+
		"\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\7\61\2\2"+
		"\u01a4\u01a5\5\22\n\2\u01a5\u01b6\3\2\2\2\u01a6\u01a8\7\r\2\2\u01a7\u01a9"+
		"\7\16\2\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2"+
		"\u01aa\u01ae\7\60\2\2\u01ab\u01ac\t\2\2\2\u01ac\u01af\5 \21\2\u01ad\u01af"+
		"\5\u0088E\2\u01ae\u01ab\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2"+
		"\2\u01b0\u01b1\t\3\2\2\u01b1\u01b2\5\u0082B\2\u01b2\u01b3\7\61\2\2\u01b3"+
		"\u01b4\5\22\n\2\u01b4\u01b6\3\2\2\2\u01b5\u017a\3\2\2\2\u01b5\u0182\3"+
		"\2\2\2\u01b5\u0188\3\2\2\2\u01b5\u0197\3\2\2\2\u01b5\u01a6\3\2\2\2\u01b6"+
		"?\3\2\2\2\u01b7\u01b8\7\21\2\2\u01b8\u01ba\6!\7\2\u01b9\u01bb\5\u009e"+
		"P\2\u01ba\u01b9\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bbA\3\2\2\2\u01bc\u01bd"+
		"\7\22\2\2\u01bd\u01bf\6\"\b\2\u01be\u01c0\5\u009eP\2\u01bf\u01be\3\2\2"+
		"\2\u01bf\u01c0\3\2\2\2\u01c0C\3\2\2\2\u01c1\u01c2\7\23\2\2\u01c2\u01c4"+
		"\6#\t\2\u01c3\u01c5\5\u0082B\2\u01c4\u01c3\3\2\2\2\u01c4\u01c5\3\2\2\2"+
		"\u01c5\u01c7\3\2\2\2\u01c6\u01c8\5\u00a6T\2\u01c7\u01c6\3\2\2\2\u01c7"+
		"\u01c8\3\2\2\2\u01c8E\3\2\2\2\u01c9\u01ca\7\24\2\2\u01ca\u01cb\7\60\2"+
		"\2\u01cb\u01cc\5\u0082B\2\u01cc\u01cd\7\61\2\2\u01cd\u01ce\5\22\n\2\u01ce"+
		"G\3\2\2\2\u01cf\u01d0\7\25\2\2\u01d0\u01d1\7\60\2\2\u01d1\u01d2\5\u0082"+
		"B\2\u01d2\u01d3\7\61\2\2\u01d3\u01d4\5J&\2\u01d4I\3\2\2\2\u01d5\u01d7"+
		"\7\62\2\2\u01d6\u01d8\5L\'\2\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8"+
		"\u01dd\3\2\2\2\u01d9\u01db\5P)\2\u01da\u01dc\5L\'\2\u01db\u01da\3\2\2"+
		"\2\u01db\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01d9\3\2\2\2\u01dd\u01de"+
		"\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\7\63\2\2\u01e0K\3\2\2\2\u01e1"+
		"\u01e3\5N(\2\u01e2\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e2\3\2\2"+
		"\2\u01e4\u01e5\3\2\2\2\u01e5M\3\2\2\2\u01e6\u01e7\7\26\2\2\u01e7\u01e8"+
		"\5\u0082B\2\u01e8\u01ea\78\2\2\u01e9\u01eb\5\30\r\2\u01ea\u01e9\3\2\2"+
		"\2\u01ea\u01eb\3\2\2\2\u01ebO\3\2\2\2\u01ec\u01ed\7\27\2\2\u01ed\u01ef"+
		"\78\2\2\u01ee\u01f0\5\30\r\2\u01ef\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0"+
		"Q\3\2\2\2\u01f1\u01f2\5t;\2\u01f2\u01f5\78\2\2\u01f3\u01f6\5\22\n\2\u01f4"+
		"\u01f6\5\u0082B\2\u01f5\u01f3\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6S\3\2\2"+
		"\2\u01f7\u01f8\7\30\2\2\u01f8\u01f9\6+\n\2\u01f9\u01fa\5\u0082B\2\u01fa"+
		"U\3\2\2\2\u01fb\u01fc\7\31\2\2\u01fc\u0200\5\26\f\2\u01fd\u01ff\5X-\2"+
		"\u01fe\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201"+
		"\3\2\2\2\u0201\u0212\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\7\31\2\2"+
		"\u0204\u0205\5\26\f\2\u0205\u0206\5Z.\2\u0206\u0212\3\2\2\2\u0207\u0208"+
		"\7\31\2\2\u0208\u020c\5\26\f\2\u0209\u020b\5X-\2\u020a\u0209\3\2\2\2\u020b"+
		"\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020f\3\2"+
		"\2\2\u020e\u020c\3\2\2\2\u020f\u0210\5Z.\2\u0210\u0212\3\2\2\2\u0211\u01fb"+
		"\3\2\2\2\u0211\u0203\3\2\2\2\u0211\u0207\3\2\2\2\u0212W\3\2\2\2\u0213"+
		"\u0214\7\32\2\2\u0214\u0215\7\60\2\2\u0215\u0218\5 \21\2\u0216\u0217\7"+
		"\t\2\2\u0217\u0219\5\u0082B\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2"+
		"\u0219\u021a\3\2\2\2\u021a\u021b\7\61\2\2\u021b\u021c\5\26\f\2\u021cY"+
		"\3\2\2\2\u021d\u021e\7\33\2\2\u021e\u021f\5\26\f\2\u021f[\3\2\2\2\u0220"+
		"\u0221\7\34\2\2\u0221]\3\2\2\2\u0222\u0229\5(\25\2\u0223\u0229\5`\61\2"+
		"\u0224\u0225\5`\61\2\u0225\u0226\7\65\2\2\u0226\u0227\5(\25\2\u0227\u0229"+
		"\3\2\2\2\u0228\u0222\3\2\2\2\u0228\u0223\3\2\2\2\u0228\u0224\3\2\2\2\u0229"+
		"_\3\2\2\2\u022a\u022f\5b\62\2\u022b\u022c\7\65\2\2\u022c\u022e\5b\62\2"+
		"\u022d\u022b\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230"+
		"\3\2\2\2\u0230a\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0236\5\u009eP\2\u0233"+
		"\u0236\5f\64\2\u0234\u0236\5l\67\2\u0235\u0232\3\2\2\2\u0235\u0233\3\2"+
		"\2\2\u0235\u0234\3\2\2\2\u0236c\3\2\2\2\u0237\u0239\5\4\3\2\u0238\u0237"+
		"\3\2\2\2\u0238\u0239\3\2\2\2\u0239e\3\2\2\2\u023a\u023c\7.\2\2\u023b\u023d"+
		"\5j\66\2\u023c\u023b\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\3\2\2\2\u023e"+
		"\u024c\7/\2\2\u023f\u0240\7.\2\2\u0240\u0241\5h\65\2\u0241\u0242\7/\2"+
		"\2\u0242\u024c\3\2\2\2\u0243\u0244\7.\2\2\u0244\u0245\5h\65\2\u0245\u0247"+
		"\7\65\2\2\u0246\u0248\5j\66\2\u0247\u0246\3\2\2\2\u0247\u0248\3\2\2\2"+
		"\u0248\u0249\3\2\2\2\u0249\u024a\7/\2\2\u024a\u024c\3\2\2\2\u024b\u023a"+
		"\3\2\2\2\u024b\u023f\3\2\2\2\u024b\u0243\3\2\2\2\u024cg\3\2\2\2\u024d"+
		"\u024f\b\65\1\2\u024e\u0250\5j\66\2\u024f\u024e\3\2\2\2\u024f\u0250\3"+
		"\2\2\2\u0250\u0252\3\2\2\2\u0251\u0253\7\b\2\2\u0252\u0251\3\2\2\2\u0252"+
		"\u0253\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0255\5\u0084C\2\u0255\u0261"+
		"\3\2\2\2\u0256\u0257\f\3\2\2\u0257\u0259\7\65\2\2\u0258\u025a\5j\66\2"+
		"\u0259\u0258\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025c\3\2\2\2\u025b\u025d"+
		"\7\b\2\2\u025c\u025b\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e\3\2\2\2\u025e"+
		"\u0260\5\u0084C\2\u025f\u0256\3\2\2\2\u0260\u0263\3\2\2\2\u0261\u025f"+
		"\3\2\2\2\u0261\u0262\3\2\2\2\u0262i\3\2\2\2\u0263\u0261\3\2\2\2\u0264"+
		"\u0266\7\65\2\2\u0265\u0264\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0265\3"+
		"\2\2\2\u0267\u0268\3\2\2\2\u0268k\3\2\2\2\u0269\u026a\7\62\2\2\u026a\u0275"+
		"\7\63\2\2\u026b\u026c\7\62\2\2\u026c\u026d\5n8\2\u026d\u026e\7\63\2\2"+
		"\u026e\u0275\3\2\2\2\u026f\u0270\7\62\2\2\u0270\u0271\5n8\2\u0271\u0272"+
		"\7\65\2\2\u0272\u0273\7\63\2\2\u0273\u0275\3\2\2\2\u0274\u0269\3\2\2\2"+
		"\u0274\u026b\3\2\2\2\u0274\u026f\3\2\2\2\u0275m\3\2\2\2\u0276\u0277\b"+
		"8\1\2\u0277\u0278\5p9\2\u0278\u027e\3\2\2\2\u0279\u027a\f\3\2\2\u027a"+
		"\u027b\7\65\2\2\u027b\u027d\5p9\2\u027c\u0279\3\2\2\2\u027d\u0280\3\2"+
		"\2\2\u027e\u027c\3\2\2\2\u027e\u027f\3\2\2\2\u027fo\3\2\2\2\u0280\u027e"+
		"\3\2\2\2\u0281\u0283\5\"\22\2\u0282\u0284\5\64\33\2\u0283\u0282\3\2\2"+
		"\2\u0283\u0284\3\2\2\2\u0284\u028b\3\2\2\2\u0285\u0286\5t;\2\u0286\u0287"+
		"\78\2\2\u0287\u0288\5\u0084C\2\u0288\u028b\3\2\2\2\u0289\u028b\5r:\2\u028a"+
		"\u0281\3\2\2\2\u028a\u0285\3\2\2\2\u028a\u0289\3\2\2\2\u028bq\3\2\2\2"+
		"\u028c\u028d\6:\r\2\u028d\u028e\5t;\2\u028e\u0290\7\60\2\2\u028f\u0291"+
		"\5^\60\2\u0290\u028f\3\2\2\2\u0290\u0291\3\2\2\2\u0291\u0292\3\2\2\2\u0292"+
		"\u0293\7\61\2\2\u0293\u0294\7\62\2\2\u0294\u0295\5d\63\2\u0295\u0296\7"+
		"\63\2\2\u0296\u02a9\3\2\2\2\u0297\u0298\7\35\2\2\u0298\u0299\5t;\2\u0299"+
		"\u029a\7\60\2\2\u029a\u029b\7\61\2\2\u029b\u029c\7\62\2\2\u029c\u029d"+
		"\5d\63\2\u029d\u029e\7\63\2\2\u029e\u02a9\3\2\2\2\u029f\u02a0\7\36\2\2"+
		"\u02a0\u02a1\5t;\2\u02a1\u02a2\7\60\2\2\u02a2\u02a3\5\36\20\2\u02a3\u02a4"+
		"\7\61\2\2\u02a4\u02a5\7\62\2\2\u02a5\u02a6\5d\63\2\u02a6\u02a7\7\63\2"+
		"\2\u02a7\u02a9\3\2\2\2\u02a8\u028c\3\2\2\2\u02a8\u0297\3\2\2\2\u02a8\u029f"+
		"\3\2\2\2\u02a9s\3\2\2\2\u02aa\u02b2\5\u009eP\2\u02ab\u02b2\7\u0093\2\2"+
		"\u02ac\u02b2\5\u009cO\2\u02ad\u02ae\7.\2\2\u02ae\u02af\5\u0084C\2\u02af"+
		"\u02b0\7/\2\2\u02b0\u02b2\3\2\2\2\u02b1\u02aa\3\2\2\2\u02b1\u02ab\3\2"+
		"\2\2\u02b1\u02ac\3\2\2\2\u02b1\u02ad\3\2\2\2\u02b2u\3\2\2\2\u02b3\u02b4"+
		"\5\u009eP\2\u02b4w\3\2\2\2\u02b5\u02b7\7\60\2\2\u02b6\u02b8\5z>\2\u02b7"+
		"\u02b6\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02ba\7\61"+
		"\2\2\u02bay\3\2\2\2\u02bb\u02bd\b>\1\2\u02bc\u02be\7\b\2\2\u02bd\u02bc"+
		"\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02bf\3\2\2\2\u02bf\u02c0\5\u0084C"+
		"\2\u02c0\u02c9\3\2\2\2\u02c1\u02c2\f\3\2\2\u02c2\u02c4\7\65\2\2\u02c3"+
		"\u02c5\7\b\2\2\u02c4\u02c3\3\2\2\2\u02c4\u02c5\3\2\2\2\u02c5\u02c6\3\2"+
		"\2\2\u02c6\u02c8\5\u0084C\2\u02c7\u02c1\3\2\2\2\u02c8\u02cb\3\2\2\2\u02c9"+
		"\u02c7\3\2\2\2\u02c9\u02ca\3\2\2\2\u02ca{\3\2\2\2\u02cb\u02c9\3\2\2\2"+
		"\u02cc\u02cd\5~@\2\u02cd\u02ce\6?\17\2\u02ce\u02cf\7\37\2\2\u02cf\u02d0"+
		"\5\u0080A\2\u02d0}\3\2\2\2\u02d1\u02db\5\"\22\2\u02d2\u02d4\7\60\2\2\u02d3"+
		"\u02d5\5\u0082B\2\u02d4\u02d3\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5\u02d7"+
		"\3\2\2\2\u02d6\u02d8\5(\25\2\u02d7\u02d6\3\2\2\2\u02d7\u02d8\3\2\2\2\u02d8"+
		"\u02d9\3\2\2\2\u02d9\u02db\7\61\2\2\u02da\u02d1\3\2\2\2\u02da\u02d2\3"+
		"\2\2\2\u02db\177\3\2\2\2\u02dc\u02dd\6A\20\2\u02dd\u02e3\5\u0084C\2\u02de"+
		"\u02df\7\62\2\2\u02df\u02e0\5d\63\2\u02e0\u02e1\7\63\2\2\u02e1\u02e3\3"+
		"\2\2\2\u02e2\u02dc\3\2\2\2\u02e2\u02de\3\2\2\2\u02e3\u0081\3\2\2\2\u02e4"+
		"\u02e5\bB\1\2\u02e5\u02e6\5\u0084C\2\u02e6\u02ec\3\2\2\2\u02e7\u02e8\f"+
		"\3\2\2\u02e8\u02e9\7\65\2\2\u02e9\u02eb\5\u0084C\2\u02ea\u02e7\3\2\2\2"+
		"\u02eb\u02ee\3\2\2\2\u02ec\u02ea\3\2\2\2\u02ec\u02ed\3\2\2\2\u02ed\u0083"+
		"\3\2\2\2\u02ee\u02ec\3\2\2\2\u02ef\u02f0\bC\1\2\u02f0\u02f1\5\u0086D\2"+
		"\u02f1\u02f2\5\u0098M\2\u02f2\u02f3\5\u0084C\6\u02f3\u02fe\3\2\2\2\u02f4"+
		"\u02fe\5\u0086D\2\u02f5\u02fe\5\24\13\2\u02f6\u02f7\5\u0086D\2\u02f7\u02f8"+
		"\7\66\2\2\u02f8\u02fa\5\u0084C\2\u02f9\u02fb\5\u00a6T\2\u02fa\u02f9\3"+
		"\2\2\2\u02fa\u02fb\3\2\2\2\u02fb\u02fe\3\2\2\2\u02fc\u02fe\5|?\2\u02fd"+
		"\u02ef\3\2\2\2\u02fd\u02f4\3\2\2\2\u02fd\u02f5\3\2\2\2\u02fd\u02f6\3\2"+
		"\2\2\u02fd\u02fc\3\2\2\2\u02fe\u0316\3\2\2\2\u02ff\u0300\f\4\2\2\u0300"+
		"\u0302\7\r\2\2\u0301\u0303\7\16\2\2\u0302\u0301\3\2\2\2\u0302\u0303\3"+
		"\2\2\2\u0303\u0304\3\2\2\2\u0304\u0308\7\60\2\2\u0305\u0306\t\2\2\2\u0306"+
		"\u0309\5 \21\2\u0307\u0309\5\u0086D\2\u0308\u0305\3\2\2\2\u0308\u0307"+
		"\3\2\2\2\u0309\u030a\3\2\2\2\u030a\u030b\t\3\2\2\u030b\u030c\5\u0082B"+
		"\2\u030c\u030d\7\61\2\2\u030d\u0315\3\2\2\2\u030e\u030f\f\3\2\2\u030f"+
		"\u0310\7\t\2\2\u0310\u0311\7\60\2\2\u0311\u0312\5\u0082B\2\u0312\u0313"+
		"\7\61\2\2\u0313\u0315\3\2\2\2\u0314\u02ff\3\2\2\2\u0314\u030e\3\2\2\2"+
		"\u0315\u0318\3\2\2\2\u0316\u0314\3\2\2\2\u0316\u0317\3\2\2\2\u0317\u0085"+
		"\3\2\2\2\u0318\u0316\3\2\2\2\u0319\u031a\bD\1\2\u031a\u031b\7!\2\2\u031b"+
		"\u032e\5\u0086D\16\u031c\u031d\7\"\2\2\u031d\u032e\5\u0086D\r\u031e\u031f"+
		"\7#\2\2\u031f\u032e\5\u0086D\f\u0320\u0321\7:\2\2\u0321\u032e\5\u0086"+
		"D\13\u0322\u0323\7;\2\2\u0323\u032e\5\u0086D\n\u0324\u0325\7<\2\2\u0325"+
		"\u032e\5\u0086D\t\u0326\u0327\7=\2\2\u0327\u032e\5\u0086D\b\u0328\u0329"+
		"\7>\2\2\u0329\u032e\5\u0086D\7\u032a\u032b\7?\2\2\u032b\u032e\5\u0086"+
		"D\6\u032c\u032e\5\u0088E\2\u032d\u0319\3\2\2\2\u032d\u031c\3\2\2\2\u032d"+
		"\u031e\3\2\2\2\u032d\u0320\3\2\2\2\u032d\u0322\3\2\2\2\u032d\u0324\3\2"+
		"\2\2\u032d\u0326\3\2\2\2\u032d\u0328\3\2\2\2\u032d\u032a\3\2\2\2\u032d"+
		"\u032c\3\2\2\2\u032e\u0382\3\2\2\2\u032f\u0330\f%\2\2\u0330\u0331\7R\2"+
		"\2\u0331\u0381\5\u0086D&\u0332\u0333\f$\2\2\u0333\u0334\7Q\2\2\u0334\u0381"+
		"\5\u0086D%\u0335\u0336\f#\2\2\u0336\u0337\7P\2\2\u0337\u0381\5\u0086D"+
		"$\u0338\u0339\f\"\2\2\u0339\u033a\7O\2\2\u033a\u0381\5\u0086D#\u033b\u033c"+
		"\f!\2\2\u033c\u033d\7N\2\2\u033d\u0381\5\u0086D\"\u033e\u033f\f \2\2\u033f"+
		"\u0340\7J\2\2\u0340\u0381\5\u0086D!\u0341\u0342\f\37\2\2\u0342\u0343\7"+
		"K\2\2\u0343\u0381\5\u0086D \u0344\u0345\f\36\2\2\u0345\u0346\7L\2\2\u0346"+
		"\u0381\5\u0086D\37\u0347\u0348\f\35\2\2\u0348\u0349\7M\2\2\u0349\u0381"+
		"\5\u0086D\36\u034a\u034b\f\34\2\2\u034b\u034c\7F\2\2\u034c\u0381\5\u0086"+
		"D\35\u034d\u034e\f\33\2\2\u034e\u034f\7G\2\2\u034f\u0381\5\u0086D\34\u0350"+
		"\u0351\f\32\2\2\u0351\u0352\7H\2\2\u0352\u0381\5\u0086D\33\u0353\u0354"+
		"\f\31\2\2\u0354\u0355\7I\2\2\u0355\u0381\5\u0086D\32\u0356\u0357\f\30"+
		"\2\2\u0357\u0358\7 \2\2\u0358\u0381\5\u0086D\31\u0359\u035a\f\27\2\2\u035a"+
		"\u035b\7\17\2\2\u035b\u0381\5\u0086D\30\u035c\u035d\f\26\2\2\u035d\u035e"+
		"\7D\2\2\u035e\u0381\5\u0086D\27\u035f\u0360\f\25\2\2\u0360\u0361\7C\2"+
		"\2\u0361\u0381\5\u0086D\26\u0362\u0363\f\24\2\2\u0363\u0364\7E\2\2\u0364"+
		"\u0381\5\u0086D\25\u0365\u0366\f\23\2\2\u0366\u0367\7<\2\2\u0367\u0381"+
		"\5\u0086D\24\u0368\u0369\f\22\2\2\u0369\u036a\7=\2\2\u036a\u0381\5\u0086"+
		"D\23\u036b\u036c\f\21\2\2\u036c\u036d\7@\2\2\u036d\u0381\5\u0086D\22\u036e"+
		"\u036f\f\20\2\2\u036f\u0370\7A\2\2\u0370\u0381\5\u0086D\21\u0371\u0372"+
		"\f\17\2\2\u0372\u0373\7B\2\2\u0373\u0381\5\u0086D\20\u0374\u0375\f&\2"+
		"\2\u0375\u0376\7\67\2\2\u0376\u0377\5\u0084C\2\u0377\u0378\78\2\2\u0378"+
		"\u0379\5\u0084C\2\u0379\u0381\3\2\2\2\u037a\u037b\f\5\2\2\u037b\u037c"+
		"\6D-\2\u037c\u0381\7:\2\2\u037d\u037e\f\4\2\2\u037e\u037f\6D/\2\u037f"+
		"\u0381\7;\2\2\u0380\u032f\3\2\2\2\u0380\u0332\3\2\2\2\u0380\u0335\3\2"+
		"\2\2\u0380\u0338\3\2\2\2\u0380\u033b\3\2\2\2\u0380\u033e\3\2\2\2\u0380"+
		"\u0341\3\2\2\2\u0380\u0344\3\2\2\2\u0380\u0347\3\2\2\2\u0380\u034a\3\2"+
		"\2\2\u0380\u034d\3\2\2\2\u0380\u0350\3\2\2\2\u0380\u0353\3\2\2\2\u0380"+
		"\u0356\3\2\2\2\u0380\u0359\3\2\2\2\u0380\u035c\3\2\2\2\u0380\u035f\3\2"+
		"\2\2\u0380\u0362\3\2\2\2\u0380\u0365\3\2\2\2\u0380\u0368\3\2\2\2\u0380"+
		"\u036b\3\2\2\2\u0380\u036e\3\2\2\2\u0380\u0371\3\2\2\2\u0380\u0374\3\2"+
		"\2\2\u0380\u037a\3\2\2\2\u0380\u037d\3\2\2\2\u0381\u0384\3\2\2\2\u0382"+
		"\u0380\3\2\2\2\u0382\u0383\3\2\2\2\u0383\u0087\3\2\2\2\u0384\u0382\3\2"+
		"\2\2\u0385\u0388\5\u008aF\2\u0386\u0388\5\u008eH\2\u0387\u0385\3\2\2\2"+
		"\u0387\u0386\3\2\2\2\u0388\u0089\3\2\2\2\u0389\u038a\bF\1\2\u038a\u038b"+
		"\5\u0090I\2\u038b\u038d\5x=\2\u038c\u038e\5\u00a6T\2\u038d\u038c\3\2\2"+
		"\2\u038d\u038e\3\2\2\2\u038e\u0394\3\2\2\2\u038f\u0391\5\u008cG\2\u0390"+
		"\u0392\5\u00a6T\2\u0391\u0390\3\2\2\2\u0391\u0392\3\2\2\2\u0392\u0394"+
		"\3\2\2\2\u0393\u0389\3\2\2\2\u0393\u038f\3\2\2\2\u0394\u03a9\3\2\2\2\u0395"+
		"\u0396\f\5\2\2\u0396\u0398\5x=\2\u0397\u0399\5\u00a6T\2\u0398\u0397\3"+
		"\2\2\2\u0398\u0399\3\2\2\2\u0399\u03a8\3\2\2\2\u039a\u039b\f\4\2\2\u039b"+
		"\u039c\7.\2\2\u039c\u039d\5\u0082B\2\u039d\u039f\7/\2\2\u039e\u03a0\5"+
		"\u00a6T\2\u039f\u039e\3\2\2\2\u039f\u03a0\3\2\2\2\u03a0\u03a8\3\2\2\2"+
		"\u03a1\u03a2\f\3\2\2\u03a2\u03a3\79\2\2\u03a3\u03a5\5\u009eP\2\u03a4\u03a6"+
		"\5\u00a6T\2\u03a5\u03a4\3\2\2\2\u03a5\u03a6\3\2\2\2\u03a6\u03a8\3\2\2"+
		"\2\u03a7\u0395\3\2\2\2\u03a7\u039a\3\2\2\2\u03a7\u03a1\3\2\2\2\u03a8\u03ab"+
		"\3\2\2\2\u03a9\u03a7\3\2\2\2\u03a9\u03aa\3\2\2\2\u03aa\u008b\3\2\2\2\u03ab"+
		"\u03a9\3\2\2\2\u03ac\u03ad\7\u0085\2\2\u03ad\u03ae\5x=\2\u03ae\u008d\3"+
		"\2\2\2\u03af\u03b3\5\u0090I\2\u03b0\u03b1\7$\2\2\u03b1\u03b3\5\u008eH"+
		"\2\u03b2\u03af\3\2\2\2\u03b2\u03b0\3\2\2\2\u03b3\u008f\3\2\2\2\u03b4\u03b5"+
		"\bI\1\2\u03b5\u03bc\5\u0096L\2\u03b6\u03bc\5\u0092J\2\u03b7\u03b8\7$\2"+
		"\2\u03b8\u03b9\5\u0090I\2\u03b9\u03ba\5x=\2\u03ba\u03bc\3\2\2\2\u03bb"+
		"\u03b4\3\2\2\2\u03bb\u03b6\3\2\2\2\u03bb\u03b7\3\2\2\2\u03bc\u03c7\3\2"+
		"\2\2\u03bd\u03be\f\6\2\2\u03be\u03bf\7.\2\2\u03bf\u03c0\5\u0082B\2\u03c0"+
		"\u03c1\7/\2\2\u03c1\u03c6\3\2\2\2\u03c2\u03c3\f\5\2\2\u03c3\u03c4\79\2"+
		"\2\u03c4\u03c6\5\u009eP\2\u03c5\u03bd\3\2\2\2\u03c5\u03c2\3\2\2\2\u03c6"+
		"\u03c9\3\2\2\2\u03c7\u03c5\3\2\2\2\u03c7\u03c8\3\2\2\2\u03c8\u0091\3\2"+
		"\2\2\u03c9\u03c7\3\2\2\2\u03ca\u03cb\7\u0085\2\2\u03cb\u03cc\7.\2\2\u03cc"+
		"\u03cd\5\u0082B\2\u03cd\u03ce\7/\2\2\u03ce\u03d3\3\2\2\2\u03cf\u03d0\7"+
		"\u0085\2\2\u03d0\u03d1\79\2\2\u03d1\u03d3\5\u009eP\2\u03d2\u03ca\3\2\2"+
		"\2\u03d2\u03cf\3\2\2\2\u03d3\u0093\3\2\2\2\u03d4\u03d6\7\3\2\2\u03d5\u03d7"+
		"\7@\2\2\u03d6\u03d5\3\2\2\2\u03d6\u03d7\3\2\2\2\u03d7\u03d9\3\2\2\2\u03d8"+
		"\u03da\5\u009eP\2\u03d9\u03d8\3\2\2\2\u03d9\u03da\3\2\2\2\u03da\u03db"+
		"\3\2\2\2\u03db\u03dd\7\60\2\2\u03dc\u03de\5^\60\2\u03dd\u03dc\3\2\2\2"+
		"\u03dd\u03de\3\2\2\2\u03de\u03df\3\2\2\2\u03df\u03e5\7\61\2\2\u03e0\u03e1"+
		"\7\62\2\2\u03e1\u03e2\5d\63\2\u03e2\u03e3\7\63\2\2\u03e3\u03e6\3\2\2\2"+
		"\u03e4\u03e6\5\22\n\2\u03e5\u03e0\3\2\2\2\u03e5\u03e4\3\2\2\2\u03e6\u0095"+
		"\3\2\2\2\u03e7\u03f3\7%\2\2\u03e8\u03f3\5\u009eP\2\u03e9\u03f3\5\u0094"+
		"K\2\u03ea\u03f3\5\b\5\2\u03eb\u03f3\5\u009aN\2\u03ec\u03f3\5l\67\2\u03ed"+
		"\u03ee\7\60\2\2\u03ee\u03ef\5\u0082B\2\u03ef\u03f0\7\61\2\2\u03f0\u03f3"+
		"\3\2\2\2\u03f1\u03f3\5f\64\2\u03f2\u03e7\3\2\2\2\u03f2\u03e8\3\2\2\2\u03f2"+
		"\u03e9\3\2\2\2\u03f2\u03ea\3\2\2\2\u03f2\u03eb\3\2\2\2\u03f2\u03ec\3\2"+
		"\2\2\u03f2\u03ed\3\2\2\2\u03f2\u03f1\3\2\2\2\u03f3\u0097\3\2\2\2\u03f4"+
		"\u03f5\t\4\2\2\u03f5\u0099\3\2\2\2\u03f6\u03f9\t\5\2\2\u03f7\u03f9\5\u009c"+
		"O\2\u03f8\u03f6\3\2\2\2\u03f8\u03f7\3\2\2\2\u03f9\u009b\3\2\2\2\u03fa"+
		"\u03fb\t\6\2\2\u03fb\u009d\3\2\2\2\u03fc\u03ff\7\u0092\2\2\u03fd\u03ff"+
		"\5\u00a0Q\2\u03fe\u03fc\3\2\2\2\u03fe\u03fd\3\2\2\2\u03ff\u009f\3\2\2"+
		"\2\u0400\u0404\5\u00a2R\2\u0401\u0404\5\u00a4S\2\u0402\u0404\t\7\2\2\u0403"+
		"\u0400\3\2\2\2\u0403\u0401\3\2\2\2\u0403\u0402\3\2\2\2\u0404\u00a1\3\2"+
		"\2\2\u0405\u0406\t\b\2\2\u0406\u00a3\3\2\2\2\u0407\u0408\t\t\2\2\u0408"+
		"\u00a5\3\2\2\2\u0409\u040e\7\64\2\2\u040a\u040e\7\2\2\3\u040b\u040e\6"+
		"T\65\2\u040c\u040e\6T\66\2\u040d\u0409\3\2\2\2\u040d\u040a\3\2\2\2\u040d"+
		"\u040b\3\2\2\2\u040d\u040c\3\2\2\2\u040e\u00a7\3\2\2\2\u040f\u0410\7\2"+
		"\2\3\u0410\u00a9\3\2\2\2r\u00ad\u00b5\u00bb\u00c4\u00d3\u00d6\u00eb\u00ef"+
		"\u00f2\u00f6\u0101\u0107\u0111\u0116\u011a\u011e\u0123\u0127\u0134\u0139"+
		"\u013f\u0144\u0148\u014e\u015a\u0162\u016d\u0175\u018b\u018f\u0193\u019d"+
		"\u01a1\u01a8\u01ae\u01b5\u01ba\u01bf\u01c4\u01c7\u01d7\u01db\u01dd\u01e4"+
		"\u01ea\u01ef\u01f5\u0200\u020c\u0211\u0218\u0228\u022f\u0235\u0238\u023c"+
		"\u0247\u024b\u024f\u0252\u0259\u025c\u0261\u0267\u0274\u027e\u0283\u028a"+
		"\u0290\u02a8\u02b1\u02b7\u02bd\u02c4\u02c9\u02d4\u02d7\u02da\u02e2\u02ec"+
		"\u02fa\u02fd\u0302\u0308\u0314\u0316\u032d\u0380\u0382\u0387\u038d\u0391"+
		"\u0393\u0398\u039f\u03a5\u03a7\u03a9\u03b2\u03bb\u03c5\u03c7\u03d2\u03d6"+
		"\u03d9\u03dd\u03e5\u03f2\u03f8\u03fe\u0403\u040d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}