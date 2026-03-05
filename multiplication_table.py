#Tabuada básica (Matriz 10x10)
def basic_table():
    list1 =list(range(1,11,1)) 
    list2=list(range(0,11,1))
    for m in list1:
        i=m-1
        print(f"Multiplication Table of {list1[i]}:")
        for n in list2:
            if(m==list1[i]):
                print(f"{m}x{n} is equal to {m*n}")
    opt2=input("Thank you! Rerun? (Y/N)")
    if(opt2=="Y" or opt2=="y"):
      main()
    else:
      print("Thank you for using this program!")
      exit()

# Função Tabuada Personalizada
def custom_table():
    m=int(input("How many tables I may calculate (Starting by 1)"))
    m+=1
    list1 =list(range(1,m,1)) 
    list2=list(range(0,11,1))
    for m in list1:
          i=m-1
          print(f"Multiplication Table of {list1[i]}:")
          for n in list2:
              if(m==list1[i]):
                print(f"{m}x{n} is equal to {m*n}")
    opt2=input("Thank you! Rerun? (Y/N)")
    if(opt2=="Y" or opt2=="y"):
        main()
    else:
        exit()
    
def main():    
    opt=0
    while opt<4:
        print('Welcome to Multiplication Table Custom')
        opt=int(input('Select a option:\n\n1-Elementary School Multiplication Table\n2-Custom Multiplation Table\n3-Exit\n'))
        match(opt):
            case(1):
                basic_table()
            case(2):
                custom_table()
            case(3):
                exit()
            case _:
              raise Exception("Invalid Option")

main()
