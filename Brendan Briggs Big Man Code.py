import webbrowser as wb
import pyautogui as pg
import time as t
points = 0

show = pg.prompt("What is your favorite show? ")
if show == "Hannah Montana":
    pg.alert ("Get Hexed ur mad lmao ")
    
    points+= 999
    wb.open("https://www.youtube.com/watch?v=t93u0qg5q_M")
elif show == "Adventure Time":
    pg.alert ("Jeez man what a tear jerker, may it forever be in our hearts") 
    points+= 7235
    wb.open("https://www.youtube.com/watch?v=74GhZ67ypRI")
elif show== "Dance Moms":
    pg.alert ("Woohoo ur a large man")
    points+= 23435
    wb.open("https://www.youtube.com/watch?v=SB09k1Avb9s")
elif show== "Gilmore Girls":
    pg.alert ("vic Roy nae nae")
elif show== "Friday Night Lights":
    pg.alert ("Woohoo ur a large man Football dude")
elif show== "Thomas the Train":
    pg.alert ("ChooChoo woohoo")
else:
    pg.alert ("Wow trash player back to the lobby ")
    points-= 69
    wb.open("https://www.youtube.com/watch?v=xkKFKwNUw40")
t.sleep(6)
food = pg.prompt("What is your favorite food? ")
if food== "Mac and Cheese":
    pg.alert ("Nice me too ")
    points += 50
    wb.open("https://www.youtube.com/watch?v=CTudZSGnkAs")
elif food== "Meatballs":
    pg.alert("Wow ur as big as a mountain")
    points += 679
    wb.open("https://www.youtube.com/watch?v=JGBE3eLpvm0")
elif food == "Loot Horse":
    pg.alert("Make Loot Horses Great AGAIN Wahoo")
    points += 23571
    wb.open("https://www.youtube.com/watch?v=g1iB_oAZYxc")
elif food== "Calzone":
    pg.alert("mountain of Man")
elif food== "Cantaloupe":
    pg.alert("Wow ur not huge")
elif food== "Watermelon":
    pg.alert("Wow ur bad")
else:
    pg.alert ("garbage rat peasant food plz just gain some kulture smh")
    wb.open("https://www.youtube.com/watch?v=Rq0DtugXMkA")
game = pg.prompt("What is your favorite video game? ")
if game == "Fortnite":
    pg.alert ("wow normie memees")
    points -= 35798
    wb.open("https://www.youtube.com/watch?v=HEVGGBkCo_Y")
elif game == "Minecraft":
    pg.alert ("ah I spy with my little eye a man of kulture")
    points += 12537
    wb.open("https://www.youtube.com/watch?v=nL4i9FKuiEA")
elif game == "PUBG":
    pg.alert ("Jeez your old")
    wb.open("https://www.youtube.com/watch?v=afFD-0TmIGg")
    points+= 999
elif game == "poolhouse":
    pg.alert ("Good Try Ryan")
    points+= 999
elif game == "Grammarly":
    pg.alert ("What the English Teacher")
    points+= 999
elif game == "pHONEAS AND fRoB":
    pg.alert ("What the memememe")
    points+= 999
elif game == "FifA":
    pg.alert ("U r a bigFlopper")
    points+= 999
elif game == "NHL":
    pg.alert ("Ruff Stuff bud")
    points+= 999
else:
    pg.alert("Im too lazy to um write out the other ones so bad answer")
    points+= 12536
    wb.open("https://www.youtube.com/watch?v=nkAEdumSfCc")
sport = pg.prompt("whats ur favorite sport")
if sport == "Hockey":
    pg.alert ("Yesss another man of Kulture")
    wb.open("https://www.youtube.com/watch?v=-5xkMNIt-5k")
    points+= 999
elif sport== "Crocquet":
    pg.alert ("Sport of Champs")
    wb.open("https://www.youtube.com/watch?v=K0XdsHfUpco")
    points+= 999
elif sport== "Dance":
    pg.alert ("Pick a better one")
    wb.open("https://www.youtube.com/watch?v=pJRHozo-jqU")
elif sport== "Lacrosse":
    pg.alert ("Sport of long hair and bruises")
    points+= 999
elif sport== "Foortball":
    pg.alert ("Theo Thinks he is large")
elif sport== "Curling":
    pg.alert ("Good Job")
    wb.open("https://www.youtube.com/watch?v=Sct5j7Quo54")
    points+= 999
else:
    pg.alert("REEEE i only chose the best sports so dont be offended")
season= pg.prompt("whats ur favorite sport")
if season == "Winter":
    pg.alert ("Yesss me too")
    points+= 999
elif season== "Fall":
    pg.alert ("Pumpkin Spice Season")
    wb.open ("http://time.com/money/5412045/pumpkin-spice-latte-most-popular-state/")
    points+= 999
elif season== "Spring":
    pg.alert ("Strong Choice")
    wb.open("https://www.youtube.com/watch?v=3hc2lLk3GoI")
    points+= 999
elif season== "Summer":
    pg.alert ("Thank God Rill cant make us do this anymore")
    wb.open("https://www.youtube.com/watch?v=a8PrHKnvgH8")
    points+= 999
elif season== "Autumn":
    pg.alert ("Extremely Fancy")
    wb.open("https://www.youtube.com/watch?v=SPKFOZBe0-o")
    points+= 999
elif season== "Hockey Season":
    pg.alert ("Good Job Mr.bas")
else:
    pg.alert("REEEE i only chose the best seasons so dont be offended")
wb.open("https://www.youtube.com/watch?v=EP8EWAk-7e4")

pg.alert("You scored: ")
pg.alert(points)
