/*
 * ESTRUCTURAS DE DATOS Y ALGORITMOS I
 * FACULTAD DE INGENIERIA, UNAM, 2021-1
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

#include <stdlib.h>

#define CAPACITY 1000

typedef struct _Queue
{
    char data[CAPACITY];
    int head;
    int tail;
    int size;
}Queue;

Queue queue_initialize()
{
    Queue Q;
    Q.head = 0;
    Q.tail = -1;
    Q.size = 0;
    return Q;
}

int queue_is_full(Queue* Q)
{
    return Q->size == CAPACITY;
}

int queue_is_empty(Queue* Q)
{
    return Q->size == 0;
}

void queue_enqueue(Queue* Q, char k)
{
    if(queue_is_full(Q))
        exit(-1);
    Q->tail = (Q->tail + 1) % CAPACITY;
    Q->data[Q->tail] = k;
    Q->size++;
}

char queue_dequeue(Queue* Q)
{
    if(queue_is_empty(Q))
        exit(-1);
    char t = Q->data[Q->head];
    Q->head = (Q->head + 1) % CAPACITY;
    Q->size--;
    return t;
}

char queue_tail(Queue* Q)
{
    return Q->data[Q->tail];
}

char queue_head(Queue* Q)
{
    return Q->data[Q->head];
}

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
    return S->top == CAPACITY - 1;
}

int stack_is_empty(Stack* S)
{
    return S->top == -1;
}

void stack_push(Stack* S, char k)
{
    if(stack_is_full(S))
        exit(-1);
    S->top++;
    S->data[S->top] = k;
}

char stack_pop(Stack* S)
{
    if(stack_is_empty(S))
        exit(-1);
    char t = S->data[S->top];
    S->top--;
    return t;
}

char stack_peek(Stack* S)
{
    return S->data[S->top];
}

char stack_bottom(Stack* S)
{
    return S->data[0];
}

Stack S1;
Stack S2;
Queue Q1;
Queue Q2;

void enqueue(int k)
{
    /*
     * TODO:
     * Implement the ENQUEUE function using only the stacks S1 and S2.
     */
    stack_push(&S1, k);
}

int dequeue()
{
    /*
     * TODO:
     * Implement the DEQUEUE function using only the stacks S1 and S2.
     */
    while(!stack_is_empty(&S1))
	stack_push(&S2, stack_pop(&S1));
    int x = stack_pop(&S2);
    while(!stack_is_empty(&S2))
	stack_push(&S1, stack_pop(&S2));
    return x;
}

void push(int k)
{
    /*
     * TODO:
     * Implement the PUSH function using only the queues Q1 and Q2.
     */
    queue_enqueue(&Q1, k);
}

int pop()
{
    /*
     * TODO:
     * Implement the POP function using only the queues Q1 and Q2
     */
    int x = queue_dequeue(&Q1);
    while(!queue_is_empty(&Q1))
    {
	queue_enqueue(&Q2, x);
	x = queue_dequeue(&Q1);
    }
    while(!queue_is_empty(&Q2))
	queue_enqueue(&Q1, queue_dequeue(&Q2));
    return x;
}

int main(int argc, char** argv)
{
    if(argc < 3)
	return -1;
    
    S1 = stack_initialize();
    S2 = stack_initialize();
    Q1 = queue_initialize();
    Q2 = queue_initialize();

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

    if(!queue_is_empty(&Q1))
	printf("Peek: %d ", queue_tail(&Q1));
    if(!stack_is_empty(&S1))
    {
	printf("Tail: %d ", stack_peek(&S1));
	printf("Head: %d", stack_bottom(&S1));
    }
    return 0;
}
