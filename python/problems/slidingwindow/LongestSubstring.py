
def find_longest_substring(input_string):
   d = {}
   left,right = 0, 0
   length = 0

   for right in range(0, len(input_string)):
      c = input_string[right]
      while c in d:
         d.pop(input_string[left], 0)
         left += 1
      d[c] = d.get(c, 0) + 1
      if right - left + 1 > length:
          length = right - left + 1

   return length

print(find_longest_substring("abcdbea"))