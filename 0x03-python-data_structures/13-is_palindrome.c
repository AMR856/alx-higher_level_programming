#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - A function to check if a linked list is palindrome
 * or not
 * @head: A pointer to a pointer that points to the head
 *
 * Return: 1 if palindrome and 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	int isP = 1;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	fast = *head;
	slow = reverseList(slow);
	while (slow != NULL)
	{
		if (slow->n != fast->n)
		{
			isP = 0;
			break;
		}
		slow = slow->next;
		fast = fast->next;
	}
	return (isP);
}

/**
 * reverseList - A function to reverse a linked list
 * @head: A pointer to the head of the linked list
 * 
 * Return: A pointer to the reversed list
*/

listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *temp;
	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
	}
	return (prev);
}