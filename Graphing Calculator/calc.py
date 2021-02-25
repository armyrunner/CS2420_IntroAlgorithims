from graphics import *
from math import *
import stack


def is_operator(char):
    
    if char == '*' or  char == '/' or char == '+' or char == '-' or char == '^':
        return True
    else:
        raise Exception(char," is not a symbol try using *,/,-,+! ")



# def is_precedence(char):
    
#     if char == '^':
#         return 3
#     elif char == '*' or  char == '/':
#         return 2
#     elif char == '+' or char == '-':
#         return 1
#     else:
#         return 0




def EvaluatePostfix(postfix,x):
    h = len(postfix)
    s = stack.Stack()

    for char in postfix:
        if char.isdigit():
            s.push(float(char))
        elif char in 'xX':
            s.push(x)
        elif char == '-':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs - rhs
            s.push(result)
        elif char == '+':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs + rhs
            s.push(result)
        elif char == '/':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs / rhs
            s.push(result)
        elif char == '*':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs * rhs
            s.push(result)
        elif char == '^':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs**rhs
            s.push(result)
        
    ans = s.pop()
    
    return ans




def InfixToPostfix(infix):


    expression = ""
    s = stack.Stack()

    # loop through all the the characters in the string
    for char in infix:
        if char == '(':
            s.push(char)
      
        elif char.isdigit(): # checks if there is a digit
            expression += char
        elif char.isalpha(): # checks if there is a letter
            expression += char
        elif char == '(':
            s.push(char)
        elif char == ')':
            while not s.is_empty() and s.top() != '(':
                expression += s.pop()
            if not s.is_empty() and s.top() != '(':
                return -1
            else:
                s.pop()
        elif is_operator(char):
            if char in '+-':
                while not s.is_empty() and s.top() != '(':
                    expression += s.pop()
                s.push(char)
            elif char in '*/':
                while not s.is_empty() and s.top() != '(':
                    if s.top() == '+' or s.top() == '-':
                        break
                    else:
                        expression += s.pop()
                s.push(char)
            elif char =='^':
                while not s.is_empty() and s.top() != '(' :
                    if s.top() == '+' or s.top() == '-'or s.top() == '*' or s.top() == '/':
                        break
                    else:
                        expression += s.pop()
                s.push(char)

    while not s.is_empty():
        expression += s.pop()

    return expression


def main():

    infix =  input("Enter your equation(ex: x*x or 3*x*x-2*x+5): ")
    postfix = InfixToPostfix(infix) # need to write this function

    points = []
    
    LOWX = -10
    HIGHX = +10
    LOWY = -10
    HIGHY = +10
    INC_X = .1

    x = LOWX
    while x <= HIGHX:
        y = EvaluatePostfix(postfix,x)  # need to write this function
        points.append( [x,y] )
        x += INC_X
        
    
    win = GraphWin("My Circle", 500, 500)
    win.setCoords(LOWX, LOWY, HIGHX, HIGHY)
    
    for i in range(len(points)-1):
        #c = Circle(Point(points[i][0], points[i][1]), .1)
        #c.draw(win)
        l = Line(Point(points[i][0], points[i][1]), Point(points[i+1][0], points[i+1][1]) )
        l.draw(win)        
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()


