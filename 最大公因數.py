
print('找最大公因數!')
x=int(input('輸入數字1:'))
y=int(input('輸入數字2:'))

#print(range(1,x+1))


list1=[]
for a in range(1,int(x)+1):
     e=int(x)/a
     if int(e)==e:
        list1.append(a)


#print(list1)




list2=[]
for b in range(1,y+1):
     f=int(y)/b
     if int(f)==f:
        list2.append(b)

#print(list2)

list=[]

for c in list1:
    for d in list2:
        if c==d:
            list.append(c)


#print(list)

s=len(list)


print(f'{x}和{y}的最大公因數是{list[int(s)-1]}')


