from turtle import *
s=Screen()
setup(750,850)
s.bgcolor("#A0CF6E")
t=Turtle()
t.speed(30)

# t.pencolor("")
# t.pensize(20)
t.penup()
t.goto(0,-300)
t.pendown()
#COLOR OF COMPUTER
t.pensize(6)
t.pencolor("#CDD977")

t.fillcolor("#E9F2A7")
t.begin_fill()
#OUTSIDE computer
t.setheading(0)
t.fd(60)
t.setheading(90)
t.fd(25)
t.setheading(180)
t.fd(30)
t.setheading(90)
t.fd(25)
t.setheading(0)
t.fd(120)
t.setheading(90)
t.fd(150)
t.setheading(180)
t.fd(100)
t.up()
t.fd(100)
t.down()
t.fd(100)

t.setheading(270)
t.fd(150)
t.setheading(0)
t.fd(120)
t.setheading(270)
t.fd(25)
t.setheading(180)
t.fd(30)
t.setheading(270)
t.fd(25)
t.setheading(0)
t.fd(60)
t.end_fill()


#inside computer

t.up()
t.goto(50,-120)
t.down()
t.pensize(3)
t.fillcolor('#CCFFFF')
t.begin_fill()
t.fd(80)
t.setheading(270)
t.fd(110)
t.setheading(180)
t.fd(260)
t.setheading(90)
t.fd(110)
t.setheading(0)
t.fd(200)
t.end_fill()
# small rect insid computer
t.up()
t.goto(-40,-170)
t.down()

t.setheading(180)
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.fd(75)
t.setheading(90)
t.fd(40)
t.setheading(0)
t.fd(75)
t.setheading(270)
t.fd(40)
t.end_fill()
# inside square for code
t.penup()
t.goto(-60,-165)
t.pendown()
t.setheading(55)
t.pencolor("white")
t.fd(20)
t.setheading(150)
t.fd(20)
t.penup()
t.goto(-90,-165)
t.pendown()
t.setheading(145)
t.fd(20)
t.setheading(55)
t.fd(20)
t.penup()
t.goto(-70,-165)
t.pendown()
t.setheading(120)
t.fd(35)
t.penup()
t.goto(45,-100)
t.pendown()
t.setheading(0)
t.pencolor("#046307")
def leaf():
    t.fillcolor("#6AA121")
    t.begin_fill()
    t.circle(40,90)
    t.fd(40)
    t.lt(127)
    t.fd(40)
    t.circle(40,90)
    t.end_fill()

# leaf()

t.penup()
t.goto(40,-70)
t.setheading(15)
t.pendown()
leaf()

t.penup()
t.goto(0,-70)
t.setheading(35)
t.pendown()
leaf()


t.penup()
t.goto(-40,-70)
t.setheading(45)
t.pendown()
leaf()








# leaf()

t.penup()
t.goto(30,-100)
t.pendown()
t.setheading(35)
leaf()

t.penup()
t.goto(-10,-100)
t.pendown()
t.setheading(40)
leaf()

t.penup()
t.goto(-35,-100)
t.pendown()
t.setheading(55)
leaf()



t.penup()
t.goto(50,-100)
t.pendown()
t.setheading(10)
leaf()






# temprature item
t.penup()
t.goto(250,50)
t.pendown()
t.pencolor("black")
t.fillcolor("#C2E5D3")
t.pensize(3)
t.begin_fill()
t.setheading(90)
t.fd(100)
t.setheading(180)
t.fd(100)
t.setheading(270)
t.fd(100)
t.setheading(0)
t.fd(100)
t.end_fill()
# x=t.position()
# print(x)
t.penup()
t.goto(200,70)
t.pendown()
t.circle(10,180)
t.setheading(90)
t.fd(40)
t.circle(5,180)
t.setheading(270)
t.fd(40)
t.setheading(180)
t.circle(10,180)
t.fd(10)
t.pencolor("green")
t.penup()
t.goto(195,75)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.circle(5,360)
t.end_fill()
t.setheading(90)
t.pensize(3)
t.fd(50)
t.penup()
t.goto(230,120)
t.pendown()
t.setheading(270)
t.fd(40)
t.setheading(0)
t.fd(10)
t.setheading(225)
t.fd(15)
t.setheading(135)
t.fd(15)
t.setheading(0)
t.fd(10)
t.setheading(90)
t.fd(40)


# wifi item 

t.penup()
t.goto(-165,50)
t.pendown()
t.pencolor("black")
t.fillcolor("#F2A2E8")
t.pensize(3)
t.begin_fill()
t.setheading(90)
t.fd(100)
t.setheading(180)
t.fd(100)
t.setheading(270)
t.fd(100)
t.setheading(0)
t.fd(100)
t.end_fill()

t.pensize(1)
t.pencolor("black")
t.penup()
t.goto(-210,85)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(3,360)
t.end_fill()
t.setheading(90)
t.penup()
t.pensize(3)
t.goto(-220,90)
t.pendown()
t.setheading(270)
t.circle(10,-180)

setheading(90)
t.penup()
t.pensize(3)
t.goto(-225,95)
t.pendown()
t.setheading(270)
t.circle(15,-180)

setheading(90)
t.penup()
t.pensize(3)
t.goto(-230,100)
t.pendown()
t.setheading(270)
t.circle(20,-180)
t.penup()
t.goto(-220,60)
t.setheading(0)
t.write("wifi",False,"left",["sans serif",13,"bold"])

# ELECTRICITY item #
t.penup()
t.goto(-200,-300)
t.pendown()
t.pencolor("black")
t.fillcolor("#F9AB7B")
t.pensize(3)
t.begin_fill()
t.setheading(90)
t.fd(100)
t.setheading(180)
t.fd(100)
t.setheading(270)
t.fd(100)
t.setheading(0)
t.fd(100)
t.end_fill()

t.penup()
t.setheading(180)
t.fd(70)
t.setheading(90)
t.fd(40)
t.pendown()
t.fillcolor('brown')
t.begin_fill()
t.fd(30)
t.setheading(0)
t.fd(10)
t.setheading(270)
t.fd(15)
t.setheading(0)
t.fd(10)
t.setheading(90)
t.fd(15)
t.setheading(0)
t.fd(10)
t.setheading(270)
t.fd(30)
t.setheading(180)
t.fd(30)
t.backward(15)
t.end_fill()
t.pensize(5)


t.setheading(270)
t.fd(30)
t.setheading(0)
t.fd(20)

#### HISTO ####

t.penup()
t.goto(300,-300)
t.pendown()
t.pencolor("black")
t.fillcolor("#9172EC")
t.pensize(3)
t.begin_fill()
t.setheading(90)
t.fd(100)
t.setheading(180)
t.fd(100)
t.setheading(270)
t.fd(100)
t.setheading(0)
t.fd(100)
t.end_fill()





t.back(10)

t.up()
t.setheading(90)
t.fd(80)
t.down()

t.fillcolor("red")
t.begin_fill()
t.setheading(180)
t.fd(10)
t.setheading(270)
t.fd(60)
t.setheading(0)
t.fd(10)
t.setheading(90)
t.fd(60)
t.end_fill()

t.back(60)
t.up()
t.setheading(0)
t.back(20)
t.down()


t.fillcolor("yellow")
t.begin_fill()
t.setheading(90)
t.fd(40)
t.setheading(180)
t.fd(10)
t.setheading(270)
t.fd(40)
t.setheading(0)
t.fd(10)
t.end_fill()


t.up()
t.back(20)
t.down()


t.fillcolor("blue")
t.begin_fill()
t.setheading(180)
t.fd(8)
t.setheading(90)
t.fd(30)
t.setheading(0)
t.fd(8)
t.setheading(270)
t.fd(30)
t.setheading(0)
t.end_fill()

t.up()
t.back(18)
t.down()

t.fillcolor("green")
t.begin_fill()
t.setheading(180)
t.fd(7)
t.setheading(90)
t.fd(20)
t.setheading(0)
t.fd(7)
t.setheading(270)
t.fd(20)
t.end_fill()


t.up()
t.fd(10)
t.setheading(0)
t.back(18)
t.down()

t.fd(80)

t.setheading(45)







# =========================cloud============================


t.up()
t.goto(100,320)
t.down()

t.pencolor("#CCFFFF")

t.fillcolor("#CCFFFF")
t.begin_fill()
t.circle(50,360)
t.end_fill()


t.up()
t.setheading(180)
t.fd(70)
t.down()
t.fillcolor("#CCFFFF")
t.begin_fill()
t.circle(60,360)
t.end_fill()

t.fillcolor("#CCFFFF")
t.begin_fill()
t.circle(70,360)
t.end_fill()

#==========================Title===================


t.up()
t.goto(100,300)
t.down()
t.setheading(0)
t.pencolor("green")
t.write("G R E E N",False,"right",["display",35,"bold"])
t.up()
t.setheading(270)
t.fd(70)
t.setheading(0)
t.fd(80)
t.down()
t.write("C O M P U T I N G",False,"right",["display",35,"bold"])




done()
























































































































































































































































