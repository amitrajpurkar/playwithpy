"""OVERVIEW OF THE GRAPHICS PROJECT:
The image is of a living room of a Northern home during Autumn/Fall. There is a fireplace which is giving
heat to the cat sitting in one of the chairs. There is also a cup of fresh tea, a functioning clock, a
bookshelf with books and a couple of frames. The sill above the fireplace has a vase of flowers, some
books, candles, and a plant. There are 2 large windows next to each other with curtains, and there is a
lamp."""

        # PARENT VARIABLE  -->   w = Rectangle(Point(0,567), Point(1078, 0))
        #                        w = Rectangle(Point(100, 567), Point(1078, 0)) # main wall > Space on right
        #                        w = Rectangle(Point(0, 567), Point(1078, 100)) # main wall > Space on top
        #                        w = Rectangle(Point(0, 467), Point(1078, 0)) # main wall > Space on bottom
        #                        w = Rectangle(Point(0, 567), Point(978, 0)) # main wall > Space on left


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
    wall = Rectangle(Point(0, 459), Point(1078, 0)) #               Main wall
    wall.draw(win)
    wall.setOutline("#E0A9A0")
    wall.setFill("#E0A9A0")
    floor = Rectangle(Point(0, 567), Point(1078, 472)) #              Flooring
    floor.draw(win)
    floor.setOutline("#D49F88")
    floor.setFill("#D49F88")
    WindowPanelSHADOW = Rectangle(Point(500, 379), Point(838, 87)) #      The Shadow from the Window Panel Frame
    WindowPanelSHADOW.draw(win)
    WindowPanelSHADOW.setOutline("#8C6A64")
    WindowPanelSHADOW.setFill("#8C6A64")
    WindowPanelFrame = Rectangle(Point(500, 365), Point(838, 87)) #     Window Panel Frame
    WindowPanelFrame.draw(win)
    WindowPanelFrame.setOutline("#C7835E") 
    WindowPanelFrame.setFill("#C7835E")
    WINDOWPANEL = Rectangle(Point(520,350), Point(818,95)) #            Window Panel
    WINDOWPANEL.draw(win)
    WINDOWPANEL.setOutline("#875940")
    WINDOWPANEL.setFill("#875940")
    Glass1 = Rectangle(Point(569, 180), Point(611,110)) #                Glass 1 = Top-most left glass
    Glass1.draw(win)
    Glass1.setOutline("#5A799C")
    Glass1.setFill("#5A799C")
    Cloud1pt1 = Circle(Point(575,135),5) #                               1 particle of Cloud 1
    Cloud1pt1.draw(win)
    Cloud1pt1.setOutline("grey")
    Cloud1pt1.setFill("grey")
    Cloud1pt2 = Circle(Point(580,135),5) #                               2 particle of Cloud 1
    Cloud1pt2.draw(win)
    Cloud1pt2.setOutline("grey")
    Cloud1pt2.setFill("grey")
    Cloud1pt3 = Circle(Point(585,135),5) #                               3 particle of Cloud 1
    Cloud1pt3.draw(win)
    Cloud1pt3.setOutline("grey")
    Cloud1pt3.setFill("grey")
    Cloud1pt4 = Circle(Point(578,135),5) #                               4 particle of Cloud 1
    Cloud1pt4.draw(win)
    Cloud1pt4.setOutline("grey")
    Cloud1pt4.setFill("grey")
    Cloud1pt5 = Circle(Point(583,125),5) #                               5 particle of Cloud 1
    Cloud1pt5.draw(win)
    Cloud1pt5.setOutline("grey")
    Cloud1pt5.setFill("grey")
    Cloud1pt6 = Circle(Point(579,130),5) #                               6 particle of Cloud 1
    Cloud1pt6.draw(win)
    Cloud1pt6.setOutline("grey")
    Cloud1pt6.setFill("grey")
    Cloud1pt7 = Circle(Point(575,175),5) #                               7 particle of Cloud 1
    Cloud1pt7.draw(win)
    Cloud1pt7.setOutline("grey")
    Cloud1pt7.setFill("grey")
    Cloud1pt8 = Circle(Point(572,177),2.5) #                             8 particle of Cloud 1
    Cloud1pt8.draw(win)
    Cloud1pt8.setOutline("grey")
    Cloud1pt8.setFill("grey")
    Cloud1pt9 = Circle(Point(579,165),5) #                               9 particle of Cloud 1
    Cloud1pt9.draw(win)
    Cloud1pt9.setOutline("grey")
    Cloud1pt9.setFill("grey")
    Cloud1pt10 = Circle(Point(581,170),5) #                              10 particle of Cloud 1
    Cloud1pt10.draw(win)
    Cloud1pt10.setOutline("grey")
    Cloud1pt10.setFill("grey")
    Glass2 = Rectangle(Point(569, 260), Point(611,187)) #                Glass 2 = Glass below Glass 1
    Glass2.draw(win)
    Glass2.setOutline("#8DAEBD")
    Glass2.setFill("#8DAEBD")
    Cloud2 = Oval(Point(578,250), Point(600,240)) #                      Cloud 2
    Cloud2.draw(win)
    Cloud2.setOutline("grey")
    Cloud2.setFill("grey")
    Glass3 = Rectangle(Point(569,340), Point(611, 268)) #                Glass 3 = Glass below Glass 2
    Glass3.draw(win)
    Glass3.setOutline("#B6D3DB")
    Glass3.setFill("#B6D3DB")
    Glass4 = Rectangle(Point(663,180), Point(620,110)) #                 Glass 4 = Glass to the right of Glass 1
    Glass4.draw(win)
    Glass4.setOutline("#5A799C")
    Glass4.setFill("#5A799C")
    Glass5 = Rectangle(Point(663,260), Point(620,187)) #                 Glass 5 = Glass to the right of Glass 
    Glass5.draw(win)
    Glass5.setOutline("#8DAEBD")
    Glass5.setFill("#8DAEBD")
    Glass6 = Rectangle(Point(663,340), Point(620,268)) #                 Glass 6 = Glass to the right of Glass 3
    Glass6.draw(win)
    Glass6.setOutline("#B6D3DB")
    Glass6.setFill("#B6D3DB")
    Glass7 = Rectangle(Point(720,180), Point(675,110)) #                 Glass 7 = Glass to the right of Glass 4
    Glass7.draw(win)
    Glass7.setOutline("#5A799C")
    Glass7.setFill("#5A799C")
    Glass8 = Rectangle(Point(720,260), Point(675,187)) #                 Glass 8 = Glass to the right of Glass 5
    Glass8.draw(win)
    Glass8.setOutline("#8DAEBD")
    Glass8.setFill("#8DAEBD")
    Glass9 = Rectangle(Point(720,340), Point(675,268)) #                 Glass 9 = Glass to the right of Glass 6
    Glass9.draw(win)
    Glass9.setOutline("#B6D3DB")
    Glass9.setFill("#B6D3DB")
    Glass10 = Rectangle(Point(772,180), Point(728,110)) #                Glass 10 = Top-most right Glass
    Glass10.draw(win)
    Glass10.setOutline("#5A799C")
    Glass10.setFill("#5A799C")
    Glass11 = Rectangle(Point(772,260), Point(728,187)) #                Glass 11 = The Glass below Glass 10
    Glass11.draw(win)
    Glass11.setOutline("#8DAEBD")
    Glass11.setFill("#8DAEBD")
    Glass12 = Rectangle(Point(772,340), Point(728,268)) #                Glass 12 = The Glass below Glass 11
    Glass12.draw(win)
    Glass12.setOutline("#B6D3DB")
    Glass12.setFill("#B6D3DB")
#####TreeTrunk = Polygon(Point(340,767),Point(,),Point(,),Point(,),Point(,),Point(,),Point(728,),Point(728,),Point(,),Point(340,757))
    # Left Curtain's first fold
    LeftCurtainFold1Color = Rectangle(Point(480,400), Point(460,60)) # Left Curtain's first fold
    LeftCurtainFold1Color.draw(win)
    LeftCurtainFold1Color.setOutline("#D4876F")
    LeftCurtainFold1Color.setFill("#D4876F")
    LeftCurtainFold1Light = Rectangle(Point(464,400), Point(460,60)) # The reflection of light on the Left Curtain's Fold 1
    LeftCurtainFold1Light.draw(win)
    LeftCurtainFold1Light.setOutline("#FFA796")
    LeftCurtainFold1Light.setFill("#FFA796")
    LeftCurtainFold1Shadow = Rectangle(Point(480,400), Point(485,60)) #The shadow casted on the Left Curtain's Fold 1
    LeftCurtainFold1Shadow.draw(win)
    LeftCurtainFold1Shadow.setOutline("#A66D61")
    LeftCurtainFold1Shadow.setFill("#A66D61")
    # Left Curtain's second fold
    LeftCurtainFold2Color = Rectangle(Point(485,400), Point(505,60)) # Left Curtain's second fold
    LeftCurtainFold2Color.draw(win)
    LeftCurtainFold2Color.setOutline("#D4876F")
    LeftCurtainFold2Color.setFill("#D4876F")
    LeftCurtainFold2Light = Rectangle(Point(485,400), Point(489,60)) # The reflection of light on the Left Curtain's Fold 1
    LeftCurtainFold2Light.draw(win)
    LeftCurtainFold2Light.setOutline("#FFA796")
    LeftCurtainFold2Light.setFill("#FFA796")
    LeftCurtainFold2Shadow = Rectangle(Point(502,400), Point(505,60)) #The shadow casted on the Left Curtain's Fold 1
    LeftCurtainFold2Shadow.draw(win)
    LeftCurtainFold2Shadow.setOutline("#A66D61")
    LeftCurtainFold2Shadow.setFill("#A66D61")
    # Left Curtain's third fold
    LeftCurtainFold3Color = Rectangle(Point(506,400), Point(525,60)) # Left Curtain's third fold
    LeftCurtainFold3Color.draw(win)
    LeftCurtainFold3Color.setOutline("#D4876F")
    LeftCurtainFold3Color.setFill("#D4876F")
    LeftCurtainFold3Light = Rectangle(Point(506,400), Point(509,60)) # The reflection of light on the Left Curtain's Fold 1
    LeftCurtainFold3Light.draw(win)
    LeftCurtainFold3Light.setOutline("#FFA796")
    LeftCurtainFold3Light.setFill("#FFA796")
    LeftCurtainFold3Shadow = Rectangle(Point(522,400), Point(525,60)) #The shadow casted on the Left Curtain's Fold 1
    LeftCurtainFold3Shadow.draw(win)
    LeftCurtainFold3Shadow.setOutline("#A66D61")
    LeftCurtainFold3Shadow.setFill("#A66D61")
    # Left Curtain's fourth fold
    LeftCurtainFold4Color = Rectangle(Point(526,400), Point(545,60)) # Left Curtain's fourth fold
    LeftCurtainFold4Color.draw(win)
    LeftCurtainFold4Color.setOutline("#D4876F")
    LeftCurtainFold4Color.setFill("#D4876F")
    LeftCurtainFold4Light = Rectangle(Point(526,400), Point(529,60)) # The reflection of light on the Left Curtain's Fold 1
    LeftCurtainFold4Light.draw(win)
    LeftCurtainFold4Light.setOutline("#FFA796")
    LeftCurtainFold4Light.setFill("#FFA796")
    LeftCurtainFold4Shadow = Rectangle(Point(542,400), Point(545,60)) #The shadow casted on the Left Curtain's Fold 1
    LeftCurtainFold4Shadow.draw(win)
    LeftCurtainFold4Shadow.setOutline("#A66D61")
    LeftCurtainFold4Shadow.setFill("#A66D61")
    # Left Curtain's fifth fold
    LeftCurtainFold5Color = Rectangle(Point(546,400), Point(560,60)) # Left Curtain's fifth fold
    LeftCurtainFold5Color.draw(win)
    LeftCurtainFold5Color.setOutline("#D4876F")
    LeftCurtainFold5Color.setFill("#D4876F")
    LeftCurtainFold5Light = Rectangle(Point(546,400), Point(549,60)) # The reflection of light on the Left Curtain's Fold 1
    LeftCurtainFold5Light.draw(win)
    LeftCurtainFold5Light.setOutline("#FFA796")
    LeftCurtainFold5Light.setFill("#FFA796")
    LeftCurtainFold5Shadow = Rectangle(Point(558,400), Point(560,60)) #The shadow casted on the Left Curtain's Fold 1
    LeftCurtainFold5Shadow.draw(win)
    LeftCurtainFold5Shadow.setOutline("#A66D61")
    LeftCurtainFold5Shadow.setFill("#A66D61")
    # Right Curtain's first fold
    RightCurtainFold1Color = Rectangle(Point(783,400), Point(800,60)) #Right Curtain's first fold
    RightCurtainFold1Color.draw(win)
    RightCurtainFold1Color.setOutline("#D4876F")
    RightCurtainFold1Color.setFill("#D4876F")
    RightCurtainFold1Light = Rectangle(Point(783,400), Point(786,60)) #The reflection of light on the Left Curtain's Fold 1
    RightCurtainFold1Light.draw(win)
    RightCurtainFold1Light.setOutline("#FFA796")
    RightCurtainFold1Light.setFill("#FFA796")
    RightCurtainFold1Shadow = Rectangle(Point(797,400), Point(800,60))#The shadow casted on the Left Curtain's Fold 1
    RightCurtainFold1Shadow.draw(win)
    RightCurtainFold1Shadow.setOutline("#A66D61")
    RightCurtainFold1Shadow.setFill("#A66D61")
    # Right Curtain's Second fold
    RightCurtainFold2Color = Rectangle(Point(801,400), Point(820,60)) #Right Curtain's second fold
    RightCurtainFold2Color.draw(win)
    RightCurtainFold2Color.setOutline("#D4876F")
    RightCurtainFold2Color.setFill("#D4876F")
    RightCurtainFold2Light = Rectangle(Point(801,400), Point(804,60)) #The reflection of light on the Left Curtain's Fold 1
    RightCurtainFold2Light.draw(win)
    RightCurtainFold2Light.setOutline("#FFA796")
    RightCurtainFold2Light.setFill("#FFA796")
    RightCurtainFold2Shadow = Rectangle(Point(817,400), Point(820,60))#The shadow casted on the Left Curtain's Fold 1
    RightCurtainFold2Shadow.draw(win)
    RightCurtainFold2Shadow.setOutline("#A66D61")
    RightCurtainFold2Shadow.setFill("#A66D61")
    # Right Curtain's Third fold
    RightCurtainFold3Color = Rectangle(Point(821,400), Point(841,60)) #Right Curtain's second fold
    RightCurtainFold3Color.draw(win)
    RightCurtainFold3Color.setOutline("#D4876F")
    RightCurtainFold3Color.setFill("#D4876F")
    RightCurtainFold3Light = Rectangle(Point(821,400), Point(824,60)) #The reflection of light on the Left Curtain's Fold 1
    RightCurtainFold3Light.draw(win)
    RightCurtainFold3Light.setOutline("#FFA796")
    RightCurtainFold3Light.setFill("#FFA796")
    RightCurtainFold3Shadow = Rectangle(Point(838,400), Point(841,60))#The shadow casted on the Left Curtain's Fold 1
    RightCurtainFold3Shadow.draw(win)
    RightCurtainFold3Shadow.setOutline("#A66D61")
    RightCurtainFold3Shadow.setFill("#A66D61")
    # Right Curtain's fourth fold
    RightCurtainFold4Color = Rectangle(Point(842,400), Point(862,60)) #Right Curtain's second fold
    RightCurtainFold4Color.draw(win)
    RightCurtainFold4Color.setOutline("#D4876F")
    RightCurtainFold4Color.setFill("#D4876F")
    RightCurtainFold4Light = Rectangle(Point(842,400), Point(845,60)) #The reflection of light on the Left Curtain's Fold 1
    RightCurtainFold4Light.draw(win)
    RightCurtainFold4Light.setOutline("#FFA796")
    RightCurtainFold4Light.setFill("#FFA796")
    RightCurtainFold4Shadow = Rectangle(Point(859,400), Point(862,60))#The shadow casted on the Left Curtain's Fold 1
    RightCurtainFold4Shadow.draw(win)
    RightCurtainFold4Shadow.setOutline("#A66D61")
    RightCurtainFold4Shadow.setFill("#A66D61")
    # Right Curtain's fifth fold
    RightCurtainFold5Color = Rectangle(Point(863,400), Point(883,60)) #Right Curtain's second fold
    RightCurtainFold5Color.draw(win)
    RightCurtainFold5Color.setOutline("#D4876F")
    RightCurtainFold5Color.setFill("#D4876F")
    RightCurtainFold5Light = Rectangle(Point(863,400), Point(866,60)) #The reflection of light on the Left Curtain's Fold 1
    RightCurtainFold5Light.draw(win)
    RightCurtainFold5Light.setOutline("#FFA796")
    RightCurtainFold5Light.setFill("#FFA796")
    RightCurtainFold5Shadow = Rectangle(Point(880,400), Point(883,60))#The shadow casted on the Left Curtain's Fold 1
    RightCurtainFold5Shadow.draw(win)
    RightCurtainFold5Shadow.setOutline("#A66D61")
    RightCurtainFold5Shadow.setFill("#A66D61")
    #Pole that holds the curtains
    Pole = Rectangle(Point(888,64), Point(457,60))
    Pole.draw(win)
    Pole.setOutline("#474747")
    Pole.setFill("#474747")
    PoleEndpoint1 = Circle(Point(457,62), 4)
    PoleEndpoint1.draw(win)
    PoleEndpoint1.setOutline("#474747")
    PoleEndpoint1.setFill("#474747")
    PoleEndpoint2 = Circle(Point(888,62), 4)
    PoleEndpoint2.draw(win)
    PoleEndpoint2.setOutline("#474747")
    PoleEndpoint2.setFill("#474747")
   ##                                                              THE FIREPLACE ON LEFT SIDE
    CementLayer = Rectangle(Point(50,250), Point(350,500)) #         Cement Layer of the fireplace
    CementLayer.draw(win)
    CementLayer.setOutline("#FFA796")
    CementLayer.setFill("#FFA796")
   ##                                                                Bricks on the Fireplace
    Brick1 = Rectangle(Point(45,255), Point(65,270)) #                 Brick 1 (casted by Shadow)
    Brick1.draw(win)
    Brick1.setOutline("#875940")
    Brick1.setFill("#875940")
    Brick2 = Rectangle(Point(45,275), Point(85,290)) #                 Brick 2
    Brick2.draw(win)
    Brick2.setOutline("#CC8661")
    Brick2.setFill("#CC8661")
    Brick3 = Rectangle(Point(45,295), Point(65,310)) #                 Brick 3
    Brick3.draw(win)
    Brick3.setOutline("#CC8661")
    Brick3.setFill("#CC8661")
    Brick4 = Rectangle(Point(45,315), Point(85,330)) #                 Brick 4
    Brick4.draw(win)
    Brick4.setOutline("#CC8661")
    Brick4.setFill("#CC8661")
    Brick5 = Rectangle(Point(45,335), Point(65,350)) #                 Brick 5 
    Brick5.draw(win)
    Brick5.setOutline("#CC8661")
    Brick5.setFill("#CC8661")
    Brick6 = Rectangle(Point(45,355), Point(85,370)) #                 Brick 6
    Brick6.draw(win)
    Brick6.setOutline("#CC8661")
    Brick6.setFill("#CC8661")
    Brick7 = Rectangle(Point(45,375), Point(65,390)) #                 Brick 7
    Brick7.draw(win)
    Brick7.setOutline("#CC8661")
    Brick7.setFill("#CC8661")
    Brick8 = Rectangle(Point(45,395), Point(85,410)) #                 Brick 8
    Brick8.draw(win)
    Brick8.setOutline("#CC8661")
    Brick8.setFill("#CC8661")
    Brick9 = Rectangle(Point(45,415), Point(65,430)) #                 Brick 9
    Brick9.draw(win)
    Brick9.setOutline("#CC8661")
    Brick9.setFill("#CC8661")
    Brick10 = Rectangle(Point(45,435), Point(85,450)) #                 Brick 10
    Brick10.draw(win)
    Brick10.setOutline("#CC8661")
    Brick10.setFill("#CC8661")
    Brick11 = Rectangle(Point(45,455), Point(65,470)) #                 Brick 11
    Brick11.draw(win)
    Brick11.setOutline("#CC8661")
    Brick11.setFill("#CC8661")
    Brick12 = Rectangle(Point(45,475), Point(85,490)) #                 Brick 12
    Brick12.draw(win)
    Brick12.setOutline("#CC8661")
    Brick12.setFill("#CC8661")
    Brick13 = Rectangle(Point(115,270), Point(71,256)) #                 Brick 13 (casted by Shadow)
    Brick13.draw(win)
    Brick13.setOutline("#875940")
    Brick13.setFill("#875940")
    Brick14 = Rectangle(Point(135,290), Point(91,275)) #                 Brick 14
    Brick14.draw(win)
    Brick14.setOutline("#CC8661")
    Brick14.setFill("#CC8661")
    Brick15 = Rectangle(Point(115,310), Point(71,295)) #                 Brick 15
    Brick15.draw(win)
    Brick15.setOutline("#CC8661")
    Brick15.setFill("#CC8661")
    Brick16 = Rectangle(Point(135,330), Point(91,315)) #                 Brick 16
    Brick16.draw(win)
    Brick16.setOutline("#CC8661")
    Brick16.setFill("#CC8661")
    Brick17 = Rectangle(Point(115,350), Point(71,335)) #                 Brick 17
    Brick17.draw(win)
    Brick17.setOutline("#CC8661")
    Brick17.setFill("#CC8661")
    Brick18 = Rectangle(Point(135,370), Point(91,355)) #                 Brick 18
    Brick18.draw(win)
    Brick18.setOutline("#CC8661")
    Brick18.setFill("#CC8661")
    Brick19 = Rectangle(Point(115,390), Point(71,375)) #                 Brick 19
    Brick19.draw(win)
    Brick19.setOutline("#CC8661")
    Brick19.setFill("#CC8661")
    Brick20 = Rectangle(Point(135,410), Point(91,395)) #                 Brick 20
    Brick20.draw(win)
    Brick20.setOutline("#CC8661")
    Brick20.setFill("#CC8661")
    Brick21 = Rectangle(Point(115,430), Point(71,415)) #                 Brick 21
    Brick21.draw(win)
    Brick21.setOutline("#CC8661")
    Brick21.setFill("#CC8661")
    Brick22 = Rectangle(Point(135,450), Point(91,435)) #                 Brick 22
    Brick22.draw(win)
    Brick22.setOutline("#CC8661")
    Brick22.setFill("#CC8661")
    Brick23 = Rectangle(Point(115,470), Point(71,455)) #                 Brick 23
    Brick23.draw(win)
    Brick23.setOutline("#CC8661")
    Brick23.setFill("#CC8661")
    Brick24 = Rectangle(Point(135,490), Point(91,475)) #                 Brick 24
    Brick24.draw(win)
    Brick24.setOutline("#CC8661")
    Brick24.setFill("#CC8661")
    Brick25 = Rectangle(Point(168,270), Point(121,256)) #                Brick 25 (casted by Shadow)
    Brick25.draw(win)
    Brick25.setOutline("#875940")
    Brick25.setFill("#875940")
    Brick26 = Rectangle(Point(187,290), Point(141,275)) #                Brick 26
    Brick26.draw(win)
    Brick26.setOutline("#CC8661")
    Brick26.setFill("#CC8661")
    Brick27 = Rectangle(Point(168,310), Point(121,295)) #                Brick 27
    Brick27.draw(win)
    Brick27.setOutline("#CC8661")
    Brick27.setFill("#CC8661")
    Brick28 = Rectangle(Point(187,330), Point(141,315)) #                Brick 28
    Brick28.draw(win)
    Brick28.setOutline("#CC8661")
    Brick28.setFill("#CC8661")
    Brick29 = Rectangle(Point(168,350), Point(121,335)) #                Brick 29
    Brick29.draw(win)
    Brick29.setOutline("#CC8661")
    Brick29.setFill("#CC8661")
    Brick30 = Rectangle(Point(187,370), Point(141,355)) #                Brick 30
    Brick30.draw(win)
    Brick30.setOutline("#CC8661")
    Brick30.setFill("#CC8661")
    Brick31 = Rectangle(Point(168,390), Point(121,375)) #                Brick 31
    Brick31.draw(win)
    Brick31.setOutline("#CC8661")
    Brick31.setFill("#CC8661")
    Brick32 = Rectangle(Point(187,410), Point(141,395)) #                Brick 32
    Brick32.draw(win)
    Brick32.setOutline("#CC8661")
    Brick32.setFill("#CC8661")
    Brick33 = Rectangle(Point(168,430), Point(121,415)) #                Brick 33
    Brick33.draw(win)
    Brick33.setOutline("#CC8661")
    Brick33.setFill("#CC8661")
    Brick34 = Rectangle(Point(187,450), Point(141,435)) #                Brick 34
    Brick34.draw(win)
    Brick34.setOutline("#CC8661")
    Brick34.setFill("#CC8661")
    Brick35 = Rectangle(Point(168,470), Point(121,455)) #                Brick 35
    Brick35.draw(win)
    Brick35.setOutline("#CC8661")
    Brick35.setFill("#CC8661")
    Brick36 = Rectangle(Point(187,490), Point(141,475)) #                Brick 36
    Brick36.draw(win)
    Brick36.setOutline("#CC8661")
    Brick36.setFill("#CC8661")
    Brick37 = Rectangle(Point(220,270), Point(174,255)) #                Brick 37 (casted by Shadow)
    Brick37.draw(win)
    Brick37.setOutline("#875940")
    Brick37.setFill("#875940")
    Brick38 = Rectangle(Point(252,290), Point(194,275)) #                Brick 38
    Brick38.draw(win)
    Brick38.setOutline("#CC8661")
    Brick38.setFill("#CC8661")
    Brick39 = Rectangle(Point(220,310), Point(174,295)) #                Brick 39
    Brick39.draw(win)
    Brick39.setOutline("#CC8661")
    Brick39.setFill("#CC8661")
    Brick40 = Rectangle(Point(252,330), Point(194,315)) #                Brick 40
    Brick40.draw(win)
    Brick40.setOutline("#CC8661")
    Brick40.setFill("#CC8661")
    Brick41 = Rectangle(Point(220,350), Point(174,335)) #                Brick 41
    Brick41.draw(win)
    Brick41.setOutline("#CC8661")
    Brick41.setFill("#CC8661")
    Brick42 = Rectangle(Point(252,370), Point(194,355)) #                Brick 42
    Brick42.draw(win)
    Brick42.setOutline("#CC8661")
    Brick42.setFill("#CC8661")
    Brick43 = Rectangle(Point(220,390), Point(174,375)) #                Brick 43
    Brick43.draw(win)
    Brick43.setOutline("#CC8661")
    Brick43.setFill("#CC8661")
    Brick44 = Rectangle(Point(252,410), Point(194,395)) #                Brick 44
    Brick44.draw(win)
    Brick44.setOutline("#CC8661")
    Brick44.setFill("#CC8661")
    Brick45 = Rectangle(Point(220,430), Point(174,415)) #                Brick 45
    Brick45.draw(win)
    Brick45.setOutline("#CC8661")
    Brick45.setFill("#CC8661")
    Brick46 = Rectangle(Point(252,450), Point(194,435)) #                Brick 46
    Brick46.draw(win)
    Brick46.setOutline("#CC8661")
    Brick46.setFill("#CC8661")
    Brick47 = Rectangle(Point(220,470), Point(174,455)) #                Brick 47
    Brick47.draw(win)
    Brick47.setOutline("#CC8661")
    Brick47.setFill("#CC8661")
    Brick48 = Rectangle(Point(252,490), Point(194,475)) #                Brick 48
    Brick48.draw(win)
    Brick48.setOutline("#CC8661")
    Brick48.setFill("#CC8661")
    Brick49 = Rectangle(Point(285,270), Point(226,255)) #                Brick 49 (Casted by Shadow)
    Brick49.draw(win)
    Brick49.setOutline("#875940")
    Brick49.setFill("#875940")
    Brick50 = Rectangle(Point(315,290), Point(259,275)) #                Brick 50
    Brick50.draw(win)
    Brick50.setOutline("#CC8661")
    Brick50.setFill("#CC8661")
    Brick51 = Rectangle(Point(285,310), Point(226,295)) #                Brick 51
    Brick51.draw(win)
    Brick51.setOutline("#CC8661")
    Brick51.setFill("#CC8661")
    Brick52 = Rectangle(Point(315,330), Point(259,315)) #                Brick 52
    Brick52.draw(win)
    Brick52.setOutline("#CC8661")
    Brick52.setFill("#CC8661")
    Brick53 = Rectangle(Point(285,350), Point(226,335)) #                Brick 53
    Brick53.draw(win)
    Brick53.setOutline("#CC8661")
    Brick53.setFill("#CC8661")
    Brick54 = Rectangle(Point(315,370), Point(259,355)) #                Brick 54
    Brick54.draw(win)
    Brick54.setOutline("#CC8661")
    Brick54.setFill("#CC8661")
    Brick55 = Rectangle(Point(285,390), Point(226,375)) #                Brick 55
    Brick55.draw(win)
    Brick55.setOutline("#CC8661")
    Brick55.setFill("#CC8661")
    Brick56 = Rectangle(Point(315,410), Point(259,395)) #                Brick 56
    Brick56.draw(win)
    Brick56.setOutline("#CC8661")
    Brick56.setFill("#CC8661")
    Brick57 = Rectangle(Point(285,430), Point(226,415)) #                Brick 57
    Brick57.draw(win)
    Brick57.setOutline("#CC8661")
    Brick57.setFill("#CC8661")
    Brick58 = Rectangle(Point(315,450), Point(259,435)) #                Brick 58
    Brick58.draw(win)
    Brick58.setOutline("#CC8661")
    Brick58.setFill("#CC8661")
    Brick59 = Rectangle(Point(285,470), Point(226,455)) #                Brick 59
    Brick59.draw(win)
    Brick59.setOutline("#CC8661")
    Brick59.setFill("#CC8661")
    Brick60 = Rectangle(Point(315,490), Point(259,475)) #                Brick 60
    Brick60.draw(win)
    Brick60.setOutline("#CC8661")
    Brick60.setFill("#CC8661")
    Brick61 = Rectangle(Point(330,270), Point(291,255)) #                Brick 61 (Casted by Shadow)
    Brick61.draw(win)
    Brick61.setOutline("#875940")
    Brick61.setFill("#875940")
    Brick62 = Rectangle(Point(355,290), Point(321,275)) #                Brick 62
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(330,310), Point(291,295)) #                Brick 63
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(355,330), Point(321,315)) #                Brick 64
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(330,350), Point(291,335)) #                Brick 65
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(355,370), Point(321,355)) #                Brick 66
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(330,390), Point(291,375)) #                Brick 67
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(355,410), Point(321,395)) #                Brick 68
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(330,430), Point(291,415)) #                Brick 69
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(355,450), Point(321,435)) #                Brick 70
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(330,470), Point(291,455)) #                Brick 71
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick62 = Rectangle(Point(355,490), Point(321,475)) #                Brick 72
    Brick62.draw(win)
    Brick62.setOutline("#CC8661")
    Brick62.setFill("#CC8661")
    Brick73 = Rectangle(Point(355,270), Point(336,255)) #                Brick 73 (Casted By Shadow of the shelf)
    Brick73.draw(win)
    Brick73.setOutline("#875940")
    Brick73.setFill("#875940")
    Brick74 = Rectangle(Point(355,310), Point(336,295)) #                Brick 74
    Brick74.draw(win)
    Brick74.setOutline("#CC8661")
    Brick74.setFill("#CC8661")
    Brick75 = Rectangle(Point(355,350), Point(336,335)) #                Brick 75
    Brick75.draw(win)
    Brick75.setOutline("#CC8661")
    Brick75.setFill("#CC8661")
    Brick76 = Rectangle(Point(355,390), Point(336,375)) #                Brick 76
    Brick76.draw(win)
    Brick76.setOutline("#CC8661")
    Brick76.setFill("#CC8661")
    Brick77 = Rectangle(Point(355,430), Point(336,415)) #                Brick 77
    Brick77.draw(win)
    Brick77.setOutline("#CC8661")
    Brick77.setFill("#CC8661")
    Brick78 = Rectangle(Point(355,470), Point(336,455)) #                Brick 78
    Brick78.draw(win)
    Brick78.setOutline("#CC8661")
    Brick78.setFill("#CC8661")
    FireplaceShelf = Rectangle(Point(30,220), Point(370,255)) #      Shelf on the Fireplace
    FireplaceShelf.draw(win)
    FireplaceShelf.setOutline("#996349")
    FireplaceShelf.setFill("#996349")
    FireplaceShelfSHADOW = Rectangle(Point(30,235), Point(370,255)) #Shadow that was casted from the shelf on the fireplace
    FireplaceShelfSHADOW.draw(win)
    FireplaceShelfSHADOW.setOutline("#B88F7A")
    FireplaceShelfSHADOW.setFill("#B88F7A")
    Bookshelf = Rectangle(Point(1056,472), Point(900,53))
    Bookshelf.draw(win)
    Bookshelf.setOutline("#856657")
    Bookshelf.setFill("#856657")
    Shelf1 = Rectangle(Point(1040,100), Point(915,75))
    Shelf1.draw(win)
    Shelf1.setOutline("#A18971")
    Shelf1.setFill("#A18971")
    Compartment1 = Rectangle(Point(1040,176), Point(915,110))
    Compartment1.draw(win)
    Compartment1.setOutline("#63422F")
    Compartment1.setFill("#63422F")
    Shelf2 = Rectangle(Point(1050,184), Point(905,180))
    Shelf2.draw(win)
    Shelf2.setOutline("#A18971")
    Shelf2.setFill("#A18971")
    Compartment2 = Rectangle(Point(1040,253), Point(915,188))
    Compartment2.draw(win)
    Compartment2.setOutline("#63422F")
    Compartment2.setFill("#63422F")
    Shelf3 = Rectangle(Point(1050,262), Point(905,257))
    Shelf3.draw(win)
    Shelf3.setOutline("#A18971")
    Shelf3.setFill("#A18971")
    Compartment3 = Rectangle(Point(1040,333), Point(915,266))
    Compartment3.draw(win)
    Compartment3.setOutline("#63422F")
    Compartment3.setFill("#63422F")
    LeftCupboard = Rectangle(Point(975,457), Point(915,350))
    LeftCupboard.draw(win)
    LeftCupboard.setOutline("#8C7763")
    LeftCupboard.setFill("#8C7763")
    LeftCupboardKnob = Circle(Point(965,410), 5)
    LeftCupboardKnob.draw(win)
    LeftCupboardKnob.setOutline("#63422F")
    LeftCupboardKnob.setFill("#63422F")
    RightCupboard = Rectangle(Point(1040,457), Point(980,350))
    RightCupboard.draw(win)
    RightCupboard.setOutline("#8C7763")
    RightCupboard.setFill("#8C7763")
    RightCupboardKnob = Circle(Point(990,410), 5)
    RightCupboardKnob.draw(win)
    RightCupboardKnob.setOutline("#63422F")
    RightCupboardKnob.setFill("#63422F")
    RightSofaBack1 = Circle(Point(833,317), 55)
    RightSofaBack1.draw(win)
    RightSofaBack1.setOutline("#D9205C")
    RightSofaBack1.setFill("#D9205C")
    RightSofaBack2 = Rectangle(Point(888,372), Point(833,262))
    RightSofaBack2.draw(win)
    RightSofaBack2.setOutline("#D9205C")
    RightSofaBack2.setFill("#D9205C")
    RightSofaBack3 = Circle(Point(893,317), 55)
    RightSofaBack3.draw(win)
    RightSofaBack3.setOutline("#D9205C")
    RightSofaBack3.setFill("#D9205C")
    RightSofaBack4 = Rectangle(Point(949,482), Point(776,317))
    RightSofaBack4.draw(win)
    RightSofaBack4.setOutline("#D9205C")
    RightSofaBack4.setFill("#D9205C")
    RightSofaLeftRestMain = Circle(Point(768,389),26)
    RightSofaLeftRestMain.draw(win)
    RightSofaLeftRestMain.setOutline("#D9205C")
    RightSofaLeftRestMain.setFill("#D9205C")
    RightSofaLeftRestLight = Circle(Point(768,389),12)
    RightSofaLeftRestLight.draw(win)
    RightSofaLeftRestLight.setOutline("#D95E78")
    RightSofaLeftRestLight.setFill("#D95E78")
    RightSofaRightRestMain = Circle(Point(938,390),26)
    RightSofaRightRestMain.draw(win)
    RightSofaRightRestMain.setOutline("#D9205C")
    RightSofaRightRestMain.setFill("#D9205C")
    RightSofaRightRestLight = Circle(Point(938,390),12)
    RightSofaRightRestLight.draw(win)
    RightSofaRightRestLight.setOutline("#D95E78")
    RightSofaRightRestLight.setFill("#D95E78")
#    LeftSofaBack1 = Circle(Point(,), )
#    LeftSofaBack1.draw(win)
#    LeftSofaBack1.setOutline("")
#    LeftSofaBack1.setFill("")
#    LeftSofaBack2 = Rectangle(Point(,), Point(,))
#    LeftSofaBack2.draw(win)
#    LeftSofaBack2.setOutline("")
#    LeftSofaBack2.setFill("")
# THE END OF PROGRAM (DO NOT DELETE)
    win.getMouse()
    win.close()
    

main()