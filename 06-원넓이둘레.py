# 1. 반지름을 입력 받아서 원의 넓이와 둘레를 계산하여 출력하라
# 2. 출력 예) 
#       '원의 면적은 : 000입니다
#       '원의 둘레는 : 000입니다
# 3. 원의 면적과 둘레는 소수점 2자리 까지만 출력하기

a = float(input('반지름을 입력 : '))
result = 2 * a * 3.14
result2 = a **2 * 3.14
print(f'원의 면적은: {result2:0.2f}입니다.')
print(f'원의 둘레는: {result:0.2f}입니다.')