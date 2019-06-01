#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h> 
#include <math.h> 
#include <ctype.h>
#include <termios.h>
#include <unistd.h>
#include <ncurses.h>
#include <sys/stat.h>
#include <form.h>

int main()
{
    char s[1000];
    int i,a;
    float x=0.0,y=0.0,z=0.0,q=0.0,p=0.0;


    while (strcmp("q",s) != 0)
    {
        x=0.0;
        y=0.0;
        z=0.0;
        printf("Enter a string: ");
        scanf("%s", s);
 
        for(i = 0; s[i] != '\0'; ++i)
        {
            a = s[i];
            p = a/127.0*2*3.1415926;
            q = (127-a)/127.0*2*3.1415925;
            y = y + sin(p)*cos(q)/(i+1);
            x = x + sin(p)*sin(q)/(i+1);
            z = z + cos(p)/(i+1);
            printf ("%d %c %d \n",i,s[i],s[i]);
        }
        printf ("%d %c %d p=%.3f q=%.3f x=%.3f y=%.3f z=%.3f \n",i,s[i],s[i],p,q,x,y,z);
        printf("Length of string: %d\n", i);

    }
}
