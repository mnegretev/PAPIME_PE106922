/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * P R A C T I C E   0 6
 * DOUBLE ENDED QUEUE
 *
 * Instructions:
 * Implement a Double Ended Queue to solve sliding window maximum problem.
 * Array data and size of subarray are passed as command line arguments:
 * ./a.out -k k_value -n n1 n2 n3 n4 ...
 * 
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define CAPACITY 10000

typedef struct _Deque
{
    int data[CAPACITY];
    int size;
    int front;
    int rear;
}Deque;

Deque* initialize_deque()
{
    Deque* Q = (Deque*)malloc(sizeof(Deque));
    Q->size  = 0;
    Q->front = 0;
    Q->rear  = -1;
    return Q;
}

int is_full(Deque* Q)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'is_full' operation. 
     */
}

int is_empty(Deque* Q)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'is_empty' operation. 
     */
}

int deque_front(Deque* Q)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'front' operation.
     * Remember 'front' is a query operation, not a modifying one.
     */
}

int deque_back(Deque* Q)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'back' operation.
     * Remember 'back' is a query operation, not a modifying one.
     */
}

void push_front(Deque* Q, int k)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'push_front' operation.
     */
}

void push_back(Deque* Q, int k)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'push_back' operation.
     */
}

int pop_front(Deque* Q)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'pop_front' operation.
     */
}

int pop_back(Deque* Q)
{
    /*
     * TODO:
     * Write the code necessary to implement the 'pop_back' operation.
     */
}

Deque* sliding_window_maximum(int* data, int k, int n)
{
    Deque* Q = initialize_deque();
    Deque* maxima = initialize_deque();

    /*
     * TODO:
     * Write the code necessary to solve the sliding window maximum problem.
     * You can follow these steps:
     *
     * FOR i=[0,k):
     *     WHILE not is_empty(Q) AND data[i] >= data[back(Q)]:
     *         pop_back(Q)
     *     push_back(Q)
     * FOR i=[k,n):
     *     push_back(maxima, data[front(Q)])
     *     WHILE not is_empty(Q) AND front(Q) <= i-k:
     *         pop_front(Q)
     *     WHILE not is_empty(Q) AND data[i] >= data[back(Q)])
     *         pop_back(Q);
     *     push_back(Q, i);
     * push_back(maxima, data[front(Q)]);
     * return maxima;
     *
     */
    return maxima;
}

void print_deque(Deque* Q)
{
    for(int i=Q->front; i!=((Q->rear+1)%CAPACITY); i=(i+1)%CAPACITY)
        printf("%d ",Q->data[i]);
    printf("\n");
}

int main(int argc, char** argv)
{
    if(argc < 5 )
    {
        printf("Too few parameters. Usage:\n");
        printf("./a.out -k k_value -n number1 number2 ...");
        return -1;
    }
    int k = atoi(argv[2]);
    int n = argc - 4;
    int data[n];
    for(int i=4; i < argc; i++)
        data[i-4] = atoi(argv[i]);
    print_deque(sliding_window_maximum(data, k, n));
    return 0;    
}
