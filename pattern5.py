for i in range(1,8):
    for j in range(8):
        print(i,end="")
    print("\r")
print("............")
for i in range(1,8):
    for j in range(i):
        print(i,end="")
    print("\r")
print("............")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("\r")