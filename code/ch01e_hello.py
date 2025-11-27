print('code in a loop.')
i = 0
while i < 5:
    print(i, 'Hello, World!')
    i += 1

print()
print('code in a function.')
def hello(i=0):
    print(i, 'Hello, World!')
    i = i + 1
    if i < 5:
        hello(i)
    else:
        return

hello()            