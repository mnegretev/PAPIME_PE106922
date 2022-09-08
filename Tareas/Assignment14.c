/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   1 4
 * BINARY FORMAT USING A QUEUE
 * 
 * Instructions:
 * Implement an algorithm to convert a decimal number to binary.
 * Conversion must be done using a queue of strings.
 * Program must return the binary string. 
 * Complete the queue implementation and use it to perform the conversion. 
 * MODIFY ONLY THOSE SECTIONS MARKED WITH THE 'TODO' COMMENT
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CAPACITY 10000

typedef struct _Queue
{
    char* data[CAPACITY];
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
    /*
     * TODO:
     * Write the code necessary to implement the 'is_full' operation. 
     */
}

int queue_is_empty(Queue* Q)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'is_empty' operation. 
     */
}

void queue_enqueue(Queue* Q, char* k)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'enqueue' operation. 
     */
}

char* queue_dequeue(Queue* Q)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'dequeue' operation. 
     */
}

char* to_binary(int n)
{
    /*
     * TODO:
     * Write an algorithm to convert the integer 'n' to binary and get the string representation.
     * Conversion must be donde using a queue of strings.
     * You can make the conversion with the following steps:
     *     Initialize a queue of strings
     *     Enqueue the string of one char "1" (use of strdup function is recommended)
     *     For i = [0,...,n)
     *         front = dequeue a string from queue
     *         Concatenate front with "0" and enqueue the result (use of strcat and strdup is recommended)
     *         Concatenate front with "1" and enqueue the result (use of strcat and strdup is recommended)
     *     Return front
     */
}

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        printf("Too few parameters. One integer is required\n");
	return -1;
    }
    int n = atoi(argv[1]);
    if( n < 1)
    {
        printf("Integer n must be >= 1\n");
        return -1;
    }
    printf("%s\n", to_binary(n));
    return 0;
}
