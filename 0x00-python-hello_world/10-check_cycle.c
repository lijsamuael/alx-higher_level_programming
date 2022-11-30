#include "lists.h"

/**
 * check_cycle - Checks for a cycle in a linked list
 * @list: Pointer to the first node in the linked list
 *
 * Return: 1 for cycle, 0 for no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;

	while (hare != NULL)
	{
		hare = hare->next;
		if (hare == NULL)
			return (0);
		hare = hare->next;

		tortoise = tortoise->next;

		if (hare == tortoise)
			return (1);
	}

	return (0);
}
