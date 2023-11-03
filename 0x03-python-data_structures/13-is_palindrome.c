#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: beginnin of list
 *
 * Return: 0 if its not, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int j, i = 0, *p;
	listint_t *l;

	if (*head == NULL)
		return (1);

	for (l = *head; l != NULL; l = l->next)
	{
		i++;
	}
	p = malloc(sizeof(int) * i);
	l = *head;

	for (j = 0; j < i; j++)
		p[j] = l->n, l = l->next;
	i--;

	for (j = 0; j <= i; j++, i--)
	{
		if (*(p + j) != *(p + i))
		{
			free(p);
			return (0);
		}
	}
	free(p);
	return (1);
}
