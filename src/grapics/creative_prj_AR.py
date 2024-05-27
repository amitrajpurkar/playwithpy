from graphics import *


score_val = 0 #this is the score.
columnWidth = 200
buttonWidth = 150
buttonHeight = 50
verticalSpace = 20
topic_answers = [
["topic","100", "200", "300", "400", "500"],
["science","Robert Hooke", "Approximately 20 AMU", "True", "NiCr", "The Fovea"],
["history","Paul Revere", "Franklin Delano Roosevelt (F.D.R.)", "300", "400", "500"],
["literature","100", "200", "300", "400", "500"],
["colleges","100", "200", "300", "400", "500"],
["wordorigins","100", "200", "300", "400", "500"],
["beforeafter","100", "200", "300", "400", "500"]
]



def draw_score_tracker(win:GraphWin):
    Scoretracker = Rectangle(Point(50, 50), Point(200, 75))
    Scoretracker.setOutline('#13066E')
    Scoretracker.setFill('lightBlue')
    Scoretracker.draw(win)
    Score = Text(Point(100, 63), score_val)
    Score.setSize(10)
    Score.setStyle('bold')
    Score.setTextColor('yellow')
    Score.draw(win)
    pass


def draw_button(win:GraphWin, label:str, x_pos:int, y_pos:int):
    button_rect = Rectangle(Point(x_pos, y_pos), Point(x_pos + buttonWidth, y_pos + buttonHeight))
    button_rect.setOutline('#13066E')
    button_rect.setFill('#13066E')
    button_rect.draw(win)
    button_text = Text(Point(x_pos+100, y_pos+25), label)
    button_text.setSize(34)
    button_text.setStyle("bold")
    button_text.setTextColor("white")
    button_text.draw(win)
    pass


def draw_column(win:GraphWin, colName:str, x_pos:int, y_pos:int):
    Column = Rectangle(Point(x_pos, y_pos), Point(x_pos + columnWidth, 200))
    Column.setOutline('#13066E')
    Column.setFill('lightBlue')
    Column.draw(win)
    ColumnName = Text(Point(x_pos+100, 150), colName)
    ColumnName.setSize(20)
    ColumnName.setStyle('bold')
    ColumnName.setTextColor('yellow')
    ColumnName.draw(win)

    draw_button(win, "100", x_pos+10, 230)
    draw_button(win, "200", x_pos+10, 330)
    draw_button(win, "300", x_pos+10, 430)
    draw_button(win, "400", x_pos+10, 530)
    draw_button(win, "500", x_pos+10, 630)

    pass




def check_answer(topic:str, quest_num:str, x:int, y:int, score:int) -> int:
    if topic == "science":
        if quest_num == "100":
            if 50 <= x <= 250 and 300 <= y <= 400:
                score += 100
                print('correct')
            else:
                score -= 100
        elif quest_num == "200":
            score +=  200
    elif topic == "history":
        if quest_num == "100":
            if 50 <= x <= 250 and 300 <= y <= 400:
                score += 100
                print('correct')
            else:
                score -= 100
    return score

def draw_q_for(winTwo:GraphWin,topic:str, quest_num:str):
    if topic =="science" and quest_num == "100":
        questionPanel = Image(Point(960, 300), "actual_science(100)question.png")
        questionPanel.draw(winTwo)
        draw_button(winTwo, "choice 1", 50, 300)
        draw_button(winTwo, "choice 2", 50, 450)
        draw_button(winTwo, "choice 3", 300, 300)
        draw_button(winTwo, "choice 4", 300, 450)
    elif topic =="science" and quest_num == "200":
        questionPanel = Image(Point(960, 300), "SCIENCE(200)QUESTION.png")
        questionPanel.draw(winTwo)
        draw_button(winTwo, "Robert Hooke", 50, 300)
        draw_button(winTwo, "Isaac Newton", 50, 450)
        draw_button(winTwo, "Pascal", 300, 300)
        draw_button(winTwo, "Adam Smith", 300, 450)
    elif topic =="science" and quest_num == "300":
        questionPanel = Image(Point(960, 300), "SCIENCE(300)qUESIOTN.png")
        questionPanel.draw(winTwo)
        draw_button(winTwo, "choice 1", 50, 300)
        draw_button(winTwo, "choice 2", 50, 450)
        draw_button(winTwo, "choice 3", 300, 300)
        draw_button(winTwo, "choice 4", 300, 450)
    elif topic =="science" and quest_num == "400":
        questionPanel = Image(Point(960, 300), "SCIENCE(400)QUESTION.png")
        questionPanel.draw(winTwo)
        draw_button(winTwo, "choice 1", 50, 300)
        draw_button(winTwo, "choice 2", 50, 450)
        draw_button(winTwo, "choice 3", 300, 300)
        draw_button(winTwo, "choice 4", 300, 450)
    elif topic =="science" and quest_num == "500":
        questionPanel = Image(Point(960, 300), "SCIENCE(500)QUESTION.png")
        questionPanel.draw(winTwo)
        draw_button(winTwo, "choice 1", 50, 300)
        draw_button(winTwo, "choice 2", 50, 450)
        draw_button(winTwo, "choice 3", 300, 300)
        draw_button(winTwo, "choice 4", 300, 450)
    pass

def show_question(topic:str,quest_num:str, score:int):
    winTwo = GraphWin("Topic: "+topic+" Question: "+quest_num+" ", 1920, 1280)
    draw_q_for(winTwo, topic, quest_num)

    clickPointTwo = winTwo.getMouse()
    xValueTwo = clickPointTwo.getX()
    yValueTwo = clickPointTwo.getY()
    chkValTwo = winTwo.checkKey()

    score_val = check_answer(topic, quest_num, xValueTwo, yValueTwo, score)
    winTwo.close()
    pass


def detect_mouse_click(win:GraphWin, score:int):
    clickPoint = win.getMouse()
    xValue = clickPoint.getX()
    yValue = clickPoint.getY()
    chk_val = win.checkKey()
    if chk_val == 'x':
        win.close()
    else:
        print(xValue, yValue, chk_val)

    # open questions for column 1
    if 60<xValue<210 and 230<yValue<330:
        print("You clicked on topic 1 button 100")
        show_question("science","100", score)
    elif 60<xValue<210 and 340<yValue<430:
        print("You clicked on topic 1 button 200")
        show_question("science","200", score)
    elif 60<xValue<210 and 440<yValue<530:
        print("You clicked on topic 1 button 300")
        show_question("science","300", score)
    elif 60<xValue<210 and 540<yValue<630:
        print("You clicked on topic 1 button 400")
        show_question("science","400", score)
    elif 60<xValue<210 and 640<yValue<730:
        print("You clicked on topic 1 button 500")
        show_question("science","500", score)

    # open questions for column 2
    if 310<xValue<460 and 230<yValue<330:
        print("You clicked on topic 2 button 100")
        # show_question("history","100")
    elif 310<xValue<460 and 340<yValue<430:
        print("You clicked on topic 2 button 200")
        # show_question("history","200")
    elif 310<xValue<460 and 440<yValue<530:
        print("You clicked on topic 2 button 300")
        # show_question("history","300")
    elif 310<xValue<460 and 540<yValue<630:
        print("You clicked on topic 2 button 400")
        # show_question("history","400")
    elif 310<xValue<460 and 640<yValue<730:
        print("You clicked on topic 2 button 500")
        # show_question("history","500")

    # open questions for column 3
    if 310<xValue<460 and 230<yValue<330:
        print("You clicked on topic 3 button 100")
        # show_question("literature","100")
    elif 310<xValue<460 and 340<yValue<430:
        print("You clicked on topic 3 button 200")
        # show_question("literature","200")
    elif 310<xValue<460 and 440<yValue<530:
        print("You clicked on topic 3 button 300")
        # show_question("literature","300")
    elif 310<xValue<460 and 540<yValue<630:
        print("You clicked on topic 3 button 400")
        # show_question("literature","400")
    elif 310<xValue<460 and 640<yValue<730:
        print("You clicked on topic 3 button 500")
        # show_question("literature","500")

    pass


def Jeopardy_Game_Board():
    win = GraphWin('JEOPARDY Game Board', 1920, 1280)
    win.setBackground('lightBlue')

    draw_score_tracker(win)
    draw_column(win, "Science", 50, 100)
    draw_column(win, "American History", 300, 100)
    draw_column(win, "Literature", 600, 100)
    draw_column(win, "Colleges", 900, 100)
    draw_column(win, "Word of Origins", 1200, 100)
    draw_column(win, "Before and After", 1500, 100)

    detect_mouse_click(win, score_val)

    pass


Jeopardy_Game_Board()
