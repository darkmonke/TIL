질문1 클래스에 정의된 함수 내에 들어가는 변수 'self'의 의미와 필요성
질문2 생성자와 소멸자 -- '__init__' 의미와 필요성
질문3 init 내에 정의된 변수 이름과 함수의 이름이 같아도 코드가 정상적으로 실행된다. 변수와 함수의 이름은 달라야 하는 것 아닌가?
질문4 복수의 인스턴스가 독립적으로 작동하게 하려면 코드를 어떻게 짜야 하는가?(아래 코드 참고)


# 1. 드럼 클래스 정의
import random

list_a = range(1, 6)
list_b = range(1, 16)
# 드럼의 각 구성 요소가 담긴 리스트를 사전에 정의해서 코드를 간단하게 만들 수도 있을 거 같음.
    
strength = random.choice(list_a)
set_up = random.choice(list_b)
    
volume = strength * set_up

class Drum:
    def __init__(snare, kick):
        self.snare = snare
        self.kick = kick
    
    def SNARE(self):
        print(volume)
        
    def KICK(self):
        print(volume)

# 드럼 객체 생성
D1 = Drum("스네어1", "킥1")
D2 = Drum("스네어2", "킥2")

# 연주 시뮬레이션 시작
print('연주 시작!!!')
while True:
    # D1 스네어, D1 킥
    print(f"{D1.snare}의 볼륨은 {volume}입니다.")
    
    print(f"{D1.kick}의 볼륨은 {volume}입니다.")
    
    # D2 스네어, D2 킥
    print(f"{D2.snare}의 볼륨은 {volume}입니다.")

    print(f"{D2.kick}의 볼륨은 {volume}입니다.")
    break
