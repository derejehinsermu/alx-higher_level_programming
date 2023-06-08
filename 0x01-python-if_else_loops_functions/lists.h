#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @data: integer data
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int data;
    struct listint_s *next;
}
