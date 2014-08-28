#include<stdlib.h>
#include<stdio.h>
int main()
{
FILE *fp=fopen("temp","r");
char ch;
FILE *fpw=fopen("temp1","w");
while( (ch=fgetc(fp))!=EOF)

{
if(ch>=97&&ch<=122)
   ch=ch-32;
fprintf (fpw,"%c", ch);
}
return 0;
}
