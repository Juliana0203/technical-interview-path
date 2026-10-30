"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
  """Elimina el n-ésimo nodo contando desde el final en una sola pasada.

  Complejidad Temporal: O(N) -> Recorremos la lista linealmente.
  Complejidad Espacial: O(1) -> Usamos punteros fijos.
  """
  dummy = ListNode(0, head)
  slow = dummy
  fast = dummy

  # 1. Adelantar el puntero 'fast' n + 1 pasos
  for _ in range(n + 1):
    fast = fast.next

  # 2. Mover ambos punteros al mismo ritmo hasta que fast llegue al final
  while fast:
    slow = slow.next
    fast = fast.next

  # 3. 'slow' está justo antes del nodo a eliminar; saltamos el nodo
  slow.next = slow.next.next

  return dummy.next