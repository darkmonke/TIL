# 로또 당첨 번호 복습
## 내가 작성한 코드
1. import random
lotto = list(range(1,46))
print(lotto)

==> 1부터 45까지 숫자가 포함된 리스트를 만든 후 무작위로 6개의 숫자를 뽑으려고 함.
==> 강사님은 for문을 활용해서 (무엇을?) 총 5번 반복하는 코드를 작성
==> 중요 아이디어: random 함수. 로또 번호들의 집합을 5번 반복하기

2. import requests

lotto_url = 'https://www.dhlottery.co.kr/common.do'
payload = {
    'method': 'getLottoNumber',
    'drwNo': 1159,
}
r = requests.get(lotto_url, params=payload)
print(r.url)
print(r.text)
lotto_dict = r.json()

print(payload["drwtNo6"])

==> payload 딕셔너리에서 로또 당첨 번호만 추출해서 리스트로 만들려고 했었음.
==> 이를 위해 payload 딕셔너리 속 로또 당첨 번호의 value값을 우선 추출하고, 리스트를 만들려고 했음.
==> 강사님은 우선 빈 저장공간(리스트)를 만듦. 이후 for문과 if문을 사용해 lotto_dict에서 로또 당첨 번호를 추출하고 이를 빈 저장공간에 저장함.
==> 중요 아이디어: 빈 공간 만들기, 'r.json()'

3. info = {'drwtNo6': 39,
       'drwtNo4': 28,
       'drwtNo5':38,
       'drwtNo2':9,
        'drwtNo3':27,
        'drwtNo1':3
}
==> 위와 같음.

4. list1 = [3, 9, 27, 28, 38, 39]

list2 = [32, 40, 5, 17, 28, 25]
list3 = [39, 44, 2, 25, 42, 18]
list4 = [19, 2, 42, 25, 20, 8]
list5 = [8, 38, 20, 16, 43, 15]
list6 = [28, 11, 40, 45, 1, 19]
==> 위와 같음.

5. for v in info.values():
    print(v)