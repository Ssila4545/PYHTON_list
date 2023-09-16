
def swapList(list):
    size_of_list=len(list)
    temp=list[size_of_list-1]
    list[size_of_list-1]=list[0]
    list[0]=temp

    return list


list=[12,44,56,43,66]

print(swapList(list))   