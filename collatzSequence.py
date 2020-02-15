def collatz(number):
    if number%2==0:
        result = int(number//2)
        print(result)
    elif number%2==1:
        result = int(3*number+1)
        print(result)

    if result != 1:
        collatz(result)

number=int(input("Give a number: "))
collatz(number)