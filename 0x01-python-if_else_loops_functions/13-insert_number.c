#include "lists.h"

/**
 * insert_node - A function to insert a node in a sorted
 * linked list
 * @head: A Pointer to a pointer that points
 * to the head of the linked list
 * @number: The number that will be put in the new node
 *
 * Return: NULL or a pointer to the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tempHead = *head;
	listint_t *newNode = (listint_t *)malloc(sizeof(listint_t));

	newNode->n = number;
	newNode->next = NULL;
	if (tempHead == NULL || tempHead->n > number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	while (tempHead != NULL && tempHead->next != NULL)
	{
		if (number >= tempHead->n && number <= tempHead->next->n)
		{
			newNode->next = tempHead->next;
			tempHead->next = newNode;
			return (newNode);
		}
		tempHead = tempHead->next;
	}
	if (newNode->next == NULL)
	{
		newNode->next = tempHead->next;
		tempHead->next = newNode;
		return (newNode);
	}
	return (NULL);
}
