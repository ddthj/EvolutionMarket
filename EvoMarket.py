'''
Stock Market Evolution Simulator
V1
Michael and Alex

todo list:
-rewrite the market logic 50% complete
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

fun = [
    "bananas",
    "children",
    "bitcoin",
    "apple stock",
    "bathtubs",
    "masterlocks",
    "fish insurance",
    "pneumatic fluid",
    "blue oranges",
    "nothing",
    "robots",
    "chinese products",
    "soft drives",
    ".com domains",
    "infomercial products",
    "time",
    "toasters",
    ]

class Bot():
    def __init__(self,bot_id,args):
        self.money = 50 #starting money
        self.stuff = 50  #starting resource
        self.bot_id = bot_id
        self.buy = False
        self.sell = False
        self.amount = 0
        self.price = 0
        self.happy = 5 #range from 1 to 10
        
        if len(args) > 1:
            self.timing = args[0] + random.randint(-5,5) 
            self.medianPrice = args[1] + random.randint(-2,2) 
            self.weight = args[2] + random.randint(-2,2)
            #self.margin = args[3] + random.randint(-2,2)
            self.fail = args[4] + random.randint(-2,2)
            self.predictionScale = args[5] + random.randint(-1,1) 
            self.savings = args[6] + random.randint(-25,25)
            self.name = names[random.randint(0,len(names)-1)]
            self.sac = args[7] + random.randint(-1,1)
        else:
            self.timing = random.randint(4,10) #how often does it check the market?
            self.medianPrice = random.randint(15,25) #the average price the bot assumes the market will move to
            self.weight = random.randint(2,4) #how quickly the bot adjusts it's median price
            #self.margin = random.randint(1,10) # how low the price must be for the bot to consider buying
            self.fail = random.randint(1,5) # how bad the bot's prediction must be before it accepts defeat and cuts losses
            self.predictionScale = random.randint(2,4) #how fast the bot thinks the price will go back up to median, 10 being fastest
            self.savings = random.randint(25,200) #how much the bots saves for itself when making a baby so that it can live on
            self.name = names[random.randint(0,len(names)-1)] #gets a random name
            self.sac = random.randint(1,5) #how much the bot sacrifices to get a succesful transaction

        self.prediction = self.medianPrice
        print("Bot "+str(self.name)+" has been born!")
    
    def tick(self,tick,price):
        self.medianPrice = self.prediction#self.medianPrice + int((price-self.medianPrice)/self.weight)
        #if tick % self.timing == 0:
            #print(str(self.name)+", id #"+str(self.bot_id)+", is thinking about the market...\n")
        if price > self.medianPrice - self.sac and self.stuff > 0 and self.buy == False:
            self.sell = True
            self.price = price - self.sac
            self.amount = self.stuff
            #print("LogSellMade: price "+str(price)+"median price" +str(self.medianPrice))
        elif price <= self.medianPrice+self.sac and self.money >0 and self.sell == False:
            self.buy = True
            self.price = price + self.sac
            self.amount = int((self.money/self.price)-1)
        elif self.buy:
            if price + self.sac > self.price:
                self.price += self.sac
        elif self.sell:
            if price - self.sac < self.price:
                self.price -= self.sac
        else:
            x = random.randint(1,2)
            if x == 1:
                sell = True
                self.price = price - self.sac
                self.amount = self.stuff
            elif x == 2:
                self.buy = True
                self.price = price + self.sac
                self.amount = int((self.money/self.price)-1)

        self.prediction = price + int((self.medianPrice - price)/self.predictionScale)
            
    def setMe(self,money,amount,buy,sell):
        #self.toString()
        self.money = money
        self.amount = amount
        self.buy = buy
        self.sell = sell
        print("Money was set to %s" % money)
        #self.toString()
            
    def toString(self):
        print("\nBot %s:\n"%self.name)
        print("Money: %s\nStuff: %s\nMedianPrice: %s" % (self.money, self.stuff, self.medianPrice))
        print("Buying: %s\nSelling: %s" %(str(self.buy),str(self.sell)))
        print("Buy/Sell Price: $%s\nBuy/Sell Amount: %s" %(self.price,self.amount))

class fakeBot():
    def __init__(self,price):
        self.price = price
        self.bot_id = -1
class fakeBotTwo():
    def __init__(self,money):
        self.money = money

class market():
    def __init__(self):
        self.bot_id = 0
        self.bots = []
        self.price = 20
        
        for i in range (0,50):
            self.bots.append(Bot(self.bot_id,[]))
            self.bot_id += 1 
            
    def tick(self, tick):
 
        
        print("\n\nTick number = %s:" % tick)
        print("Price = $"+str(self.price))
        #FIRST DANG CASE WHERE THE BUYER ISN"T BUYING AS MUCH AS THE SELLER IS SELLING KINDOF
        for i in range(0,5):
            maxPrice = 0
            minPrice = 0
            for j in range(0,len(self.bots)):           #In this chunk we get the highest and lowest prices being traded
                if self.bots[j].price > self.bots[maxPrice].price and self.bots[j].buy:
                    maxPrice = j
                elif self.bots[j].price < self.bots[minPrice].price and self.bots[j].sell:
                    minPrice = j

            
            if self.bots[maxPrice].price >= self.bots[minPrice].price and self.bots[maxPrice].amount <= self.bots[minPrice].amount and self.bots[maxPrice].amount >0 and self.bots[maxPrice].bot_id != self.bots[minPrice].bot_id and self.bots[maxPrice].buy and self.bots[minPrice].sell:
                print("Bot %s is buying %s %s from Bot %s" % (self.bots[maxPrice].name, self.bots[maxPrice].amount,fun[random.randint(0,len(fun)-1)], self.bots[minPrice].name))
                self.bots[minPrice].amount -= self.bots[maxPrice].amount
                self.bots[minPrice].stuff -= self.bots[maxPrice].amount
                self.bots[minPrice].money += (self.bots[maxPrice].price * self.bots[maxPrice].amount)
                if self.bots[minPrice].amount == 0:
                    self.bots[minPrice].sell = False
                self.bots[maxPrice].stuff += self.bots[maxPrice].amount
                self.bots[maxPrice].money -= (self.bots[maxPrice].amount * self.bots[maxPrice].price)
                self.bots[maxPrice].amount = 0
                self.bots[maxPrice].buy = False
                self.price = self.bots[maxPrice].price
            elif self.bots[maxPrice].price >= self.bots[minPrice].price and self.bots[maxPrice].amount > self.bots[minPrice].amount and self.bots[maxPrice].amount >0 and self.bots[maxPrice].bot_id != self.bots[minPrice].bot_id and self.bots[maxPrice].buy and self.bots[minPrice].sell:
                print("Bot %s is buying %s %s from Bot %s" % (self.bots[maxPrice].name, self.bots[maxPrice].amount,fun[random.randint(0,len(fun)-1)], self.bots[minPrice].name))
                self.bots[maxPrice].amount -= self.bots[minPrice].amount
                self.bots[maxPrice].money -= (self.bots[minPrice].amount * self.bots[maxPrice].price)
                self.bots[maxPrice].stuff += self.bots[minPrice].amount
                self.bots[minPrice].money += (self.bots[minPrice].amount * self.bots[maxPrice].price)
                self.bots[minPrice].stuff -= self.bots[minPrice].amount
                self.bots[minPrice].amount = 0
                self.bots[minPrice].sell = False
                self.price = self.bots[maxPrice].price

            
        for i in range(0,len(self.bots)):
            if tick == 50:
                self.bots[i].toString()
            self.bots[i].tick(tick,self.price)
            if self.bots[i].money < 5 and self.bots[i].stuff < 2:
                print("A bot is broke")
                time.sleep(3)
        if tick == 50:
            time.sleep(30)
            #self.bots[i].toString()

                        
EvoMarket = market()

while True:
    EvoMarket.tick(tickNumber)
    tickNumber+=1
    time.sleep(0.1)
    
    
  













    
        
        
        
