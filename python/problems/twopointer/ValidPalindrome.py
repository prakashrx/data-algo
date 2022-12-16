

def is_palindrome(s):
  
  left = 0
  right = len(s) - 1
  while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1

  return True

print(is_palindrome("aba"))
print(is_palindrome("abba"))
print(is_palindrome("abca"))
print(is_palindrome("cbba"))
print(is_palindrome(""))
print(is_palindrome("a"))
