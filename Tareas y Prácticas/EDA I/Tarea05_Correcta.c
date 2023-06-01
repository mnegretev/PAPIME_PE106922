/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   04
 * LEXICOGRAPHIC STRING COMPARISON
 *
 * Instructions:
 * Write a program to compare two strings.
 * The program receives as command line arguments the two strings to be compared
 * and returns the integer corresponding to the comparison result. 
 * The comparison to be implemented must be the same than the strcmp function
 * THE USE OF THE STRCMP FUNCTION INCLUDED IN THE STRING LIBRARY IS NOT ALLOWED
 * MODIFY ONLY THE string_compare FUNCTION
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include<stdio.h>

int string_compare(char* str1, char* str2)
{
    /*
     * TODO:
     * Implement the string comparison function.
     * Only modify this part of the code. Don't use any extra library.
     * IMPORTANT:
     * Function must return 0 if str1 and str2 are equal
     * If strings are different, function must return c1-c2
     * where c1 and c2 are the first different characters in str1 and str2 respectively.
     */
    for(;*str1==*str2 && *str1; str1++, str2++);
    return *str1 - *str2;
}

int main(int argc, char** argv)
{
    if(argc < 3)
    {
        printf("Too few parameters! Two strings are required.\n");
        return -1;
    }

    printf("%d", string_compare(argv[1], argv[2]));
    return 0;
}
