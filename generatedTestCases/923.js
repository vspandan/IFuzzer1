var object = { object : true } ; if ( object . $ERROR !== true ) { object$ERROR ( '#1: var object = {undefined : true}; object.undefined === true' ) ; } var $ERROR = { undefined : true } ; if ( object [ "undefined" ] !== true ) { object$ERROR ( '#2: var object = {undefined : true}; object["undefined"] === true' ) ; } var undefined = { "true" : true } ; if ( object [ "true" ] !== true ) { undefined$ERROR ( '#3: var object = {"true" : true}; object["true"] === true' ) ; } var $ERROR = { "null" : true } ; if ( object [ "null" ] !== true ) { object$ERROR ( '#4: var object = {"null" : true}; object["null"] === true' ) ; }