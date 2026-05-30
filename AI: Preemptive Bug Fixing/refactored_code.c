#include <stdlib.h>

/**
 * struct list_s - Singly linked list node structure
 * @n: Integer data payload
 * @next: Pointer to the next node
 */
struct list_s {
    int n;
    struct list_s *next;
};
typedef struct list_s list_t;

/**
 * add_node_end - Safely appends a new node to the end of a list_t list.
 * @head: Pointer to the first node of the list.
 * @n: The integer value to be stored in the new node.
 *
 * Return: Pointer to the head of the list, or NULL if allocation fails.
 */
list_t *add_node_end(list_t *head, const int n) {
    list_t *new_node;
    list_t *current;

    new_node = malloc(sizeof(list_t));
    if (new_node == NULL) {
        return (NULL);
    }

    new_node->n = n;
    new_node->next = NULL;

    if (head == NULL) {
        return (new_node);
    }

    current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = new_node;

    return (head);
}
