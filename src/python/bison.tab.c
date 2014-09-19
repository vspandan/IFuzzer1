/* A Bison parser, made by GNU Bison 3.0.2.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2013 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */

#line 67 "bison.tab.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 1
#endif

/* In a future release of Bison, this section will be replaced
   by #include "bison.tab.h".  */
#ifndef YY_YY_BISON_TAB_H_INCLUDED
# define YY_YY_BISON_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    INT_LITERAL = 258,
    STRING_LITERAL = 259,
    null = 260,
    true = 261,
    false = 262,
    Class = 263,
    Enum = 264,
    Extends = 265,
    Super = 266,
    Const = 267,
    Export = 268,
    Import = 269,
    Implements = 270,
    Let = 271,
    Private = 272,
    Public = 273,
    Interface = 274,
    Package = 275,
    Protected = 276,
    Static = 277,
    Yield = 278,
    SemiColon = 279,
    break = 280,
    do = 281,
    instanceof = 282,
    typeof = 283,
    case = 284,
    else = 285,
    new = 286,
    var = 287,
    catch = 288,
    finally = 289,
    return = 290,
    void = 291,
    continue = 292,
    for = 293,
    switch = 294,
    while = 295,
    debugger = 296,
    function = 297,
    this = 298,
    with = 299,
    default = 300,
    if = 301,
    throw = 302,
    delete = 303,
    in = 304,
    try = 305,
    ID = 306,
    ASSIGN_OP = 307,
    E_ASSIGN_OP = 308,
    CHAR_LITERAL = 309,
    EQ_OP = 310,
    COND_OP = 311,
    REL_OP = 312,
    ARITH_OP = 313
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE YYSTYPE;
union YYSTYPE
{
#line 3 "../../output/bison.y" /* yacc.c:355  */

 int a;
float b;
char *c;

#line 172 "bison.tab.c" /* yacc.c:355  */
};
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_BISON_TAB_H_INCLUDED  */

/* Copy the second part of user declarations.  */
#line 8 "../../output/bison.y" /* yacc.c:358  */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#line 13 "../../output/bison.y" /* yacc.c:358  */

char *s;

#line 195 "bison.tab.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  162
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   1631

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  104
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  84
/* YYNRULES -- Number of rules.  */
#define YYNRULES  253
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  445

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   335

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    75,     2,     2,     2,    78,    90,     2,
      64,    65,    76,    72,    61,    73,    69,    77,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    66,    63,
      82,    62,    83,    93,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,    67,     2,    68,    91,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    59,     2,    60,    74,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    70,    71,    79,    80,    81,    84,
      85,    86,    87,    88,    89,    92,    94,    95,    96,    97,
      98,    99,   100,   101,   102,   103
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    18,    18,    20,    23,    24,    28,    29,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    51,    55,    56,    58,    61,    65,    66,
      70,    71,    73,    76,    80,    84,    88,    89,    93,    94,
      95,    96,    97,    98,    99,   100,   101,   102,   103,   104,
     105,   106,   107,   108,   112,   113,   117,   118,   122,   123,
     127,   131,   135,   136,   137,   138,   139,   140,   144,   145,
     149,   150,   154,   155,   159,   163,   167,   168,   169,   173,
     177,   181,   185,   186,   190,   191,   195,   197,   200,   201,
     202,   206,   207,   216,   220,   221,   223,   226,   227,   228,
     229,   234,   242,   243,   244,   248,   249,   250,   254,   258,
     259,   264,   273,   277,   278,   279,   280,   281,   282,   283,
     284,   285,   286,   287,   288,   289,   290,   291,   292,   293,
     294,   295,   296,   297,   298,   299,   300,   301,   302,   303,
     304,   305,   306,   307,   308,   309,   310,   311,   312,   313,
     314,   315,   316,   317,   318,   319,   320,   321,   325,   326,
     327,   328,   329,   330,   331,   332,   333,   334,   338,   339,
     343,   344,   345,   346,   347,   348,   349,   350,   351,   352,
     353,   354,   355,   356,   357,   358,   359,   360,   361,   362,
     363,   364,   365,   366,   367,   368,   372,   373,   374,   375,
     379,   380,   381,   382,   386,   390,   394,   398,   399,   403,
     404,   405,   406,   407,   408,   409,   410,   411,   412,   413,
     414,   415,   416,   417,   418,   422,   424,   427,   431,   435,
     439,   443,   447,   451,   455,   459,   463,   467,   471,   475,
     479,   483,   487,   491,   495,   499,   503,   507,   511,   515,
     519,   523,   527,   531
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 1
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "INT_LITERAL", "STRING_LITERAL", "null",
  "true", "false", "Class", "Enum", "Extends", "Super", "Const", "Export",
  "Import", "Implements", "Let", "Private", "Public", "Interface",
  "Package", "Protected", "Static", "Yield", "SemiColon", "break", "do",
  "instanceof", "typeof", "case", "else", "new", "var", "catch", "finally",
  "return", "void", "continue", "for", "switch", "while", "debugger",
  "function", "this", "with", "default", "if", "throw", "delete", "in",
  "try", "ID", "ASSIGN_OP", "E_ASSIGN_OP", "CHAR_LITERAL", "EQ_OP",
  "COND_OP", "REL_OP", "ARITH_OP", "'{'", "'}'", "','", "'='", "';'",
  "'('", "')'", "':'", "'['", "']'", "'.'", "\"++\"", "\"--\"", "'+'",
  "'-'", "'~'", "'!'", "'*'", "'/'", "'%'", "\"<<\"", "\">>\"", "\">>>\"",
  "'<'", "'>'", "\"<=\"", "\">=\"", "\"==\"", "\"!=\"", "\"===\"",
  "\"!==\"", "'&'", "'^'", "\"&&\"", "'?'", "\"*=\"", "\"/=\"", "\"%=\"",
  "\"+=\"", "\"-=\"", "\"<<=\"", "\">>=\"", "\">>>=\"", "\"&=\"", "\"^=\"",
  "$accept", "program", "sourceElements", "sourceElement", "statement",
  "block", "statementList", "variableStatement", "variableDeclarationList",
  "variableDeclaration", "initialiser", "emptyStatement",
  "expressionStatement", "ifStatement", "iterationStatement",
  "continueStatement", "breakStatement", "returnStatement",
  "withStatement", "switchStatement", "caseBlock", "caseClauses",
  "caseClause", "defaultClause", "labelledStatement", "throwStatement",
  "tryStatement", "catchProduction", "finallyProduction",
  "debuggerStatement", "functionDeclaration", "formalParameterList",
  "functionBody", "arrayLiteral", "elementList", "elisionExpr", "elision",
  "objectLiteral", "propertyNameAndValueList", "propertyAssignment",
  "propertyName", "propertySetParameterList", "arguments", "argumentList",
  "expressionSequence", "singleExpression", "assignmentOperator",
  "identifierName", "keyword", "reservedWord", "literal", "numericLiteral",
  "StringLiteral", "NullLiteral", "BooleanLiteral", "futureReservedWord",
  "eos", "Break", "Do", "Instanceof", "Typeof", "Case", "Else", "New",
  "Var", "Catch", "Finally", "Return", "Void", "Continue", "For", "Switch",
  "While", "Debugger", "Function", "This", "With", "Default", "If",
  "Throw", "Delete", "In", "Try", "Identifier", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   123,
     125,    44,    61,    59,    40,    41,    58,    91,    93,    46,
     314,   315,    43,    45,   126,    33,    42,    47,    37,   316,
     317,   318,    60,    62,   319,   320,   321,   322,   323,   324,
      38,    94,   325,    63,   326,   327,   328,   329,   330,   331,
     332,   333,   334,   335
};
# endif

#define YYPACT_NINF -342

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-342)))

#define YYTABLE_NINF -200

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
     656,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,   583,  -342,    28,   113,
     113,   113,   113,  1450,  1450,    16,  -342,   656,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,   458,   366,
    -342,  -342,  -342,  -342,     8,   707,  1450,  1450,    -2,   838,
    1450,     8,   -31,     9,    23,    48,    -2,  -342,    38,    57,
    1450,  1450,    69,    60,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,    73,   707,
      83,    53,  -342,    87,  -342,  -342,  -342,    88,   103,   104,
     107,  -342,   -12,   707,  -342,  1450,  -342,  -342,  1450,   -32,
    -342,  -342,   780,  1450,     4,   -31,     9,    23,   -10,  -342,
     108,    38,  -342,    57,  1450,  1450,  -342,    69,    61,  -342,
    -342,    42,    43,   911,  -342,  -342,  -342,  -342,  1523,   458,
    -342,   458,  -342,  -342,  1450,   960,  1450,  1580,  -342,  -342,
    1450,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  1450,  1450,  1450,   113,   113,   113,   113,   113,
     113,   113,   113,   113,   113,   113,   113,   113,   113,   113,
     113,   113,   113,   113,  -342,  -342,    48,    92,   458,   458,
      48,   114,   133,    48,  -342,   458,  -342,    48,   829,  1450,
    1450,  -342,   112,  1450,  1450,    48,   458,   707,    97,   707,
    -342,  -342,  -342,  -342,   156,  1450,   -27,   159,  -342,  -342,
    -342,   458,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,   164,  -342,  -342,   170,   458,   173,
    -342,  -342,   191,  -342,   458,   458,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -342,  -342,  -342,  -342,  -342,   174,  -342,  -342,    -2,
    1450,  -342,  -342,  -342,  1009,   179,   458,    -2,   178,   180,
      30,   182,   183,  -342,   210,  -342,   185,    69,  -342,  -342,
     458,   192,   187,  -342,    44,  -342,  -342,  1450,  1450,  -342,
     458,  1058,   193,  1107,  1450,   196,    39,   195,   707,   204,
     199,   189,   707,   707,  -342,    -2,  -342,   656,   206,  -342,
     458,   201,   707,   202,  1156,  1205,   205,   207,   441,  1254,
    1450,    34,  -342,  -342,   656,   212,    -2,  -342,   239,   209,
    -342,   217,   656,    48,  -342,   707,   707,   213,   707,   214,
    1303,   707,  1352,   218,   215,  -342,    15,   253,     1,  1450,
     229,   238,   656,  -342,   707,    69,  -342,   240,  -342,  -342,
    -342,   707,  -342,   707,   707,   241,  -342,   707,   243,  1401,
     707,  -342,     2,  -342,  -342,   244,   237,   707,  -342,   245,
    -342,  -342,  -342,  -342,  -342,  -342,   707,  -342,   707,   707,
     246,  -342,  -342,   252,  -342,   707,  -342,  -342,  -342,  -342,
    -342,   707,  -342,  -342,  -342
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       3,   204,   205,   206,   207,   208,   227,   228,   230,   233,
     234,   237,   238,   239,   240,   241,   242,   243,   244,   245,
     246,   248,   249,   250,   252,   253,     0,    34,    96,     0,
       0,     0,     0,     0,     0,     0,     2,     4,     6,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    17,    19,
      18,    20,    21,    22,     7,   156,   157,    35,   112,   155,
     202,   203,   200,   201,   226,     0,     0,     0,    32,   226,
       0,   226,     0,     0,     0,   226,     0,   153,     0,     0,
       0,     0,     0,   154,   209,   210,   211,   212,   213,   214,
     215,   216,   217,   218,   219,   220,   221,   222,   223,   224,
     229,   231,   232,   235,   236,   247,   251,   100,     0,    24,
       0,     0,   101,     0,   105,   196,   169,   202,   203,   200,
     201,   197,   226,   171,   172,   173,   174,   175,   176,    32,
     178,   179,   226,   181,   226,   183,   184,   185,   226,   187,
     153,   189,   190,   191,   192,   193,   194,   195,   154,    94,
      88,     0,    96,     0,   123,   124,   125,   126,     0,   127,
     154,   128,     1,     5,     0,     0,     0,     0,   118,   119,
       0,   158,   159,   160,   161,   162,   163,   164,   165,   166,
     167,   115,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   225,    57,   226,     0,   122,   117,
     226,    29,    30,   226,    59,   121,    55,   226,     0,     0,
       0,    81,     0,     0,     0,   226,   120,    26,     0,     0,
      99,    25,    23,    98,     0,     0,     0,    96,    89,    91,
      95,    93,   107,   106,   198,   199,   170,   171,   173,   176,
     177,   180,   181,   182,   183,   184,   185,   186,   188,   189,
     191,   192,   193,   195,   168,   151,   110,     0,   111,     0,
     114,   168,     0,   152,   141,   142,   132,   133,   129,   130,
     131,   134,   135,   136,   137,   138,   139,   140,   143,   144,
     145,   146,   147,   148,   149,    56,     0,   115,    27,    32,
       0,    31,    58,    54,     0,     0,   112,    32,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,    74,    97,
     102,     0,     0,   108,     0,   109,   113,     0,     0,    28,
      33,     0,     0,     0,     0,     0,    29,     0,     0,     0,
       0,    85,     0,     0,    78,     0,    80,    87,     0,    90,
     150,     0,     0,     0,     0,     0,     0,     0,   112,     0,
       0,     0,    61,    39,    87,     0,     0,    60,    37,     0,
      86,     0,    87,   226,    47,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    67,     0,    68,     0,     0,
       0,     0,    87,    84,     0,     0,   103,     0,    38,    43,
      46,     0,    45,     0,     0,     0,    52,     0,     0,     0,
       0,    64,     0,    69,    66,     0,     0,    26,    83,     0,
      36,    79,   104,    41,    42,    44,     0,    51,     0,     0,
       0,    53,    63,     0,    65,    26,    72,    82,    40,    50,
      49,     0,    62,    70,    48
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -342,  -342,    29,  -342,    -8,   -80,  -108,  -342,  -272,     7,
    -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,  -342,
    -342,  -305,  -342,   -70,  -342,  -342,  -342,  -342,     3,  -342,
    -342,   -48,  -295,  -342,   168,  -342,    84,  -342,  -342,  -342,
    -342,  -342,   116,  -342,   -58,   349,  -342,   161,  -342,  -342,
      12,    -1,    32,   -20,   -19,  -342,   -54,   -18,   -17,   -16,
      -3,    10,   -45,    14,   -22,    98,  -215,    20,    21,    22,
      24,    25,   -21,    26,    27,    59,    64,  -341,    65,    66,
      67,   -23,    72,     0
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,    35,   370,    37,    38,    39,   110,    40,   210,   211,
     301,    41,    42,    43,    44,    45,    46,    47,    48,    49,
     362,   386,   387,   388,    50,    51,    52,   314,   315,    53,
      54,   340,   371,    55,   151,   152,   153,    56,   111,   112,
     113,   322,   181,   267,    57,    58,   182,   114,   115,   116,
      59,    60,    61,    62,    63,   121,   205,    64,    65,   183,
      66,   389,   127,    67,    68,   130,   131,    69,    70,    71,
      72,    73,    74,    75,    76,    77,    78,   142,    79,    80,
      81,   184,    82,   160
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      83,   231,   228,   146,   129,   137,   119,   120,   122,   123,
     124,   213,   204,   317,   204,   214,   162,   216,   109,    25,
     390,   221,   225,   125,    25,   117,   148,   329,   204,    36,
     101,   101,   204,   218,  -177,   335,   126,    83,   321,    25,
     128,   154,   155,   156,   157,   390,   132,   133,   134,    25,
     135,   136,   138,   139,  -170,    25,  -186,   207,   118,    25,
     105,   414,   432,   101,   206,    83,   163,   228,   212,   391,
    -182,   217,   204,   219,   213,   411,   222,   397,   214,   105,
     216,    25,   413,   415,   221,   140,   225,   220,   106,   149,
     141,   143,   144,   145,   385,   339,   150,   419,   147,   317,
     299,   109,   223,   237,   149,   240,   265,   433,   269,    83,
     238,   -92,   349,   233,   234,   207,     1,     2,     3,     4,
       5,   224,   206,    83,   273,   236,   229,   229,   227,   212,
     103,   104,    16,   230,   217,   146,   250,   256,   244,   245,
     246,   247,   124,   232,   146,   250,   256,   244,   245,   246,
     247,   124,   295,   235,  -107,   248,   298,   242,   264,   302,
     305,   308,   309,   303,   248,   311,   312,   271,   126,  -106,
    -198,   313,   249,  -199,  -188,   299,   310,   126,   251,   252,
     253,   249,   254,   255,   257,   139,   296,   251,   252,   253,
     243,   254,   255,   257,   139,   300,   307,   276,   277,   278,
     279,   280,   281,   282,   283,   284,   285,   286,   287,   288,
     289,   290,   291,   292,   293,   294,   319,   258,   100,   109,
     149,   318,   259,   260,   261,   262,   258,    83,   236,    83,
     263,   259,   260,   261,   262,   325,   323,   346,   328,   263,
     106,   326,   333,   337,   104,   338,   332,   342,   343,   345,
     366,   347,   348,   164,   361,   165,   354,   327,   166,   359,
     167,   168,   169,   364,   365,   372,   373,   375,   380,   102,
     351,   392,   381,   353,   395,   356,   357,   396,   401,   403,
     410,   409,   101,   334,   170,   171,   172,   173,   174,   175,
     176,   177,   178,   179,   180,   417,   377,   379,   418,   212,
     422,   383,   384,   435,   434,   437,   426,   212,   428,   436,
     341,   441,   442,   360,   336,   421,   412,   344,   393,   398,
     239,   324,   405,   394,   408,   297,   316,   443,   270,     0,
     363,   416,     0,     0,   367,   368,     0,     0,    83,     0,
       0,     0,    83,    83,   374,   369,     0,    83,     0,     0,
       0,   430,    83,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    83,     0,   341,   399,   400,     0,
     402,     0,    83,   406,     0,    83,    83,     0,    83,     0,
       0,    83,   159,   161,     0,     0,   420,     0,     0,     0,
       0,     0,    83,   423,    83,   424,   425,     0,     0,   427,
       0,    83,   431,    83,    83,     0,     0,    83,     0,   109,
      83,     0,     0,     0,     0,   208,   209,    83,   438,   215,
     439,   440,     0,     0,     0,     0,    83,   109,    83,    83,
     226,     0,     0,   444,     0,    83,     0,     0,   185,   186,
       0,    83,   187,   188,   189,   190,   191,   192,   193,   194,
     195,   196,   197,   198,   199,   200,   201,   202,   203,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   100,     0,
       0,     0,     0,     0,   208,     0,     0,   209,     0,     0,
       0,     0,   215,     0,     0,   100,     0,     0,     0,     0,
     106,     0,     0,     0,   226,     0,     0,     0,     0,     0,
       0,     0,   241,   164,  -142,   165,     0,   106,   166,     0,
     167,   168,   169,     0,   268,     0,     0,     0,     0,   272,
     164,     0,   165,     0,     0,   166,     0,   167,   168,   169,
       0,     0,   274,   275,   170,   171,   172,   173,   174,   175,
     176,   177,   178,   179,   180,     0,     0,     0,     0,     0,
       0,   170,   171,   172,   173,   174,   175,   176,   177,   178,
     179,   180,     0,     0,     0,     0,     0,   306,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   320,     0,     1,     2,     3,     4,
       5,    84,    85,    86,    87,    88,    89,    90,    91,    92,
      93,    94,    95,    96,    97,    98,    99,     0,     6,     7,
     100,     8,   101,   102,     9,    10,   103,   104,    11,    12,
      13,    14,    15,    16,    17,    18,    19,    20,   105,    21,
      22,    23,   106,    24,    25,     0,     0,     0,     0,     0,
       0,     0,    26,   107,   108,     0,    27,     0,     0,   330,
      28,     0,     0,    29,    30,    31,    32,    33,    34,     1,
       2,     3,     4,     5,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   350,     0,     0,     0,
       0,     6,     7,   358,     8,     0,     0,     9,    10,     0,
       0,    11,    12,    13,    14,    15,    16,    17,    18,    19,
      20,     0,    21,    22,    23,     0,    24,    25,     0,     0,
       1,     2,     3,     4,     5,    26,     0,     0,     0,    27,
       0,     0,     0,    28,     0,     0,    29,    30,    31,    32,
      33,    34,     6,     7,     0,     8,     0,     0,     9,    10,
       0,     0,    11,    12,    13,    14,    15,    16,    17,     0,
      19,    20,     0,    21,    22,    23,     0,    24,    25,     0,
       0,     0,     0,     0,     0,     0,    26,     0,     0,     0,
      27,     0,     0,     0,    28,     0,     0,    29,    30,    31,
      32,    33,    34,     1,     2,     3,     4,     5,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   204,     0,     0,     0,     8,     0,
       0,     9,     0,     0,     0,     0,    12,     0,     0,     0,
       0,     0,     0,    19,     0,     0,     0,     0,    23,     0,
       0,    25,     1,     2,     3,     4,     5,     0,     0,   158,
       0,     1,     2,     3,     4,     5,  -180,    28,     0,     0,
      29,    30,    31,    32,    33,    34,     0,     8,     0,     0,
       9,    10,   204,     0,     0,    12,     8,     0,     0,     9,
       0,     0,    19,     0,    12,     0,     0,    23,     0,     0,
      25,    19,     0,     0,     0,     0,    23,     0,   158,    25,
       0,     0,   304,     0,     0,     0,    28,   158,     0,    29,
      30,    31,    32,    33,    34,    28,     0,     0,    29,    30,
      31,    32,    33,    34,     1,     2,     3,     4,     5,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     8,
       0,     0,     9,     0,     0,     0,     0,    12,     0,     0,
       0,     0,     0,     0,    19,     0,     0,     0,     0,    23,
       0,     0,    25,     1,     2,     3,     4,     5,     0,     0,
     158,     0,   240,     0,     0,     0,     0,     0,    28,     0,
       0,    29,    30,    31,    32,    33,    34,     0,     8,     0,
       0,     9,     0,     0,     0,     0,    12,     0,     0,     0,
       0,     0,     0,    19,     0,     0,     0,     0,    23,     0,
       0,    25,     1,     2,     3,     4,     5,     0,     0,   158,
       0,     0,     0,     0,     0,   266,     0,    28,     0,     0,
      29,    30,    31,    32,    33,    34,     0,     8,     0,     0,
       9,     0,     0,     0,     0,    12,     0,     0,     0,     0,
       0,     0,    19,     0,     0,     0,     0,    23,     0,     0,
      25,     1,     2,     3,     4,     5,     0,     0,   158,     0,
       0,     0,   331,     0,     0,     0,    28,     0,     0,    29,
      30,    31,    32,    33,    34,     0,     8,     0,     0,     9,
       0,     0,     0,     0,    12,     0,     0,     0,     0,     0,
       0,    19,     0,     0,     0,     0,    23,     0,     0,    25,
       1,     2,     3,     4,     5,     0,     0,   158,     0,     0,
       0,     0,     0,   352,     0,    28,     0,     0,    29,    30,
      31,    32,    33,    34,     0,     8,     0,     0,     9,     0,
       0,     0,     0,    12,     0,     0,     0,     0,     0,     0,
      19,     0,     0,     0,     0,    23,     0,     0,    25,     1,
       2,     3,     4,     5,     0,     0,   158,     0,     0,     0,
     355,     0,     0,     0,    28,     0,     0,    29,    30,    31,
      32,    33,    34,     0,     8,     0,     0,     9,     0,     0,
       0,     0,    12,     0,     0,     0,     0,     0,     0,    19,
       0,     0,     0,     0,    23,     0,     0,    25,     1,     2,
       3,     4,     5,     0,     0,   158,     0,     0,     0,     0,
       0,   376,     0,    28,     0,     0,    29,    30,    31,    32,
      33,    34,     0,     8,     0,     0,     9,     0,     0,     0,
       0,    12,     0,     0,     0,     0,     0,     0,    19,     0,
       0,     0,     0,    23,     0,     0,    25,     1,     2,     3,
       4,     5,     0,     0,   158,     0,     0,     0,     0,     0,
     378,     0,    28,     0,     0,    29,    30,    31,    32,    33,
      34,     0,     8,     0,     0,     9,     0,     0,     0,     0,
      12,     0,     0,     0,     0,     0,     0,    19,     0,     0,
       0,     0,    23,     0,     0,    25,     1,     2,     3,     4,
       5,     0,     0,   158,     0,     0,     0,   382,     0,     0,
       0,    28,     0,     0,    29,    30,    31,    32,    33,    34,
       0,     8,     0,     0,     9,     0,     0,     0,     0,    12,
       0,     0,     0,     0,     0,     0,    19,     0,     0,     0,
       0,    23,     0,     0,    25,     1,     2,     3,     4,     5,
       0,     0,   158,     0,     0,     0,     0,     0,   404,     0,
      28,     0,     0,    29,    30,    31,    32,    33,    34,     0,
       8,     0,     0,     9,     0,     0,     0,     0,    12,     0,
       0,     0,     0,     0,     0,    19,     0,     0,     0,     0,
      23,     0,     0,    25,     1,     2,     3,     4,     5,     0,
       0,   158,     0,     0,     0,     0,     0,   407,     0,    28,
       0,     0,    29,    30,    31,    32,    33,    34,     0,     8,
       0,     0,     9,     0,     0,     0,     0,    12,     0,     0,
       0,     0,     0,     0,    19,     0,     0,     0,     0,    23,
       0,     0,    25,     1,     2,     3,     4,     5,     0,     0,
     158,     0,     0,     0,     0,     0,   429,     0,    28,     0,
       0,    29,    30,    31,    32,    33,    34,     0,     8,     0,
       0,     9,     0,     0,     0,     0,    12,     0,     0,     0,
       0,     0,     0,    19,     0,     0,     0,     0,    23,     0,
       0,    25,     0,     0,     0,     0,     0,     0,     0,   158,
       0,     0,     0,     0,     0,     0,     0,    28,     0,     0,
      29,    30,    31,    32,    33,    34,     1,     2,     3,     4,
       5,    84,    85,    86,    87,    88,    89,    90,    91,    92,
      93,    94,    95,    96,    97,    98,    99,     0,     6,     7,
     100,     8,   101,   102,     9,    10,   103,   104,    11,    12,
      13,    14,    15,    16,    17,    18,    19,    20,   105,    21,
      22,    23,   106,    24,    25,     0,     0,     0,     0,     0,
       0,     0,     0,   107,   108,     3,     4,     5,    84,    85,
      86,    87,    88,    89,    90,    91,    92,    93,    94,    95,
      96,    97,    98,    99,     0,     6,     7,   100,     8,   101,
     102,     9,    10,   103,   104,    11,    12,    13,    14,    15,
      16,    17,    18,    19,    20,   105,    21,    22,    23,   106,
      24,    25
};

static const yytype_int16 yycheck[] =
{
       0,   109,    82,    26,    26,    26,    26,    26,    26,    26,
      26,    69,    24,   228,    24,    69,     0,    71,    26,    51,
     361,    75,    80,    26,    51,    26,    26,   299,    24,     0,
      29,    29,    24,    64,    66,   307,    26,    37,    65,    51,
      26,    29,    30,    31,    32,   386,    26,    26,    26,    51,
      26,    26,    26,    26,    66,    51,    66,    65,    26,    51,
      45,    60,    60,    29,    64,    65,    37,   147,    68,   364,
      66,    71,    24,    64,   132,    60,    76,   372,   132,    45,
     134,    51,   387,   388,   138,    26,   144,    64,    49,    61,
      26,    26,    26,    26,    60,    65,    68,   392,    26,   314,
      61,   109,    64,    61,    61,    61,   164,   412,   166,   109,
      68,    68,    68,    60,    61,   123,     3,     4,     5,     6,
       7,    64,   122,   123,   182,    64,    66,    66,    59,   129,
      33,    34,    40,    60,   134,   158,   158,   158,   158,   158,
     158,   158,   158,    60,   167,   167,   167,   167,   167,   167,
     167,   167,   206,    66,    66,   158,   210,   158,   158,   213,
     218,   219,   220,   217,   167,   223,   224,   167,   158,    66,
      66,   225,   158,    66,    66,    61,    64,   167,   158,   158,
     158,   167,   158,   158,   158,   158,   207,   167,   167,   167,
     158,   167,   167,   167,   167,    62,   218,   185,   186,   187,
     188,   189,   190,   191,   192,   193,   194,   195,   196,   197,
     198,   199,   200,   201,   202,   203,    60,   158,    27,   227,
      61,   229,   158,   158,   158,   158,   167,   227,    64,   229,
     158,   167,   167,   167,   167,    65,   236,   317,    64,   167,
      49,    68,    63,    65,    34,    65,   304,    65,    65,    64,
      61,    59,    65,    62,    59,    64,    63,    66,    67,    63,
      69,    70,    71,    59,    65,    59,    65,    65,    63,    30,
     328,    59,    65,   331,    65,   333,   334,    60,    65,    65,
      65,    63,    29,   306,    93,    94,    95,    96,    97,    98,
      99,   100,   101,   102,   103,    66,   354,   355,    60,   299,
      60,   359,   360,    66,    60,    60,    65,   307,    65,   417,
     310,    65,    60,   336,   307,   395,   386,   314,   366,   373,
     152,   237,   380,   368,   382,   209,   228,   435,   167,    -1,
     338,   389,    -1,    -1,   342,   343,    -1,    -1,   338,    -1,
      -1,    -1,   342,   343,   352,   345,    -1,   347,    -1,    -1,
      -1,   409,   352,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   364,    -1,   366,   375,   376,    -1,
     378,    -1,   372,   381,    -1,   375,   376,    -1,   378,    -1,
      -1,   381,    33,    34,    -1,    -1,   394,    -1,    -1,    -1,
      -1,    -1,   392,   401,   394,   403,   404,    -1,    -1,   407,
      -1,   401,   410,   403,   404,    -1,    -1,   407,    -1,   417,
     410,    -1,    -1,    -1,    -1,    66,    67,   417,   426,    70,
     428,   429,    -1,    -1,    -1,    -1,   426,   435,   428,   429,
      81,    -1,    -1,   441,    -1,   435,    -1,    -1,    72,    73,
      -1,   441,    76,    77,    78,    79,    80,    81,    82,    83,
      84,    85,    86,    87,    88,    89,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    -1,
      -1,    -1,    -1,    -1,   125,    -1,    -1,   128,    -1,    -1,
      -1,    -1,   133,    -1,    -1,    27,    -1,    -1,    -1,    -1,
      49,    -1,    -1,    -1,   145,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   153,    62,    63,    64,    -1,    49,    67,    -1,
      69,    70,    71,    -1,   165,    -1,    -1,    -1,    -1,   170,
      62,    -1,    64,    -1,    -1,    67,    -1,    69,    70,    71,
      -1,    -1,   183,   184,    93,    94,    95,    96,    97,    98,
      99,   100,   101,   102,   103,    -1,    -1,    -1,    -1,    -1,
      -1,    93,    94,    95,    96,    97,    98,    99,   100,   101,
     102,   103,    -1,    -1,    -1,    -1,    -1,   218,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   235,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    -1,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    43,    44,    45,    46,
      47,    48,    49,    50,    51,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    59,    60,    61,    -1,    63,    -1,    -1,   300,
      67,    -1,    -1,    70,    71,    72,    73,    74,    75,     3,
       4,     5,     6,     7,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   327,    -1,    -1,    -1,
      -1,    25,    26,   334,    28,    -1,    -1,    31,    32,    -1,
      -1,    35,    36,    37,    38,    39,    40,    41,    42,    43,
      44,    -1,    46,    47,    48,    -1,    50,    51,    -1,    -1,
       3,     4,     5,     6,     7,    59,    -1,    -1,    -1,    63,
      -1,    -1,    -1,    67,    -1,    -1,    70,    71,    72,    73,
      74,    75,    25,    26,    -1,    28,    -1,    -1,    31,    32,
      -1,    -1,    35,    36,    37,    38,    39,    40,    41,    -1,
      43,    44,    -1,    46,    47,    48,    -1,    50,    51,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    59,    -1,    -1,    -1,
      63,    -1,    -1,    -1,    67,    -1,    -1,    70,    71,    72,
      73,    74,    75,     3,     4,     5,     6,     7,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    24,    -1,    -1,    -1,    28,    -1,
      -1,    31,    -1,    -1,    -1,    -1,    36,    -1,    -1,    -1,
      -1,    -1,    -1,    43,    -1,    -1,    -1,    -1,    48,    -1,
      -1,    51,     3,     4,     5,     6,     7,    -1,    -1,    59,
      -1,     3,     4,     5,     6,     7,    66,    67,    -1,    -1,
      70,    71,    72,    73,    74,    75,    -1,    28,    -1,    -1,
      31,    32,    24,    -1,    -1,    36,    28,    -1,    -1,    31,
      -1,    -1,    43,    -1,    36,    -1,    -1,    48,    -1,    -1,
      51,    43,    -1,    -1,    -1,    -1,    48,    -1,    59,    51,
      -1,    -1,    63,    -1,    -1,    -1,    67,    59,    -1,    70,
      71,    72,    73,    74,    75,    67,    -1,    -1,    70,    71,
      72,    73,    74,    75,     3,     4,     5,     6,     7,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,
      -1,    -1,    31,    -1,    -1,    -1,    -1,    36,    -1,    -1,
      -1,    -1,    -1,    -1,    43,    -1,    -1,    -1,    -1,    48,
      -1,    -1,    51,     3,     4,     5,     6,     7,    -1,    -1,
      59,    -1,    61,    -1,    -1,    -1,    -1,    -1,    67,    -1,
      -1,    70,    71,    72,    73,    74,    75,    -1,    28,    -1,
      -1,    31,    -1,    -1,    -1,    -1,    36,    -1,    -1,    -1,
      -1,    -1,    -1,    43,    -1,    -1,    -1,    -1,    48,    -1,
      -1,    51,     3,     4,     5,     6,     7,    -1,    -1,    59,
      -1,    -1,    -1,    -1,    -1,    65,    -1,    67,    -1,    -1,
      70,    71,    72,    73,    74,    75,    -1,    28,    -1,    -1,
      31,    -1,    -1,    -1,    -1,    36,    -1,    -1,    -1,    -1,
      -1,    -1,    43,    -1,    -1,    -1,    -1,    48,    -1,    -1,
      51,     3,     4,     5,     6,     7,    -1,    -1,    59,    -1,
      -1,    -1,    63,    -1,    -1,    -1,    67,    -1,    -1,    70,
      71,    72,    73,    74,    75,    -1,    28,    -1,    -1,    31,
      -1,    -1,    -1,    -1,    36,    -1,    -1,    -1,    -1,    -1,
      -1,    43,    -1,    -1,    -1,    -1,    48,    -1,    -1,    51,
       3,     4,     5,     6,     7,    -1,    -1,    59,    -1,    -1,
      -1,    -1,    -1,    65,    -1,    67,    -1,    -1,    70,    71,
      72,    73,    74,    75,    -1,    28,    -1,    -1,    31,    -1,
      -1,    -1,    -1,    36,    -1,    -1,    -1,    -1,    -1,    -1,
      43,    -1,    -1,    -1,    -1,    48,    -1,    -1,    51,     3,
       4,     5,     6,     7,    -1,    -1,    59,    -1,    -1,    -1,
      63,    -1,    -1,    -1,    67,    -1,    -1,    70,    71,    72,
      73,    74,    75,    -1,    28,    -1,    -1,    31,    -1,    -1,
      -1,    -1,    36,    -1,    -1,    -1,    -1,    -1,    -1,    43,
      -1,    -1,    -1,    -1,    48,    -1,    -1,    51,     3,     4,
       5,     6,     7,    -1,    -1,    59,    -1,    -1,    -1,    -1,
      -1,    65,    -1,    67,    -1,    -1,    70,    71,    72,    73,
      74,    75,    -1,    28,    -1,    -1,    31,    -1,    -1,    -1,
      -1,    36,    -1,    -1,    -1,    -1,    -1,    -1,    43,    -1,
      -1,    -1,    -1,    48,    -1,    -1,    51,     3,     4,     5,
       6,     7,    -1,    -1,    59,    -1,    -1,    -1,    -1,    -1,
      65,    -1,    67,    -1,    -1,    70,    71,    72,    73,    74,
      75,    -1,    28,    -1,    -1,    31,    -1,    -1,    -1,    -1,
      36,    -1,    -1,    -1,    -1,    -1,    -1,    43,    -1,    -1,
      -1,    -1,    48,    -1,    -1,    51,     3,     4,     5,     6,
       7,    -1,    -1,    59,    -1,    -1,    -1,    63,    -1,    -1,
      -1,    67,    -1,    -1,    70,    71,    72,    73,    74,    75,
      -1,    28,    -1,    -1,    31,    -1,    -1,    -1,    -1,    36,
      -1,    -1,    -1,    -1,    -1,    -1,    43,    -1,    -1,    -1,
      -1,    48,    -1,    -1,    51,     3,     4,     5,     6,     7,
      -1,    -1,    59,    -1,    -1,    -1,    -1,    -1,    65,    -1,
      67,    -1,    -1,    70,    71,    72,    73,    74,    75,    -1,
      28,    -1,    -1,    31,    -1,    -1,    -1,    -1,    36,    -1,
      -1,    -1,    -1,    -1,    -1,    43,    -1,    -1,    -1,    -1,
      48,    -1,    -1,    51,     3,     4,     5,     6,     7,    -1,
      -1,    59,    -1,    -1,    -1,    -1,    -1,    65,    -1,    67,
      -1,    -1,    70,    71,    72,    73,    74,    75,    -1,    28,
      -1,    -1,    31,    -1,    -1,    -1,    -1,    36,    -1,    -1,
      -1,    -1,    -1,    -1,    43,    -1,    -1,    -1,    -1,    48,
      -1,    -1,    51,     3,     4,     5,     6,     7,    -1,    -1,
      59,    -1,    -1,    -1,    -1,    -1,    65,    -1,    67,    -1,
      -1,    70,    71,    72,    73,    74,    75,    -1,    28,    -1,
      -1,    31,    -1,    -1,    -1,    -1,    36,    -1,    -1,    -1,
      -1,    -1,    -1,    43,    -1,    -1,    -1,    -1,    48,    -1,
      -1,    51,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    59,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,    -1,
      70,    71,    72,    73,    74,    75,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    -1,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    43,    44,    45,    46,
      47,    48,    49,    50,    51,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    60,    61,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    -1,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,     4,     5,     6,     7,    25,    26,    28,    31,
      32,    35,    36,    37,    38,    39,    40,    41,    42,    43,
      44,    46,    47,    48,    50,    51,    59,    63,    67,    70,
      71,    72,    73,    74,    75,   105,   106,   107,   108,   109,
     111,   115,   116,   117,   118,   119,   120,   121,   122,   123,
     128,   129,   130,   133,   134,   137,   141,   148,   149,   154,
     155,   156,   157,   158,   161,   162,   164,   167,   168,   171,
     172,   173,   174,   175,   176,   177,   178,   179,   180,   182,
     183,   184,   186,   187,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      27,    29,    30,    33,    34,    45,    49,    60,    61,   108,
     110,   142,   143,   144,   151,   152,   153,   155,   156,   157,
     158,   159,   161,   162,   163,   164,   165,   166,   167,   168,
     169,   170,   171,   172,   173,   174,   175,   176,   177,   178,
     179,   180,   181,   182,   183,   184,   185,   186,   187,    61,
      68,   138,   139,   140,   154,   154,   154,   154,    59,   149,
     187,   149,     0,   106,    62,    64,    67,    69,    70,    71,
      93,    94,    95,    96,    97,    98,    99,   100,   101,   102,
     103,   146,   150,   163,   185,    72,    73,    76,    77,    78,
      79,    80,    81,    82,    83,    84,    85,    86,    87,    88,
      89,    90,    91,    92,    24,   160,   187,   108,   149,   149,
     112,   113,   187,   148,   160,   149,   160,   187,    64,    64,
      64,   160,   187,    64,    64,   148,   149,    59,   109,    66,
      60,   110,    60,    60,    61,    66,    64,    61,    68,   138,
      61,   149,   155,   156,   157,   158,   161,   162,   164,   167,
     168,   171,   172,   173,   174,   175,   176,   177,   179,   180,
     182,   183,   184,   186,   187,   148,    65,   147,   149,   148,
     151,   187,   149,   148,   149,   149,   154,   154,   154,   154,
     154,   154,   154,   154,   154,   154,   154,   154,   154,   154,
     154,   154,   154,   154,   154,   160,   176,   146,   160,    61,
      62,   114,   160,   160,    63,   148,   149,   168,   148,   148,
      64,   148,   148,   160,   131,   132,   169,   170,   108,    60,
     149,    65,   145,   187,   140,    65,    68,    66,    64,   112,
     149,    63,   148,    63,   185,   112,   113,    65,    65,    65,
     135,   187,    65,    65,   132,    64,   109,    59,    65,    68,
     149,   148,    65,   148,    63,    63,   148,   148,   149,    63,
     185,    59,   124,   108,    59,    65,    61,   108,   108,   187,
     106,   136,    59,    65,   108,    65,    65,   148,    65,   148,
      63,    65,    63,   148,   148,    60,   125,   126,   127,   165,
     181,   136,    59,   135,   166,    65,    60,   136,   160,   108,
     108,    65,   108,    65,    65,   148,   108,    65,   148,    63,
      65,    60,   127,   125,    60,   125,   148,    66,    60,   136,
     108,   109,    60,   108,   108,   108,    65,   108,    65,    65,
     148,   108,    60,   125,    60,    66,   110,    60,   108,   108,
     108,    65,    60,   110,   108
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   104,   105,   105,   106,   106,   107,   107,   108,   108,
     108,   108,   108,   108,   108,   108,   108,   108,   108,   108,
     108,   108,   108,   109,   110,   110,   110,   111,   112,   112,
     113,   113,   113,   114,   115,   116,   117,   117,   118,   118,
     118,   118,   118,   118,   118,   118,   118,   118,   118,   118,
     118,   118,   118,   118,   119,   119,   120,   120,   121,   121,
     122,   123,   124,   124,   124,   124,   124,   124,   125,   125,
     126,   126,   127,   127,   128,   129,   130,   130,   130,   131,
     132,   133,   134,   134,   135,   135,   136,   136,   137,   137,
     137,   138,   138,   139,   140,   140,   140,   141,   141,   141,
     141,   142,   143,   143,   143,   144,   144,   144,   145,   146,
     146,   147,   148,   149,   149,   149,   149,   149,   149,   149,
     149,   149,   149,   149,   149,   149,   149,   149,   149,   149,
     149,   149,   149,   149,   149,   149,   149,   149,   149,   149,
     149,   149,   149,   149,   149,   149,   149,   149,   149,   149,
     149,   149,   149,   149,   149,   149,   149,   149,   150,   150,
     150,   150,   150,   150,   150,   150,   150,   150,   151,   151,
     152,   152,   152,   152,   152,   152,   152,   152,   152,   152,
     152,   152,   152,   152,   152,   152,   152,   152,   152,   152,
     152,   152,   152,   152,   152,   152,   153,   153,   153,   153,
     154,   154,   154,   154,   155,   156,   157,   158,   158,   159,
     159,   159,   159,   159,   159,   159,   159,   159,   159,   159,
     159,   159,   159,   159,   159,   160,   160,   161,   162,   163,
     164,   165,   166,   167,   168,   169,   170,   171,   172,   173,
     174,   175,   176,   177,   178,   179,   180,   181,   182,   183,
     184,   185,   186,   187
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     0,     1,     2,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     3,     1,     2,     0,     3,     3,     1,
       1,     2,     0,     2,     1,     1,     7,     5,     7,     5,
       9,     8,     8,     7,     8,     7,     7,     6,    10,     9,
       9,     8,     7,     8,     3,     2,     3,     2,     3,     2,
       5,     5,     5,     4,     3,     4,     3,     2,     1,     2,
       4,     3,     3,     2,     3,     3,     3,     3,     4,     5,
       2,     2,     8,     7,     3,     1,     1,     0,     2,     3,
       5,     2,     1,     2,     1,     2,     0,     4,     3,     3,
       2,     1,     3,     6,     7,     1,     1,     1,     1,     3,
       2,     1,     1,     4,     3,     2,     3,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       5,     3,     3,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     0,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:
#line 18 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1858 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 3:
#line 20 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)="EMPTY";}
#line 1864 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 4:
#line 23 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1870 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 5:
#line 25 "../../output/bison.y" /* yacc.c:1646  */
    {printf("<<<sourceElements: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));}
#line 1876 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 6:
#line 28 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1882 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 7:
#line 30 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1888 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 8:
#line 33 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1894 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 9:
#line 34 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1900 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 10:
#line 35 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1906 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 11:
#line 36 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1912 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 12:
#line 37 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1918 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 13:
#line 38 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1924 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 14:
#line 39 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1930 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 15:
#line 40 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1936 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 16:
#line 41 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1942 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 17:
#line 42 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1948 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 18:
#line 43 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1954 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 19:
#line 44 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1960 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 20:
#line 45 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1966 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 21:
#line 46 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1972 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 22:
#line 48 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1978 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 23:
#line 52 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+8 ;char *s22=malloc(sizeof(char)*len);sprintf(s22," <<<block: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s22;}
#line 1984 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 24:
#line 55 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 1990 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 25:
#line 56 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+15 ;char *s24=malloc(sizeof(char)*len);sprintf(s24," <<<statementList: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s24;}
#line 1996 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 26:
#line 58 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)="EMPTY";}
#line 2002 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 27:
#line 62 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+20 ;char *s26=malloc(sizeof(char)*len);sprintf(s26," <<<variableStatement: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s26;}
#line 2008 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 28:
#line 65 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+26 ;char *s27=malloc(sizeof(char)*len);sprintf(s27," <<<variableDeclarationList: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s27;}
#line 2014 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 29:
#line 67 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2020 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 30:
#line 70 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2026 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 31:
#line 71 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+21 ;char *s30=malloc(sizeof(char)*len);sprintf(s30," <<<variableDeclaration: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s30;}
#line 2032 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 32:
#line 73 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)="EMPTY";}
#line 2038 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 33:
#line 77 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+13 ;char *s32=malloc(sizeof(char)*len);sprintf(s32," <<<initialiser: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s32;}
#line 2044 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 34:
#line 81 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2050 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 35:
#line 85 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2056 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 36:
#line 88 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s35=malloc(sizeof(char)*len);sprintf(s35," <<<ifStatement: %s %s %s %s %s %s %s >>>",(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s35;}
#line 2062 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 37:
#line 90 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+16 ;char *s36=malloc(sizeof(char)*len);sprintf(s36," <<<ifStatement: %s %s %s %s %s >>>",(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s36;}
#line 2068 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 38:
#line 93 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+25 ;char *s37=malloc(sizeof(char)*len);sprintf(s37," <<<iterationStatement: %s %s %s %s %s %s %s >>>",(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s37;}
#line 2074 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 39:
#line 94 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+23 ;char *s38=malloc(sizeof(char)*len);sprintf(s38," <<<iterationStatement: %s %s %s %s %s >>>",(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s38;}
#line 2080 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 40:
#line 95 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-8].c))+strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+27 ;char *s39=malloc(sizeof(char)*len);sprintf(s39," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",(yyvsp[-8].c),(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s39;}
#line 2086 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 41:
#line 96 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+26 ;char *s40=malloc(sizeof(char)*len);sprintf(s40," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s40;}
#line 2092 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 42:
#line 97 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+26 ;char *s41=malloc(sizeof(char)*len);sprintf(s41," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s41;}
#line 2098 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 43:
#line 98 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+25 ;char *s42=malloc(sizeof(char)*len);sprintf(s42," <<<iterationStatement: %s %s %s %s %s %s %s >>>",(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s42;}
#line 2104 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 44:
#line 99 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+26 ;char *s43=malloc(sizeof(char)*len);sprintf(s43," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s43;}
#line 2110 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 45:
#line 100 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+25 ;char *s44=malloc(sizeof(char)*len);sprintf(s44," <<<iterationStatement: %s %s %s %s %s %s %s >>>",(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s44;}
#line 2116 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 46:
#line 101 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+25 ;char *s45=malloc(sizeof(char)*len);sprintf(s45," <<<iterationStatement: %s %s %s %s %s %s %s >>>",(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s45;}
#line 2122 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 47:
#line 102 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+24 ;char *s46=malloc(sizeof(char)*len);sprintf(s46," <<<iterationStatement: %s %s %s %s %s %s >>>",(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s46;}
#line 2128 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 48:
#line 103 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-9].c))+strlen((yyvsp[-8].c))+strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+28 ;char *s47=malloc(sizeof(char)*len);sprintf(s47," <<<iterationStatement: %s %s %s %s %s %s %s %s %s %s >>>",(yyvsp[-9].c),(yyvsp[-8].c),(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s47;}
#line 2134 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 49:
#line 104 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-8].c))+strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+27 ;char *s48=malloc(sizeof(char)*len);sprintf(s48," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",(yyvsp[-8].c),(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s48;}
#line 2140 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 50:
#line 105 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-8].c))+strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+27 ;char *s49=malloc(sizeof(char)*len);sprintf(s49," <<<iterationStatement: %s %s %s %s %s %s %s %s %s >>>",(yyvsp[-8].c),(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s49;}
#line 2146 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 51:
#line 106 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+26 ;char *s50=malloc(sizeof(char)*len);sprintf(s50," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s50;}
#line 2152 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 52:
#line 107 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+25 ;char *s51=malloc(sizeof(char)*len);sprintf(s51," <<<iterationStatement: %s %s %s %s %s %s %s >>>",(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s51;}
#line 2158 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 53:
#line 109 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+26 ;char *s52=malloc(sizeof(char)*len);sprintf(s52," <<<iterationStatement: %s %s %s %s %s %s %s %s >>>",(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s52;}
#line 2164 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 54:
#line 112 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+20 ;char *s53=malloc(sizeof(char)*len);sprintf(s53," <<<continueStatement: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s53;}
#line 2170 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 55:
#line 114 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s54=malloc(sizeof(char)*len);sprintf(s54," <<<continueStatement: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s54;}
#line 2176 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 56:
#line 117 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+17 ;char *s55=malloc(sizeof(char)*len);sprintf(s55," <<<breakStatement: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s55;}
#line 2182 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 57:
#line 119 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+16 ;char *s56=malloc(sizeof(char)*len);sprintf(s56," <<<breakStatement: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s56;}
#line 2188 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 58:
#line 122 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s57=malloc(sizeof(char)*len);sprintf(s57," <<<returnStatement: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s57;}
#line 2194 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 59:
#line 124 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+17 ;char *s58=malloc(sizeof(char)*len);sprintf(s58," <<<returnStatement: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s58;}
#line 2200 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 60:
#line 128 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s59=malloc(sizeof(char)*len);sprintf(s59," <<<withStatement: %s %s %s %s %s >>>",(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s59;}
#line 2206 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 61:
#line 132 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+20 ;char *s60=malloc(sizeof(char)*len);sprintf(s60," <<<switchStatement: %s %s %s %s %s >>>",(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s60;}
#line 2212 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 62:
#line 135 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+14 ;char *s61=malloc(sizeof(char)*len);sprintf(s61," <<<caseBlock: %s %s %s %s %s >>>",(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s61;}
#line 2218 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 63:
#line 136 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+13 ;char *s62=malloc(sizeof(char)*len);sprintf(s62," <<<caseBlock: %s %s %s %s >>>",(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s62;}
#line 2224 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 64:
#line 137 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+12 ;char *s63=malloc(sizeof(char)*len);sprintf(s63," <<<caseBlock: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s63;}
#line 2230 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 65:
#line 138 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+13 ;char *s64=malloc(sizeof(char)*len);sprintf(s64," <<<caseBlock: %s %s %s %s >>>",(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s64;}
#line 2236 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 66:
#line 139 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+12 ;char *s65=malloc(sizeof(char)*len);sprintf(s65," <<<caseBlock: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s65;}
#line 2242 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 67:
#line 141 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+11 ;char *s66=malloc(sizeof(char)*len);sprintf(s66," <<<caseBlock: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s66;}
#line 2248 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 68:
#line 144 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2254 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 69:
#line 146 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+13 ;char *s68=malloc(sizeof(char)*len);sprintf(s68," <<<caseClauses: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s68;}
#line 2260 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 70:
#line 149 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+14 ;char *s69=malloc(sizeof(char)*len);sprintf(s69," <<<caseClause: %s %s %s %s >>>",(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s69;}
#line 2266 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 71:
#line 151 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+13 ;char *s70=malloc(sizeof(char)*len);sprintf(s70," <<<caseClause: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s70;}
#line 2272 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 72:
#line 154 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+16 ;char *s71=malloc(sizeof(char)*len);sprintf(s71," <<<defaultClause: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s71;}
#line 2278 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 73:
#line 156 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+15 ;char *s72=malloc(sizeof(char)*len);sprintf(s72," <<<defaultClause: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s72;}
#line 2284 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 74:
#line 160 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+20 ;char *s73=malloc(sizeof(char)*len);sprintf(s73," <<<labelledStatement: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s73;}
#line 2290 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 75:
#line 164 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+17 ;char *s74=malloc(sizeof(char)*len);sprintf(s74," <<<throwStatement: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s74;}
#line 2296 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 76:
#line 167 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+15 ;char *s75=malloc(sizeof(char)*len);sprintf(s75," <<<tryStatement: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s75;}
#line 2302 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 77:
#line 168 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+15 ;char *s76=malloc(sizeof(char)*len);sprintf(s76," <<<tryStatement: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s76;}
#line 2308 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 78:
#line 170 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+16 ;char *s77=malloc(sizeof(char)*len);sprintf(s77," <<<tryStatement: %s %s %s %s >>>",(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s77;}
#line 2314 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 79:
#line 174 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+20 ;char *s78=malloc(sizeof(char)*len);sprintf(s78," <<<catchProduction: %s %s %s %s %s >>>",(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s78;}
#line 2320 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 80:
#line 178 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s79=malloc(sizeof(char)*len);sprintf(s79," <<<finallyProduction: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s79;}
#line 2326 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 81:
#line 182 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s80=malloc(sizeof(char)*len);sprintf(s80," <<<debuggerStatement: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s80;}
#line 2332 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 82:
#line 185 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-7].c))+strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+27 ;char *s81=malloc(sizeof(char)*len);sprintf(s81," <<<functionDeclaration: %s %s %s %s %s %s %s %s >>>",(yyvsp[-7].c),(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s81;}
#line 2338 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 83:
#line 187 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+26 ;char *s82=malloc(sizeof(char)*len);sprintf(s82," <<<functionDeclaration: %s %s %s %s %s %s %s >>>",(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s82;}
#line 2344 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 84:
#line 190 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+22 ;char *s83=malloc(sizeof(char)*len);sprintf(s83," <<<formalParameterList: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s83;}
#line 2350 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 85:
#line 192 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2356 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 86:
#line 195 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2362 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 87:
#line 197 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)="EMPTY";}
#line 2368 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 88:
#line 200 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+14 ;char *s87=malloc(sizeof(char)*len);sprintf(s87," <<<arrayLiteral: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s87;}
#line 2374 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 89:
#line 201 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+15 ;char *s88=malloc(sizeof(char)*len);sprintf(s88," <<<arrayLiteral: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s88;}
#line 2380 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 90:
#line 203 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+17 ;char *s89=malloc(sizeof(char)*len);sprintf(s89," <<<arrayLiteral: %s %s %s %s %s >>>",(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s89;}
#line 2386 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 91:
#line 206 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+13 ;char *s90=malloc(sizeof(char)*len);sprintf(s90," <<<elementList: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s90;}
#line 2392 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 92:
#line 208 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2398 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 93:
#line 217 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+13 ;char *s94=malloc(sizeof(char)*len);sprintf(s94," <<<elisionExpr: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s94;}
#line 2404 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 94:
#line 220 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2410 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 95:
#line 221 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+9 ;char *s96=malloc(sizeof(char)*len);sprintf(s96," <<<elision: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s96;}
#line 2416 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 96:
#line 223 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)="EMPTY";}
#line 2422 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 97:
#line 226 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+17 ;char *s98=malloc(sizeof(char)*len);sprintf(s98," <<<objectLiteral: %s %s %s %s >>>",(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s98;}
#line 2428 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 98:
#line 227 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+16 ;char *s99=malloc(sizeof(char)*len);sprintf(s99," <<<objectLiteral: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s99;}
#line 2434 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 99:
#line 228 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+16 ;char *s100=malloc(sizeof(char)*len);sprintf(s100," <<<objectLiteral: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s100;}
#line 2440 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 100:
#line 230 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+15 ;char *s101=malloc(sizeof(char)*len);sprintf(s101," <<<objectLiteral: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s101;}
#line 2446 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 101:
#line 235 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2452 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 102:
#line 242 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+21 ;char *s105=malloc(sizeof(char)*len);sprintf(s105," <<<propertyAssignment: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s105;}
#line 2458 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 103:
#line 243 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+24 ;char *s106=malloc(sizeof(char)*len);sprintf(s106," <<<propertyAssignment: %s %s %s %s %s %s >>>",(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s106;}
#line 2464 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 104:
#line 245 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-6].c))+strlen((yyvsp[-5].c))+strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+25 ;char *s107=malloc(sizeof(char)*len);sprintf(s107," <<<propertyAssignment: %s %s %s %s %s %s %s >>>",(yyvsp[-6].c),(yyvsp[-5].c),(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s107;}
#line 2470 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 105:
#line 248 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2476 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 106:
#line 249 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2482 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 107:
#line 251 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2488 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 108:
#line 255 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2494 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 109:
#line 258 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+12 ;char *s112=malloc(sizeof(char)*len);sprintf(s112," <<<arguments: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s112;}
#line 2500 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 110:
#line 260 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+11 ;char *s113=malloc(sizeof(char)*len);sprintf(s113," <<<arguments: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s113;}
#line 2506 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 111:
#line 265 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2512 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 112:
#line 274 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2518 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 113:
#line 277 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+20 ;char *s119=malloc(sizeof(char)*len);sprintf(s119," <<<singleExpression: %s %s %s %s >>>",(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s119;}
#line 2524 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 114:
#line 278 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s120=malloc(sizeof(char)*len);sprintf(s120," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s120;}
#line 2530 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 115:
#line 279 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s121=malloc(sizeof(char)*len);sprintf(s121," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s121;}
#line 2536 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 116:
#line 280 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s122=malloc(sizeof(char)*len);sprintf(s122," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s122;}
#line 2542 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 117:
#line 281 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s123=malloc(sizeof(char)*len);sprintf(s123," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s123;}
#line 2548 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 118:
#line 282 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s124=malloc(sizeof(char)*len);sprintf(s124," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s124;}
#line 2554 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 119:
#line 283 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s125=malloc(sizeof(char)*len);sprintf(s125," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s125;}
#line 2560 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 120:
#line 284 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s126=malloc(sizeof(char)*len);sprintf(s126," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s126;}
#line 2566 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 121:
#line 285 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s127=malloc(sizeof(char)*len);sprintf(s127," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s127;}
#line 2572 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 122:
#line 286 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s128=malloc(sizeof(char)*len);sprintf(s128," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s128;}
#line 2578 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 123:
#line 287 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s129=malloc(sizeof(char)*len);sprintf(s129," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s129;}
#line 2584 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 124:
#line 288 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s130=malloc(sizeof(char)*len);sprintf(s130," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s130;}
#line 2590 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 125:
#line 289 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s131=malloc(sizeof(char)*len);sprintf(s131," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s131;}
#line 2596 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 126:
#line 290 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s132=malloc(sizeof(char)*len);sprintf(s132," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s132;}
#line 2602 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 127:
#line 291 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s133=malloc(sizeof(char)*len);sprintf(s133," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s133;}
#line 2608 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 128:
#line 292 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+18 ;char *s134=malloc(sizeof(char)*len);sprintf(s134," <<<singleExpression: %s %s >>>",(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s134;}
#line 2614 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 129:
#line 293 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s135=malloc(sizeof(char)*len);sprintf(s135," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s135;}
#line 2620 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 130:
#line 294 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s136=malloc(sizeof(char)*len);sprintf(s136," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s136;}
#line 2626 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 131:
#line 295 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s137=malloc(sizeof(char)*len);sprintf(s137," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s137;}
#line 2632 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 132:
#line 296 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s138=malloc(sizeof(char)*len);sprintf(s138," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s138;}
#line 2638 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 133:
#line 297 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s139=malloc(sizeof(char)*len);sprintf(s139," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s139;}
#line 2644 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 134:
#line 298 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s140=malloc(sizeof(char)*len);sprintf(s140," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s140;}
#line 2650 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 135:
#line 299 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s141=malloc(sizeof(char)*len);sprintf(s141," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s141;}
#line 2656 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 136:
#line 300 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s142=malloc(sizeof(char)*len);sprintf(s142," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s142;}
#line 2662 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 137:
#line 301 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s143=malloc(sizeof(char)*len);sprintf(s143," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s143;}
#line 2668 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 138:
#line 302 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s144=malloc(sizeof(char)*len);sprintf(s144," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s144;}
#line 2674 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 139:
#line 303 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s145=malloc(sizeof(char)*len);sprintf(s145," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s145;}
#line 2680 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 140:
#line 304 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s146=malloc(sizeof(char)*len);sprintf(s146," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s146;}
#line 2686 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 141:
#line 305 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s147=malloc(sizeof(char)*len);sprintf(s147," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s147;}
#line 2692 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 142:
#line 306 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s148=malloc(sizeof(char)*len);sprintf(s148," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s148;}
#line 2698 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 143:
#line 307 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s149=malloc(sizeof(char)*len);sprintf(s149," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s149;}
#line 2704 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 144:
#line 308 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s150=malloc(sizeof(char)*len);sprintf(s150," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s150;}
#line 2710 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 145:
#line 309 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s151=malloc(sizeof(char)*len);sprintf(s151," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s151;}
#line 2716 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 146:
#line 310 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s152=malloc(sizeof(char)*len);sprintf(s152," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s152;}
#line 2722 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 147:
#line 311 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s153=malloc(sizeof(char)*len);sprintf(s153," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s153;}
#line 2728 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 148:
#line 312 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s154=malloc(sizeof(char)*len);sprintf(s154," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s154;}
#line 2734 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 149:
#line 313 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s155=malloc(sizeof(char)*len);sprintf(s155," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s155;}
#line 2740 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 150:
#line 314 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-4].c))+strlen((yyvsp[-3].c))+strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+21 ;char *s156=malloc(sizeof(char)*len);sprintf(s156," <<<singleExpression: %s %s %s %s %s >>>",(yyvsp[-4].c),(yyvsp[-3].c),(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s156;}
#line 2746 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 151:
#line 315 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s157=malloc(sizeof(char)*len);sprintf(s157," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s157;}
#line 2752 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 152:
#line 316 "../../output/bison.y" /* yacc.c:1646  */
    {int len=strlen((yyvsp[-2].c))+strlen((yyvsp[-1].c))+strlen((yyvsp[0].c))+7+19 ;char *s158=malloc(sizeof(char)*len);sprintf(s158," <<<singleExpression: %s %s %s >>>",(yyvsp[-2].c),(yyvsp[-1].c),(yyvsp[0].c));(yyval.c)=s158;}
#line 2758 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 153:
#line 317 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2764 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 154:
#line 318 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2770 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 155:
#line 319 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2776 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 156:
#line 320 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2782 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 157:
#line 322 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2788 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 158:
#line 325 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2794 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 159:
#line 326 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2800 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 160:
#line 327 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2806 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 161:
#line 328 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2812 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 162:
#line 329 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2818 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 163:
#line 330 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2824 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 164:
#line 331 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2830 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 165:
#line 332 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2836 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 166:
#line 333 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2842 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 167:
#line 335 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2848 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 168:
#line 338 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2854 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 169:
#line 340 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2860 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 170:
#line 343 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2866 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 171:
#line 344 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2872 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 172:
#line 345 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2878 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 173:
#line 346 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2884 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 174:
#line 347 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2890 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 175:
#line 348 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2896 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 176:
#line 349 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2902 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 177:
#line 350 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2908 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 178:
#line 351 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2914 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 179:
#line 352 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2920 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 180:
#line 353 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2926 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 181:
#line 354 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2932 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 182:
#line 355 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2938 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 183:
#line 356 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2944 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 184:
#line 357 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2950 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 185:
#line 358 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2956 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 186:
#line 359 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2962 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 187:
#line 360 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2968 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 188:
#line 361 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2974 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 189:
#line 362 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2980 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 190:
#line 363 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2986 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 191:
#line 364 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2992 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 192:
#line 365 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 2998 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 193:
#line 366 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3004 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 194:
#line 367 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3010 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 195:
#line 369 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3016 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 196:
#line 372 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3022 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 197:
#line 373 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3028 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 198:
#line 374 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3034 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 199:
#line 376 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3040 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 200:
#line 379 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3046 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 201:
#line 380 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3052 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 202:
#line 381 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3058 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 203:
#line 383 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3064 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 204:
#line 387 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3070 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 205:
#line 391 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3076 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 206:
#line 395 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3082 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 207:
#line 398 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3088 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 208:
#line 400 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3094 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 209:
#line 403 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3100 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 210:
#line 404 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3106 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 211:
#line 405 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3112 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 212:
#line 406 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3118 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 213:
#line 407 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3124 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 214:
#line 408 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3130 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 215:
#line 409 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3136 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 216:
#line 410 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3142 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 217:
#line 411 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3148 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 218:
#line 412 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3154 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 219:
#line 413 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3160 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 220:
#line 414 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3166 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 221:
#line 415 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3172 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 222:
#line 416 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3178 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 223:
#line 417 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3184 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 224:
#line 419 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3190 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 225:
#line 422 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3196 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 226:
#line 424 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)="EMPTY";}
#line 3202 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 227:
#line 428 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3208 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 228:
#line 432 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3214 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 229:
#line 436 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3220 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 230:
#line 440 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3226 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 231:
#line 444 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3232 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 232:
#line 448 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3238 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 233:
#line 452 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3244 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 234:
#line 456 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3250 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 235:
#line 460 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3256 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 236:
#line 464 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3262 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 237:
#line 468 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3268 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 238:
#line 472 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3274 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 239:
#line 476 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3280 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 240:
#line 480 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3286 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 241:
#line 484 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3292 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 242:
#line 488 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3298 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 243:
#line 492 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3304 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 244:
#line 496 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3310 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 245:
#line 500 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3316 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 246:
#line 504 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3322 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 247:
#line 508 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3328 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 248:
#line 512 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3334 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 249:
#line 516 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3340 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 250:
#line 520 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3346 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 251:
#line 524 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3352 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 252:
#line 528 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3358 "bison.tab.c" /* yacc.c:1646  */
    break;

  case 253:
#line 531 "../../output/bison.y" /* yacc.c:1646  */
    {(yyval.c)=(yyvsp[0].c);}
#line 3364 "bison.tab.c" /* yacc.c:1646  */
    break;


#line 3368 "bison.tab.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 534 "../../output/bison.y" /* yacc.c:1906  */

int main()
{
yyparse();
}
