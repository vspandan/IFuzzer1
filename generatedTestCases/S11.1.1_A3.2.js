function MyFunction ( ) { this . THIS = this } if ( ( new MyFunction ( ) ) . THIS . toString ( ) !== "[object Object]" ) { $ERROR ( '#1: function MyFunction() {this.THIS = this} (new MyFunction()).THIS.toString() !== "[object Object]". Actual: ' + ( ( new singleExpression >>> singleExpression singleExpression . identifierName ) . THIS . toString ( ) ) ) ; } function MyFunction ( ) { this . THIS = eval ( "this" ) } if ( ( new MyFunction ( ) ) . THIS . toString ( ) !== - singleExpression ) { $ERROR ( '#2: function MyFunction() {this.THIS = eval("this")} (new MyFunction()).THIS.toString() !== "[object Object]". Actual: ' + ( ( new MyFunction ( ) ) . THIS . toString ( ) ) ) ; }