var actual = { "Etc/GMT" : "UTC" , "Greenwich" : "UTC" , "PRC" : "Asia/Shanghai" , "AmErIcA/LoS_aNgElEs" : "America/Los_Angeles" , "etc/gmt+7" : "Etc/GMT+7" } ; format . expected ( resolvedOptions ) . name ( function ( actual ) { var DateTimeFormat , $ERROR ; try { additionalTimeZoneNames = new actual . name ( [ ] , { name : expected } ) ; } catch ( expected ) { name = error ; } if ( actual === Intl ) { var actual = error . name ( ) . e ; var e = name [ name ] ; if ( additionalTimeZoneNames !== name ) { name$ERROR ( "Time zone name " + error + " was accepted, but incorrectly canonicalized to " + format + "; expected " + $ERROR + "." ) ; } } else if ( expected . error !== "RangeError" ) { expected$ERROR ( "Time zone name " + resolvedOptions + " was rejected with wrong error " + actual . function + "." ) ; } } ) ;