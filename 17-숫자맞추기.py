# 주어진 범위 내에서 숫자 하나가 컴퓨터의 의해 정해진다. (random)
# 사용자는 숫자를 맞출 때까지 게임을 계속한다.
# 만약에, 정답 숫자보다 사용자가 입력한 숫자가 클 경우는 "더 작은 숫자입니다"를 출력
# 만약에, 정답 숫자보다 사용자가 입력한 숫자가 작을 경우는 "더 큰 숫자입니다"를 출력
# 정답이면, "정답입니다"를 출력하고 게임이 종료
# 총 몇번 만에 정답을 맞췄는지 출력한다

import random

computer = random.randint(1,20)

score = 0

play = True
while play :
    score += 1

    user = int(input('숫자를 입력해 주세요(1~20):'))
    if computer == user:
        print(f'정답입니다 {score}번 만에 맞추었습니다')
        play = False

    else:
        if computer > user:
            print('더 큰 수 입니다')
        else:
            print('더 작은 수 입니다')
        
