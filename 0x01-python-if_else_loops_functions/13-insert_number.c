#include "lists.h"
/**
* insert_node - Inserts a node with a given number into a sorted linked list.
* @head: A pointer to the head of the linked list.
* @number: The value to insert into the linked list.
* Return: A pointer to the newly inserted node.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr_node;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	else if (number <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{
		curr_node = *head;
		while (curr_node->next && curr_node->next->n < number)
		{
			curr_node = curr_node->next;
		}
		new_node->next = curr_node->next;
		curr_node->next = new_node;
		return (new_node);
	}
}
