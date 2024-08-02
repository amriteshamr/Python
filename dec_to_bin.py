#converting decimal to binary without built in function
 
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

n = int(input("Enter a number"))

bin = decimal_to_binary(n)

print(bin)