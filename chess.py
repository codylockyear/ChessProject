import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
chess = pd.read_csv('/Users/codylockyear/Documents/PythonProject/games.csv')
# x = opening names 
# y = number of white wins
def filter_color(color):
     color= ('')
     if color == 'black':
        chess[chess.winner == color]
        chess.sort_values(by =['opening_name'])
        chess[chess.rated != 'FALSE']
    
#create bar graph showing top 5 white openings

print(filter_color('black'))


