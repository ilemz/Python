def plus():
    print "plus progress..."
    print "input number1"
    num1 = raw_input()
    print "input number2"
    num2 = raw_input()
    c = int(num1)+int(num2)
    return c

def minus():
    print "minus progress..."
    print "input number1"
    num1 = raw_input()
    print "input number2"
    num2 = raw_input()
    c = int(num1)-int(num2)
    return c

def times():
    print "times progress..."
    print "input number1"
    num1 = raw_input()
    print "input number2"
    num2 = raw_input()
    c = int(num1)*int(num2)
    return c

def divide():
    print "divide progress..."
    print "input number1"
    num1 = raw_input()
    print "input number2"
    num2 = raw_input()
    c = int(num1)/int(num2)
    return c

command = 1
while command != 0:
    value = 0
    print"input your command(1.plus, 2.minus, 3.times, 4.divide, 0.exit) :"
    command = raw_input()
    command = int(command)
    if(command == 1):
        value = plus()
    elif(command == 2):
        value = minus()
    elif(command == 3):
        value = times()
    elif(command == 4):
        value = divide()
    elif(command == 0):
        print "program is turning down"
    else:
        print "wrong input"

    print "value : " + str(value)
    print
