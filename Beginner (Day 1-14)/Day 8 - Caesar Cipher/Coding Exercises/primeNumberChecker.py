#Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#----------------  VERSION 1  ----------------
def prime_checker(num):
    prime = True
    #divide from 2 up to the number less than the specified number
    for i in range(2,num): 
        if num <= 1 or num % i == 0:
            prime = False

    if prime == True and num > 1: #1 is not considered a prime number
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        
n = int(input("Check this number: "))
prime_checker(n)


#----------------   VERSION 2  ----------------
def prime_checker(num):
    if num <= 1:  #1 is not considered a prime number
        print("It's not a prime number.")
        return
        
    #divide from 2 up to the number less than the specified number
    for i in range(2,num): 
        if num <= 1 or num % i == 0:
            print("It's not a prime number.")
            return #ends the function
    print("It's a prime number.")
        
n = int(input("Check this number: "))
prime_checker(n)
