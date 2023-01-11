import threading
import time
import tkinter
import random
import sys
import os

gameOver = False
score = 0
squaresToClear = 0
bombfield = []

print("You will have 200 seconds to find all the safe squares!")

def play_bombdodgger():
  create_bombfield(bombfield)
  window = tkinter.Tk()
  layout_window(window)
  window.mainloop()

  
def create_bombfield(bombfield):
  global squaresToClear
  for row in range(0,10):
    rowList = []
    for column in range(0,10):
      if random.randint(1,100) < 20:
        rowList.append(1)
      else:
        rowList.append(0)
        squaresToClear = squaresToClear + 1
    bombfield.append(rowList)
  printfield(bombfield)

def printfield(bombfield):
  for rowList in bombfield:
    print(rowList)

def layout_window(window):
  for rowNumber, rowList in enumerate(bombfield):
    for columnNumber, columnEntry in enumerate(rowList):
      if random.randint(1,100) < 25:
        square = tkinter.Label(window, text = "    ", bg = "darkgreen")
      elif random.randint(1,100) > 75:
        square = tkinter.Label(window, text = "    ", bg = "seagreen")
      else:
        square = tkinter.Label(window, text = "    ", bg = "green")
      square.grid(row = rowNumber, column = columnNumber)
      square.bind("<Button-1>", on_click)

def on_click(event):
  global score
  global gameOver
  global squaresToClear
  square = event.widget
  row = int(square.grid_info()["row"])
  column =int(square.grid_info()["column"])
  currentText=square.cget("text")
  if gameOver==False:
    if bombfield[row][column]==1:
      gameOver=True
      square.config(bg="red")
      print("Game Over! You hit a bomb!")
      print("Your score was:", score)
      playAgain()
    elif currentText=="    ":
      square.config(bg="brown")
      totalBombs=0

      if row<9:
        if bombfield[row+1][column]==1:
          totalBombs=totalBombs+1

      if row>0:
        if bombfield[row-1][column]==1:
          totalBombs=totalBombs+1

      if column>0:
        if bombfield[row][column-1]==1:
          totalBombs=totalBombs+1

      if column <9:
        if bombfield[row][column+1]==1:
          totalBombs=totalBombs+1

      if row>0 and column>0:
        if bombfield[row-1][column-1]==1:
          totalBombs=totalBombs+1

      if row<9 and column>0:
        if bombfield[row+1][column-1]==1:
          totalBombs=totalBombs+1

      if row >0 and column <9:
        if bombfield[row-1][column+1]==1:
          totalBombs=totalBombs+1

      if row <9 and column <9:
        if bombfield[row+1][column+1]==1:
          totalBombs=totalBombs+1

      square.config(text = " " + str(totalBombs) + " ")
      squaresToClear = squaresToClear - 1
      score = score + 1
      if squaresToClear == 0:
        gameOver = True
        print("Well done! You found all the safe squares!")
        print("You score was:", score)
        playAgain()

def trigger():
    time.sleep(200)
    print("Time is up!")
    print("You score was:", score)
    playAgain()

thread = threading.Thread(target=trigger)
thread.daemon = True
thread.start()

def playAgain():
  PLAG = input("do you wish to play again? Yes or No").upper()
  if PLAG == "YES" :
    os.execl(sys.executable, sys.executable, * sys.argv)
  elif PLAG == "NO":
    print("Bye!")
  else:
    print("Sorry, you did not enter yes or no.")

play_bombdodgger()  

