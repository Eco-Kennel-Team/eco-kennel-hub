import urllib.request as urllib2
#Call with an int. Will return the n'th line of data

def toPHP(Var1, Var2, Var3):
   
    urllib2.urlopen("https://design.ece.msstate.edu/2020/team_harris/EcoKennelServer/Data.php?Var1=" + Var1 + "&Var2=" + Var2 + "&Var3=" + Var3)
    
            
#Below lines are for testing purposes only
#toPHP("Hello", "Hi", "Bonnie")
            