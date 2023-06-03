/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T  1 0
 * POSITIONAL NOTATION
 *
 * Instructions:
 * Write a program to convert a given number in decimal to a differente base. 
 * Decimal number and desired base are passed as a command line arguments.
 * Example: The command:
 *    ./a.out 54 13
 * (convert 54 to base 13) should print the output:
 *    42
 * Use of libraries different to the ones already included is not allowed. 
 * ONLY MODIFY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include<stdio.h>
#include<math.h>
#include<stdlib.h>

char* decimal_to_base(int x, int b)
{
    /*
     * TODO:
     * Convert the positive integer 'x' to a positional system with base 'b'.
     * Return a string containing the characters that represent the converted number.
     * Example: if x=3144 and b=17 this function should return the string "AEG".
     * Base 'b' will always be in the range[2,20], thus, the symbols you can use are 0123456789ABCDEFGHIJ
     * Important: the function returns a string, not an integer.
     * Remember: strings are arrays of chars ended with a null character.
     * Mandatory: the string must contain only the mininum number of digits necessary
     * to represent number 'x' in base 'b'.
     */
    char symbols[20] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J'};
    int n = floor(log(x)/log(b))+1;
    char* str = (char*)malloc(n+1);
    str[n] = 0;
    for(;x;n--, x/=b)
        str[n-1] = symbols[x%b];
    return str;
}

int main(int argc, char** argv)
{
    if(argc < 3)
    {
        printf("Too few parameters! Usage:\n");
        printf("./a.out dec_number base\n");
	return -1;
    }
    int x = atoi(argv[1]);
    int b = atoi(argv[2]);
    if( x <= 0)
    {
        printf("Decimal number must be x > 0\n");
        return -1;
    }
    if( b < 2 || b > 20)
    {
        printf("Desired base must be in the range [2,20]\n");
        return -1;
    }
    printf("%s", decimal_to_base(x,b));
    return 0;    
}
