/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * P R A C T I C E   0 3
 * POLYGONS IN 2D
 *
 * Instructions:
 * Write a program to calculate the coordinates XY of the set of vertices of a regular 2D polygon
 * when the number of vertices 'n', apotheme, center coordinates and angle of rotation are given.
 *
 * The program receives as command line arguments the number of vertices,
 * apotheme, center_x, center_y and rotation.
 * ONLY MODIFY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include<stdio.h>
#include<math.h>
#include<stdlib.h>

typedef struct _Vector2
{
    /*
     * TODO:
     * Declare the necessary members to represent a vector in R2
     */
    float x;
    float y;
}Vector2;

Vector2* calculate_vertices(int n, float apotheme, float center_x, float center_y, float rotation)
{
    Vector2* vertices = (Vector2*)malloc(n*sizeof(Vector2));

    /*
     * TODO:
     * Calculate the coordinates XY of the 'n' vertices of a regular polygon with the
     * given apotheme, center coordinates and rotation angle.
     * Store the coordinates in 'vertices' (an array of Vector2)
     */

    return vertices;
}

void print_vertices_xy(Vector2* vertices, int n)
{
    int i;
    for(i=0; i<n; i++)
        printf("%+0.4f  %+0.4f\n", vertices[i].x, vertices[i].y);
}

int main(int argc, char** argv)
{
    if(argc < 6)
    {
        printf("Too few parameters! Usage:\n");
        printf("./a.out n apotheme center_x center_y rotation\n");
	return -1;
    }
    int   n  = atoi(argv[1]);
    float a  = atof(argv[2]);
    float cx = atof(argv[3]);
    float cy = atof(argv[4]);
    float r  = atof(argv[5]);
    if(n < 3)
    {
        printf("Invalid number of vertices. \n");
        return -1;
    }
    if(a <= 0)
    {
        printf("Invalid apotheme.\n");
        return -1;
    }

    Vector2* vertices = calculate_vertices(n, a, cx, cy, r);
    print_vertices_xy(vertices, n);
    free(vertices);
    
    return 0;    
}
