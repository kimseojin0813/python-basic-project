import random


menu = '''
0 : 앞
1 : 뒤
'''
print("\n동전 게임에 오신것을 환영합니다!")

# 컴퓨터가 동존을 던진다
computer = random.randint(0, 1)
    

# 사용자 값받기
play = True
while play :


    print(menu)
    user = int(input('동전의 앞, 뒤를 선택하세요 : '))

# 컴퓨터와 사용자의 선택을 출력해 준다.

    if computer == 0:
        print('컴퓨터: 앞')
    else:
        print('컴퓨터 : 뒤')

    if user == 0:
        print('you: 앞')
    else:
        print('you : 뒤')

    # 결과

    if computer == user:
        print(f'축하합니다')
        play = False
    else:
        print(f'애석합니다.')










