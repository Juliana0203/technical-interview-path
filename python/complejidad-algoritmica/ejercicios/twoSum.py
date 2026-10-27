"""
Two Sum
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Explanation: The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Explanation: The sum of nums[1] and nums[2] is 2 + 4 = 6, which equals the target. Therefore, the indices [1, 2] are returned.

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Explanation: The sum of nums[0] and nums[1] is 3 + 3 = 6, which equals the target. Therefore, the indices [0, 1] are returned.

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
  """Encuentra los índices de dos números en una lista que suman el target.

  Complejidad Temporal: O(N) -> Recorremos la lista a lo sumo una vez.
  Complejidad Espacial: O(N) -> Guardamos los elementos en un diccionario.
  """
  # Diccionario para almacenar los números que ya visitamos: {valor: índice}
  vistos = {}

  for i, num in enumerate(nums):
    complemento = target - num

    # Si el complemento ya está en el diccionario, encontramos la pareja
    if complemento in vistos:
      return [vistos[complemento], i]

    # Si no está, guardamos el número actual y su índice en el diccionario
    vistos[num] = i

  return []  # Por si no hay solución (aunque el problema garantiza que siempre hay una)


# --- Ejemplo de prueba local ---
if __name__ == "__main__":
  nums = [2, 7, 11, 15]
  target = 9
  print(f"Entrada: nums = {nums}, target = {target}")
  print(f"Salida esperada: [0, 1]")
  print(f"Resultado de la función: {twoSum(nums, target)}")