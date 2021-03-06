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
    "Pip",
    "Richard",
    "Nixon",
    "Drew",
    "Nick",
    "Gatsby",
    "Donny",
    "Jacob",
    "Dog",
    "Jeff",
    "Skinny",
    "Joseph",
    "RAiZ",
    "Granny",
    "Ethan",
    "Hannah",
    "Moneybags McGee",
    "Mary",
    "Jesus",
    "Asher",
    "Atticus",
    "Declan",
    "Oliver",
    "Olivia",
    "Charlotte",
    "Ava",
    "Elanor",
    "Astrid",
    "Leo",
    "Jasper",
    "Henry",
    ]

fun = [
    "bananas",
    "children",
    "bitcoin",
    "apple stock",
    "bathtubs",
    "masterlocks",
    "fish insurance contracts",
    "pneumatic fluid cpntainers",
    "blue oranges",
    "nothing bottles",
    "robots",
    "chinese products",
    "soft drives",
    ".com domains",
    "infomercial products",
    "time",
    "toasters",
    "earthquakes",
    "dogs",
    "cats",
    "toilets",
    "reputable .tk domains",
    "'legit' video games",
    "orange oranges",
    "lockpicks",
    "steam accounts",
    "not hacks",
    "not viruses i swear",
    "drum sets",
    "banjos",
    "college degrees",
    "money bags",
    "swag",
    ]

class Bot():
    def __init__(self,bot_id,args):
        self.money = 80 #starting money
        self.stuff = 80  #starting resource
        self.bot_id = bot_id
        self.buy = False
        self.sell = False
        self.amount = 0
        self.price = 0
        self.alive = True #bots can kill themselves
        self.makeBaby = False
        
        if len(args) > 1:
            self.timing = args[0] + random.randint(-5,5) 
            self.medianPrice = args[1] + random.randint(-2,2) 
            self.weight = args[2] + random.randint(-2,2)
            #self.margin = args[3] + random.randint(-2,2)
            self.fail = args[4] + random.randint(-2,2)
            self.predictionScale = args[5] + random.randint(-1,1) 
            self.savings = args[6] + random.randint(-100,100)
            if self.savings < 0:
                self.savings = 0
            self.name = names[random.randint(0,len(names)-1)]
            self.sac = args[7] + random.randint(-1,1)
            if self.predictionScale <=0:
                self.predictionScale = 1
        else:
            self.timing = random.randint(4,10) #how often does it check the market?
            self.medianPrice = random.randint(15,25) #the average price the bot assumes the market will move to
            self.weight = random.randint(1,3) #how quickly the bot adjusts it's median price
            #self.margin = random.randint(1,10) # how low the price must be for the bot to consider buying
            self.fail = random.randint(1,5) # how bad the bot's prediction must be before it accepts defeat and cuts losses
            self.predictionScale = random.randint(2,4) #how fast the bot thinks the price will go back up to median, 10 being fastest
            self.savings = random.randint(10,1500) #how much the bots saves for itself when making a baby so that it can live on
            self.name = names[random.randint(0,len(names)-1)] #gets a random name
            self.sac = random.randint(1,5) #how much the bot sacrifices to get a succesful transaction

        self.prediction = self.medianPrice
        print("Bot "+str(self.name)+" has been born!")
    
    def tick(self,tick,price):
        self.medianPrice = self.medianPrice + int((price-self.medianPrice)/random.randint(1,2)) + random.randint(-2,2)
        self.prediction = price + int((self.medianPrice - price)/self.predictionScale)
        if self.alive:
            if 100 < self.money - self.savings:
                self.makeBaby = True
                self.money -= 100
            if self.money < price and self.stuff < 50 and self.sell == False:
                self.alive = False
                print("\n\n%s has commited suicide after running out of money and %s to sell\n\n" % (self.name,fun[random.randint(0,len(fun)-1)]))

            if price > self.medianPrice:
                if price < self.price - self.fail and self.sell == True:
                    self.price -= self.fail
                if self.stuff >= self.money and self.buy == False:
                    self.sell = True
                    self.amount = self.stuff
                    self.price = price - self.sac
                else:
                    self.buy = False

            elif price < self.medianPrice:
                if price > self.fail + self.price and self.buy == True:
                    self.price += self.fail
                if self.money >= self.stuff and self.sell == False:
                    self.buy = True
                    self.price = price + self.sac
                    if self.price + 1 <= 0:
                        self.price = 0
                    self.amount = int(self.money/(self.price + 1))
                else:
                    self.sell = False
            
            
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
        
        for i in range (0,100):
            self.bots.append(Bot(self.bot_id,[]))
            self.bot_id += 1 
            
    def tick(self, tick):
        print("\n\nTick number = %s:" % tick)
        print("Price = $"+str(self.price))
        #FIRST DANG CASE WHERE THE BUYER ISN"T BUYING AS MUCH AS THE SELLER IS SELLING KINDOF
        transaction = False
        for i in range(0,5):
            maxPrice = 0
            minPrice = 0
            
            for j in range(0,len(self.bots)):           #In this chunk we get the highest and lowest prices being traded
                if self.bots[j].price > self.bots[maxPrice].price and self.bots[j].buy and self.bots[j].alive:
                    maxPrice = j
                elif self.bots[j].price < self.bots[minPrice].price and self.bots[j].sell and self.bots[j].alive:
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
                self.price = int((self.bots[maxPrice].price - (self.bots[maxPrice].price-self.bots[minPrice].price)/ 5))
                transaction = True
            elif self.bots[maxPrice].price >= self.bots[minPrice].price and self.bots[maxPrice].amount > self.bots[minPrice].amount and self.bots[maxPrice].amount >0 and self.bots[maxPrice].bot_id != self.bots[minPrice].bot_id and self.bots[maxPrice].buy and self.bots[minPrice].sell:
                print("Bot %s is buying %s %s from Bot %s" % (self.bots[maxPrice].name, self.bots[maxPrice].amount,fun[random.randint(0,len(fun)-1)], self.bots[minPrice].name))
                self.bots[maxPrice].amount -= self.bots[minPrice].amount
                self.bots[maxPrice].money -= (self.bots[minPrice].amount * self.bots[maxPrice].price)
                self.bots[maxPrice].stuff += self.bots[minPrice].amount
                self.bots[minPrice].money += (self.bots[minPrice].amount * self.bots[maxPrice].price)
                self.bots[minPrice].stuff -= self.bots[minPrice].amount
                self.bots[minPrice].amount = 0
                self.bots[minPrice].sell = False
                self.price = int((self.bots[maxPrice].price - (self.bots[maxPrice].price-self.bots[minPrice].price)/ 5))
                transaction = True

        dead = 0
        for i in range(0,len(self.bots)):
            if self.bots[i].alive == False:
                dead +=1
            if self.bots[i].makeBaby == True and self.bots[j].alive:
                self.bots.append(Bot(self.bot_id,[self.bots[i].timing,self.bots[i].medianPrice,self.bots[i].weight,1,self.bots[i].fail,self.bots[i].predictionScale,self.bots[i].savings,self.bots[i].sac]))
                self.bots[i].makeBaby = False
                self.bot_id +=1    
            self.bots[i].tick(tick,self.price)
            
        if transaction == False:
            if self.price > 67:
                self.price = int(((self.bots[maxPrice].price + self.bots[minPrice].price)-4)/ 2 )
            else:
                self.price = int(((self.bots[maxPrice].price + self.bots[minPrice].price)-2)/ 2 )
        if self.price <= 5:
            self.price = 5
            
        if tick % 100 == 0:
            maxMoney = 0
            minMoney = 0
            for a in range(0,len(self.bots)):
                if self.bots[a].money+(self.bots[a].stuff*self.price) > self.bots[maxPrice].money and self.bots[a].alive:
                    maxMoney = a
                elif self.bots[a].money+(self.bots[a].stuff*self.price) < self.bots[minPrice].money and self.bots[a].alive:
                    minMoney = a
            print("\nThe bot with the most money is %s with $%s!" % (self.bots[maxMoney].name,self.bots[maxMoney].money))
            print("The bot with the least money is %s with $%s!" % (self.bots[minMoney].name,self.bots[minMoney].money))
            print("There are %s alive bots and %s dead bots" % ((len(self.bots) - dead),dead))
            input(">")
            
            #self.bots[i].toString()

                        
EvoMarket = market()

while True:
    EvoMarket.tick(tickNumber)
    tickNumber+=1
    #time.sleep(0.1)
    
    
  













    
        
        
        
