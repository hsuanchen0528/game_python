

import math

while True:


    選擇=input('''
            
    (1) (a+b)^2 = a^2+2ab+b^2
    (2) (a-b) = a^2-2ab+b^2
    (3) a^2-b^2 = (a+b)(a-b)
    (4) (a+b)^3 = a^3+3a^2b+3ab^2+b^3
    (5) (a-b)^3 = a^3-3a^2b+3ab^2-b^3
    選擇公式:''')

    if 選擇=='1':
        a=float(input('a=  ?'))
        b=float(input('b=  ?'))
        print(f'''
    ({a}+{b})
    ={a}^2+2*{a}*{b}+{b}^2
    ={a**2+2*a*b+b**2}


    ''')


    elif 選擇=='2':
        a=float(input('a=  ?'))
        b=float(input('b=  ?'))
        print(f'''
    ({a}-{b})
    ={a}^2-2*{a}*{b}+{b}^2
    ={a**2-2*a*b+b**2}


    ''')



    elif 選擇=='3':
        a=float(input('a=  ?'))
        b=float(input('b=  ?'))
        print(f'''
    ({a}^2-{b}^2)
    =({a}+{b})({a}-{b})
    ={a**2-b**2}


    ''')



    elif 選擇=='4':
        a=float(input('a=  ?'))
        b=float(input('b=  ?'))
        print(f'''
    (a+b)^3 
    ={a}^3+3*{a}^2*{b}+3*{a}*{b}^2+{b}^3
    ={math.pow(a, 3)+3*math.pow(a, 2)*b+3*a*math.pow(b, 2)+math.pow(b, 3)}


    ''')
        

    else:
        a=float(input('a=  ?'))
        b=float(input('b=  ?'))
        print(f'''
    (a-b)^3 
    ={a}^3-3*{a}^2*{b}+3*{a}*{b}^2-{b}^3
    ={math.pow(a, 3)-3*math.pow(a, 2)*b+3*a*math.pow(b, 2)-math.pow(b, 3)}


    ''')