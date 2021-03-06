# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:35:23 2020

@author: franc
"""
from time import sleep 

from os import system, name 
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from random import randint

import keyboard

from sys import exit

def clear(): 
  
    # for windows 
    if name == 'nt': 
        system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear') 

printgrid = lambda grid: [print(i) for i in grid]

def printgame(board):
    dic = {"X":" ", "A":"<", "D":">", "S":"v", "W":"^", "^":"O", "v":"O", "<":"O",">":"O", "a":"A"}
    out = ""
    for i in board:
        out += "]"
        for j in i:
            out += dic[j] + " "
        out += "[\n"
    print(out)
                
def keypress():
    while True:  
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('w'):   
                return "W"
                break  
            elif keyboard.is_pressed('a'):  
                return "A"
                break  
            elif keyboard.is_pressed('s'):  
                return "S"
                break  
            elif keyboard.is_pressed('d'):  
                return "D"
                break  
            else:
                return "x"
                break
        except:
            break

class Snake:
    def __init__ (self):
        self.snake = [[0, 4, "D"],[1,4, "D"],[2,4, "D"],[3,4, "D"]]
    def extend(self, direction):
        if direction.upper() == "W":
            self.snake.append([self.snake[-1][0], self.snake[-1][1] - 1, "W"])
        elif direction.upper() == "A":
            self.snake.append([self.snake[-1][0] - 1, self.snake[-1][1], "A"])
        elif direction.upper() == "S":
            self.snake.append([self.snake[-1][0], self.snake[-1][1] + 1, "S"])
        elif direction.upper() == "D":
            self.snake.append([self.snake[-1][0] + 1, self.snake[-1][1], "D"])
    def retract(self):
        self.snake = self.snake[1:]
             
class Board:  
    def __init__(self, size):
        self.board = [['X' for i in range(size)] for j in range(size)]
    def snakein(self, snake):
        "Puts a snake into the board"
        dictionary = {"A":">", "D":"<", "S":"^", "W":"v"}
        self.board[snake.snake[-1][1]][snake.snake[-1][0]] = dictionary[snake.snake[-1][2]]
        for i in range(len(snake.snake) - 1):
            self.board[snake.snake[i][1]][snake.snake[i][0]] = snake.snake[i][2]
            
    def applein(self):
        "Places an apple into the board as long as the snake isn't there"
        a = True
        while a:
            b = (randint(0,len(self.board) - 1), randint(0,len(self.board) - 1))
            if not self.board[b[0]][b[1]] in "WASD<>v^":
                self.board[b[0]][b[1]] = "a"
                a = False
    def tailclear(self, snake):
        self.board[snake.snake[0][1]][snake.snake[0][0]] = "X"
                
def apple_test(snake, board):
    """Returns true if the head of the snake is in the same position as an apple,
    otherwise returns false. The head of the snake is the final element in the snake list.
    """
    if board.board[snake.snake[-1][1]][snake.snake[-1][0]] == "a":
        return True
    else:
        return False
    
def death_test(snake, board):
    """Retruns true if the snake head goes outside of the board, or if the snake head
    has the same position as any of the other coordinates in the snake object
    """
    if snake.snake[-1][0] >= len(board.board) or snake.snake[-1][1] >= len(board.board) or snake.snake[-1][0] < 0 or snake.snake[-1][1] < 0:        
        return True
    else:
        for i in snake.snake[:-1]:
            if i[:-1] == snake.snake[-1][:-1]:                
                return True
    return False
            
def move_snake(snake, board):
    """Takes appletest and direction and chooses whether to extend or to move 
    the snake in a given direction
    """
    a = False  
    try:
        if apple_test(snake, board):
            a = True
        else:
            board.tailclear(snake)
            snake.retract()
    except:
      ...  
    return (death_test(snake, board), a)
        
        
"""
Insert snake, Insert apple, , print board, extend snake, test if snake eats apple if yes, extend, if no, , insert snake, insert apple
if snake ate an apple, counter +=1
"""        
def rungame():       
    board = Board(20)
    snake = Snake()   
    board.snakein(snake)
    clear()   
    printgame(board.board)    
    a = "D"
    b = "False"
    counter = -1
    input("Press Enter To Start")
    while a.upper() != "X":        
        if b:
            board.applein()
            counter += 1       
        clear()   
        printgame(board.board)
        print("Score: " + str(counter))
        for i in range(6):
          if keypress() in "WASD":
            a = keypress()
          sleep(0.03)
        if a.upper() == "X":
            ...
        else:
            if keypress() in "WASD":
                 a = keypress()
            snake.extend(a)             
            dead, b = move_snake(snake, board)
            if dead:
                print("You Lose" + "\n" + "Score " + str(counter))
                file = open("Highscores.txt", "a")
                file.close()
                file = open("Highscores.txt")
                filelist = [int(i) for i in file]
                file.close()
                if len(filelist) == 0:
                    file = open("Highscores.txt", "a")                   
                    print("New High Score!")
                    file.write(str(counter) + "\n")
                    file.close()
                elif counter > filelist[-1]:
                    file = open("Highscores.txt", "a")                    
                    print("New High Score!")
                    file.write(str(counter)  + "\n")
                    file.close()
                file.close()
                if input("Press Enter to Play Again, X to exit ").upper() == "X":
                    exit()                   
                else:                    
                    rungame()                   
            if keypress() in "WASD":
                 a = keypress()    
            board.snakein(snake)
rungame()            







        



