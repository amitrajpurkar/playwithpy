from graphics import *


def main():
  win = GraphWin("My Circle", 500, 500)
  c = Circle(Point(100,100), 40)
  c.setOutline("#ccff99")
  c.setWidth(10)
  c.setFill("#ffcc00")


  c.draw(win)
  win.getMouse() # pause for click in window
  win.close()


main()