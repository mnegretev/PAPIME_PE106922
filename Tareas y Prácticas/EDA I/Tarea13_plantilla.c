/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   1 3
 * POSTFIX AND PREFIX NOTATION
 * 
 * Instructions:
 * Implement an algorithm to evaluate a POSTFIX or PREFIX arithmetic expression.
 * Expression is passed as command line arguments where each argument
 * is either an operarand or operator. Example:
 *    ./a.out 3.14 2.71 +
 * should print the output:
 *    5.85
 * The program recognizes the type of expression (prefix or postfix), thus, the command:
 *    ./a.out + 3.14 2.71
 * also prints the output:
 *    5.85
 * You can assume that the expression is syntactically correct.
 * Complete the stack implementation and use it to evaluate the expression.
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CAPACITY 10000

typedef struct _Stack
{
    float data[CAPACITY];
    int top;
}Stack;

Stack stack_initialize()
{
    Stack S;
    S.top = -1;
    return S;
}

int stack_is_full(Stack* S)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'is_full' operation. 
     */
    return S->top == CAPACITY - 1;
}

int stack_is_empty(Stack* S)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'is_empty' operation. 
     */
    return S->top == -1;
}

void stack_push(Stack* S, float k)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'push' operation. 
     */
    if(stack_is_full(S))
        exit(-1);
    S->top++;
    S->data[S->top] = k;
}

float stack_pop(Stack* S)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'pop' operation. 
     */
    if(stack_is_empty(S))
        exit(-1);
    float t = S->data[S->top];
    S->top--;
    return t;
}

float evaluate_postfix(char** expression, int argc)
{
    /*
     * TODO:
     * Write an algorithm to evaluate the postfix expression given as an array of strings.
     * The number of elements in the expression (number of strings in the array) is indicated by 'argc'.
     * You can use 'strcmp' and 'atof' to process the strings.
     * You can assume that expression is syntactically correct. 
     * To evaluate the expression you can use the following steps:
     *     Initialize a stack of floats.
     *     For all strings str in expression:
     *         If str is an operand, then push the value to the stack.
     *         If str is an operator, then
     *             pop operand2 from stack
     *             pop operand1 from stack
     *             Operate operand1 and operand2 and push the result to stack
     *     Pop from stack and return the result.
     */
    
    Stack S = stack_initialize();
    float op1,op2;
    for(int i=0; i<argc; i++)
    {
	if(strcmp(expression[i],"+") == 0)
	    stack_push(&S, stack_pop(&S) + stack_pop(&S));
        else if(strcmp(expression[i],"*") == 0)
	    stack_push(&S, stack_pop(&S) * stack_pop(&S));
        else if(strcmp(expression[i],"-") == 0)
	{
	    op2 = stack_pop(&S);
	    op1 = stack_pop(&S);
	    stack_push(&S, op1 - op2);
	}
        else if(strcmp(expression[i],"/") == 0)
	{
	    op2 = stack_pop(&S);
	    op1 = stack_pop(&S);
	    stack_push(&S, op1 / op2);
	}
	else
	    stack_push(&S, atof(expression[i]));
    }
    return stack_pop(&S);
}

float evaluate_prefix(char** expression, int argc)
{
    /*
     * TODO:
     * Write an algorithm to evaluate the prefix expression given as an array of strings.
     * The number of elements in the expression (number of strings in the array) is indicated by 'argc'.
     * You can use 'strcmp' and 'atof' to process the strings.
     * You can assume that expression is syntactically correct. 
     * To evaluate the expression you can use the following steps:
     *     Initialize a stack of floats.
     *     Loop over all strings str in expression in reverse order (from last to first):
     *         If str is an operand, then push the value to the stack.
     *         If str is an operator, then
     *             pop operand1 from stack
     *             pop operand2 from stack
     *             Operate operand1 and operand2 and push the result to stack
     *     Pop from stack and return the result.
     */
    
    Stack S = stack_initialize();
    float op1,op2;
    for(int i=argc-1; i>=0; i--)
    {
	if(strcmp(expression[i],"+") == 0)
	    stack_push(&S, stack_pop(&S) + stack_pop(&S));
        else if(strcmp(expression[i],"*") == 0)
	    stack_push(&S, stack_pop(&S) * stack_pop(&S));
        else if(strcmp(expression[i],"-") == 0)
	{
	    op1 = stack_pop(&S);
	    op2 = stack_pop(&S);
	    stack_push(&S, op1 - op2);
	}
        else if(strcmp(expression[i],"/") == 0)
	{
	    op1 = stack_pop(&S);
	    op2 = stack_pop(&S);
	    stack_push(&S, op1 / op2);
	}
	else
	    stack_push(&S, atof(expression[i]));
    }
    return stack_pop(&S);
}

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        printf("Type a postfix or prefix expression\n");
	return -1;
    }
    if(strcmp(argv[1],"+")==0 || strcmp(argv[1],"-")==0 || strcmp(argv[1],"*")==0 || strcmp(argv[1],"/")==0)
        printf("%f", evaluate_prefix(&argv[1], argc-1));
    else
        printf("%f", evaluate_postfix(&argv[1], argc-1));
    return 0;
}
