from turtle import Turtle
from itertools import cycle
class Blocks():
    def __init__(self):
        super().__init__()
        self.blocks= []
        
    def create_blocks(self): #THIS WAS ALL TRIAL AND ERROR
        colors = ['pink', 'brown', 'violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
        color_iterator = cycle(colors) #Need this to not mess with the double for loop
        for y in range(280, 0, -32):
            color = next(color_iterator)
            for x in range(-354, 390, 87):
                block = Turtle(shape='square')
                block.penup()
                block.shapesize(stretch_wid= 1.5, stretch_len= 4.25)
                block.color(color)
                block.goto(x,y)
                self.blocks.append(block)
    
    def remove_block(self, block):
        block.hideturtle()
        self.blocks.remove(block)
        