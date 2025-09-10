class HelloMessage:
    def show():
        helloMsg = 'Hello Programming World'
        print(helloMsg)
        courseMsg = "Programming Principles with Python"
        print(courseMsg)
        courseNo = 10004
        print('#prog', courseNo, sep='')        

#use the class and its method defined above
msg = HelloMessage()
msg.show()
