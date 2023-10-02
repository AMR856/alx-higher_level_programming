#include "lists.h"

/**
 * check_cycle - A function to check if there is a cycle or not
 * @list: A pointer to the head of the list
 *
 * Return: 1 if there is a cycle and 0 if not
*/

int check_cycle(listint_t *list)
{
	listint_t *myFirstHead = list;
	listint_t *mySecondHead = list;

	while (myFirstHead != NULL && mySecondHead != NULL
	&& mySecondHead->next != NULL)
	{
		myFirstHead = myFirstHead->next;
		mySecondHead = mySecondHead->next->next;
		if (myFirstHead == mySecondHead)
			return (1);
	}
	return (0);
}
