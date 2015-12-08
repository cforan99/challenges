from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystr):
    # your code here
    reversed = ""
    string_stack = Stack()
    for char in mystr:
        string_stack.push(char)
    while not string_stack.isEmpty():
        last = string_stack.pop()
        reversed += last
    return reversed

testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
