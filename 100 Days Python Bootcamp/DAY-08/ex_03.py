# prime number checker

# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.

# Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

def is_prime(num):

    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for n in range(2, (num + 2) // 2):
            if num % n == 0:
                return False
        else:
            return True

for num in range(1,101):
    if is_prime(num):
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")

num = int(input("Which number do you want to check?\n>> "))
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")