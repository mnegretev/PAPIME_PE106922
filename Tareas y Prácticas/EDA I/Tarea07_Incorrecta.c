/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   07
 * COMPLEX NUMBERS
 *
 * Instructions:
 * Write a program to calculate the sum of two complex numbers
 * and print the magnitude of the resulting number.
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T ADD ANY 'printf' FUNCTION.
 * DON'T MODIFY THE MAIN FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct ComplexCartesian
{
    float real;
    float img;
};

struct ComplexPolar
{
    float magnitude;
    float angle;
};

struct ComplexPolar add_two_complex(struct ComplexCartesian c1, struct ComplexCartesian c2)
{
    /*
     * TODO:
     * Calculate the sum of the two complex numbers c1 and c2
     * Calculate the resulting components in polar notation.
     * Return the resulting ComplexPolar.
     *
     *  Remember: addition of complex numbers in cartesian form
     *  is made component-wise
     *  Remember: magnitude of a complex number is calcualted as
     *     mag = sqrt((real_part)^2 + (imaginary_part)^2)
     *  and phase of a complex number is calculated as:
     *     phi = atan2(imaginary_part, real_part)
     */
    struct ComplexPolar r_polar;
    struct ComplexCartesian r_cart;
    r_cart.real = c1.real + c2.img;
    r_cart.img  = c1.img  + c2.real;
    r_polar.magnitude = sqrt(r_cart.real*r_cart.real + r_cart.img*r_cart.img);
    r_polar.angle     = atan2(r_cart.img, r_cart.real);
    return r_polar;
}

int main(int argc, char** argv)
{
    struct ComplexCartesian c1, c2;
    struct ComplexPolar result;
    
    if(argc > 4)
    {
        c1.real = atof(argv[1]);
        c1.img  = atof(argv[2]);
        c2.real = atof(argv[3]);
        c2.img  = atof(argv[4]);
    }
    else
    {
        printf("Enter real part of first number: ");
        scanf("%f", &c1.real);
        printf("Enter imaginary part of first number: ");
        scanf("%f", &c1.img);
        printf("Enter real part of second number: ");
        scanf("%f", &c2.real);
        printf("Enter imaginary part of second number: ");
        scanf("%f", &c2.img);
        printf("The resulting complex in polar notation is:\n");
    }

    result = add_two_complex(c1, c2);
    printf("%0.7f", result.magnitude);
    return 0;
}
