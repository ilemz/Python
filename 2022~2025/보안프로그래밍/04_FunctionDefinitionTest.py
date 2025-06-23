#덧셈의 결과를 출력하고 반환 하는 함수 구현/사용하기

#함수 구현
def sum_print(x,y):
    k = x + y

    print("function print")
    print(x, ' + ', y, ' = ', k)  #덧셈의 결과 출력
    return k #덧셈의 결과 반환

#함수 사용
a = 1
b = 2
print("---Test 1---")
print("c = a + b -> 3 = 1 + 2")
print("---함수 호출---")
c = sum_print(a, b)

print("---저장된 c값 확인---")
print("c = ", c)

print("")
print("---Test 2---")
print("d = b + c -> 5 = 2 + 3")
print("---함수 호출---")
d = sum_print(b, c)

print("---저장된 d값 확인---")
print("d = ", d)

#한번 함수를 구현 하면 여러번 반복 사용할 수 있다.