# 신장과 체중을 입력하면 비만도 계산
# 비만도 기준
# 18.5:저체중
# 23 미만: 정상
# 25 미만: 과체중
# 25 이상: 비만
# 입력한 결과에 대한 비만도 판정 결과를 판정


height = float(input('키(cm)를 입력하세요:'))
weight = float(input('몸무게(kg)을 입력하세요:'))
bmi = weight / (height * height) * 10000
if bmi < 18.5:
    print('저체중')
elif bmi < 23:
    print('정상')
elif bmi < 25:
    print('과체중')
else:
    print('비만')



