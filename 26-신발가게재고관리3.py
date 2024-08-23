stock = {}

def read_size():
    f = open('신발재고.txt', 'r', encoding='utf8')
    lines = f.readlines()
    for line in lines:
        size, num = line.split(':')
        size = size.strip()
        num = int(num.strip())
        stock[size] = num
    f.close()

def write_size():
    f = open('신발재고.txt', 'w', encoding='utf8')
    for i in stock:
        data = f'{i} : {stock[i]}\n'
        f.write(data)
    f.close()

def display_size():
    for i in stock:
        print(f'{i}mm : {stock[i]}개')

read_size()

play = True
while play :
    menu = '''
    1 : 상품보기
    2 : 입고
    3 : 출고
    4 : 상품등록
    5 : 상품삭제
    6 : 종료
    '''
  
    print(menu)
    out_in = input('메뉴를 번호로 선택해 주세요:')
    if out_in == '1':
        display_size()
    elif out_in == '2':
        size, num = input('재고를 추가할 사이즈와 수량을 입력 하세요:').split()
        num = int(num)
        if size in stock:
            if stock[size] + num <= 30:
                stock[size] = stock[size] + num 
                write_size()
                display_size()
            else:
                print('30개를 초과 합니다.')
        else:
            print('없는 사이즈 입니다')
    elif out_in == '3':
        size, num = input('재고의 사이즈와 수량을 입력해 주세요:').split()
        num = int(num)
        if size in stock:
            if stock[size] >= num:
                stock[size] = stock[size] - num
                write_size()
                display_size()
            else:
                print('재고가 부족합니다.')
        else:
            print('없는 사이즈 입니다')
    elif out_in == '4':
        size = input(' 새로 등록할 상품의 사이즈를 입력하세요:')
        if size in stock:
            print('이미 존재하는 상품 입니다.')
        else:
            stock[size] = 0
            write_size()
            display_size()
    elif out_in == '5':
        size = input('삭제할 상품의 사이스를 입력하세요:')
        if size in stock:
            del stock[size]
            write_size()
            display_size()          
        else:
            print('없는 사이즈 입니다')
    elif out_in == '6':
        play = False