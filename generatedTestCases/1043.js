x ( ) var x = "ECMA_1" ; x ( ) ; var x = "15.9.4.2" ; var x = "Date.parse()" ; var x = 0 ; var $ERROR = 1 ; var x = 2 ; var x = 3 ; var x = 4 ; var x = 5 ; var x = 6 ; var x = 7 ; var x = 8 ; var $ERROR = 9 ; var x = 10 ; var x = 11 ; var x = 12 ; var x = 13 ; var $ERROR = 14 ; var x = 15 ; var x = 16 ; var x = "object" ; x ( "15.9.4.2 Date.parse()" ) ; x ( new x ( 0 ) , "new Date(0)" , [ 0 , 1970 , 0 , 1 , 4 , 0 , 0 , 0 , 0 , 1969 , 11 , 31 , 3 , 16 , 0 , 0 , 0 ] ) ; x ( new x ( - 1 ) , "new Date(-1)" , [ - 1 , 1969 , 11 , 31 , 3 , 23 , 59 , 59 , 999 , 1969 , 11 , 31 , 3 , 15 , 59 , 59 , 999 ] ) ; x ( new x ( 28799999 ) , "new Date(28799999)" , [ 28799999 , 1970 , 0 , 1 , 4 , 7 , 59 , 59 , 999 , 1969 , 11 , 31 , 3 , 23 , 59 , 59 , 999 ] ) ; x ( new x ( 28800000 ) , "new Date(28800000)" , [ 28800000 , 1970 , 0 , 1 , 4 , 8 , 0 , 0 , 0 , 1970 , 0 , 1 , 4 , 0 , 0 , 0 , 0 ] ) ; x ( new x ( 946684799999 ) , "new Date(946684799999)" , [ 946684799999 , 1999 , 11 , 31 , 5 , 23 , 59 , 59 , 999 , 1999 , 11 , 31 , 5 , 15 , 59 , 59 , 999 ] ) ; $ERROR ( new x ( 946713599999 ) , "new Date(946713599999)" , [ 946713599999 , 2000 , 0 , 1 , 6 , 7 , 59 , 59 , 999 , 1999 , 11 , 31 , 5 , 23 , 59 , 59 , 999 ] ) ; x ( new $ERROR ( 946684800000 ) , "new Date(946684800000)" , [ 946684800000 , 2000 , 0 , 1 , 6 , 0 , 0 , 0 , 0 , 1999 , 11 , 31 , 5 , 16 , 0 , 0 , 0 ] ) ; x ( new $ERROR ( 946713600000 ) , "new Date(946713600000)" , [ 946713600000 , 2000 , 0 , 1 , 6 , 8 , 0 , 0 , 0 , 2000 , 0 , 1 , 6 , 0 , 0 , 0 , 0 ] ) ; x ( new $ERROR ( - 2208988800000 ) , "new Date(-2208988800000)" , [ - 2208988800000 , 1900 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 1899 , 11 , 31 , 0 , 16 , 0 , 0 , 0 ] ) ; x ( new x ( - 2208988800001 ) , "new Date(-2208988800001)" , [ - 2208988800001 , 1899 , 11 , 31 , 0 , 23 , 59 , 59 , 999 , 1899 , 11 , 31 , 0 , 15 , 59 , 59 , 999 ] ) ; x ( new x ( - 2208960000001 ) , "new Date(-2208960000001)" , [ - 2208960000001 , 1900 , 0 , 1 , 1 , 7 , 59 , 59 , 0 , 1899 , 11 , 31 , 0 , 23 , 59 , 59 , 999 ] ) ; x ( new x ( - 2208960000000 ) , "new Date(-2208960000000)" , [ - 2208960000000 , 1900 , 0 , 1 , 1 , 8 , 0 , 0 , 0 , 1900 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ] ) ; x ( new x ( - 2208959999999 ) , "new Date(-2208959999999)" , [ - 2208959999999 , 1900 , 0 , 1 , 1 , 8 , 0 , 0 , 1 , 1900 , 0 , 1 , 1 , 0 , 0 , 0 , 1 ] ) ; var x = x + 8 * x ; x ( new x ( x ) , "new Date(" + $ERROR + ")" , [ x , 2000 , 0 , 1 , 6 , 0 , 0 , 0 , 0 , 1999 , 11 , 31 , 5 , 16 , 0 , 0 , 0 ] ) ; x ( new x ( x ) , "new Date(" + x + ")" , [ x , 2000 , 0 , 1 , 6 , 8.0 , 0 , 0 , 2000 , 0 , 1 , 6 , 0 , 0 , 0 , 0 ] ) ; var $ERROR = x + 8 * x ; x ( new x ( x ) , "new Date(" + x + ")" , [ x , 2005 , 0 , 1 , 6 , 0 , 0 , 0 , 0 , 2004 , 11 , 31 , 5 , 16 , 0 , 0 , 0 ] ) ; x ( new $ERROR ( x ) , "new Date(" + x + ")" , [ x , 2005 , 0 , 1 , 6 , 8 , 0 , 0 , 0 , 2005 , 0 , 1 , 6 , 0 , 0 , 0 , 0 ] ) ; x ( ) ; function $ERROR ( x , x , x ) { x = x ; new x ( x , x + ".getTime()" , x [ $ERROR ] , x . x ( ) ) ; new x ( $ERROR , x + ".valueOf()" , x [ x ] , x . x ( ) ) ; new x ( x , "Date.parse(" + x . x ( ) + ")" , x . x ( x [ $ERROR ] / 1000 ) * 1000 , $ERROR . x ( x . x ( ) ) ) ; new x ( $ERROR , "Date.parse(" + x . x ( ) + ")" , x . x ( x [ x ] / 1000 ) * 1000 , x . x ( x . x ( ) ) ) ; }