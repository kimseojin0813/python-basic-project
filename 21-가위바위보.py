# 컴퓨터와 사용자가 가위바위보 게임을 한다
# 컴퓨터는 랜덤으로 가위바위보를 선택하고
# 사용자는 가위바위보를 입력한다

# 0 : 가위
# 1 : 바위
# 2 : 보

# 매 가위바위보 마다 컴퓨터는 무엇 사용자는 무엇을 냈는 말해서 판정한다
# 계속 y 
# 그만 N

# 최종값 출력
import random

c_win = 0
u_win = 0

game_list = ['가위', '바위', '보']

play = True
while play :

    user = int(input('가위바위보를 선택하시오 (0,1,2):'))

    computer = random.randint(0,2)

    print(f'컴퓨터: {game_list[computer]}, 사용자: {game_list[user]}')

    if computer == user :
        print('비겼습니다')
    elif (computer == 0 and user == 2) or (computer == 1 and user == 0) or (computer == 2 and user == 1):
        c_win += 1
        print('컴퓨터가 이겼습니다')
    else:
        u_win += 1
        print('사용자가 이겼습니다')

    go = input('게임을 계속하겠습니까? (y/n) : ')
    if go != 'y':
        play =False

print(f'컴퓨터 : {c_win}승, 사용자 : {u_win}승으로 게임이 종료 되었습니다')
