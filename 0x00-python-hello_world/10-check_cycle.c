#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *ptr1 = list;
    listint_t *ptr2 = list;

    while (ptr1 && ptr2 && ptr2->next)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next->next;

        if (ptr1 == ptr2)
            return (1);
    }
    return (0);
}
