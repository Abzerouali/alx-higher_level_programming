#ifndef Listyy_H
#define Listyy_H

#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

/**
* struct listint_s - singly linked list
* @n: int
* @next: Pointer to the next node
*
* Description: structure for singly linked list node
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif
