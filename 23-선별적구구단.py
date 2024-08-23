#  사용자로 부터 입력을 받은 구구단의 단을 출력하되
# 곱셈의 결과가 홀수 혹은 짝수 혹은 전체를 선택하여 출력하도록 코딩




c = True
while c :
    a = int(input('원하는 구구단의 단을 입력하세요:'))
    b = input(f'{a}단의 답을 짝수/홀수/전체 중 선택하세요:')

       
# if b == '짝수':
#     for i in range(1,10):
#         print(f'{a} x {i} = {a * i }')
# if b == '홀수':
#     for i in range(1,10,2):
#         print(f'{a} x {i} = {a * i }')
# if b == '전체':
#     for i in range(1,10):
#         print(f'{a} x {i} = {a * i }')
        
    for i in range(1,10):
        result = a * i
        if b == '홀수':
            if result % 2 == 1:
                print(f'{a} x {i} = {a * i}')
        elif b == '짝수':
            if result % 2 == 0:
                print(f'{a} x {i} = {a * i}')
        elif b == '전체':
                print(f'{a} x {i} = {a * i}')
    go = input('계속하시겠습니까? : ')
    if go != 'y':
         c = False




