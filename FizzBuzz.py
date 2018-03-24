for i in range(1,101): # loop for numbers 1 to 100
    if i % 15 == 0:
        print('FizzBuzz') # starting with dividing by 15 to avoid intersections
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 ==0:
        print('Fizz')
    else:
        print(i)