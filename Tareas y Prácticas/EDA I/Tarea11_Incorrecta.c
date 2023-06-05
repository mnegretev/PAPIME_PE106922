/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   1 1
 * FUNCTION POINTERS FOR NUMERICAL INTEGRATION
 *
 * Instructions:
 * Write the code to implement a numerical integrator using the trapezoidal rule. 
 * The integrator must be implemented using function pointers, such that it can calculate
 * the definite integral of any real function (satisfying integrability conditions).
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

double integrate_by_trapezoidal_rule(double a, double b, double step, double (*f)(double))
{
    /*
     * TODO:
     * Implement an integrator using the trapezoidal rule.
     * Function to be integrated is given by the function pointer *f
     * Return the integration result.
     */
    double result = 0;
    for(; a<b; a+=step)
        result += step*((*f)(a) + (*f)(a+step));
    return result;
}

double my_function(double x)
{
    return cos(x)*cos(x) + exp(0.5*x);
}

int main(int argc, char** argv)
{
    if(argc < 5)
    {
        printf("Too few parameters! Usage:\n");
        printf("./a.out function lower_limit upper_limit delta\n");
	return -1;
    }
    double lower_limit = atof(argv[2]);
    double upper_limit = atof(argv[3]);
    double step        = atof(argv[4]);
    if (step <= 0)
    {
        printf("Integration step must be greater than zero.\n");
        return -1;
    }

    if(strcmp(argv[1],"sin")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, sin));
    else if(strcmp(argv[1],"cos")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, cos));
    else if(strcmp(argv[1],"tan")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, tan));
    else if(strcmp(argv[1],"sinh")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, sinh));
    else if(strcmp(argv[1],"cosh")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, cosh));
    else if(strcmp(argv[1],"tanh")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, tanh));
    else if(strcmp(argv[1],"asin")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, asin));
    else if(strcmp(argv[1],"acos")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, acos));
    else if(strcmp(argv[1],"atan")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, atan));
    else if(strcmp(argv[1],"exp")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, exp));
    else if(strcmp(argv[1],"log")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, log));
    else if(strcmp(argv[1],"sqrt")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, sqrt));
    else if(strcmp(argv[1],"user")==0)
        printf("%0.4lf", integrate_by_trapezoidal_rule(lower_limit, upper_limit, step, my_function));
    else
        printf("Program can only integrate trascendental functions.\n");
    return 0;    
}
