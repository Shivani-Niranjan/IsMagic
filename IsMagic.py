def magic(number):
    sum = 0
    while(number > 0 or sum > 9):
        if(number == 0):
            number = sum
            sum = 0
        rem = number % 10
        sum += rem
        number //= 10
    return (1 if sum == 1 else 0)

number = int(input())
print(magic(number))