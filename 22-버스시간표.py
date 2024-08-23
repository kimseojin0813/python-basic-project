# 버스의 시간표를 작성하는 프로그램을 코딩
# 첫 운행 : 오전 9:00
# 마지막 운행 : 오후 6:00
# 9 ~ 18시(9와 18시가 포함)

# 배차 간격을 입력(분 단위) 하루에 버스 운핸 시간을 출력하라
# 예) 25

# 프로그램은 반복되게 하며,
# 계속하시겠습니까? (y/n), y면 계속 n면 종료

play = True
while play:
    user = int(input('배차 간격 입력:'))

    hour = 9
    min = 0

    loop = True
    while loop:
        min = min + user
        if min >= 60:
            hour += 1
            min = min - 60

        
        if hour == 18 and min > 0:
            loop = False
        else:
            print(f'{hour}시 {min}분')

    go_stop = input('버스 배차 시간을 계속 계산 하시겠습니까?:')
    if go_stop != 'y':
        play = False


