class test:
    def highest(self, lists):

        def get_total(name):
            return sum(lists[name])

        return max(lists, key=get_total)
    def total(self,list):
        return sum(list)
    def avarage(self,lis):
        return sum(lis)/len(lis)
g={}
name=[]
cat=test()
while True:
    print("\n                        CHOOSE                                   \n")
    print("1)enter mark for student")
    print("2)know the highest mark")
    print("3)know the average for a student")
    print("4)know the total for a student")
    print("5)know how many students in system")
    print("type exit if u are done")
    a=input("enter your choice: ")
    if a=="1":
        d=input("enter name: ")
        if d in g:
            again=input("do u wanna replace the marks? ")
            if again=="no":
                print("ok")
                continue
            if again=="yes":
                g.pop(d)
                mark=[]
                name.append(d)
                for i in range(2):
                    mark1=(int(input("enter marks: ")))
                    if mark1>100 or mark1<0:
                        print("mark not acpectable")
                    else:
                        mark.append(mark1)
                        g[d]=mark
            print("student suscessfully added")
            print(g)
        if d not in g:
            mark=[]
            name.append(d)
            for i in range(2):
                mark1=(int(input("enter marks: ")))
                if mark1>100 or mark1<0:
                 print("mark not acpectable")
                else:
                    mark.append(mark1)
                    g[d]=mark
            print("student suscessfully added")
            print(g)


    elif a=="2":
        if g:
            hi = cat.highest(g)
            print("the highest total was achieved by", hi)
        else:
            print("no data")
    elif a=="3":
        average1=input("enter name of the student: ")
        if average1 in g:
            hello=cat.avarage(g[average1])
            print(f"{average1}'s average is {hello}")
    elif a=="4":
        total1=input("enter the name: ")
        if total1 in g:
           bag= cat.total(g[total1])
           print(f"the total for {total1} is {bag}")
        else:
            print("name not in system")
    elif a=="exit":
        print("thanks for visting !")
        break
    elif a=="5":
       if g:    
        print(f'number of students in system is {len(name)}')
       else:
           print("no data")
if __name__=="__main__":
    print(cat.total([2,2]))
    print(cat.avarage([10,2]))
    print(cat.highest([10,2],[100,1]))





   
