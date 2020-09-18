def check(n):
    if n==1:
        return 1
    elif n>=2 and n<=6:
        return 0
    elif n>=7 and n<=11:
        for m in range(2,11):
            if check(n-m)==1:
               return check(n-m)
        return check(n-m)
    else:
        for j in range(10,1,-1):
            if check(n-j)==1:
               return check(n-j)
        return check(n-j)

def main():
    judge=0
    isEnd=0
    n=int(input("please input the numbers of sticks(20-50):"))
    while(1):
        print()
        pltake=int(input('how many do you want to take?(between1-5):'))
        n=n-pltake
        if(n==1):
            print('you win')
            break
        elif(n%6!=1):
            if(n%6!=0):
                factor=n//6*6+1
            else:
                factor=n-5
            print('computer took {} sticks'.format(n-factor))
            n=factor
        else:
            for i in range(5,0,-1):
                judge=check(n-i)
                if(judge==1):
                    n=n-i
                    print('computer took {} sticks'.format(i))
                    break
            else:
                #print(judge)
                print('computer surrender,you win')
                isEnd=1
        if(isEnd):
            break
        print('there is {} left'.format(n))
        if(n==1):
            print('you lose')
            break


main()
