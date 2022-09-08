/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   0 9
 * ROTATION AND TRANSLATION OF 2D POLYGONS
 *
 * Instructions:
 * Write the code to initialize, rotate and translate a polygon with 'n' vertices. 
 * 
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>

typedef struct _Vector2
{
    float x;
    float y;
}Vector2;

typedef struct _Polygon2D
{
    int n;              //Number of vertices
    Vector2* vertices;  //Pointer to the array of Vector2 where vertices coordinates will be stored. 
}Polygon2D;

Vector2* calculate_vertices(int n, float apotheme)
{
    Vector2* vertices = (Vector2*)malloc(n*sizeof(Vector2));
    /*
     * TODO:
     * Calculate the coordinates XY of the 'n' vertices of a regular polygon with the
     * given apotheme and assuming it is zero-centered and no-rotated.
     * Store the coordinates in 'vertices' (an array of Vector2).
     */
    return vertices;
}

Polygon2D* initialize_polygon2D(int n, float apotheme)
{
    Polygon2D* polygon = (Polygon2D*)malloc(sizeof(Polygon2D));
    /*
     * TODO:
     * Allocate memory to store a Polygon2D.
     * Initialize the corresponding variables:
     * Assign 'n' to the polygon's 'n'.
     * Assign polygon's 'vertices' to the result of calling the calculate_vertices function.
     */
    return polygon;
}

void rotate_polygon(Polygon2D* polygon, float theta)
{
    /*
     * TODO:
     * Rotate all vertices of 'polygon' an angle theta (in radians) on Z-axis 
     * Rotation is calcuated as:
     *  new_x = x*cos(theta) - y*sin(theta)
     *  new_y = x*sin(theta) + y*cos(theta)
     * Store the new coordinates of the vertices in the same variable.
     * Declare as many variables as you need. 
     */
}

void translate_polygon(Polygon2D* polygon, float dx, float dy)
{
    /*
     * TODO:
     * Translate by (dx, dy) all vertices of 'polygon'
     * Translation is performed only by adding 'dx' and 'dy' to the corresponding variables.
     * Store the new coordinates of the vertices in the same variables.
     * Declare as many variables as you need. 
     */
}

void print_polygon(Polygon2D* polygon)
{
    printf("Vertices:\n");
    int i;
    for(i=0; i < polygon->n; i++)
        printf("%+0.4f  %+0.4f\n", polygon->vertices[i].x, polygon->vertices[i].y);
}

int main(int argc, char** argv)
{
    if(argc < 4)
    {
        printf("Too few parameters! Usage:\n");
        printf("./Practice03 center_x center_y rotation\n");
	return -1;
    }
    srand(time(NULL));
    float dx = atof(argv[1]);
    float dy = atof(argv[2]);
    float r  = atof(argv[3]);
    int   n  =  rand()%8 + 3;
    float a  = (rand()%1000)/100.0 + 1.0;
    
    Polygon2D* pol = initialize_polygon2D(n, a);
    printf("Original polygon:\n");
    print_polygon(pol);
    rotate_polygon(pol, r);
    translate_polygon(pol, dx, dy);
    printf("Transformed polygon:\n");
    print_polygon(pol);
    free(pol->vertices);
    free(pol);
    return 0;    
}
