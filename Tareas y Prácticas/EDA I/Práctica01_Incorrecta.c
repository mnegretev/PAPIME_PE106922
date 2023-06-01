/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * P R A C T I C E   1
 * MATRIX TRANSPOSE
 *
 * Instructions:
 * Calculate the transpose of a matrix using ONLY ONE-DIMENSIONAL ARRAYS, i.e., 
 * you CANNOT USE the double bracket [][] notation.
 * Matrix order is passed as command line arguments, e.g:
 * ./Practice01 3 5 indicates a 3x5 matrix.
 * The program must fill the matrix with random integers in the interval [-99,99].
 * The program must print both the original and the transposed matrix.
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(int argc, char** argv)
{
    if(argc < 3)
    {
        printf("Too few parameters! At least two integers are required.\n");
        return -1;
    }
    /*
     * The variables 'rows' and 'cols' contain the order of the matrix to be transposed
     */
    int rows = atoi(argv[1]);
    int cols = atoi(argv[2]);
    if(rows < 1 || cols < 1)
    {
        printf("Invalid columns or rows.");
        return -1;
    }

    /*
     * First, declare two one-dimensional arrays with enough space to store the
     * elements of both, the original and the transposed matrix:
     */

    int matrix_original[rows*cols];    
    int matrix_transposed[rows*cols];  

    /*
     * TODO:
     * Fill the first matrix with random integers in the interval [-99,99]
     * Hint: use the functions rand(), srand() and time().
     */


    /*
     * TODO:
     * Transpose the original matrix and store the resulting elements in
     * the 'matrix_transposed' array.
     * You can declare as many variables as you need.
     */
    
    /*
     * Don't modify the following lines. 
     */
    printf("The original matrix is:");
    for(i = 0; i < rows*cols; i++)
    {
	if(i%cols == 0) printf("\n");
	printf("%d\t", matrix_original[i]);
    }
    printf("\nThe transposed matrix is:");
    for(i = 0; i < rows*cols; i++)
    {
	if(i%rows == 0) printf("\n");
	printf("%d\t", matrix_transposed[i]);
    }
    printf("\n");
    return 0;
}
