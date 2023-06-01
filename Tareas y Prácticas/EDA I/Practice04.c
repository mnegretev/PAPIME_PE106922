/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * P R A C T I C E   04
 * MATRIX MULTIPLICATION
 *
 * Instructions:
 * Multiply three matrices whose orders are given by a0Xa1, a1Xa2, a2Xa3
 * The three matrices must be filled with random integers in [-99,99]
 * The program must print the three generated matrices and the result of the product.
 * Values a0, a1, a2 and a3 are passed as command line arguments.
 *
 * IT IS MANDATORY TO USE THE 'malloc' FUNCTION TO ALLOCATE ALL THE SPACE NEEDED
 * TO STORE THE MATRICES ELEMENTS.
 * THE USE OF THE BRACKET NOTATION [] IS NOT ALLOWED. STUDENTS MUST USE POINTERS INSTEAD.
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int* fill_matrix(int rows, int cols)
{
    /*
     * TODO:
     * Allocate enough memory to store a rows x cols matrix of integers.
     * Fill the matrix with random integers in [-99,99]
     * Return the pointer to the allocated space.
     */
}

int* multiply_matrices(int* M1, int* M2, int* M3, int a0, int a1, int a2, int a3)
{
    /*
     * TODO:
     * Allocate enough memory to store the resulting matrix (M = M1xM2xM3 with resulting order of a0xa3)
     * Write the code to perform the product M1xM2xM3
     * You can declare as many variables as you need.
     * You can allocate as many space as you need.
     * Assume matrices M1, M2 and M3 are already allocated and filled with valid elements. 
     * Return the pointer to the resulting matrix. 
     */
}

void print_matrix(int* m, int rows, int cols)
{
    int i,j;
    for(i = 0; i < rows; i++)
    {
	for(j = 0; j < cols; j++)
	    printf("%d\t", m[i*cols + j]);
        printf("\n");
    }
}

int main(int argc, char** argv)
{
    if(argc < 5)
    {
        printf("Too few parameters! Usage: Practice04 a1 a2 a3 a4\n");
	return -1;
    }
    int a0 = atoi(*(argv + 1));
    int a1 = atoi(*(argv + 2));
    int a2 = atoi(*(argv + 3));
    int a3 = atoi(*(argv + 4));
    if(a0 <= 0 || a1 <= 0 || a2 <= 0 || a3 <= 0)
    {
        printf("Matrix orders must be positive integers\n");
	return -1;
    }

    srand(time(NULL));
    int* m1 = fill_matrix(a0, a1);
    int* m2 = fill_matrix(a1, a2);
    int* m3 = fill_matrix(a2, a3);
    int* mr = multiply_matrices(m1, m2, m3, a0, a1, a2, a3);

    printf("Matrix one   is:\n");
    print_matrix(m1, a0, a1);
    printf("Matrix two   is:\n");
    print_matrix(m2, a1, a2);
    printf("Matrix three is:\n");
    print_matrix(m3, a2, a3);
    printf("Resulting matrix is:\n");
    print_matrix(mr, a0, a3);

    free(m1);
    free(m2);
    free(m3);
    free(mr);

    return 0;
}
