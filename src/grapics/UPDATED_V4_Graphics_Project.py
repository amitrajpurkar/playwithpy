"""OVERVIEW OF THE GRAPHICS PROJECT:
The image is of a living room of a Northern home during Autumn/Fall. There is a fireplace which is giving
heat to the cat sitting in one of the chairs. There is also a cup of fresh tea, a functioning clock, a
bookshelf with books and a couple of frames. The sill above the fireplace has a vase of flowers, some
books, candles, and a plant. There are 2 large windows next to each other with curtains, and there is a
lamp."""

        # PARENT VARIABLE  -->   w = Rectangle(Point(0,567), Point(1078, 0))
        #w = Rectangle(Point(100, 567), Point(1078, 0)) # main wall > Space on right
        #w = Rectangle(Point(0, 567), Point(1078, 100)) # main wall > Space on top
        #w = Rectangle(Point(0, 467), Point(1078, 0)) # main wall > Space on bottom
        #w = Rectangle(Point(0, 567), Point(978, 0)) # main wall > Space on left


#
#
#                                 MOTION, MOVEMENT, AND ANIMATION NOTES
#
#
#
#       #move right or down - positive
#       #move left or up - negative
#for i in range(10):
#    head.move(10,0)
#    arm.move(10,0)
#    arm2.move(10,10)
#    ...
#    apple.move(0,10)
#    stem.move(0,10)
#    for j in range(9000000):  -->  number in range changes speed
#        t=0





#                                                                        LABELS FOR YOUR SHAPES AND IMAGES



from graphics import *

def main():
    win = GraphWin("Living Room", 1078, 567)
    wall = Rectangle(Point(0, 459), Point(1078, 0)) #                      Main wall
    wall.draw(win)
    wall.setOutline("#E0A9A0")
    wall.setFill("#E0A9A0")
    floor = Rectangle(Point(0, 567), Point(1078, 472)) #                   Flooring
    floor.draw(win)
    floor.setOutline("#D49F88")
    floor.setFill("#D49F88")
    WindowPanelSHADOW = Rectangle(Point(500, 379), Point(838, 87)) #      The Shadow from the Window Panel Frame
    WindowPanelSHADOW.draw(win)
    WindowPanelSHADOW.setOutline("#8C6A64")
    WindowPanelSHADOW.setFill("#8C6A64")
    WindowPanelFrame = Rectangle(Point(500, 365), Point(838, 87)) #       Window Panel Frame
    WindowPanelFrame.draw(win)
    WindowPanelFrame.setOutline("#C7835E") 
    WindowPanelFrame.setFill("#C7835E")
    WINDOWPANEL = Rectangle(Point(520,350), Point(818,95)) #              Window Panel
    WINDOWPANEL.draw(win)
    WINDOWPANEL.setOutline("#875940")
    WINDOWPANEL.setFill("#875940")
    Glass1 = Rectangle(Point(564, 180), Point(606,110)) #                 Glass 1 = Top-most left glass
    Glass1.draw(win)
    Glass1.setOutline("#51769E")
    Glass1.setFill("#51769E")
    Glass2 = Rectangle(Point(564, 260), Point(606,187)) #                 Glass 2 = Glass below Glass 1
    Glass2.draw(win)
    Glass2.setOutline("#71A4DB")
    Glass2.setFill("#71A4DB")
    Glass3 = Rectangle(Point(564,340), Point(606, 268)) #                 Glass 3 = Glass below Glass 2
    Glass3.draw(win)
    Glass3.setOutline("#9BD4ED")
    Glass3.setFill("#9BD4ED")
    Glass4 = Rectangle(Point(656,180), Point(613,110)) #                  Glass 4 = Glass to the right of Glass 1
    Glass4.draw(win)
    Glass4.setOutline("#51769E")
    Glass4.setFill("#51769E")
    Glass5 = Rectangle(Point(656,260), Point(613,187)) #                  Glass 5 = Glass to the right of Glass 
    Glass5.draw(win)
    Glass5.setOutline("#71A4DB")
    Glass5.setFill("#71A4DB")
    Glass6 = Rectangle(Point(656,340), Point(613,268)) #                  Glass 6 = Glass to the right of Glass 3
    Glass6.draw(win)
    Glass6.setOutline("#9BD4ED")
    Glass6.setFill("#9BD4ED")
    Glass7 = Rectangle(Point(720,180), Point(675,110)) #                  Glass 7 = Glass to the right of Glass 4
    Glass7.draw(win)
    Glass7.setOutline("#51769E")
    Glass7.setFill("#51769E")
    Glass8 = Rectangle(Point(720,260), Point(675,187)) #                  Glass 8 = Glass to the right of Glass 5
    Glass8.draw(win)
    Glass8.setOutline("#71A4DB")
    Glass8.setFill("#71A4DB")
    Glass9 = Rectangle(Point(720,340), Point(675,268)) #                  Glass 9 = Glass to the right of Glass 6
    Glass9.draw(win)
    Glass9.setOutline("#9BD4ED")
    Glass9.setFill("#9BD4ED")
    Glass10 = Rectangle(Point(772,180), Point(728,110)) #                 Glass 10 = Top-most right Glass
    Glass10.draw(win)
    Glass10.setOutline("#51769E")
    Glass10.setFill("#51769E")
    Glass11 = Rectangle(Point(772,260), Point(728,187)) #                 Glass 11 = The Glass below Glass 10
    Glass11.draw(win)
    Glass11.setOutline("#71A4DB")
    Glass11.setFill("#71A4DB")
    Glass12 = Rectangle(Point(772,340), Point(728,268)) #                 Glass 12 = The Glass below Glass 11
    Glass12.draw(win)
    Glass12.setOutline("#9BD4ED")
    Glass12.setFill("#9BD4ED")
    # Left Curtain's first fold
#     LeftCurtainFold1Color = Rectangle((Point(,), Point(,))) #                Left Curtain's first fold
#     LeftCurtainFold1Color.draw(win)
#     LeftCurtainFold1Color.setOutline("")
#     LeftCurtainFold1Color.setFill("")
#     LeftCurtainFold1Light = Rectangle((Point(,), Point(,))) #                The reflection of light on the Left Curtain's Fold 1
#     LeftCurtainFold1Light.draw(win)
#     LeftCurtainFold1Light.setOutline("")
#     LeftCurtainFold1Light.setFill("")
#     LeftCurtainFold1Shadow = Rectangle((Point(,), Point(,))) #               The shadow casted on the Left Curtain's Fold 1
#     LeftCurtainFold1Shadow.draw(win)
#     LeftCurtainFold1Shadow.setOutline("")
#     LeftCurtainFold1Shadow.setFill("")
#     # Left Curtain's second fold
#     LeftCurtainFold2Color = Rectangle((Point(,), Point(,))) #                Left Curtain's first fold
#     LeftCurtainFold2Color.draw(win)
#     LeftCurtainFold2Color.setOutline("")
#     LeftCurtainFold2Color.setFill("")
#     LeftCurtainFold2Light = Rectangle((Point(,), Point(,))) #                The reflection of light on the Left Curtain's Fold 1
#     LeftCurtainFold2Light.draw(win)
#     LeftCurtainFold2Light.setOutline("")
#     LeftCurtainFold2Light.setFill("")
#     LeftCurtainFold2Shadow = Rectangle((Point(,), Point(,))) #               The shadow casted on the Left Curtain's Fold 1
#     LeftCurtainFold2Shadow.draw(win)
#     LeftCurtainFold2Shadow.setOutline("")
#     LeftCurtainFold2Shadow.setFill("")
#     # Left Curtain's third fold
#     LeftCurtainFold3Color = Rectangle((Point(,), Point(,))) #                Left Curtain's first fold
#     LeftCurtainFold3Color.draw(win)
#     LeftCurtainFold3Color.setOutline("")
#     LeftCurtainFold3Color.setFill("")
#     LeftCurtainFold3Light = Rectangle((Point(,), Point(,))) #                The reflection of light on the Left Curtain's Fold 1
#     LeftCurtainFold3Light.draw(win)
#     LeftCurtainFold3Light.setOutline("")
#     LeftCurtainFold3Light.setFill("")
#     LeftCurtainFold3Shadow = Rectangle((Point(,), Point(,))) #               The shadow casted on the Left Curtain's Fold 1
#     LeftCurtainFold3Shadow.draw(win)
#     LeftCurtainFold3Shadow.setOutline("")
#     LeftCurtainFold3Shadow.setFill("")
#     # Left Curtain's fourth fold
#     LeftCurtainFold4Color = Rectangle((Point(,), Point(,))) #                Left Curtain's first fold
#     LeftCurtainFold4Color.draw(win)
#     LeftCurtainFold4Color.setOutline("")
#     LeftCurtainFold4Color.setFill("")
#     LeftCurtainFold4Light = Rectangle((Point(,), Point(,))) #                The reflection of light on the Left Curtain's Fold 1
#     LeftCurtainFold4Light.draw(win)
#     LeftCurtainFold4Light.setOutline("")
#     LeftCurtainFold4Light.setFill("")
#     LeftCurtainFold4Shadow = Rectangle((Point(,), Point(,))) #               The shadow casted on the Left Curtain's Fold 1
#     LeftCurtainFold4Shadow.draw(win)
#     LeftCurtainFold4Shadow.setOutline("")
#     LeftCurtainFold4Shadow.setFill("")
#     # Left Curtain's fifth fold
#     LeftCurtainFold5Color = Rectangle((Point(,), Point(,))) #                Left Curtain's first fold
#     LeftCurtainFold5Color.draw(win)
#     LeftCurtainFold5Color.setOutline("")
#     LeftCurtainFold5Color.setFill("")
#     LeftCurtainFold5Light = Rectangle((Point(,), Point(,))) #                The reflection of light on the Left Curtain's Fold 1
#     LeftCurtainFold5Light.draw(win)
#     LeftCurtainFold5Light.setOutline("")
#     LeftCurtainFold5Light.setFill("")
#     LeftCurtainFold5Shadow = Rectangle((Point(,), Point(,))) #               The shadow casted on the Left Curtain's Fold 1
#     LeftCurtainFold5Shadow.draw(win)
#     LeftCurtainFold5Shadow.setOutline("")
#     LeftCurtainFold5Shadow.setFill("")
    # Right Curtain's first fold
    # Right Curtain's Second fold
    # Right Curtain's Third fold
    # Right Curtain's fourth fold
    # Right Curtain's fifth fold
# THE END OF PROGRAM (DO NOT DELETE)
    win.getMouse()
    win.close()
    

main()