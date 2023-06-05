/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   02
 * DETERMINE IF A YEAR IS A LEAP YEAR.
 *
 * Instructions:
 * Write an algorithm to determine whether a given year
 * will be a leap year or not, according to the Gregorian Calendar.
 * Modify the function 'is_leap_year' such that it returns '1'
 * if the argument 'year' is a leap year, and '0', otherwise.
 * MODIFY ONLY THE SECTION MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION AND DON'T CHANGE THE FUNCTION NAMES.
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include <stdio.h>
#include <stdlib.h>

int is_leap_year(int year)
{
    /*
     * TODO:
     * Write the code to determine whether 'year' is a leap year or not.
     * Return '1' if it is leap year and '0' otherwise.
     * Check Wikipedia article about leap years for calculation according to
     * Gregorian Calendar. 
     * https://en.wikipedia.org/wiki/Leap_year
     */
    return year%4 == 0;
}

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        printf("Too few parameters.\n");
        return 0;
    }
    if(is_leap_year(atoi(argv[1])))
	printf("True");
    else
	printf("False");
    return 0;
}
