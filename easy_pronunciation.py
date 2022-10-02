t = int(input())
while t>0:
    n = int(input())
    s = input()
    s = list(s)
    count = 0
    
    for var in s:
        if(var=='a' or var=='e' or var=='i' or var=='o' or var=='u'):
            count = 0
        else:
            count += 1

        if(count==4):
            break
    if(count==4):
        print("NO")
    else:
        print("YES")
    t -= 1
