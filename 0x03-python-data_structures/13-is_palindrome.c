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
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *next;
    int isPalindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (isPalindrome);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    while (prev != NULL)
    {
        if (prev->n != slow->n)
        {
            isPalindrome = 0;
            break;
        }
        prev = prev->next;
        slow = slow->next;
    }

    return (isPalindrome);
}