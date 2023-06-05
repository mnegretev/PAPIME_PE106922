/*
 * ESTRUCTURA DE DATOS Y ALGORITMOS I
 * FACULTAD DE INGENIERIA, UNAM, 2020-1
 * A S S I G N M E N T   16
 * URLIFY A STRING 
 *
 * Instructions:
 * URLify a string (which is defined inside a struct),
 * i.e., replace all spaces by the string "%20", e.g:
 * If the input string is "hello world!", the output string should be "hello%20world!"
 * The program must receive the input string as a command line parameter
 * and print only the resulting string, e.g., the command:
 *     ./a.out "hello world!"
 * should print the output
 *     hello%20world
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T ADD ANY LIBRARY
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include<stdio.h>
#include<stdlib.h>

char* URLify(char* input_string)
{
    /*
     * TODO
     * Calculate the length of 'input_string'
     * Allocate enough memory to replace every space by the string '%20'
     * Replace every space by the string '%20'
     * Return the pointer to the URLified string
     */
    int str_len = 0;
    int spaces  = 0;
    while(*(input_string + str_len))
    {
        str_len++;
        spaces += *(input_string + str_len) == ' ' ? 1 : 0;
    }
    
    char* output_string = (char*)malloc(str_len + spaces*3);  

    int idx = 0;
    int aux = 0;
    for(idx=0, aux=0; input_string[idx]; idx++, aux++)
        if(input_string[idx] == 0x20)
        {
            output_string[aux    ] = '%';
            output_string[aux + 1] = '2';
            output_string[aux + 2] = '0';
        }
        else
            output_string[aux] = input_string[idx];
    
    return output_string;
}

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        printf("Too few parameters! At least one string is required.\n");
        return -1;
    }

    char* output_string = URLify(argv[1]);
    printf("%s\n", output_string);
    free(output_string);
    return 0;
}
