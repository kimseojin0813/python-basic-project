# 1. 부산에서 서울을 갑니다.
# 2. 먼저 부모님에게서 여비를 입력 받습니다.
# 3. 부산에서 서울을 가는 교통편은 다음과 같다
#   비행기 : 90000
#   ktx : 65000
#   고속버스 : 35000

# 4. 목적지까지
#   지하철 : 1700
#   택시 : 6700

#여비에 최소 금액 : 36700

# 여비에 따라, 가장 편안한 교통편을 선택하고, 남은금액 출력  


money = int(input('여비를 입력해 주세요:'))

remain = 0
method = ""

if money < 35000 + 1700:
    print('여비가 부족합니다')
else:
    if money >= 90000 + 6700:
        remain = money - 90000 - 6700
        method = '비행기, 택시'
    elif money >= 90000 + 1700:
        remain = money - 90000 - 1700
        method = '비행기, 지하철'
    elif money >= 65000 + 6700:
        remain = money - 65000 - 6700
        method = 'KTX, 택시'
    elif money >= 65000 + 1700:
        remain = money - 65000 - 1700
        method = 'KTX, 지하철'
    elif money >= 35000 + 6700:
        remain = money - 35000 - 6700
        method = '고속버스, 택시'
    elif money >= 35000 + 1700:
        remain = money - 35000 - 1700
        method = '고속버스, 지하철'

print(f'{method}(을/를) 타고 갑니다 남은 돈은 {remain}원 입니다.')
    


























