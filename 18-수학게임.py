# 컴퓨터가 세개의 임의의 숫자를 선택한다.
# 사용자는 숫자 3개로 num1 * num2 - num3 식의 정답을 맞추면 된다
# 각 숫자의 범위는1,9까지 입니다
# 정답을 맞출때 마다 점수가 1씩 오른다
# 정답이 틀릴때까지 게임은 계속된다
# 숫자가 3, 2, 1 일 경우에 화면에 다음과 같이 출력하고 사용자로 부터 정답을 입력 받는다
# 3 * 2 - 1 =





import random 
import time


score = 0

play = True
while play : 
    start_time = time.time()
    num1 = random.randint(1,12)
    num2= random.randint(1,12)
    num3 = random.randint(1,12)
    user = int(input(f'{num1} x {num2} - {num3} = '))
    end_time = time.time()
    if end_time - start_time > 10:
        print(f'시간이 초과 되었습니다. 정답은{num1 * num2 - num3}입니다')
        play = False
    else:

        if num1 * num2 - num3 == user:
            score += 1
            print('정답입니다')
        else:
            print(f'틀렸습니다 정답은{num1 * num2 - num3}입니다 ')
            play = False
print(f'점수는 {score}점 입니다')













































