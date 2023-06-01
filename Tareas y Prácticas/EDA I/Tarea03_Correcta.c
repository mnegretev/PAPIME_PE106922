/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   03
 * LCD AND GCD
 *
 * Author: Student full name
 *
 * Instructions:
 * Write a program to calculate the Least Common Multiple and the
 * Greatest Common Divisor of two positive integers.
 * 
 * THE USE OF EXTRA LIBRARIES IS NOT ALLOWED
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T ADD ANY PRINTF FUNCTION
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 */

#include<stdio.h>
#include<stdlib.h>

int calculate_gcd(int a, int b)
{
    /*
     * TODO:
     * Write the code to calculate the Greatest Common Divisor of 'a' and 'b'.
     * Function must return the GCD.
     * Hint: You can use the Euclidean algorithm:
     * https://en.wikipedia.org/wiki/Euclidean_algorithm
     */
    if(a==b)
        return a;
    if (a > b)
        return calculate_gcd(a-b, b);
    return calculate_gcd(a, b-a);
}

int calculate_lcm(int a, int b)
{
    /*
     * TODO:
     * Write the code to calculate the Least Common Multiple of 'a' and 'b'.
     * Function must return the LCM.
     * Hint: Check Wikipedia's article about LCM using the GCD.
     * https://en.wikipedia.org/wiki/Least_common_multiple
     */
    int gcd = calculate_gcd(a, b);
    return a*b/gcd;
}

int main(int argc, char** argv)
{
    if(argc < 3)
    {
        printf("Too few parameters! Two integers are required.\n");
        return -1;
    }

    int a  = atoi(argv[1]);
    int b  = atoi(argv[2]);
    int gcd = calculate_gcd(a,b);
    int lcm = calculate_lcm(a,b);
    printf("%d_%d", lcm, gcd);
    return 0;
}
