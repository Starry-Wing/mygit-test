def main():
    print("-"*60)
    for i in range(1,11):
        for j in range(1,11):
            print("|{:5d}".format(i*j),end='')
        print("|")
    print("-"*60)

main()

