#reverse a number

num = int(input("Enter a number"))
rev = 0
while(num!=0):
    n = num%10
    rev = (rev*10) + n
    num //= 10

print(rev)