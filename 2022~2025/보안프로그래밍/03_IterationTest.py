#5번 반복하는 반복문 만들기

#For문
print("for문 : 5번 반복")
for i in range(0,5):
    print(i)

#While문
print("")
print("while문 : 5번 반복")
iter = 1
while(1):
    print(iter)
    iter = iter + 1
    if iter > 4:
        break

#반복문 중첩 예제
#반복문 안에 반복문 중첩사용
#구구단 출력하기

#for문 중첩사용
print("")
print("for문 중첩사용: 구구단 출력")
for i in range(1,10):
    print(i, '단')
    print("")
    for j in range(1, 10):
        print(i, " * ", j, " = ", i*j)
    print("")


#while문 중첩사용
print("")
print("while문 중첩사용: 구구단 출력")
iter1 = 1
while(1):
    print(iter1, '단')
    print()
    iter2 = 1
    while(1):
        print(iter1, " * ", iter2, " = ", iter1*iter2)
        iter2 = iter2 + 1
        if iter2 > 10:
            break
    print("")
    iter1 = iter1 + 1
    if iter1 > 10:
        break

#for문과 while문은 상호 호환이 가능합니다.