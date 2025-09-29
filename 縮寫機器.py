print('縮寫機器')

print('''
將取每組詞開頭的第一個字(每組字詞以空格隔開)；
如果為英文的話,則取每個單字的自首,並轉為大寫；

如想要縮寫中有空格的話,請在需要空格的地方按兩下空白鍵
###請注意!按兩下空格之後方的首字也會被加入縮寫中(判定為字首)!!
''')


範例=input('要看範例嗎(Y)要(N)不要?(回答YN)').upper()
while 範例!='Y' and 範例!='N':
    print('偵測錯誤,請重新填寫!!!')
    del 範例
    範例=input('要看範例嗎(Y)要(N)不要?(回答YN)').upper()



if 範例=='Y':
    print(''' _ (底線) 代替   (空格)以方便示範
中文例子:皮皮無敵皮_爸爸是最皮_是皮者唯其_最是皮中帝_皮得沒人敵__皮皮皮_!!__皮皮皮_!!
縮寫成果------>皮爸是最皮 皮! 皮!

英文例子:Please_put__dangerous_apples_down!
縮寫成果------>PP DAD
''')
else:
    print('好的!')


空格=input('需要在縮寫中加入空格嗎(A)是(B)否?(回答AB):').upper()
while 空格!='A' and 空格!='B':
    print('回答不符規定,請重新填寫!!!')
    del 空格
    空格=input('需要在縮寫中加入空格嗎(A)是(B)否?(回答AB):').upper()


字串=input('''
輸入字串(每個字請以空格間隔)
###如果上題回答"否",會幫你自動刪除多餘的空格喔###:''')

#空格位置=(字串.find(' '))

list=[]

for pos,char in enumerate(字串):
    if(char == ' '):
        list.append(pos)
#print(list)

長度=len(字串)
while 長度==int(list[-1]+1) :
    list.pop()
    



縮寫=[]
縮寫.append(字串[0])
for 開頭 in list:

    A=字串[int(開頭)+1]
    #print(A)
    縮寫.append(A) 
    



成品=str(''.join(縮寫)).upper()


if 空格=='B':
    成品=成品.replace(' ', '')

print(f'{字串}的縮寫為: {成品} ')

再一次=input('要再使用一次嗎(C)要(D)不要?').upper
if 再一次=='C':
    print('自己重開吧!')
    input('按一下 Enter ')
elif 再一次=='D':
    print('881')
else:
    print('ㄌㄩㄝˉ')







