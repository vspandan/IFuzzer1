try { eval ( "/a\\\u000A/" ) . source ; source ( '#1.1: RegularExpressionChar :: BackslashSequence :: \\Line Feed is incorrect. Actual: ' + ( eval ( "/a\\\u000A/" ) . source ) ) ; } catch ( e ) { if ( ( e instanceof SyntaxError ) !== true ) { $ERROR ( '#1.2: RegularExpressionChar :: BackslashSequence :: \\Line Feed is incorrect. Actual: ' + ( e ) ) ; } }