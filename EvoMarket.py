'''
Stock Market Evolution Simulator
V1
Michael and Alex

todo list:
-make todo list
hi
'''
import random

class NewBot():
    def __init__(self):
        self.money = 100 #starting money
        self.stuff = 10  #starting resource
        
        self.timing = random.randint(5,25) #how often does it check the market?
        self.medianPrice = random.randint(5,15) #the average price the bot assumes the market will move to
        self.weight = random.randint(1,99) #how quickly the bot adjusts it's median price
        self.margin = random.randint(1,10) # how low the price must be for the bot to consider buying
        self.fail = random.randint(1,10) # how bad the bot's prediction must be before it accepts defeat and cuts losses
        self.prediction = random.randint(2,10) #how fast the bot thinks the price will go back up to median, 10 being fastest
        self.savings = random.randint(25,200) #how much the bots saves for itself when making a baby so that it can live on
        
        
        
class Bot():
    def __init__(self,timing,medianPrice,weight,margin,fail,prediction,savings):
        self.money = 100
        self.stuff = 10
        
        self.timing = timing + random.randint(-5,5) 
        self.medianPrice = medianPrice + random.randint(-2,2) 
        self.weight = weight random.randint(1,99)
        self.margin = random.randint(1,10)
        self.fail = random.randint(1,10)
        self.prediction = random.randint(2,10) 
        self.savings = random.randint(25,200)
        
        
        
