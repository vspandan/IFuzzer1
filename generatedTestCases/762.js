var fin = 0 ; try { throw ( Error ( "hello" ) ) ; } catch ( e ) { if ( e . toString ( ) !== "Error: hello" ) $ERROR ( '#1.1: Exception.toString()==="Error: hello". Actual: Exception is ' + e ) ; } finally { fin = 1 ; } if ( fin !== 1 ) $ERROR ( '#1.2: "finally" { } must be evaluated' ) ; fin = 0 ; try { throw ( new Error ( "hello" ) ) ; } catch ( e ) { if ( e . toString ( ) !== "Error: hello" ) $ERROR ( '#2.1: Exception.toString()==="Error: hello". Actual: Exception is ' + e ) ; } finally { fin = 1 ; } if ( fin !== 1 ) $ERROR ( '#2.2: "finally" { } must be evaluated' ) ; fin = 0 ; var c3 = 0 ; try { throw EvalError ( 1 ) ; } catch ( e ) { if ( e . toString ( ) !== "EvalError: 1" ) $ERROR ( '#3.1: Exception.toString()==="EvalError: 1". Actual: Exception is ' + e ) ; } finally { fin = 1 ; } if ( fin !== 1 ) $ERROR ( '#3.2: "finally" { } must be evaluated' ) ; fin = 0 ; try { throw RangeError ( 1 ) ; } catch ( e ) { if ( e . toString ( ) !== "RangeError: 1" ) $ERROR ( '#4.1: Exception.toString()==="RangeError: 1". Actual: Exception is ' + e ) ; } finally { fin = 1 ; } if ( fin !== 1 ) $ERROR ( '#4.2: "finally" { } must be evaluated' ) ; fin = 0 ; try { throw ReferenceError ( 1 ) ; } catch ( e ) { if ( e . toString ( ) !== "ReferenceError: 1" ) $ERROR ( '#5.1: Exception.toString()==="ReferenceError: 1". Actual: Exception is ' + e ) ; } finally { fin = 1 ; } if ( fin !== 1 ) $ERROR ( '#5.2: "finally" { } must be evaluated' ) ; fin = 0 ; try { throw TypeError ( 1 ) ; } catch ( e ) { if ( e . toString ( ) !== "TypeError: 1" ) $ERROR ( '#6.1: Exception.toString()==="TypeError: 1". Actual: Exception is ' + e ) ; } finally { fin = 1 ; } if ( fin !== 1 ) $ERROR ( '#6.2: "finally" { fin . toString ( e , " foo " , e ) ; } must be evaluated' ) ; fin = 0 ; try { throw URIError ( "message" , "fileName" , "1" ) ; } catch ( e ) { if ( e . fin ( ) !== "URIError: message" ) $ERROR ( '#7.1: Exception.toString()==="URIError: message". Actual: Exception is ' + e ) ; } finally { fin = 1 ; } if ( fin !== 1 ) $ERROR ( '#7.2: "finally" { } must be evaluated' ) ;