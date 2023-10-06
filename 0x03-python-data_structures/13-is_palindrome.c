#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#define MAX_SIZE 1000

/**
 * is_palindrome - A function to check if a linked list is palindrome
 * or not
 * @head: A pointer to a pointer that points to the head
 *
 * Return: 1 if palindrome and 0 if not
*/

int is_palindrome(listint_t **head)
{
	int myArray[MAX_SIZE] = {0};
	listint_t *tempHead = *head;
	int counter = 0, anLooper, flag = 1;

	while (tempHead != NULL)
	{
		myArray[counter] = tempHead->n;
		counter++;
		tempHead = tempHead->next;
	}
	anLooper = counter - 1;
	for (int i = 0; i < counter / 2; i++, anLooper--)
	{
		if (myArray[i] != myArray[anLooper])
		{
			flag = 0;
			break;
		}
	}
	return (flag);
}
