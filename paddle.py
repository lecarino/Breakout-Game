from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid= 1, stretch_len= 6)
        self.setposition(coordinates)
    
    def left(self):
        new_x = self.xcor()-20
        self.goto((new_x,self.ycor()))
    
    def right(self):
        new_x = self.xcor()+20
        self.goto((new_x,self.ycor()))


