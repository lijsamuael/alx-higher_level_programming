#include "lists.h"

/**
 * insert_node - Inserts a node in the correct spot in a sorted linked list
 * @head: Pointer to a pointer pointing to the first node in the linked list
 * @number: Number for the new node to have
 *
 * Return: Pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	newnode->n = number;

	if (!node)
	{
		newnode->next = NULL;
		*head = newnode;
		return (newnode);
	}

	if ((*head)->n > number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (node->next != NULL && node->next->n < number)
		node = node->next;

	newnode->next = node->next;
	node->next = newnode;
	return (newnode);
}
