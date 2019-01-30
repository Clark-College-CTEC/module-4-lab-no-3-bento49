# Lab No. 3
# CTEC 121
# BENTON CHUN

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    circle1 = Circle(Point(400,150),50)
    circle2 = Circle(Point(400,300),100)
    circle3 = Circle(Point(400,600),200)

    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)


    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = Circle(Point(365,140),10)
    eye1.setFill('blue')
    eye2 = eye1.clone()
    eye2.move(65,0)
    eye1.draw(win)
    eye2.draw(win)

    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    nose = Polygon(Point(400,160),Point(400,175),Point(365,170))
    nose.setFill('orange')
    nose.draw(win)

    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(350,115),Point(450,80))
    hat.setFill('black')
    hat.draw(win)


    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    hatline = Line(Point(325,115),Point(475,115))
    hatline.setWidth(5)
    hatline.draw(win)

    #adding arms
    leftArm = Line(Point(300,300),Point(200,200))
    rightArm = Line(Point(500,300),Point(600,200))
    leftArm.setFill('brown')
    rightArm.setFill('brown')
    leftArm.setWidth(5)
    rightArm.setWidth(5)
    leftArm.draw(win)
    rightArm.draw(win)

    #and ground
    ground = Line(Point(0,795),Point(800,795))
    ground.setWidth(10)
    ground.setFill('green')
    ground.draw(win)


    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()