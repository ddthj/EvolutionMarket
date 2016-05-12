'''
Stock Market Evolution Simulator
V1
Michael and Alex

todo list:
-make todo list
hi
'''
import random


names = [
    "Bob",
    "Joe",
    "Bill",
    "Jonny",
    "Albert",
    "Alvan",
    "Alex",
    "Adam",
    "Bond",
    "James",
    "Johnson",
    "Steve",
    ]

class Bot():
    def __init__(self,bot_id,args):
        self.money = 100 #starting money
        self.stuff = 10  #starting resource
        self.bot_id = bot_id
        self.buying = False
        self.selling = False
        self.amount = 0
        self.price = 0
        self.happy = 5 #range from 0 to 10
        

        if len(args) > 1:
            self.timing = args[0] + random.randint(-5,5) 
            self.medianPrice = args[1] + random.randint(-2,2) 
            self.weight = args[2] + random.randint(-5,5)
            self.margin = args[3] + random.randint(-2,2)
            self.fail = args[4] + random.randint(-2,2)
            self.prediction = args[5] + random.randint(-1,1) 
            self.savings = args[6] + random.randint(-25,25)
            self.name = names[random.randint(0,11)]

        else:
            self.timing = random.randint(5,25) #how often does it check the market?
            self.medianPrice = random.randint(5,15) #the average price the bot assumes the market will move to
            self.weight = random.randint(1,99) #how quickly the bot adjusts it's median price
            self.margin = random.randint(1,10) # how low the price must be for the bot to consider buying
            self.fail = random.randint(1,10) # how bad the bot's prediction must be before it accepts defeat and cuts losses
            self.prediction = random.randint(2,10) #how fast the bot thinks the price will go back up to median, 10 being fastest
            self.savings = random.randint(25,200) #how much the bots saves for itself when making a baby so that it can live on
            self.name = names[random.randint(0,11)] #gets a random name

        print("Bot "+str(self.name)+" has been born!")
    
    def tick(tick,price):
        pass     

class market():
    def __init__(self):
        self.tick = 0
        self.bot_id = 0
        self.bots = []
        self.price  = 5
        
        for i in range (0,20):
            self.bots.append(Bot(self.bot_id,[]))
            self.bot_id += 1 
            
    def tick(tick):
        maxPrice = None
        minPrice = None
        for item in self.bots:           #In this chunk we get the highest and lowest prices being traded
            if item.price > maxPrice && item.buy == True:
                maxPrice = item
            elif item.price < minPrice && item.sell == True:
                minPrice = item
        if maxPrice.price >= minPrice.price && maxPrice.amount <= minPrice.amount:
            
            
                

m = market()

        
        













    
        
        
        
