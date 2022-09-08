/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   01
 * HELLO WORLD
 *
 * Instructions:
 * Write a program to print 'hello world' as many times as
 * indicated by the integer passed as command line parameters.
 * Example: the command
 *     ./a.out 3
 * should print the output:
 *     Hello world!
 *     Hello world!
 *     Hello world!
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 */

#include<stdio.h>
#include<stdlib.h>
#define MAX_LENGTH 10000

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        printf("Too few parameters! An integer is required.\n");
        return -1;
    }

    int n = atoi(argv[1]);
    if(n <= 0)
    {
        printf("Invalid value. Plase enter n>=1.\n");
        return -1;
    }
    
    /*
     * TODO
     * Write the code neccesary to print 'n' times the string
     * "Hello world!\n"
     * Print EXACTLY this string (without the double quotes, of course).
     * Declare as many variables as you need. 
     * DON'T MODIFY THE REST OF THE CODE
     * 
     */
        
    return 0;
}
