"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

"""
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def reverseList(head: ListNode) -> ListNode:
  """Invierte una lista enlazada completa en el lugar.

  Complejidad Temporal: O(N) -> Recorremos cada nodo una sola vez.
  Complejidad Espacial: O(1) -> Solo usamos punteros auxiliares.
  """
  prev = None
  current = head

  while current:
    next_node = current.next  # 1. Guardamos el siguiente nodo
    current.next = prev  # 2. Invertimos el puntero hacia atrás
    prev = current  # 3. Avanzamos 'prev' un paso
    current = next_node  # 4. Avanzamos 'current' un paso

  return prev  # 'prev' se convierte en la nueva cabeza de la lista
