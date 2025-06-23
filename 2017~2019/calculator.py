def plus():
    print "input number1"
    num1 = raw_input()
    print "input number2"
    num2 = raw_input()
    c = int(num1)+int(num2)
    return c

command = 1
while command != 0:
    print"input your command(1.plus  ,0.exit) :"
          
    command = raw_input()
    command = int(command)
    if(command == 1):
        value = plus()
        print "value : " + str(value)
        print
