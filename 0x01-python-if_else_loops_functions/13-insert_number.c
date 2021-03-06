#include <stdlib.h>
#include "lists.h"
/**
 * *insert_node - insert node in singly list
 * @head: header node
 * @number: number insert
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (current->n > number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next != NULL)
		{
			if ((current->n < number
			    && (current->next)->n > number)
			    || current->n == number)
			{
			new->next = current->next;
			current->next = new;
			break;
			}
			current = current->next;
		}
		if (current->n < number)
			current->next = new;
	}

	return (new);
}
