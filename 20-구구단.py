# 구구단의 단을 입력 받아서 아래와 같이 출력하는 프로그램을 작성하라
# 2를 입력하면
# 2 x 1 =2
#   .
#   .
#   .
#   .
#   .

# 계속 프로그램을 실행하게 한다
# 단, '프로그램을 종료하시겠습니까? : 'yes가 아니면 프로그램 종료

play = True
while play :
    user = int(input('원하는 구구단의 숫자를 입력하시오 : '))


    for i in range(1,10):
        print(f'{user} x {i} = {user * i}')
    
    go = input('계속 하겠습니까? (y/n) :')
    if go != 'y':
        play = False