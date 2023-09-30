is_prime= False
#function to check if a number is prime or not
def prime_checker(n):
   global is_prime
   for i in range(2, int((n / 2) + 1)):
         if(n % i == 0):
            is_prime = False
            break
         else:
            is_prime = True


n= int (input("Enter a number to check: "))
if n==2:
    is_prime= True
   #  print(f"{n} is a prime number")
elif n==1 or n==0:
    is_prime= False
elif n>2:
   prime_checker(n)
if is_prime:
    print(f'{n} is a prime number')
else:
     print(f'{n} is not a prime number')


    
