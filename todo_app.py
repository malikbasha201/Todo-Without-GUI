def write_data(data,path="storage.txt"):
    with open(path,'w') as file:
        file.writelines(data)

def get_data(path="storage.txt"):
    with open(path,"r")as file:
        res = file.readlines()
        return res


while True:    
    user = input("Type add,edit,show,remove or exit: ").strip()
    if user=="add":
        data = input("Enter the todo: ")
        res = get_data()
        res.append(data+"\n")
        write_data(res)
    elif user=="edit":
        try:
            new = int(input("Enter the index of todo to edit: "))
            new_data = input("Enter the New todo: ")
            res = get_data()
            res[new-1]=new_data
            write_data(res)
        except:
            print("check the index Number once....")
    elif user=="remove":
        try:
            del_ind = int(input("Enter the index of the todo to remove: "))
            res = get_data()
            res.pop(del_ind-1)
            write_data(res)
        except:
            print("Check the index Number once.....")
    elif user=="show":
        res = get_data()
        res = [i.strip("\n") for i in res]
        for i,j in enumerate(res):
            print(f"{i+1}.{j}")
    elif user=="exit":
        print("Tata.....:)")
        break
    else:
        print("Hey!You entered the wrong one...")
        
