t = int(input())
while t>0:
    a, b = map(int, input().split())
    c = a+b
    sum = 0
    while(c>0):
        r = c%10
        if(r==0 or r==6 or r==9):
            sum = sum + 6
        elif(r==1):
            sum = sum + 2
        elif(r==2 or r==3 or r==5):
            sum = sum + 5
        elif(r==4):
            sum = sum + 4
        elif(r==7):
            sum = sum + 3
        elif(r==8):
            sum = sum + 7
        c = c//10
    print(sum)
    t -= 1
