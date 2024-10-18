class Book:
    #PROPERTYLAR!
    def __init__(self,id:int,name:str,author:str,count:int,price:int):
        self.id = id
        self.name = name
        self.author = author
        self.count = count
        self.price = price


    def yozish(self,ptr):
        self.id = int(input("ID: "))
        self.name = input("NAME: ")
        self.author = input("AUTHOR: ")
        self.count = int(input("COUNT: "))
        self.price = int(input("PRICE: "))
        ptr.write(f"{self.id},{self.name},{self.author},{self.count},{self.price}\n")


    def ochirish(self, n,file):
        with open(file, "r") as ptr:
            oqi = ptr.readlines()
        with open(file, "w") as ptr:

            #hello today dam alish
            for i in oqi:
                id = i.split(',')[0]
                if id != str(n):
                    ptr.write(i)

try:
    file = "Bookstore.txt"
    kitob = Book(0,"","",0,0)

    while True:
        choice = int(input("[1] qoshish     [2] ochirish     [0] exit\nCHOICE: "))
        if choice == 1:
            with open(file,"a") as ptr:
                for i in range(int(input("NECHTA KITOB KIRITASIZ: "))):
                    print(f"{i+1} - KITOB\n")
                    kitob.yozish(ptr)

        elif choice == 2:
            n = input("ID KIRITING: ")
            kitob.ochirish(n,file)
        else:
            break

except FileNotFoundError:
    print("FAYL TOPILMADI!!!")

