#include "lists.h"
/**
 * check_cycle - check the node if is cycle or not
 * @list: list struct
 * Return: 1 is cycle or 0 is not cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *first = list;

	if (!list)
		return (0);
	while (list->next)
	{
		if (first == list->next)
			return (1);
		list = list->next;
	}

	return (0);
}
