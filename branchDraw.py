#! -*-coding:utf-8 -*-
"""

"""
import turtle

def draw_true(branch_length):

    if branch_length > 5:
        if branch_length < 20:
            turtle.color('green')
        else:
            turtle.color("red")

        turtle.forward(branch_length)
        print("向前"+ str(branch_length))
        turtle.right(20)
        print("右转")
        draw_true(branch_length-15)
        turtle.left(40)
        print("左转40")
        draw_true(branch_length-15)
        turtle.right(20)
        print("右转20")
        turtle.backward(branch_length)
        print("返回"+str(branch_length))

def main():
    """
    主函数
    """

    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('red')
    draw_true(80)
    turtle.exitonclick()

if __name__ == '__main__':
    main()