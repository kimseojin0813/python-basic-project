# 사용자로 부터 시작 숫자와 종료 숫자를 두개 입력 받는다
# 예 1 10


# 두 숫자 사이의 모든 값을 함해서 결과를 출력한다.



num1,num2 = input('숫자를 두개 입력해 주세요').split(' ')
num2 = int(num2)
num1 = int(num1)

total = 0
for i in range(num1, num2 + 1):
    total += i
print(total)
    





















