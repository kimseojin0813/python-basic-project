# 1. 변수에 특정 비밀번호를 저장한다. 예) "A!1245"
# 2. 사용자로 부터 비밀번호를 입력 받는다.
# 3. 변수에 저장된 비밀번호와 입력한 번호가 같은지 여부에 대함 결과를 출력

passward = "A!12345"
a = input('비밀번호 : ')
if passward == a:
    print('일치치합니다.')
else:
    print('일치하지 않습니다.')