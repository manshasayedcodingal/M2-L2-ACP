#Power Calculator

num = int(input("Enter the number: "))
n = int(input("Enter how many powers you want: "))

print("Powers of", num, "are:")

for i in range(1, n + 1):
    print(num, "power", i, "=", num ** i)