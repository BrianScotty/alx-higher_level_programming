#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node
 * Return: pointer to the first node in the new list
 */

void reverse_listint(listint_t **head)
{
	listint_t *old = NULL;
	listint_t *temp = *head;
	listint_t *new = NULL;
	
	while (temp)
	{
		new = temp->next;
		temp->next = old;
		old = temp;
		temp = new;
	}
	*head = old;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer of the first node
 * Return: 1 (true), 0 (false)
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
