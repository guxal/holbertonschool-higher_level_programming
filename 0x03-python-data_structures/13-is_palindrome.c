#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * *add_nodeint - add node integer
 * @head: head
 * @n: new integer
 * Return: listint_t
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;

	return (new);

}
/**
 * is_palindrome - is palindrome
 * @head: header
 * Return: integer
 */
int is_palindrome(listint_t **head)
{
	listint_t *new = NULL;
	listint_t *tmp;

	tmp = *head;

	if (head == NULL)
		return (1);

	if (tmp->next == NULL)
		return (0);

	while (tmp)
	{
		new = add_nodeint(&new, tmp->n);
		if (tmp->n == (tmp->next)->n)
		{
			tmp = tmp->next;
			break;
		}
		tmp = tmp->next;
	}

	while (tmp)
	{
		if (tmp->n != new->n)
			return (0);
		tmp = tmp->next;
		new = new->next;
	}

	return (1);
}
