/*
 * ESTRUCTURA DE DATOS Y ALGORITMOS I
 * FACULTAD DE INGENIERIA, UNAM, 2019-1
 * A S S I G N M E N T   09
 * Instructions:
 * Write a program to determine if a string is one-edit away of another string..
 * A string S1 is said to be a one-edit of another string S2 if ONLY ONE of the following conditions is held:
 * a) S1 is obtained from S2 by chaging one character
 * b) S1 is obtained from S2 by deleting one character
 * c) S1 is obtained from S2 by inserting one character
 * Examples:
 * bear -> beer  = true
 * bear -> bar   = true
 * bear -> beard = true
 * bear -> ber   = false
 * The program must receive as command line arguments the two strings two be analized.
 * The output of the program must be 1, if S1 is one-edit away of S2, and 0, otherwise.
 * THE USE OF EXTRA LIBRARIES IS NOT ALLOWED
 * MODIFY ONLY THE is_one_edit FUNCTION AND THE string_length FUNCTION
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include<stdio.h>

int string_length(char* str)
{
    char* aux = str;
    while(*str)
	str++;
    return str - aux;
}

int is_one_edit_replace(char* str1, char* str2)
{
    int found_difference = 0;
    for(; *str1; str1++, str2++)
	if(*str1 != *str2)
	{
	    if(found_difference)
		return 0;
	    found_difference++;
	}
    return found_difference;
}

int is_one_edit_insert(char* str1, char* str2)
{
    int found_difference = 0;
    while(*str1 && *str2)
    {
	if(*str1 != *str2)
	{
	    if(found_difference)
		return 0;
	    found_difference = 1;
	    str2++;
	}
	else
	{
	    str1++;
	    str2++;
	}
    }
    return 1;
}

int is_one_edit(char* str1, char* str2)
{
    int len1 = string_length(str1);
    int len2 = string_length(str2);
    if(len1 == len2)
	return is_one_edit_replace(str1, str2);
    else if(len1 + 1 == len2)
	return is_one_edit_insert(str1, str2);
    else if(len1 - 1 == len2)
	return is_one_edit_insert(str2, str1);
    else
	return 0;
}

int main(int argc, char** argv)
{
    if(argc < 3)
    {
        printf("Too few parameters! Two strings are required.\n");
        return -1;
    }

    if(is_one_edit(argv[1], argv[2]))
        printf("True");
    else
        printf("False");
    return 0;
}
