/*
 * ESTRUCTURAS DE DATOS Y ALGORITMOS I
 * FACULTAD DE INGENIERÍA, UNAM, 2021-1
 * P R A C T I C E   05
 * Instructions:
 * Implement a Stack using two queues and a Queue using two stacks. 
 * Don't modify the Stack.h nor Queue.h files.
 * To manipulate the data structures, only the following functions are allowed:
 *    stack_int_push
 *    stack_int_pop
 *    stack_int_is_full
 *    stack_int_is_empty
 *    queue_int_enqueue
 *    queue_int_dequeue
 *    queue_int_is_full
 *    queue_int_is_empty
 * These functions are already implemented in the Stack.h and Queue.h files.
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Stack.h"
#include "Queue.h"

StackInt S1;
StackInt S2;
QueueInt Q1;
QueueInt Q2;

void enqueue(int k)
{
    /*
     * TODO:
     * Implement the ENQUEUE function using only the stacks S1 and S2.
     */
    stack_int_push(&S1, k);
}

int dequeue()
{
    /*
     * TODO:
     * Implement the DEQUEUE function using only the stacks S1 and S2.
     */
    while(!stack_int_is_empty(&S1))
	stack_int_push(&S2, stack_int_pop(&S1));
    int x = stack_int_pop(&S2);
    while(!stack_int_is_empty(&S2))
	stack_int_push(&S1, stack_int_pop(&S2));
    return x;
}

void push(int k)
{
    /*
     * TODO:
     * Implement the PUSH function using only the queues Q1 and Q2.
     */
    queue_int_enqueue(&Q1, k);
}

int pop()
{
    /*
     * TODO:
     * Implement the POP function using only the queues Q1 and Q2
     */
    int x = queue_int_dequeue(&Q1);
    while(!queue_int_is_empty(&Q1))
    {
	queue_int_enqueue(&Q2, x);
	x = queue_int_dequeue(&Q1);
    }
    while(!queue_int_is_empty(&Q2))
	queue_int_enqueue(&Q1, queue_int_dequeue(&Q2));
    return x;
}

int main(int argc, char** argv)
{
    if(argc < 3)
	return -1;
    
    S1 = stack_int_initialize();
    S2 = stack_int_initialize();
    Q1 = queue_int_initialize();
    Q2 = queue_int_initialize();

    int i=0;
    int value;
    while(++i < argc)
    {
	if(!strcmp(argv[i], "push"))
	    push(atoi(argv[++i]));
	else if(!strcmp(argv[i], "pop"))
	    pop();
	else if(!strcmp(argv[i], "enq"))
	    enqueue(atoi(argv[++i]));
	else if(!strcmp(argv[i], "deq"))
	    dequeue();
    }

    if(!queue_int_is_empty(&Q1))
	printf("Peek: %d\n", queue_int_tail(&Q1));
    if(!stack_int_is_empty(&S1))
    {
	printf("Tail: %d\n", stack_int_peek(&S1));
	printf("Head: %d\n", stack_int_bottom(&S1));
    }
    return 0;
}
