# break
print()
print('1')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

print()
print('2')
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')

print()
print('3')
for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')

# conditional expresiion
raining = False
print("Let's go to the", 'beach' if not raining else 'library')

raining = True
print("Let's go to the", 'beach' if not raining else 'library')

age = 12
s = 'teen' if age < 21 else 'adult'
s

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'

# else if
x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


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

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")

name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")

x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')

print('After conditional')

if 'foo' in ['foo', 'bar', 'baz']:
    print('Outer condition is true')

    if 10 > 20:
        print('Inner condition 1')

    print('Between inner conditions')

    if 10 < 20:
        print('Inner condition 2')

    print('End of outer condition')
print('After outer condition')

# nested while

a = ['foo', 'bar']

while len(a):
    print(a.pop(0))

    b = ['baz', 'qux']

    while len(b):
        print('>', b.pop(0))

if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")

if 'f' in 'foo':
    print('1')
    print('2')
    print('3')

if 'z' in 'foo':
    print('1')
    print('2')
    print('3')

x = 2

if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')

# one line while
n = 5
while n > 0:
    n -= 1
    print(n)

# pass
if True:
    pass
print('foo')

print()
print('1')
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)


print()
print('2')
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

print()
print('3')
for k in d.values():
    print(k)

print()
print('3')
for k, v in d.items():
    print(k, ":", v)

print('1')
n = 5
while n > 0:
    n -= 1
    print(n)

print()
print('2')
i = 1
while i < 6:
    print(i)
    i += 1

print()
print('3')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break  # Break Statement
    print(n)
print('Loop ended.')

print()
print('4')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')
