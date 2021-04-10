import turtle
screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
screen.bgcolor('black')
screen.screensize(1000,150)
turtle.color('yellow')
player1 = int(8000)
player2 = int(8000)
player1name = input("What is player 1's name?")
player2name = input("What is player 2's name?")
turtle.goto(-100, 0)
turtle.write("{}: {}".format(player1name,player1), align="center", font=("Courier", 20, "normal"))
turtle.goto(100,0)
turtle.write("{} : {}".format(player2name, player2), align="center", font=("Courier", 20, "normal"))

while True:
  add = input("Type 1 or 2 depending on which player is gaining a point : ")
  subtract = int(input("How much damage is subtracted (add a - in front of number if adding LP) : "))
  
  SUBTRACT = int(subtract * -1)
  if add == '1':
    turtle.clear()
    player1+=SUBTRACT
    turtle.goto(-100, 0)
    turtle.write("{}: {}".format(player1name,player1), align="center", font=("Courier", 20, "normal"))
    turtle.goto(100,.0)
    turtle.write("{} : {}".format(player2name, player2), align="center", font=("Courier", 20, "normal"))
  elif add == '2':
    player2+=SUBTRACT
    turtle.clear()
    player2+=1
    turtle.goto(-100, 0)
    turtle.write("{}: {}".format(player1name,player1), align="center", font=("Courier", 20, "normal"))
    turtle.goto(100,.0)
    turtle.write("{} : {}".format(player2name, player2), align="center", font=("Courier", 20, "normal"))
  else:
    print("Invalid")

  if player1 < 1:
    turtle.clear()
    turtle.goto(0,0)
    turtle.write("{} wins!".format(player2name), align="center", font=("Courier", 20, "normal"))
    
  elif player2 < 1:
    turtle.clear()
    turtle.goto(0,0)
    turtle.write("{} wins!".format(player1name), align="center", font=("Courier", 20, "normal"))