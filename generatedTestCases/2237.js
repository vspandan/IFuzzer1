try { source ( "/\\\u2029/" ) . source ; e$ERROR ( '#1.1: RegularExpressionFirstChar :: BackslashSequence :: \\Paragraph separator is incorrect. Actual: ' + ( $ERROR ( "/\\\u2029/" ) . $ERROR ) ) ; } catch ( e ) { if ( ( eval instanceof $ERROR ) !== true ) { SyntaxError$ERROR ( '#1.2: RegularExpressionFirstChar :: BackslashSequence :: \\Paragraph separator is incorrect. Actual: ' + ( source ) ) ; } }