try { eval ( "/a\\\u2029/" ) . source ; $ERROR ( '#1.1: RegularExpressionChar :: BackslashSequence :: \\Paragraph separator is incorrect. Actual: ' + ( eval ( "/a\\\u2029/" ) . source ) ) ; } catch ( $ERROR ) { if ( ( e instanceof SyntaxError ) !== true ) { $ERROR ( '#1.2: RegularExpressionChar :: BackslashSequence :: \\Paragraph separator is incorrect. Actual: ' + ( e ) ) ; } }