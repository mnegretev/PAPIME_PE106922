/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * P R A C T I C E   0 8
 * PRIORITY QUEUE IMPLEMENTED WITH HEAP
 *
 * Instructions:
 * Solve the problem of the K smallest elements in an array using a
 * priority queue implemented with a min heap. 
 *
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT.
 * DON'T MODIFY THE MAIN FUNCTION.
 * DON'T ADD ANY 'printf' FUNCTION.
 *
 * This work was supported by UNAM-DGAPA under grant PAPIME-PE106922
 *
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define CAPACITY 1000000

typedef struct _MinHeap
{
    int data[CAPACITY];
    int size;
}MinHeap;

MinHeap initialize_min_heap()
{
    MinHeap h;
    h.size = 0;
    return h;
}

int parent(int i) { return (i-1)/2; }
  
int left(int i) { return (2*i + 1); }

int right(int i) { return (2*i + 2); }

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void minheapify(MinHeap* H, int i)
{
    /*
     * TODO:
     * Check if subtree with root at index 'i' holds the heap property
     * If not, heapify subtree and check recursively if all subtrees are heapified.
     */
}

void insert(MinHeap* H, int k)
{
    /*
     * TODO:
     * Insert value 'k' at the end of the array
     * Check the heap property between added value and its parent, if it is not hold
     * then, swap values.
     * Keep checking until the root element
     */
}

int pop(MinHeap* H)
{
    /*
     * TODO:
     * Implement the pop function:
     * Store in temporal var the first element of the array (root value)
     * Store last element of the array at the first position
     * Decrease heap size
     * Heapify the resulting array starting at index 0.
     */
}

void print_heap(MinHeap* H)
{
    printf("Heap: ");
    for(int i=0; i< H->size; i++)
        printf("%d ", H->data[i]);
    printf("\n");
}

int main(int argc, char** argv)
{
    if(argc < 5 )
    {
        printf("Too few parameters. Usage:\n");
        printf("./a.out -k k_value -a int1 int2 ...\n");
        return -1;
    }
    int k = atoi(argv[2]);
    MinHeap H = initialize_min_heap();
    for(int i=4; i < argc; i++)
        insert(&H, atoi(argv[i]));
    print_heap(&H);
    printf("Smallest k-values: ");
    for(int i=0; i< k; i++)
        printf("%d ", pop(&H));
    printf("\n");
    return 0;    
}
