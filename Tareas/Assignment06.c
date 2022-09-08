/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   06
 * STRING PERMUTATION
 *
 * Instructions:
 * Write a program to determine if a string is a permutation of another one.
 * A string S1 is said to be a permutation of another string S2 if the
 * counting of each different character in S1 is the same than string S2.
 * The strings to be analized are passed as command line arguments.
 * THE USE OF EXTRA LIBRARIES IS NOT ALLOWED.
 * MODIFY ONLY THE is_permutation FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include<stdio.h>

int is_permutation(char* str1, char* str2)
{
    /*
     * TODO:
     * Implement an algorithm to check if str1 is a permutation of str2
     * You can follow these steps:
     * Declare two 256-sized arrays of integers, arr1 and arr2, one for each string.
     * Initialize both arrays with zeros
     * Loop over str1 and count the total number of each different character.
     * (How many 'a', how many 'b' and so on). Store the character countings in arr1.
     * Loop over str2 and count the total number of each different character.
     * (How many 'a', how many 'b' and so on). Store the character countings in arr2.
     * If all values in arr1 and arr2 are equal, return 1. Otherwise, return 0.
     * MODIFY ONLY THIS FUNCTION. 
     */
}

int main(int argc, char** argv)
{
    if(argc < 3)
    {
        printf("Too few parameters! Two strings are required.\n");
        return -1;
    }

    printf("%d\n", is_permutation(argv[1], argv[2]));
    return 0;
}
