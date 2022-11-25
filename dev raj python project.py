n=int(input("Enter the end point of table:"))

for i in range(2,n+1):
    print("\n")
print("Table of:-",i)
print("\n")
for j in range(1,11):
    print(i,"X",j,"=",i*j)
