def fib(a):
    if a<=2:
        return 1
    else:
        return fib(a-1)+fib(a-2)

def main():
    n=int(input("第几项？"))
    print("{}".format(fib(n)))

main()
