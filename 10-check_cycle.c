#include "lists.h"
/**
* check_cycle - Checks if a singly linked list has a cycle.
* @list: A pointer to the head of the linked list.
* Return: 1 if there is a cycle, 0 otherwise.
*/
int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}

	return (0);
}
