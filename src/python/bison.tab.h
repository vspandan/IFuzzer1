/* A Bison parser, made by GNU Bison 3.0.2.  */

/* Bison interface for Yacc-like parsers in C

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
#line 3 "../../output/bison.y" /* yacc.c:1909  */

 int a;
float b;
char *c;

#line 119 "bison.tab.h" /* yacc.c:1909  */
};
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_BISON_TAB_H_INCLUDED  */
