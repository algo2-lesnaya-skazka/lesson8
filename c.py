a = int (input('a = '))
b = int (input('a = '))
op = input ('add/sub/mull/div:')
if op == 'add':
 c = a + b
elif op == 'sub':
 c = a - b
elif op == 'mul':
 c = a * b
elif op == 'div':
 c = a / b
else:
 c = 'Error'
print('Answer = ',c)