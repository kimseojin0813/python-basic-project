# 신발가게에 사이즈 별로 재고가 있습니다

# 240mm : 14
# 245mm : 20
# 250mm : 11
# 255mm : 14
# 260mm : 28
# 265mm : 32
# 270mm : 17
# 275mm : 9

# input을 통해 사이즈를 입력 받고 수량을 입력하면 : 한번에 input
# 기존의 재고에서 수량을 빼준다

# 재고가 부족하다면 재고가 부족하다고 말하고 현 재고 말하기


# 매번 주문을 실행하고 나면 모든 사이즈 재고 현황을 출력한다


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

size, num = input('사이즈와 사이즈 재고의 수량을 입력해 주세요:').split(',')
num = int(num)

if size in stock:
    if stock[size] >= num:

        stock[size] = stock[size] - num

        for i in stock:
            print(f'{i} : {stock[i]}개')
    else:
        print('재고가 부족합니다.')
else:
    print('재고가 없습니다')


































