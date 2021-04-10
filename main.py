import turtle

wn = turtle.Screen()
turtle = turtle.Turtle()

turtle.hideturtle()
wn.bgcolor('black')
wn.setup(width=1500, height=500)
turtle.color('sky blue')
player1 = int(8000)
player2 = int(8000)
player1name = input("What is player 1's name?")
player2name = input("What is player 2's name?")
turtle.goto(-200, 0)
turtle.write("{}: {}".format(player1name,player1), align="center", font=("Courier", 40, "normal"))
turtle.goto(200,0)
turtle.write("{} : {}".format(player2name, player2), align="center", font=("Courier", 40, "normal"))

while True:
  add = input("Type 1 or 2 depending on which player is gaining a point : ")
  subtract = int(input("How much damage is subtracted (add a - in front of number if adding LP) : "))
  
  SUBTRACT = int(subtract * -1)
  if add == '1':
    turtle.clear()
    player1+=SUBTRACT
    turtle.goto(-200, 0)
    turtle.write("{}: {}".format(player1name,player1), align="center", font=("Courier", 40, "normal"))
    turtle.goto(200,0)
    turtle.write("{} : {}".format(player2name, player2), align="center", font=("Courier", 40, "normal"))
  elif add == '2':
    player2+=SUBTRACT
    turtle.clear()
    player2+=1
    turtle.goto(-200, 0)
    turtle.write("{}: {}".format(player1name,player1), align="center", font=("Courier", 40, "normal"))
    turtle.goto(200,.0)
    turtle.write("{} : {}".format(player2name, player2), align="center", font=("Courier", 40, "normal"))
  else:
    print("Invalid")

  if player1 < 1:
    turtle.clear()
    turtle.goto(0,0)
    turtle.write("✨{} wins!✨".format(player2name), align="center", font=("Courier", 100, "normal"))
    
  elif player2 < 1:
    turtle.clear()
    turtle.goto(0,0)
    turtle.write("✨{} wins!✨".format(player1name), align="center", font=("Courier", 100, "normal"))