def sort(list):
    
    for i in range(0,len(list)):
        small= i
        for j in range(i,len(list)):

           if list[j]<list[small]:
                small=j
                temp=list[i]
                list[i]=list[small]
                list[small]=temp

   



list=[7,5,4,9,3]

sort(list)
print(list)

