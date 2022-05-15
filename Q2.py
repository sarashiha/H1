n = int(input('Please, Enter a number: '))
binary = []
while n > 0:
    binary.append(n%2)
    n=n//2
binary.reverse()
for b in binary:
    print(b, end='')
