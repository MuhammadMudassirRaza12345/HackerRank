
a=int(input('Enter a number: '))

def fizzbuzz(a):

    if a % 3 == 0:

        return ('Fizz')

    elif a % 5 == 0:

        return ( 'Buzz' )

    elif a % 15 == 0:

        return ('Fizzbuzz')

    else:

        return a

print(fizzbuzz(a))

# second solution
def fizzBuzz(n):
    for n in range(1,n+1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)

# third solution
a=int(input('Enter a number: '))

def fizzbuzz(a):
    if a % 3 == 0 and a % 5 == 0:
        return('Fizzbuzz')
    elif a % 3 == 0:
        return('Fizz')
    elif a % 5 == 0:
        return('Buzz')
    else:
        return a

print(fizzbuzz(a))

