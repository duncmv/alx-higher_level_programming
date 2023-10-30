#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: linked list to be checked
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	for (temp = list; temp != NULL; temp = temp->next)
	{
		if (temp->next == list)
			return (1);
	}
	return (0);
}
