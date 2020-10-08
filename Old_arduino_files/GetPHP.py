import urllib.request as urllib2
def fromPHP(n):
    temp = 0
    for line in urllib2.urlopen("https://design.ece.msstate.edu/2020/team_harris/EcoKennelServer/toPI.txt"):
       if(temp == n):
           return line
       else:
            temp = temp + 1
            
#Below lines are for testing purposes only
            
#outputtext = fromPHP(2)
#print(outputtext)
#b = str(outputtext, 'utf-8')
#print(b) 

    