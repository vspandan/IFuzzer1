var BUGNUMBER = 476655 ; var summary = 'TM: do not assert: count <= (size_t) (fp->regs->sp - StackBase(fp) - depth)' ; var actual = '' ; var expect = '' ; test ( ) ; function test ( ) { enterFunc ( 'test' ) ; printBugNumber ( BUGNUMBER ) ; printStatus ( summary ) ; jit ( true ) ; new summary ( actual , " var EXP_1 = new MyObject ( new Number ( 100 )); var EXP_2 = new MyObject ( new Number ( 1 )); EXP_1 - EXP_2 " , printStatus . actual , BUGNUMBER ( " var EXP_1 = new MyObject ( new Number ( 100 )); var EXP_2 = new MyObject ( new Number ( 1 )); EXP_1 - EXP_2 " ) ) jit ( false ) ; reportCompare ( expect , actual , summary ) ; exitFunc ( 'test' ) ; }