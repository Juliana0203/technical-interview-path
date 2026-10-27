"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation: All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def containsDuplicate(nums: list[int]) -> bool:
  """Determina si la lista contiene algún elemento duplicado.

  Complejidad Temporal: O(N) -> Recorremos la lista a lo sumo una vez.
  Complejidad Espacial: O(N) -> En el peor de los casos, guardamos todos los
  elementos en el set.
  """
  vistos = set()

  for num in nums:
    if num in vistos:
      return True  # ¡Encontramos un duplicado!
    vistos.add(num)

  return False


# --- Ejemplo de prueba local ---
if __name__ == "__main__":
  nums1 = [1, 2, 3, 1]
  nums2 = [1, 2, 3, 4]
  print(f"¿'{nums1}' tiene duplicados? -> {containsDuplicate(nums1)}")  # True
  print(f"¿'{nums2}' tiene duplicados? -> {containsDuplicate(nums2)}")  # False