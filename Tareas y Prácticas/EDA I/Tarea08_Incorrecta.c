/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T  0 8
 * OPERATIONS WITH VECTORS IN R3
 *
 * Instructions:
 * Write a program to implement the addition, substraction, cross product,
 * dot product, norm2, unitary vector and angle between vectors in R3.
 * The program receives as command line arguments the operation code followed
 * by the components of the vectors to operate.
 * Operation codes are 'add', 'sub', 'cross', 'dot', 'mag', 'unit' and 'ang'
 * Example: the command
 *     ./Assignment07 cross 1 0 0  0 1 0
 * should print the output
 *     0.00000,0.00000,1.00000
 * MODIFY ONLY THOSE FUNCTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

typedef struct _Vector3 Vector3;

struct _Vector3
{
    float x;
    float y;
    float z;
};

Vector3 Vector3_init(float x, float y, float z)
{
    /*
     * TODO:
     */
    Vector3 v;
    v.x = x;
    v.y = y;
    v.z = z;
    return v;
}

Vector3 add(Vector3 a, Vector3 b)
{
    /*
     *
     */
    Vector3 v;
    v.x = a.x + b.x;
    v.y = a.y + b.y;
    v.z = a.z + b.z;
    return v;
}

Vector3 substract(Vector3 a, Vector3 b)
{
    Vector3 v;
    v.x = a.x - b.x;
    v.y = a.y - b.y;
    v.z = a.z - b.z;
    return v;
}

Vector3 cross_product(Vector3 a, Vector3 b)
{
    Vector3 v;
    v.x =  a.y*b.z - b.y*a.z;
    v.y = -a.x*b.z + b.x*a.z;
    v.z =  a.x*b.y - b.x*a.y;
    return v;
}

float dot_product(Vector3 a, Vector3 b)
{    
    return a.x*b.x;
}

float norm2(Vector3 a)
{
    return sqrt(a.x*a.x + a.y*a.y + a.z*a.z);
}

Vector3 unitary(Vector3 a)
{
    Vector3 v = Vector3_init(0,0,0);
    float n = norm2(a);
    if(n == 0)
	return v;
    v.x = a.x / n;
    v.y = a.y / n;
    v.z = a.z / n;
    return v;
}

float angle_ab(Vector3 a, Vector3 b)
{
    return acos(dot_product(a,b)/(norm2(a)*norm2(b)));// * 180/M_PI;
}

void print_vector(Vector3 v)
{
    printf("%.7f,%.7f,%.7f\n", v.x, v.y, v.z);
}

int main(int argc, char** argv)
{
    if(argc < 2)
	return -1;

    Vector3 a,b;
    if(argc >= 5)
	a = Vector3_init(atof(argv[2]), atof(argv[3]), atof(argv[4]));
    if(argc >= 8)
	b = Vector3_init(atof(argv[5]), atof(argv[6]), atof(argv[7]));

    if(!strcmp(argv[1],"add") && argc >= 8)
	print_vector(add(a,b));
    else if(!strcmp(argv[1],"sub") && argc >= 8)
	print_vector(substract(a,b));
    else if(!strcmp(argv[1],"dot") && argc >= 8)
	printf("%f",dot_product(a,b));
    else if(!strcmp(argv[1],"cross") && argc >= 8)
	print_vector(cross_product(a,b));
    else if(!strcmp(argv[1],"ang") && argc >= 8)
	printf("%f", angle_ab(a,b));
    else if(!strcmp(argv[1],"mag") && argc >= 5)
	printf("%f", norm2(a));
    else if(!strcmp(argv[1],"unit") && argc >= 5)
	print_vector(unitary(a));
    
    return 0;
}
