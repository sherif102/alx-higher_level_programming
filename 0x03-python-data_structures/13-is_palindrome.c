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
    listint_t *front, *back, *middle;
    int n = 0, center = 0, i = 0;
    
    if (*head == NULL || (*head)->next == NULL)
        return (1);
    front = middle = *head;

    /* list item count = n */
    for (n = 0; front != NULL; n++)
        front = front->next;

    if (n % 2 == 1)
        center = (n / 2) + 1;
    else
        center = n / 2;

    for (i = 0; i < center; i++)
        middle = middle->next;

    back = middle;
    front = *head;
    n = n / 2;

    while (back)
    {
        for (i = 0; i < n - 1; i++)
            front = front->next;

        if (front->n != back->n)
            return (0);
            
        back = back->next;
        front = *head;
        n--;
    }
    return (1);
}