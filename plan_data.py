class Plan(object):
    def __init__(self,meals,points,price,year):
        self.meals = meals
        self.points = points
        self.price = price
        self.year = year
    def worth(self):
        return 8.75*self.meals*16 + self.points

class Block_Plan(Plan):
    def worth(self):
        return 8.75*self.meals + self.points        

year = 2018
plan_objects = []
plans = open('plan_data.txt').read().splitlines()
i = 0
while (i<len(plans)):
    if plans[i]=='.':
        year-=1
        i+=1
    else:
        plan_objects.append(Plan(int(plans[i]),int(plans[i+1]),int(plans[i+2]),year))
        i+=3

    
for p in plan_objects:
    print str(p.year)+" "+str(p.meals)+" meal plan: "+str(p.worth()-p.price)
    
year = 2017
block_objects = []
block_plans = open('block_data.txt').read().splitlines()
i = 0
while (i<len(block_plans)):
    if block_plans[i]=='.':
        year-=1
        i+=1
    else:
        block_objects.append(Block_Plan(int(block_plans[i]),int(block_plans[i+1]),int(block_plans[i+2]),year))
        i+=3

print "blocks:"
for p in block_objects:
    print str(p.year)+" "+str(p.meals)+" meal plan: "+str(p.worth()-p.price)
