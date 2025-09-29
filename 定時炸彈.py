
import random as RD
import time


def 函數 ():
    print('歡迎來玩 終極炸彈,這是一個兩人遊戲喔!')
    範圍小=input('請輸入範圍(下限)')
    範圍大=input('請輸入範圍(上限)')

    while int(範圍大)<int(範圍小):
        print('請重新輸入')
        範圍小=input('請輸入範圍(下限)')
        範圍大=input('請輸入範圍(上限)')


    選擇=input('想要(A)系統隨機出數字,(B)還是互相出題(AorB)?').upper()
    while 選擇 != "A" and 選擇!="B":
        選擇=input('想要(A)系統隨機出數字,(B)還是互相出題(AorB)?').upper()

    if 選擇=='A' :

        答案=RD.randint(int(範圍小),int(範圍大))

        
        if int(答案)<(int(範圍大)-int(範圍小))/2+int(範圍小):
            print('數字已經已經打好了!')
        elif int(答案)>(int(範圍大)-int(範圍小))/2+int(範圍小):
            print('數字已經打好了!!!')
        else :
            print('數字已經打好了!!')


        print(f'接下來請在{int(範圍小)}~{int(範圍大)}中猜數字喔')




        猜低=int(範圍小)
        猜高=int(範圍大)
    

        


        while  True:

            玩家一猜=input(f'玩家一請猜一個數字({int(猜低)}~{int(猜高)}):')
            while int(玩家一猜)<int(猜低) or int(玩家一猜)>int(猜高):
                print('''
                亂輸入系統都知道喔!請看清楚範圍
            
                ''')
                玩家一猜=input(f'玩家一請猜一個數字({int(猜低)}~{int(猜高)}):')


            if int(玩家一猜)==int(答案):
                print(f'''恭喜答對!玩家一贏了!
                答案是{答案}
                再次恭喜 玩家一贏得比賽
                ''')
                
                break
            elif int(猜低)-1<int(玩家一猜)<int(答案):
                del 猜低
                猜低=int(玩家一猜)
                print(f'''{猜低}~{猜高}之間
                
                    ''')
            elif  int(猜高)+1>int(玩家一猜)>int(答案):
                del 猜高
                猜高=int(玩家一猜)
                print(f'''{猜低}~{猜高}之間
                
                    ''')
            else :
                print('''
                亂輸入系統都知道喔!請看清楚範圍
            
                ''')
        


            玩家二猜=input(f'玩家二請猜一個數字({int(猜低)}~{int(猜高)}):')
            while int(玩家二猜)<int(猜低) or int(玩家二猜)>int(猜高):
                print('''
                亂輸入系統都知道喔!請看清楚範圍
            
                ''')
                玩家二猜=input(f'''玩家二請猜一個數字({int(猜低)}~{int(猜高)}):''')


            if int(玩家二猜)==int(答案):
                print(f'''恭喜答對!玩家二贏了!
                答案是{答案}
                再次恭喜 玩家二贏得比賽
                ''')
                break
            elif int(猜低)-1<int(玩家二猜)<int(答案):
                del 猜低
                猜低=int(玩家二猜)
                print(f'''{猜低}~{猜高}之間
                    
                    ''')
            elif  int(猜高)+1>int(玩家二猜)>int(答案):
                del 猜高
                猜高=int(玩家二猜)
                print(f'''{猜低}~{猜高}之間
                
                    ''')
            else :
                print('''
                亂輸入系統都知道喔!請看清楚範圍
            
                ''')

    else :
        玩家一=input(f'玩家一,輸入你想讓對方猜的數字({int(範圍小)}~{int(範圍大)}):')
        while int(玩家一)<int(範圍小) or int(玩家一)>int(範圍大):
            print('有人犯規!有人犯規!!!')
            del 玩家一
            玩家一=input(f'玩家一,輸入你想讓對方猜的數字({int(範圍小)}~{int(範圍大)}):')

        print('''
        




















        玩家二不要偷看玩家一的數字喔!!!  
        













        










        




        

        
        
        
        
        
        
        
        
        
        ''')



        if int(玩家一)<(int(範圍大)-int(範圍小))/2+int(範圍小):
            print('玩家一已經打好了!')
        elif int(玩家一)>(int(範圍大)-int(範圍小))/2+int(範圍小):
            print('玩家一已經打好了!!!')
        else :
            print('玩家一已經打好了!!')
    
        玩家二=input(f'玩家二,輸入你想讓對方猜的數字({int(範圍小)}~{int(範圍大)}):')
        while int(玩家二)<int(範圍小) or int(玩家二)>int(範圍大):
            print('有人犯規!有人犯規!!!')
            del 玩家二
            玩家二=input(f'玩家二,輸入你想讓對方猜的數字({int(範圍小)}~{int(範圍大)}):')



        print('''
        




















            玩家一不要偷看玩家二的數字喔!!!  
        
        


        




        






        




        

        
        
        
        
        
        
        
        
        
            ''')



        print(f'接下來請在{int(範圍小)}~{int(範圍大)}中猜對方的數字喔')




        一猜低=int(範圍小)
        一猜高=int(範圍大)
        二猜低=int(範圍小)
        二猜高=int(範圍大)

        if int(玩家二)<(int(範圍大)-int(範圍小))/2+int(範圍小):
            print('玩家二已經打好了!')
        elif int(玩家二)>(int(範圍大)-int(範圍小))/2+int(範圍小):
            print('玩家二已經打好了!!!')
        else :
            print('玩家二已經打好了!!')


        while  True:

            玩家一猜=input(f'玩家一請猜一個數字({int(一猜低)}~{int(一猜高)}):')
            while int(玩家一猜)<int(一猜低) or int(玩家一猜)>int(一猜高):
                print('''
                亂輸入系統都知道喔!請看清楚範圍
            
                ''')
                玩家一猜=input(f'玩家一請猜一個數字({int(一猜低)}~{int(一猜高)}):')


            if int(玩家一猜)==int(玩家二):
                print(f'''恭喜答對!玩家一贏了!
                玩家一的數字是:{玩家一}
                玩家二的數字是:{玩家二}
                再次恭喜 玩家一贏得比賽
                ''')
                break
            elif int(一猜低)-1<int(玩家一猜)<int(玩家二):
                del 一猜低
                一猜低=int(玩家一猜)
                print(f'''{一猜低}~{一猜高}之間
                
                    ''')
            elif  int(一猜高)+1>int(玩家一猜)>int(玩家二):
                del 一猜高
                一猜高=int(玩家一猜)
                print(f'''{一猜低}~{一猜高}之間
                
                    ''')
            else :
                print('''
                亂輸入系統都知道喔!請看清楚範圍
            
                    ''')
        


            玩家二猜=input(f'玩家二請猜一個數字({int(二猜低)}~{int(二猜高)}):')
            while int(玩家二猜)<int(二猜低) or int(玩家二猜)>int(二猜高):
                print('''
                亂輸入系統都知道喔!請看清楚範圍
            
                ''')
                玩家二猜=input(f'''玩家二請猜一個數字({int(二猜低)}~{int(二猜高)}):''')


            if int(玩家二猜)==int(玩家一):
                print(f'''恭喜答對!玩家二贏了!
                玩家一的數字是:{玩家一}
                玩家二的數字是:{玩家二}
                再次恭喜 玩家二贏得比賽
                ''')
                break
            elif int(二猜低)-1<int(玩家二猜)<int(玩家一):
                del 二猜低
                二猜低=int(玩家二猜)
                print(f'''{二猜低}~{二猜高}之間
                    
                    ''')
            elif  int(二猜高)+1>int(玩家二猜)>int(玩家一):
                del 二猜高
                二猜高=int(玩家二猜)
                print(f'''{二猜低}~{二猜高}之間
                
                    ''')
            else :
                print('''
                亂輸入系統都知道喔!請看清楚範圍
            
                ''')
    




                
                
                
                
函數() 


最後=input("還要在玩一次嗎(A)要(B)不要(AorB)?").upper()
while 最後=="A":
    函數()
    最後=input("還要在玩一次嗎(A)要(B)不要(AorB)?").upper()

time.sleep(5)            
            
                
