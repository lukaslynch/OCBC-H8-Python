# Iteration means executing the same block of code over and over, potentially many times. A programming structure that implements iteration is called a loop.

# In programming, there are two types of iteration, indefinite and definite:

# With indefinite iteration, the number of times the loop is executed isn’t specified explicitly in advance. Rather, the designated block is executed repeatedly as long as some condition is met. Use while for this iteration.

# With definite iteration, the number of times the designated block will be executed is specified explicitly at the time the loop starts. Use 'for' for this iteration.

print('==WHILE LOOP==')

n = 5
while n > 0 :
    n -= 1      # decrement n = n -1
    print(n)
print('====')

i = 1
while i < 6 :
    print(i)
    i += 1
print('====')

print('==BREAK & CONTINUE IN LOOPING==')

print('==ini pake break==')
i = 0

while i < 5 :
    j = 0
    
    while j < 3 :
        print(i, j)

        if(j ==2) : 
            break

        print('----')

        j += 1
    i += 1

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

print('==ini pake continue==')
i = 0

while i < 5 :
    j = 0
    
    while j < 3 :
        print(i, j)

        j += 1

        if(j ==2) : 
            continue

        print('----')

    i += 1

print('==nested while loop==')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))     # pop --> hapus elemen dri list
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))

print('==FOR LOOP==')

books = ['book a', 'book b', 'book c']

for book in books: 
    print(book)

print('== one line while looop==')
n = 5
while n > 0: 
    n -= 1; 
    print(n)

print('==iterate with range==')
# x = range(5) --> [1, 2, 3, 4]
# x = range(2, 9) --> 2 s/d angka sebelum 9
# x = range(0, 20, 100) --> mulai dri angka 0, incremnt 20, brhenti sblum angka 100

x = range(0, 10)
for n in x:    
    print(n)

print('==iterate dictionary==')
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

print('this is dictionary key')

for k in d:
    print(d[k])

print('this is dictionary value')

for k in d.values():
    print(k)

print('this is dictionary value')

for k, v in d.items(): 
    print(k, ":", v) 

print('this is dictionary value & key')