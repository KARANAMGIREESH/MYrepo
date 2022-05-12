n=input("enter any string: ")
half=int((len(n)/2)+1)
if len(n)%2==0:
        first=n[:half]
        last=n[half:]
else:
       first=n[:half]
       last=n[half+1:]
if first==last:
    print("given string is symmetric ",n)
else:
    print("entered string is not symmetric ",n)

if n==n[::-1]:
    print("given string is polindrome",n)
else:
    print("given string is not polindrome",n)