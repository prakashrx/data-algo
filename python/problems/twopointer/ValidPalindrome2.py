def is_palindrome(s):  
  left = 0
  right = len(s) - 1
  count = 0
  while left < right:
    if s[left] != s[right]:
      if count > 0:
        return False
      count += 1
      if s[left + 1] == s[right]:
        right += 1
      elif  s[right - 1] == s[left]:
        left -= 1
      else:
        return False
    left += 1
    right -= 1
  return True



print(is_palindrome("A"))
print(is_palindrome("AA"))
print(is_palindrome("ABCEBA"))
print(is_palindrome("ABECBA"))
print(is_palindrome("ABECCBA"))
print(is_palindrome("ABCCEBA"))
print(is_palindrome("ABC"))
print(is_palindrome("ADBCACBA"))
print(is_palindrome("ADFCACBA"))