#단순 if 문
print("---단순 if문---")
print("")

A = 10
if A == 10:
    print("A는 10입니다.")

#if else 문
print("")
print("---if else문---")
print("")

print("Notice: B는 7로 설정했습니다.")
print("")
B = 7

if B == 7:
    print("B는 7입니다.")
else:
    print("B는 7이 아닙니다.")

print("")
print("Notice: B는 8로 설정했습니다.")
print("")
B = 8

if B == 7:
    print("B는 7입니다.")
else:
    print("B는 7이 아닙니다.")

#if elif else 문
print("")
print("---if elif else문---")
print("")

print("Notice: C는 5로 설정했습니다.")
print("")
C = 5

if C < 6:
    print("C는 6보다 작습니다.")
elif C == 6:
    print("C는 6입니다.")
else:
    print("C는 6보다 큽니다.")

print("")
print("Notice: C는 6로 설정했습니다.")
print("")
C = 6

if C < 6:
    print("C는 6보다 작습니다.")
elif C == 6:
    print("C는 6입니다.")
else:
    print("C는 6보다 큽니다.")

print("")
print("Notice: C는 7로 설정했습니다.")
print("")
C = 7

if C < 6:
    print("C는 6보다 작습니다.")
elif C == 6:
    print("C는 6입니다.")
else:
    print("C는 6보다 큽니다.")
