def prime_checker(number): #COULD USE BOOLEAN IS_PRIME = TRUE OR FALSE. TRY USING THIS MORE
  check = 0
  for n in range (1, number - 1):
    if (number % n) == 0:
      check = n
  if check <= 1:
    print("It's a prime number")
  else:
    print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
