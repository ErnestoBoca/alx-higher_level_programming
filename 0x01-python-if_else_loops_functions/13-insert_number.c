#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the firt node of the list
 * @number: the data of the new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	if (*head == NULL)
	{
		new_node->n = number;
		*head = new_node;
		return (new_node);
	}

	if (number < temp->n)
	{
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
	} else
	{
		while (temp->next != NULL)
		{
			if (temp->next->n < number)
				temp = temp->next;
			else
				break;
		}

		new_node->n = number;
		new_node->next = temp->next;
		temp->next = new_node;
	}

	return (new_node);
}
