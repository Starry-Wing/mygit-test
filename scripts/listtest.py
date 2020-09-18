def initTable():
    return ['姓名','年龄','性别','爱好']

def table(name,years,sex,hoby):
    return [name,years,sex,hoby]

def main():
    x=[]
    x.append(initTable())
    for i in range(1,4):
        x.append(table("{:5}".format('a'*i),i,'不明',"{:5}".format('h'*i)))
    for j in x:
        print(j)

main()

