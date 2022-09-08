/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * P R A C T I C E   0 5
 * STACKS AND QUEUES
 *
 * Instructions:
 * Implement a Stack using two queues and a Queue using two stacks. 
 * Don't modify the Stack.h nor Queue.h files.
 * To manipulate the data structures, only the following functions are allowed:
 *    stack_push
 *    stack_pop
 *    stack_is_full
 *    stack_is_empty
 *    queue_enqueue
 *    queue_dequeue
 *    queue_is_full
 *    queue_is_empty
 * These functions are already implemented in the Stack.h and Queue.h files.
 * Use the Stack and Queue implemented here to process a string in the following way:
 *    If an * is found, delete an element (either pop or dequeue)
 *    Otherwise, add the char (either push or enqueue).
 * The program receives as command line arguments the structure to use and the string to process.
 * Example:
 *    ./a.out stack abc**def**gh    should give the output:
 *    adgh
 *    ./a.out queue abc**def**gh    should give the output:
      efgh
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Stack.h"
#include "Queue.h"

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
}

int dequeue()
{
    /*
     * TODO:
     * Implement the DEQUEUE function using only the stacks S1 and S2.
     */
}

void push(int k)
{
    /*
     * TODO:
     * Implement the PUSH function using only the queues Q1 and Q2.
     */
}

int pop()
{
    /*
     * TODO:
     * Implement the POP function using only the queues Q1 and Q2
     */
}


void process_string_with_stack(char* str)
{
    /*
     * TODO:
     * Loop over the string and do the following:
     * If a char c is an '*', pop an element (use the previous pop() function)
     * Otherwise, push the char c (use the previous push() function)
     */
}

void process_string_with_queue(char* str)
{
    /*
     * TODO:
     * Loop over the string and do the following:
     * If a char c is an '*', dequeue an element (use the previous dequeue() function)
     * Otherwise, enqueue the char c (use the previous enqueue() function)
     */
}

void print_queue()
{
    for(int i=0; i<=S1.top; i++)
        printf("%c",S1.data[i]);
    printf("\n");
}

void print_stack()
{
    for(int i=Q1.head; i!=((Q1.tail+1)%CAPACITY); i=(i+1)%CAPACITY)
        printf("%c",Q1.data[i]);
    printf("\n");
}
 
int main(int argc, char** argv)
{
    if(argc < 3 )
    {
        printf("Too few parameters. Usage:\n");
        printf("./a.out stack|queue string\n");
        return -1;
    }
    S1 = stack_initialize();
    S2 = stack_initialize();
    Q1 = queue_initialize();
    Q2 = queue_initialize();
    if(!strcmp(argv[1], "stack"))
    {
        process_string_with_stack(argv[2]);
        print_stack();
    }
    else if(!strcmp(argv[1], "queue"))
    {
        process_string_with_queue(argv[2]);
        print_queue();
    }
    else printf("Invalid command\n");
    
    return 0;    
}
