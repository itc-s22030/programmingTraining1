import random
import math
from tkinter import messagebox



class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.sy = 0
        self.score = self.canvas.create_text(215, 15, text=self.sy, tag="score", font=("", 20))
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5
        self.speed = 0
        self.x = 0
        self.y = 0

    def up(self):
        self.sy += 1
        self.canvas.delete("score")
        self.score = self.canvas.create_text(215, 15, text=self.sy, tag="score", font=("", 20))
        

    def start(self, evt):
        if self.speed != 0:
            return
        
        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 4.3      
        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])  
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)
        if pos[1] <= 0:
            self.fix(0, pos[1])
        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)
        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)
            self.failed()  
            self.sy = 0
            self.canvas.delete("score")
            self.score = self.canvas.create_text(215, 15, text=self.sy, tag="score", font=("", 20))
            messagebox.showinfo("終わり", "GAME OVER")     
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.fix(0, pos[3] - paddle_pos[1])
            self.up()
        
        
    def fix(self, diff_x, diff_y):
        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))
        if diff_x != 0:
            self.x = -self.x
            
        if diff_y != 0:
            self.y = -self.y

    def failed(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        

        





















    
