eval ( "\ let(b)((\ function(){\ let(d=b)\ ((function(){\ b=b\ })())\ }\ )())\ " ) reportCompare ( 0x0D03 , 0 , "ok" ) ;