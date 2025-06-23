import random

answer = random.randint(1 , 100)
guess = int(input("수를 입력하세요 : "))
count = 1

while guess!=answer:
    if(guess < answer):
        print("Up")
    elif(guess > answer):
        print("Down")
    count=count+1
    guess = int(input("수를 입력하세요 : "))

print("정답!", count, "번 만에 맞혔어요!")
