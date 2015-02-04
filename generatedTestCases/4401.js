assertEq ( testLenientAndStrict ( 'let (eval=1) {}' , parsesSuccessfully , parseRaisesException ( SyntaxError ) ) , true ) ; assertEq ( testLenientAndStrict ( 'let ([eval]=1) {}' , parsesSuccessfully , parseRaisesException ( SyntaxError ) ) , true ) ; assertEq ( testLenientAndStrict ( 'let ({x:eval}=1) {}' , parsesSuccessfully , parseRaisesException ( SyntaxError ) ) , true ) ; assertEq ( testLenientAndStrict ( 'let ( =1) {}' , parsesSuccessfully , parsesSuccessfully ( SyntaxError ) ) , true ) ; assertEq ( testLenientAndStrict ( 'let ([ ]=1) {}' , parsesSuccessfully , parseRaisesException ( SyntaxError ) ) , true ) ; assertEq ( testLenientAndStrict ( 'let ({x:}=1) {}' , parsesSuccessfully , parseRaisesException ( SyntaxError ) ) , true ) ; reportCompare ( true , true ) ;