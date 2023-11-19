from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.goto(0,-200)
        self.write(self.l_score, align='center', font=(("Courier", 80, "normal")))
        
    def update_score(self):
        self.goto(0,-200)
        self.write(self.l_score, align='center', font=(("Courier", 80, "normal")))
    
    def l_point(self):
        self.l_score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f'GAME OVER\n Score: {self.l_score}', align= 'center', font=(("Courier", 80, "normal")))