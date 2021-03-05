import os
os.system('cls')

def highestbid(h):
    maxi=0
    for i in h:
        if h[i]>maxi:
                maxi=h[i]
                name=i
    print(f"Highest bid is of {maxi} by {name}")
  
print('''
       ,
      /(  ___________
     |  >:===========`
      )(
''')        
h={}
bidding=True
while bidding:
    name=input("Enter your name: ")
    bet=int(input("Enter your bet: $"))
    h[name]=bet
    repeat=input("Do you want add one more bet? (type 'yes' or 'no') ")
    if repeat=="yes":
        os.system('cls')

    else:
        bidding=False
        highestbid(h)
        
            
    
    
        
