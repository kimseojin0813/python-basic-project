stock = {
    '240mm' : 14,
    '245mm' : 20,
    '250mm' : 11,
    '255mm' : 14,
    '260mm' : 28,
    '265mm' : 32,
    '270mm' : 17,
    '275mm' : 9
}

size, num = input('재고를 추가할 사이즈와 몇개 추가 할지 입력해 주세요:').split(',')
num = int(num)

if size in stock:
    if stock[size] + num <= 30:

        stock[size] = stock[size] + num 

        for i in stock:
            print(f'{i} : {stock[i]}개')
    else:
        print('재고가 30개를 넘어 갑니다.')
else:
    print('재고가 없는 사이즈 입니다')


































