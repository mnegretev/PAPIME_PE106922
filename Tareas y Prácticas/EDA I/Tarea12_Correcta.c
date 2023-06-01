/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   1 2
 * BALANCED PARENTHESIS
 * 
 * Instructions:
 * Implement an algorithm to check whether an expression has balanced
 * parentheses, brackets and braces. 
 * You can assume that the expression only has numbers, operators and the mentioned symbols.
 * Complete the stack implementation and use it to check the expression.
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CAPACITY 10000

typedef struct _Stack
{
    char data[CAPACITY];
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

void stack_push(Stack* S, char k)
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

char stack_pop(Stack* S)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'pop' operation. 
     */
    if(stack_is_empty(S))
        exit(-1);
    char t = S->data[S->top];
    S->top--;
    return t;
}

int check_balance(char* expression)
{
    /*
     * TODO:
     * Write an algorithm to check if the given expression has a balanced number of
     * parenthesis (), brackets [] and braces {}.
     * Return 1 if the expression is balanced, and 0, otherwise.
     * You can use the following algorithm:
     *    Initialize a stack of chars.
     *    For all char c in the string:
     *        If c is a starting char ([{, then push it to stack.
     *        If c is a closing char )]}, then pop from stack.
     *            If the poped char matches c, then continue checking, otherwise, return 0.
     *    If the stack if empty, return 1, otherwise, return 0.
     */
    Stack S = stack_initialize();
    for(;*expression; expression++)
        if(*expression == '(' || *expression == '[' || *expression == '{')
            stack_push(&S, *expression);
        else if (*expression == ')' && (stack_is_empty(&S) || stack_pop(&S) != '(')) return 0;
        else if (*expression == ']' && (stack_is_empty(&S) || stack_pop(&S) != '[')) return 0;
        else if (*expression == '}' && (stack_is_empty(&S) || stack_pop(&S) != '{')) return 0;
    return stack_is_empty(&S);
}

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        printf("A least one string is required\n");
	return -1;
    }
    printf("%d", check_balance(argv[1]));
    return 0;
}
