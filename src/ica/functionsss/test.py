import math
def is_prime(num):
   if num <= 1:
       return False
   elif num <= 3:
       return True
   elif num % 2 == 0 or num % 3 == 0:
       return False
   i = 5
   while i <= math.isqrt(num):
       if num % i == 0 or num % (i + 2) == 0:
           return False
       i += 6
   return True
user_input = int(input("Enter a number: "))
print("Checking if", user_input, "is prime...")
if is_prime(user_input):
   print(user_input, "is a prime number.")
else:
   print(user_input, "is not a prime number.")