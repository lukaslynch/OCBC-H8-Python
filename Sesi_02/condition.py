x = 0
y = 5

if x < y:               #True
    print('yes', '1st state')

if y < x:               #False
    print('yes', '2nd state')

if x:                      #False, karena x = 0, 0 bernilai falsy
    print('yes', 'x state')

if y:
    print('yes', 'y state')


if 'aul' in 'grault': #do check if 'aul' ada di dlm 'grault'
    print('grault contains aul')

print('========')
# make conditionals from this case 
# If the weather is nice, then I will:
# Mow the lawn
# Weed the garden
# Take the dog for a walk
# (If the weather isn’t nice, then I won’t do any of these things.)

# weather = 'nice'
weather = 'cloudy'

if weather == 'nice' :
    print('inside if scope')
    print('\nMow the lawn')
    print('\n Weed the garden')
print('after conditionals')
print('\n Take the dog for walk')

print('===NESTED IF===')
# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz', 'qux']: #         x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')       #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x

print('==IF ELSE==')
weather = 'cloudy'

if weather == 'nice' :
    print('inside if scope')
    print('\nMow the lawn')
    print('\n Weed the garden')
    print('\n Take the dog for walk')  
else:
    print('make indomie rebus')
    print('do binge watching')

# ANOTHER IF ELSE EXAMPLE
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")

print('==IF ELIF ELSE==')
hargaBuku = 20000
hargaMajalah = 5000
uang = 10000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")

print('tes string')

# another elif example
name = 'Saw'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xavier':
    print('Hello Xavier')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

print('==ONE LINE STATEMENT==')
if 'f' in 'foo': print('1'); print('2'); print('3')
# SELAIN STATEMENT TERAKHIR HARUS DIIKUTI DENGAN SEMICOLON(;)
name = 'Arnold'
if name == 'Fred': print('Hello Fred')
elif name == 'Xavier': print('Hello Xavier')
elif name == 'Hacktiv8': print('Hello Hacktiv8')
elif name == 'Arnold': print('Hello Arnold')
else: print("I don't know who you are!")

print('==TERNARY OPERATOR==')
# convert if else to ternary
# <expr1> if <conditional_expr> else <expr2>

nomor_undian = 150
# if nomor_undian < 100 :  --> conditional_expr
#     prize = 'box 1' --> expr1
# else :
#     prize = 'box 2' --> expr2

prize = 'box 1' if nomor_undian < 100 else 'box 2'
print(prize)

print('==python pass statement==')
# Occasionally, you may find that you want to write what is called a code stub: a placeholder for where you will eventually put a block of code that you haven’t implemented yet.

# If you try to run foo.py, you’ll get this:

#   File "foo.py", line 3
#     print('foo')
#         ^
# IndentationError: expected an indented block
# The Python pass statement solves this problem. It doesn’t change program behavior at all. It is used as a placeholder to keep the interpreter happy in any situation where a statement is syntactically required, but you don’t really want to do anything:

# if True:
#     pass

# print('foo')

if True:
    pass
print('foo')