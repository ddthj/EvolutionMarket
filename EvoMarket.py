'''
Stock Market Evolution Simulator
V1
Michael and Alex

todo list:
-make effects of a transaction actually apply to the bots that made that transaction...
-fix the damn maxPrice issue
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
        self.money = 100 #starting money
        self.stuff = 10  #starting resource
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
            self.name = names[random.randint(0,20)]
            self.sac = args[7] + random.randint(-1,1)
        else:
            self.timing = random.randint(4,10) #how often does it check the market?
            self.medianPrice = random.randint(5,15) #the average price the bot assumes the market will move to
            self.weight = random.randint(1,5) #how quickly the bot adjusts it's median price
            #self.margin = random.randint(1,10) # how low the price must be for the bot to consider buying
            self.fail = random.randint(1,10) # how bad the bot's prediction must be before it accepts defeat and cuts losses
            self.predictionScale = random.randint(2,4) #how fast the bot thinks the price will go back up to median, 10 being fastest
            self.savings = random.randint(25,200) #how much the bots saves for itself when making a baby so that it can live on
            self.name = names[random.randint(0,20)] #gets a random name
            self.sac = random.randint(1,5) #how much the bot sacrifices to get a succesful transaction

        self.prediction = self.medianPrice
        print("Bot "+str(self.name)+" has been born!")
    
    def tick(self,tick,price):
        self.medianPrice = self.medianPrice + int((price-self.medianPrice)/self.weight)
        if tick % self.timing == 0:
            #print(str(self.name)+", id #"+str(self.bot_id)+", is thinking about the market...\n")
            if price > self.medianPrice and self.stuff > 0 and self.buy == False:
                self.sell = True
                self.price = price - self.sac
                self.amount = self.stuff
                print("LogSellMade: price "+str(price)+"median price" +str(self.medianPrice))
            elif price <= self.medianPrice and self.money >0 and self.sell == False:
                self.buy = True
                self.price = price + self.sac
                self.amount = int((self.price/self.money)-1)

            self.prediction = price + int((self.medianPrice - price)/self.predictionScale)
    def set(self.money,amount,buy,sell):
        
            
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
        self.price = 10
        
        for i in range (0,200):
            self.bots.append(Bot(self.bot_id,[]))
            self.bot_id += 1 
            
    def tick(self, tick):
 
        maxPrice = 0
        minPrice = 0

        print("Price = $"+str(self.price))
        
        for i in range(0,len(self.bots)):           #In this chunk we get the highest and lowest prices being traded
            if self.bots[i].price > self.bots[maxPrice].price and self.bots[i].buy == True:
                maxPrice = i
                print("maxPrice: HELPPPP")
                print(self.bots[i].price)
            elif self.bots[i].price < self.bots[minPrice].price and self.bots[i].sell == True:
                minPrice = i
                print("minPrice: HELPPPPP")
                print(self.bots[i].name)
  
        # CASE ONE: BUYER IS BUYING LESS THAN OR EQUAL TO CHEAPEST SELLER
        if self.bots[maxPrice].price >= self.bots[minPrice].price and self.bots[maxPrice].amount <= self.bots[minPrice].amount:
            self.bots[minPrice].amount -= self.bots[maxPrice].amount
            self.bots[minPrice].stuff -= self.bots[maxPrice].amount                   #getting the seller's values all good
            self.bots[minPrice].money += self.bots[maxPrice].amount * self.bots[maxPrice].price#Seller always gets the best deal here
            if self.bots[minPrice].amount == 0:
                self.bots[minPrice].sell = False
            self.bots[maxPrice].stuff += self.bots[maxPrice].amount
            self.bots[maxPrice].money -= self.bots[maxPrice].amount * self.bots[maxPrice].price # getting buyer's values all good
            self.bots[maxPrice].buy = False
            self.bots[maxPrice].amount = 0
            self.price = self.bots[maxPrice].price
            print("an unknown transaction was made")
        # CASE TWO: BUYER IS BUYING MORE THAN CHEAPEST SELLER
        elif self.bots[maxPrice].price >= self.bots[minPrice].price and self.bots[maxPrice].amount > self.bots[minPrice].amount:
            self.bots[minPrice].stuff -= self.bots[minPrice].amount
            self.bots[minPrice].money += self.bots[minPrice].amount * self.bots[maxPrice].price
            self.bots[maxPrice].amount -= self.bots[minPrice].amount
            self.bots[maxPrice].money -= self.bots[maxPrice].price * self.bots[minPrice].amount
            self.bots[maxPrice].stuff += self.bots[minPrice].amount
            print("Bot %s, id #%s, bought %s %s for $%s" % self.bots[maxPrice].name, self.bots[maxPrice].bot_id, self.bots[maxPrice].amount, fun[random.randint(0,16)], self.bots[maxPrice].amount*self.bots[maxPrice].price)
            self.bots[minPrice].amount = 0
            self.bots[minPrice].sell = False
            self.price = self.bots[maxPrice].price
            
                
        for i in range(0,len(self.bots)):
            self.bots[i].tick(tick,self.price)
            self.bots[i].toString()

                        
EvoMarket = market()

while True:
    print("\nTick number %s:" % tickNumber)
    EvoMarket.tick(tickNumber)
    tickNumber+=1
    time.sleep(3)
    
    
  













    
        
        
        
