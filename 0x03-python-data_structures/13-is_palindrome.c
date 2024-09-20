#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


/**
 * is_palindrome - checks if a list is palindrome
 * @head: head parsed
 * Return: 0 if not palindrome and 1 if otherwise
 */

int is_palindrome(listint_t **head)
{
    listint_t *front, *back;
    int n = 0, center = 0, i = 0;
    if (*head == NULL || (*head)->next == NULL)
        return (1);
    front = *head;

    /* list item count = n */
    while (front != NULL)
    {
        front = front->next;
        n++;
    }
    front = *head;
    
    center = n / 2;

    while (center >= 0)
    {
        back = *head;
        i = 0;
        while (i < n - 1)
        {
            back = back->next;
            i++;
        }
        if (front->n != back->n)
            return (0);

        front = front->next;

        center--;
        n--;
    }
    return (1);
}