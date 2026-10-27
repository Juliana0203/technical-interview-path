"""
Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false

Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true

Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def isPalindrome(s: str) -> bool:
  """Verifica si una cadena es un palíndromo considerando solo caracteres alfanuméricos.

  Complejidad Temporal: O(N) -> Recorremos la cadena a lo sumo una vez con los
  dos punteros.
  Complejidad Espacial: O(1) -> No creamos estructuras adicionales, solo usamos
  dos variables de puntero.
  """
  izquierda = 0
  derecha = len(s) - 1

  while izquierda < derecha:
    # Ignorar caracteres que no sean letras o números desde la izquierda
    while izquierda < derecha and not s[izquierda].isalnum():
      izquierda += 1

    # Ignorar caracteres que no sean letras o números desde la derecha
    while izquierda < derecha and not s[derecha].isalnum():
      derecha -= 1

    # Comparar ignorando mayúsculas/minúsculas
    if s[izquierda].lower() != s[derecha].lower():
      return False

    izquierda += 1
    derecha -= 1

  return True


# --- Ejemplo de prueba local ---
if __name__ == "__main__":
  texto1 = "A man, a plan, a canal: Panama"
  texto2 = "race a car"

  print(
      f"¿'{texto1}' es palíndromo? -> {isPalindrome(texto1)}"
  )  # True (ignora comas, espacios y mayúsculas)
  print(f"¿'{texto2}' es palíndromo? -> {isPalindrome(texto2)}")  # False