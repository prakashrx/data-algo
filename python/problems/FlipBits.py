
from ast import In


input = 2147483647 
print(int('0xFFFFFFFF',16) ^ int(f'{input:032b}', 2))