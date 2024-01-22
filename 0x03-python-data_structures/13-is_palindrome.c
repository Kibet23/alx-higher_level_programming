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
	listint_t *slow, *fast, *prev_slow, *second_half;
	slow = fast = *head;
	prev_slow = NULL;

	/*find the middle of the linked list*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		listint_t *temp = slow->next;
		slow->next = prev_slow;
		prev_slow = slow;
		slow = temp;
	}
	if (fast != NULL)
		slow = slow->next;

	second_half = slow;
	while (prev_slow != NULL && second_half != NULL)
	{
		if (prev_slow->n != second_half->n)
			return (0);

		prev_slow = prev_slow->next;
		second_half = second_half->next;
	}
	return (1);
}
