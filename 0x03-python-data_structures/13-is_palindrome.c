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
	listint_t *new, *tmp, *clear;
	int _break = 1;

	new = NULL, tmp = *head;
	if (!head || !(*head) || !(*head)->next)
		return (1);
	while (tmp->next != NULL || _break)
	{
		if (add_nodeint(&new, tmp->n) == NULL)
			return (0);
		if (tmp->n == (tmp->next)->n)
		{
			tmp = tmp->next;
			break;
		}
		if (tmp->n == ((tmp->next)->next)->n)
		{
			tmp = (tmp->next)->next;
			break;
		} tmp = tmp->next;
	} clear = new;
	if (tmp->next == NULL)
	{
		free_listint(clear);
		return (0);
	}
	while (tmp->next != NULL)
	{
		if (tmp->n != new->n)
		{
			free_listint(clear);
			return (0);
		} tmp = tmp->next, new = new->next;
	}
	if (new->next == NULL)
	{
		free_listint(clear);
		return (1);
	} free_listint(clear);
	return (0);
}
