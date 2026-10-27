"""
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

from collections import Counter


def isAnagram(s: str, t: str) -> bool:
  """Determina si la cadena t es un anagrama de la cadena s.

  Complejidad Temporal: O(N) -> Recorremos ambas cadenas para contar frecuencias.
  Complejidad Espacial: O(1) -> El espacio extra está acotado por el alfabeto
  inglés (26 letras máximo), por lo que no escala con el tamaño de la entrada.
  """
  # Si las longitudes son diferentes, no pueden ser anagramas
  if len(s) != len(t):
    return False

  # Comparamos las frecuencias de los caracteres usando Counter
  return Counter(s) == Counter(t)


# --- Alternativa lógica pura (sin importar librerías avanzadas) ---
def isAnagramManual(s: str, t: str) -> bool:
  if len(s) != len(t):
    return False

  conteo = {}

  # Sumamos frecuencias de 's'
  for char in s:
    conteo[char] = conteo.get(char, 0) + 1

  # Restamos frecuencias usando 't'
  for char in t:
    if char not in conteo or conteo[char] == 0:
      return False
    conteo[char] -= 1

  return True


# --- Ejemplo de prueba local ---
if __name__ == "__main__":
  s1, t1 = "anagram", "nagaram"
  s2, t2 = "rat", "car"

  print(f"¿'{t1}' es anagrama de '{s1}'? -> {isAnagram(s1, t1)}")  # True
  print(f"¿'{t2}' es anagrama de '{s2}'? -> {isAnagram(s2, t2)}")  # False