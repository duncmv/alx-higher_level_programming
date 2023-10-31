#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number in a sorted linked list
 * @head: beginning of list
 * @number: number to be inserted
 * Return: address of node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *current;

	current = *head;
	if (current == NULL || number < current->n)
	{
		node = malloc(sizeof(listint_t));
		if (node == NULL)
			return (NULL);
		if (current != NULL)
		{
			node->n = current->n;
			current->n = number;
			node->next = current->next;
			current->next = node;
			return (node);
		}
		else
		{
			node->n = number;
			node->next = NULL;
			current = node;
			return (node);
		}
	}
	else
	{
		insert_node(&(current->next), number);
	}
	return (NULL);
}
