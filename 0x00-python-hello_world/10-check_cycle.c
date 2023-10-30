#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: linked list to be checked
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *check;

	for (temp = list, check = list; temp != NULL; temp = temp->next)
	{
		while (check >= temp && check != NULL);
		{
			if (temp->next == check)
				return (1);
			check = check->next;
		}
		check = list;
	}
	return (0);
}
