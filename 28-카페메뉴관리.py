# 카페의 메뉴를 관리하는 프로그램
# 메뉴 관리 기능은
# 1. 메뉴출력
# 2. 메뉴추가
# 3. 메뉴삭제
# 4. 메뉴이름변경
# 5. 종료

# 카페의 초기메뉴
# 리스트로, ['사과', '당근', '망고'] 이다 ['사과쥬스', '당근쥬스', '망고쥬스']

# 각 기능을 선택한 다음, 각 기능을 구현함

menu =  '''
- 메뉴 관리 -
1. 메뉴출력
2. 메뉴추가
3. 메뉴삭제
4. 메뉴이름변경
5. 종료
'''
cafa = ['사과', '당근', '망고']

play = True
while play:
    print(menu)
    selsct =  input('기능을 선택하세요 : ')

    if selsct == '1':
        for i in cafa:
            print(f'{i}주스')
    elif selsct == '2':
        asd = input(' 새로 등록할 상품을 입력하세요:')
        if asd in cafa:
            print('이미 존재하는 상품 입니다.')
        else:
            cafa.append(asd)
    elif selsct == '3':
        qwe = input('삭제할 상품을 입력하세요:')
        if qwe in cafa: 
            cafa.remove(qwe)        
    elif selsct == '4':
        before = input('이름을 변경할 음료를 입력해 주세요:')
        after = input('변경된 이름을 입력해 주세요:')
        idx = -1
        for i in cafa:
            idx += 1    
            if i == 'before':
                break

        if idx == -1:
            print('없는 메뉴 입니다')
        else:
            cafa[idx] = after

    elif selsct == '5':
        play = False