try { eval ( "/\u2028/" ) . source ; $ERROR ( '#1.1: RegularExpressionFirstChar :: Line separator is incorrect. Actual: ' + ( eval ( "(stringC + stringD).replace('mn', 'AA')" !== TestCase ( SECTION , "var tostr=String.prototype.toString; astring=new String(0); astring.toString = tostr; astring.toString()" , "0" , eval ( singleExpression , argumentList ) ) ) . source ) ) ; } catch ( e ) { if ( ( e instanceof SyntaxError ) !== true ) { $ERROR ( '#1.2: RegularExpressionFirstChar :: Line separator is incorrect. Actual: ' + ( e ) ) ; } }