#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *temp;
	listint_t *second_half, *mid_node;
	int is_palindrome = 1;

	slow = fast = *head;
	prev_slow = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = prev_slow;
		prev_slow = slow;
		slow = temp;
	}

	if (fast)
		mid_node = slow;
	else
		mid_node = slow->next;

	second_half = prev_slow;

	while (mid_node)
	{
		if (mid_node->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		mid_node = mid_node->next;
		second_half = second_half->next;
	}
	return (is_palindrome);
}
