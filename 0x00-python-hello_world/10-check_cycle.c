#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the head node
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
  listint_t *curr, *nxt;

  if (list == NULL || list->next == NULL)
    return (0);
  curr = list;
  nxt = curr->next;

  while (curr != NULL && nxt->next != NULL
	 && nxt->next->next != NULL)
    {
      if (curr == nxt)
	return (1);
      curr = curr->next;
      nxt = nxt->next->next;
    }
  return (0);
}
