#include <stdio.h>
#include <stdlib.h>
#include "hash_tables.h" 

/**
 * hash_table_delete - Delete a hash table and its contents.
 * @ht: The hash table to delete.
 */
void hash_table_delete(hash_table_t *ht)
{
    if (ht == NULL)
        return;

    for (unsigned long int i = 0; i < ht->size; i++)
    {
        hash_node_t *current = ht->array[i];

        while (current != NULL)
        {
            hash_node_t *temp = current;
            current = current->next;

            free(temp->key);
            free(temp->value);
            free(temp);
        }
    }

    free(ht->array);

    free(ht);
}