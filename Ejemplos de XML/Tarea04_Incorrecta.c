/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   04
 * FIBONACCI SEQUENCE
 *
 * Instructions:
 * Write an algorithm to generate the first 'n' Fibonacci numbers.
 * Consider [0,1] as the first two numbers.
 * MODIFY ONLY THE SECTION MARKED WITH THE 'TODO' COMMENT
 */

#include<stdio.h>
#include<stdlib.h>

void print_numbers(int* numbers, int n)
{
    int i=0;
    for( i=0; i< n; i++)
        printf("%d_", numbers[i]);
}

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        printf("Too few parameters. At least an integer is required.\n");
        return 0;
    }
    int n = atoi(argv[1]);
    if( n < 2)
    {
        printf("Invalid argument.\n");
        printf("'n' must be greater or equal than 2.\n");
        return -1;
    }

    /*
     * TODO:
     * Declare an array of 'n' integers.
     * Calculate the first 'n' Fibonacci numbers and store them in the declared array.
     * Consider [0,1] as the first two numbers.
     * Assume n >= 2. 
     * Call the 'print_numbers' function passing as arguments
     * the name of the declared array and 'n'. 
     * You can declare as many variables as you need. 
     */
    int numbers[n];
    numbers[0] = 0;
    numbers[1] = 1;
    for(int i=2; i < n; i++)
        numbers[i] = numbers[i] + numbers[i-1];
    print_numbers(numbers, n);
    
    return 0;
}
