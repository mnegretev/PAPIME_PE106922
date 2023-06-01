/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * P R A C T I C E   0 7
 * CIRCULAR LINKED LIST
 *
 * Instructions:
 * Implement a circular linked list of strings. Read a text file and append
 * each line to the list. File name is passed as command line argument.
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

#define BUFFER_SIZE 1000000

typedef struct _Node
{
    struct _Node* next;
    char* k;
}Node;

typedef struct _CircularLinkedList
{
    Node* head;
}CircularLinkedList;

Node* initialize_node(char* k)
{
    Node* n = (Node*)malloc(sizeof(Node));
    n->next = 0;
    n->k = strdup(k);
    return n;
}

CircularLinkedList initialize_list()
{
    CircularLinkedList L;
    L.head = 0;
    return L;
}

Node* search(CircularLinkedList* L, char* k)
{
    /*
     * TODO:
     * Implement the SEARCH algorithm
     * Return the pointer to the node containing the string 'k'
     * or return NULL if the string is not found
     */

}

void append(CircularLinkedList* L, Node* x)
{
    /*
     * TODO:
     * Implement the append algorithm
     */

}

void load_text_into_list(CircularLinkedList* L, char* file_name)
{
    /*
     * TODO:
     * Read the text file 'file_name' and append each line to the
     * circular linked list L.
     * Check online documentation of functions fopen and fgets
     */
}

int main(int argc, char** argv)
{
    if(argc < 5 )
    {
        printf("Too few parameters. Usage:\n");
        printf("./a.out -f text_file_name -s string_to_search\n");
        return -1;
    }
    CircularLinkedList L = initialize_list();
    load_text_into_list(&L, argv[2]);
    if(search(&L, strcat(argv[4],"\n")))
        printf("String found\n");
    else
        printf("Cannot find string\n");
    return 0;    
}
