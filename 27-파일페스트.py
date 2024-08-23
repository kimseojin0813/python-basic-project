size, num = input('사이즈와 수량을 입력하세요:').split()
num = int(num)

f = open('신발재고.txt', 'a', encoding= 'utf8')
data = f'{size}: {num} \n'
f.write(data)
f.close()

f = open('신발재고.txt', 'r', encoding='utf8')
lines = f.readlines()
for line in lines:
    size, num = line.split(':')
    size = size.strip()
    num = num.strip()
    print(f'{size}mm : {num}개')
f.close()

stock = {
    '240' : 14,
    '245' : 20,
    '250' : 11,
    '255' : 14,
    '260' : 28,
    '265' : 32,
    '270' : 17,
    '275' : 9
}

f = open('신발재고.txt', 'w', encoding= 'utf8')
for size,num in stock.items():
    data = f'{size} : {num} \n'
    f.write(data)
f.close()