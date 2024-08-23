# 1. 컴퓨터가 동전을 던지고 사용자가 동전을 앞, 뒤 면을 맞추는 게임을 코딩한다
# 2. 컴퓨터가 던져 앞면 혹은 뒷면에 나오게 하는 것은 random 함수를 사용
# 3. 사용자는 앞면인지 뒷면인지를 입력한다
# 4. 결과를 판정하여, 사용자가 동전의 면을 맞추거나 틀리면
#       '축하합니다
#       '애석합니다
# 5. 컴퓨터기 던진 동전이 앞면인지 뒷면인지 출력
#     사용자가 입력한것이 앞면인지 뒷면인지 출력


import random


menu = '''
0 : 앞
1 : 뒤
'''
print("\n동전 게임에 오신것을 환영합니다!")

# 컴퓨터가 동존을 던진다
computer = random.randint(0, 1)

# 사용자 값받기
print(menu)
user = int(input('동전의 앞, 뒤를 선택하세요 : '))

# 컴퓨터와 사용자의 선택을 출력해 준다.

if computer == 0:
    print('컴퓨터: 앞')
else:
    print('컴퓨터 : 뒤')

if computer == 0:
    print('you: 앞')
else:
    print('you : 뒤')

# 결과

if computer == user:
    print(f'애석합니다')
else:
    print(f'축하합니다.')











