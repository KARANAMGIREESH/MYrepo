n=int(input("enter any number: "))
if n>2:
    for i in range(2,n+1,1):
      if (n%i==0):
          print("entered number is not a prime numbers: ")
          break
    else:
        print("prime number",n)





