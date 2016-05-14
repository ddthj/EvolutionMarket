'''
Stock Market Evolution Simulator
V1
Michael and Alex

todo list:
-make todo list
hi
'''
import random
import time

tickNumber = 0
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
    "Slade",
    "Woodrow",
    "Cymone",
    "Chase",
    "Jason",
    "Edwin",
    "Kyle",
    "Walter",
    "Pip"
    ]

class Bot:
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
            #self.margin = args[3] + random.randint(-2,2)
            self.fail = args[4] + random.randint(-2,2)
            self.predictionScale = args[5] + random.randint(-1,1) 
            self.savings = args[6] + random.randint(-25,25)
            self.name = names[random.randint(0,20)]
        else:
        
            self.timing = random.randint(4,10) #how often does it check the market?
            self.medianPrice = random.randint(5,15) #the average price the bot assumes the market will move to
            self.weight = random.randint(1,99) #how quickly the bot adjusts it's median price
            #self.margin = random.randint(1,10) # how low the price must be for the bot to consider buying
            self.fail = random.randint(1,10) # how bad the bot's prediction must be before it accepts defeat and cuts losses
            self.predictionScale = random.randint(2,10) #how fast the bot thinks the price will go back up to median, 10 being fastest
            self.savings = random.randint(25,200) #how much the bots saves for itself when making a baby so that it can live on
            self.name = names[random.randint(0,20)] #gets a random name
        self.prediction = medianPrice
        print("Bot "+str(self.name)+" has been born!")
    
    def tick(self,tick,price):
        if tick % self.timing == 0:
            print(str(self.name)+", id #"+str(self.bot_id)+", is thinking about the market...\n")
            if self.buy:
                pass
            elif self.sell:
                pass
            else:
                if price > self.medianPrice and self.stuff > 0:
                    self.sell = True
                    self.price = price -
                elif price <= self.medianPrice and self.money >0:
                    pass
                
            
            
            
            
            

class market:
    def __init__(self):
        self.bot_id = 0
        self.bots = []
        self.price = 5
        
        for i in range (0,20):
            self.bots.append(Bot(self.bot_id,[]))
            self.bot_id += 1 
            
    def tick(self, tick):
        maxPrice = 0
        minPrice = 0 #this will break
        
        for item in self.bots:           #In this chunk we get the highest and lowest prices being traded
            if item.price > maxPrice and item.buy == True:
                maxPrice = item
            elif item.price < minPrice and item.sell == True:
                minPrice = item
        if maxPrice != 0 and minPrice != 0:
            # CASE ONE: BUYER IS BUYING LESS THAN OR EQUAL TO CHEAPEST SELLER
            if maxPrice.price >= minPrice.price and maxPrice.amount <= minPrice.amount:
                minPrice.amount -= maxpPrice.amount
                minPrice.stuff -= maxPrice.amount                   #getting the seller's values all good
                minPrice.money += maxPrice.amount * maxPrice.price#Seller always gets the best deal here
                if minPrice.amount == 0:
                    minPrice.sell = False

                maxPrice.stuff += maxPrice.amount
                maxPrice.money -= maxPrice.amount * maxPrice.price # getting buyer's values all good
                maxPrice.buy = False
                maxPrice.amount = 0
                self.price = maxPrice.price
            # CASE TWO: BUYER IS BUYING MORE THAN CHEAPEST SELLER
            elif maxPrice.price >= minPrice.price and maxPrice.amount > minPrice.amount:
                minPrice.stuff -= minPrice.amount
                minPrice.money += minPrice.amount * maxPrice.price
                maxPrice.amount -= minPrice.amount
                maxPrice.money -= maxPrice.price * minPrice.amount
                maxPrice.stuff += minPrice.amount
                minPrice.amount = 0
                minPrice.sell = False
                self.price = maxPrice.price
        for item in self.bots:
            item.tick(tick,self.price)

                        
EvoMarket = market()

while True:
    print("Tick number %s:\n" % tickNumber)
    EvoMarket.tick(tickNumber)
    tickNumber+=1
    time.sleep(3)
    
    
  













    
        
        
        
