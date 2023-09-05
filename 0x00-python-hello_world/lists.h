#ifndef Lisyyyy_H
#define Lisyyyy_H

#include <stdlib.h>

/**
* struct listint_s - singly linked list
* @n: integer
* @next: pointer to the next node.
*
* Description: singly linked list (node structure).
*/

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;



#endif
