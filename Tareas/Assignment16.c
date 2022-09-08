/*
 * DATA STRUCTURES AND ALGORITHMS I
 * FI-UNAM-2022-2
 * A S S I G N M E N T   1 6
 * PLAYLIST USING CIRCULAR DOUBLE LINKED LIST
 * 
 * Instructions:
 * Implement the code to insert, append, delete and search strings in a circular double linked list.
 * Using these functions, the program should resemble the behavior of a playlist
 * 
 * DON'T ADD ANY LIBRARY (APPART FROM THE ONES ALREADY INCLUDED)
 * DON'T CHANGE THE MAIN FUNCTION
 * MODIFY ONLY THE SECTIONS MARKED WITH THE 'TODO' COMMENT
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Node
{
    char* k;
    struct _Node* next;
    struct _Node* prev;
    
}Node;

typedef struct _CircularDoubleLinkedList
{
    Node* head;
}CircularDoubleLinkedList;

CircularDoubleLinkedList circular_double_linked_list_initialize()
{
    CircularDoubleLinkedList L;
    L.head = 0;
    return L;
}

Node* node_initialize(char* data)
{
    /*
     * TODO
     * Allocate memory to store a Node
     * Allocate memory in node->data to store the string 'data'
     * Copy the string 'data' to node->data
     * Set next and prev pointers to null.
     * Return the pointer to the allocated node. 
     */
    Node* n = (Node*)malloc(sizeof(Node));
    int len = strlen(data);
    n->k    = (char*)malloc(len+1);
    memcpy(n->k, data, len);
    *(n->k + len) = 0;
    n->next = 0;
    n->prev = 0;
    return n;
}

Node* circular_double_linked_list_search(CircularDoubleLinkedList* L, char* k)
{
    /*
     * TODO:
     * Implement search in a circular double linked list of strings.
     * Return a pointer to the node containing the key 'k'.
     * Return NULL if value 'k' is not found in the list.
     * You can use the strcmp function to compare strings.
     */
}

void circular_double_linked_list_insert(CircularDoubleLinkedList* L, char* k)
{
    Node* x = node_initialize(k);
    /*
     * TODO:
     * Write the code to insert node x in the circular double linked list L;
     */
}

void circular_double_linked_list_append(CircularDoubleLinkedList* L, char* k)
{
    Node* x = node_initialize(k);
    /*
     * TODO:
     * Write the code to append node x to the circular double linked list L;
     */
}

Node* circular_double_linked_list_delete(CircularDoubleLinkedList* L, char* k)
{
    /*
     * TODO:
     * Implement deletion of the node containing the string 'k'
     * If there is not a node containing string 'k', don't do anything.
     * You can use the strcmp function to compare strings
     * Return the pointer to the deleted node
     */
}

void print_playlist(CircularDoubleLinkedList* L, Node* current)
{
    Node* x = L->head;
    if(x == 0)
    {
        printf("\nYOUR PLAYLIST IS EMPTY:\n");
        return;
    }
    printf("\nYOUR PLAYLIST:\n");
    
    while(x != 0)
    {
        if(x == current)
            printf("-> %s\n", x->k);
        else
            printf("   %s\n", x->k);
        if((x = x->next) == L->head)
            x = 0;
    }
    printf("\n");
}

void print_help()
{
    printf("Valid commands:\n");
    printf("  prev         : moves current title to the next one\n");
    printf("  next         : moves current title to the previous one\n");
    printf("  insert title : inserts the given title\n");
    printf("  append title : appends the given title\n");
    printf("  delete title : deletes the given title\n");
    printf("  ctrl+c       : terminates execution\n");
    printf("\n");
}

int main(int argc, char** argv)
{
    CircularDoubleLinkedList L = circular_double_linked_list_initialize();
    circular_double_linked_list_insert(&L, "BohemianRapsody");
    circular_double_linked_list_insert(&L, "Imagine");
    circular_double_linked_list_insert(&L, "AnotherBrickInTheWall");
    Node* current = L.head;
    print_playlist(&L, current);

    char cmd[1000];
    int valid_cmd = 0;
    printf("Type command (or type 'help'): ");
    scanf("%s", cmd);
    while(strcmp(cmd, "exit") != 0)
    {
        valid_cmd = 1;
        if(strcmp(cmd, "prev") == 0)
            current = current == 0 ? 0 : current->prev;
        else if(strcmp(cmd, "next") == 0)
            current = current == 0 ? 0 : current->next;
        else if(strcmp(cmd, "insert") == 0)
        {
            scanf("%s", cmd);
            circular_double_linked_list_insert(&L, cmd);
        }
        else if(strcmp(cmd, "append") == 0)
        {
            scanf("%s", cmd);
            circular_double_linked_list_append(&L, cmd);
        }
        else if(strcmp(cmd, "delete") == 0)
        {
            scanf("%s", cmd);
            if(circular_double_linked_list_delete(&L, cmd) == current)
                current = current->next;
            if(L.head == 0) current = 0;
        }
        else if(strcmp(cmd, "help") == 0)
        {
            valid_cmd = 0;
            print_help();
        }
        else
        {
            printf("Invalid command\n");
            print_help();
            valid_cmd = 0;
        }

        if(current == 0)
            current = L.head;
        
        if(valid_cmd)
            print_playlist(&L, current);
        printf("Type command (or type 'help'): ");
        scanf("%s", cmd);
    }
    
    
    return 0;
}
