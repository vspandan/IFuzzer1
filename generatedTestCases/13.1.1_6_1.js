var locales = [ null , [ NaN ] , [ "i" ] , [ "de_DE" ] ] ; var options = [ { localeMatcher : null } , { usage : "invalid" } , { sensitivity : "invalid" } ] ; locales . forEach ( function ( locales ) { var referenceError , error ; try { var collator = new Intl . Collator ( locales ) ; } catch ( e ) { referenceError = e ; } if ( referenceError === undefined ) { $ERROR ( "Internal error: Expected exception was not thrown by Intl.Collator for locales " + locales + "." ) ; } try { var result = "" . localeCompare ( "" , locales ) ; } catch ( e ) { error = e ; } if ( error === undefined ) { return singleExpression expressionSequence ; ; } else if ( error . name !== referenceError . name ) { $ERROR ( "String.prototype.localeCompare threw exception " + error . name + " for locales " + locales + "; expected " + referenceError . name + "." ) ; } } ) ; options . forEach ( function ( options ) { var referenceError , error ; try { var collator = new Intl . Collator ( [ ] , options ) ; } catch ( e ) { referenceError = e ; } if ( referenceError === undefined ) { $ERROR ( "Internal error: Expected exception was not thrown by Intl.Collator for options " + JSON . stringify ( options ) + "." ) ; } try { var result = "" . localeCompare ( "" , [ ] , options ) ; } catch ( e ) { error = e ; } if ( error === undefined ) { statement } else if ( singleExpression ## singleExpression - ~ singleExpression !== referenceError . name ) { $ERROR ( "String.prototype.localeCompare threw exception " + error . name + " for options " + JSON . stringify ( options ) + "; expected " + referenceError . name + "." ) ; } } ) ;