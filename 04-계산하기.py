# 1. input을 리룔하여 두개의 수를 입력 받는다(input 1번 사용)
# 2. 2개의수를 곱한 결과를 출력한다
# 3. 출력 예) '3과 4의 곱하기 결과는 12입니다.'

result = (input('두개의 숫자를 입력하시오:')).split()
a, b = result
print(f'{a}와 {b}의 곱하기 결과는 {int(a) * int(b)}입니다.')