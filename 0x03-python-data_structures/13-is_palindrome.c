#include "lists.h"

/**
 * reverse_listint - Function to reverse a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
void reverse_listint(listint_t **head)
{
	listint_t *old = NULL;
	listint_t *recent = *head;
	listint_t *next = NULL;

	while (recent != NULL)
	{
		next = recent->next;
		recent->next = old;
		old = recent;
		recent = next;
	}

	*head = old;
}

/**
 * is_palindrome - Function checks if a linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	dup = slow->next;
	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n != dup->n)
			return (0);

		temp = temp->next;
		dup = dup->next;
	}

	return (1);
}
