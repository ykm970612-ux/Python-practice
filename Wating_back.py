from collections import deque

waiting_list = deque()

def enqueue(name):
    waiting_list.append(name)
    print("대기열에 추가되었습니다.")

def dequeue():
    if not waiting_list :
        print("대기자가 없습니다.")
    else:
        print(f"{waiting_list.popleft()} 님 창구로 이동해주세요. -- 남은대기{len(waiting_list)}명")


while True:
    num = input("1:입장, 2:호출, 3:종료 -->")

    if num == "1":
        name = input("이름을 입력하세요 -->")
        enqueue(name)
    elif num == "2":
        dequeue()
    else:
        print("프로그램을 종료합니다")
        break
        

        








