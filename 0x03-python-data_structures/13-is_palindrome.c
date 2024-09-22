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
    listint_t *front, *middle;
    int n = 0, center = 0, i = 0;
    int *front_value;
    
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

    front = *head;
    n = n / 2;

    front_value = malloc((n - 1) * sizeof(int));
    if (front_value == NULL)
    {
        free(front_value);
        return (0);
    }

    for (center = 0; center < n; center++)
    {
        front_value[center] = front->n;
        front = front->next;
    }

    while (middle)
    {
        if (front_value[center - 1] != middle->n)
        {
            free(front_value);
            return (0);
        }
            
        middle = middle->next;
        center--;
    }
    free(front_value);
    return (1);
}