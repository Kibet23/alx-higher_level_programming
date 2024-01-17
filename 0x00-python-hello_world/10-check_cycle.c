#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks if a singly linked ist has a cycle
 * @list: pointer to the singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list, *y = list;

	while (y != NULL && y->next != NULL)
	{
		x = x->next;
		y = y->next->next;

		if (x == y)
		{
			return (1);
		}
	}
	return (0);
}
