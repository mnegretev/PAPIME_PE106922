/*
 * ESTRUCTURAS DE DATOS Y ALGORITMOS I
 * FI-UNAM-2022-2
 * P R A C T I C E   2
 * CAESAR CIPHER
 *
 * Instructions:
 * Write a program to implement an extended Caesar Cipher
 * The program receives as command line arguments, the number
 * of positions to shift, and the string to be ciphered.
 * Only the characters in a-z and A-Z must be shifted and
 * all the other chars must remain the same.
 
 * ONLY MODIFY THE FUNCTION caesar_cipher
 * USE OF POINTERS IS MANDATORY
 * THE ARRAY NOTATION [] IS NOT ALLOWED. USE POINTERS INSTEAD.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include <stdio.h>
#include <stdlib.h>

char* caesar_cipher(char* str, int n)
{
    /*
     * TODO:
     * Implement the Caesar Cipher.
     * The parameter 'n' indicates the number of positions the characters will be shifted.
     * Only shift those chars in the intervals a-z and A-Z
     * The function must return the pointer to the ciphered string.
     * ONLY MODIFY THIS FUNCTION
     * USE OF POINTERS IS MANDATORY        
     * THE ARRAY NOTATION [] IS NOT ALLOWED!!!
     */
}

int main(int argc, char** argv)
{
    int i, n;
    if(argc < 3)
    {
        printf("Too few parameters! Usage:\n");
        printf("./Practice_02 n string\n");
	return -1;
    }
    n = atoi(argv[1]);
    for(i=2; i < argc; i++)
        printf("%s\n", caesar_cipher(*(argv + i), n));
    
    return 0;    
}
