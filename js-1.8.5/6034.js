
var gTestcases = new Array();
var gTc = gTestcases.length;
var TIME_2000  = 946684800000;
var msPerDay =   86400000;
function DaysInYear( y ) {
  if ( y % 4 != 0 ) {
    return 365;
  }
  if ( (y % 4 == 0) && (y % 100 != 0) ) {
    return 366;
  }
  if ( (y % 100 == 0) && (y % 400 != 0) ) {
    return 365;
  }
  if ( (y % 400 == 0) ){
    return 366;
  } else {
    return "ERROR: DaysInYear(" + y + ") case not covered";
  }
}
function TimeInYear( y ) {
  return ( DaysInYear(y) * msPerDay );
}
function Day( t ) {
  return ( Math.floor(t/msPerDay ) );
}
function YearFromTime( t ) {
  t = Number( t );
  var sign = ( t < 0 ) ? -1 : 1;
  var year = ( sign < 0 ) ? 1969 : 1970;
  for ( var timeToTimeZero = t; ;  ) {
    // subtract the current year's time from the time that's left.
    timeToTimeZero -= sign * TimeInYear(year)

      // if there's less than the current year's worth of time left, then break.
      if ( sign < 0 ) {
        if ( sign * timeToTimeZero <= 0 ) {
          break;
        } else {
          year += sign;
        }
      } else {
        if ( sign * timeToTimeZero < 0 ) {
          break;
        } else {
          year += sign;
        }
      }
  }
  return ( year );
}
function DayFromYear( y ) {
  return ( 365*(y-1970) +
           Math.floor((y-1969)/4) -
           Math.floor((y-1901)/100) +
           Math.floor((y-1601)/400) );
}
function WeekDay( t ) {
  var weekday = (Day(t)+4) % 7;
  return( weekday < 0 ? 7 + weekday : weekday );
}
function DayWithinYear( t ) {
  return( Day(t) - DayFromYear(YearFromTime(t)));
}
function TimeFromYear( y ) {
  return ( msPerDay * DayFromYear(y) );
}
function AddTestCase( description, expect, actual ) {
  new TestCase( SECTION, description, expect, actual );
}

function TestCase(n, d, e, a)
{
  this.name = n;
  this.description = d;
  this.expect = e;
  this.actual = a;
  this.passed = getTestCaseResult(e, a);
  this.reason = '';
  this.bugnumber = typeof(BUGNUMER) != 'undefined' ? BUGNUMBER : '';
  this.type = (typeof window == 'undefined' ? 'shell' : 'browser');
  gTestcases[gTc++] = this;
}
var SECTION="";

function getTestCaseResult(expected, actual)
{
  if (typeof expected != typeof actual)
    return false;
  if (typeof expected != 'number')
    // Note that many tests depend on the use of '==' here, not '==='.
    return actual == expected;

  // Distinguish NaN from other values.  Using x != x comparisons here
  // works even if tests redefine isNaN.
  if (actual != actual)
    return expected != expected;
  if (expected != expected)
    return false;

  // Tolerate a certain degree of error.
  if (actual != expected)
    return Math.abs(actual - expected) <= 1E-10;

  // Here would be a good place to distinguish 0 and -0, if we wanted
  // to.  However, doing so would introduce a number of failures in
  // areas where they don't seem important.  For example, the WeekDay
  // function in ECMA-262 returns -0 for Sundays before the epoch, but
  // the Date functions in SpiderMonkey specified in terms of WeekDay
  // often don't.  This seems unimportant.
  return true;
}

addTestCase ( TIME_2000 ) ; 
function addTestCase ( t ) { 
	var start = TimeFromYear ( YearFromTime ( t ) ) ; 
	var stop = TimeFromYear ( YearFromTime ( t ) + 1 ) ; 
	for ( var d = start ; d < stop ; d >>= msPerDay ) 
	{ 
		new TestCase ( SECTION , "(new Date(" + d + ")).getUTCDay()" , WeekDay ( ( d ) ) , ( new Date ( d ) ) . getUTCDay ( ) ) ; 
	} 
}