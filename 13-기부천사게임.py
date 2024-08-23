# 1. 기부금을 입력합니다.
# 2. 퀴즈를 맞힐 때마다 기부금이 2배가 된다
# 3. 퀴즈를 못 맞히면 원래 기부한 금액만 기부가 된다.

import random

print('''
     기부천사 게임에 오신 것을 환영합니다.
      퀴즈를 맞힐 때마다 기부 금액이 2배가 됩니다.
      퀴즈를 맞추지 못하면, 원래 기부금만 기부 됩니다.
''')

asd = int(input('기부금액을 입력하세요:'))
print(f'총 {asd}원을 기부 하셨습니다.')
print('지금부터 퀴즈 나갑니다.')
qwe1 = int(input('세 갈래 길이 있습니다. 하나를 선택해 주세요(1, 2, 3) :'))
winning_num = random.randint(1,3)

if qwe1 == winning_num:
    asd *= 2
    print(f'정답입니다. 기부금액이 {asd}로 2배로 늘었습니다')

    go = input('계속 도전 하겠습니까? (y/n) : ').lower()
    if go == 'y':
        qwe2 = int(input('세개의 문 중 몇번째 문을 통과 겠습니까?: (1, 2, 3)'))
        winning_num = random.randint(1,3)
        if qwe1 == winning_num:
            asd *= 2
            print(f'정답입니다. 기부금액이 {asd}로 2배로 늘었습니다')
        else:
            print('틀렸습니다')
    else:
        pass
else:
    print('틀렸습니다')

print('=' * 80)
print(f'당신의 총 기부 금액은{asd}입니다')