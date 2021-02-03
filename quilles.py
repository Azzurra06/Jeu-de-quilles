#Azzurra LHOEST - Wiam ELHASNAOUI - PeiP1 G2
#test

from random import *
from turtle import *
import time


#graphique

#procédure qui dessine les demi-cercles pour les quilles
def dessineDemiCercle(l,color):
    color("black","white")
    width(2)
    speed(0)
    begin_fill()
    circle(l,180)
    end_fill()

#procédure pour faire la spirale pour les quilles
def dessineSpirale(l,color):
    color("pink")
    width(3)
    speed(0)
    circle(l+3,-90)
    i=0
    while i<=3:
        circle(l,-180)
        l=l-3
        i=i+1

#procédure pour dessiner les quilles debouts
def quilleDebout(res):
    up()
    goto(-405,-110)
    down()
    
    a=1
    for l in res: #nb_quilles:

        #dessiner les demis-cercles
        i=0
        while i<=5:
            dessineDemiCercle(10,color)
            right(360/3)
            i=i+1
    
        color("white")
        setheading(90)
        begin_fill()

        #dessiner l'hexagone du milieu
        j=0
        while j<=5 :
            forward(19.4)
            left(360/6)
            j=j+1
        end_fill()
    
        #dessiner la spirale
        up()
        x=xcor()-3
        y=ycor()+13
        goto(x,y)
        down()
        dessineSpirale(13,color)

        #se déplacer
        up()
        goto(-405,-110)
        setheading(0)
        forward(a*60)       
        down()
        a=a+1
        


def quilleTombée(res):
    up()
    goto(-405,-110)
    down()
    
    a=1
    for l in res: #nb_quilles:

        if l==".":

            i=0
            while i<=1:
                dessineDemiCercle(10,color)
                right(360/3)
                i=i+1
    
            x1=xcor()
            y1=ycor()
    
            while i<=5:
                print(dessineDemiCercle(10,color))
                right(360/3)
                i=i+1

    
            color("white")
            setheading(90)
            begin_fill()

            j=0
            while j<=5 :
                forward(19.4)
                left(360/6)
                j=j+1
            end_fill()
    

            up()
            x=xcor()-3
            y=ycor()+13
            goto(x,y)
            down()
            dessineSpirale(13,color)

            #dessiner le demi cercle marron pour cacher la moitié de la quille
            up()
            goto(x1,y1+10)
            setheading(180)
            color("#673508")
            begin_fill()
            down()
            circle(30,-180)
            end_fill()

    
        up()
        goto(-405,-110)
        setheading(0)
        forward(a*60)       
        down()
    
        a=a+1
        


#fonction affiche quilles

def afficheQuilles(q,n):
    res=[]
    i=0
    while i<n:
        res.append(".")   #la liste prend autant de . que le nombre de quilles initial
        i=i+1
        
    for l in q :          #pour chaque sous-liste dans liste q
        x=l[1]-l[0]       #calcule le total de quilles levées dans une sous liste
        i=0
        while i<=x:       #pour chaque quille de la sous liste on va lui attribuer "|"
            res[l[0]+i]="|"
            i=i+1
    res="".join(res)      #transforme la liste en chaine de caractère

    up()
    goto(-200,275)
    color("#D5D5D5")
    begin_fill()
    down()
    forward(300)
    left(90)
    forward(20)
    left(90)
    forward(300)
    left(90)
    forward(20)
    left(90)
    end_fill()
    goto(-30,275)
    color("black")
    write("Voici les quilles, il y a "+str(len(q))+" ligne(s)", align = "center", font = ("Arial", 15, "bold"))

    return(res)




#fonction ordinateur

def ordiJoue(q):
    i=randint(0,len(q)-1)     #l'ordinateur choisit une valeur entre 1 et le nombre de sous listes de la liste
    p=choice(["G","M","D"])
    res=str(i)+":"+str(p)
    return res



#fonction joueur

def joueurJoue(q):
    up()
    goto(-30,350)
    i=int(textinput("A vous de jouer !","Choisissez quelle ligne viser entre 1 et " +str(len(q))+ ": "))
    while i<1 or i>len(q):
            i=int(textinput("Erreur","Veuillez choisir une ligne entre 1 et " +str(len(q))+ ": "))  
    i=i-1
    p=str(textinput("A vous de jouer !","Choisissez entre tirer à droite (D), gauche (G) ou milieu (M) : "))
    if p in "GMD":
        p=p
    else:
        p=(str(textinput("Erreur","Veuillez choisir une lettre entre D, G et M : ")))
        while p not in "GMD":
            p=(str(textinput("Erreur","Veuillez choisir une lettre entre D, G et M : ")))
        p=p
        
    res = str(i)+":"+str(p)
    return res



#procédure jouerMilieu

def jouerMilieu(i,q): #pas de p car c'est le milieu
    milieu = (q[i][1]-q[i][0])//2

    if (q[i][1]-q[i][0]+1)%2==0:    #pair
        q.insert(i+1,[q[i][0]+milieu+2,q[i][1]])
        q[i]=[q[i][0],q[i][0]+milieu-1]

    else:    #impair
        b=randint(0,1)

        if b==0:    #impair et on fait tomber la quille de gauche
            q.insert(i+1,[q[i][0]+milieu+2,q[i][1]])
            q[i]=[q[i][0],q[i][0]+milieu-1]

        else:        #impair et on fait tomber la quille de droite
            q.insert(i+1,[q[i][0]+milieu+1,q[i][1]])
            q[i]=[q[i][0],q[i][0]+milieu-2]
            
        
    if q[i+1][0]>q[i+1][1]:
        del(q[i+1])
    if q[i][0]>q[i][1]:    #pour supprimer les listes vides
        del(q[i])
    return q
        

        
#procédure jouerCote

def jouerCote(i,p,q): 
    if p=="G":
        q[i]=[q[i][0]+1,q[i][1]]
        
    else:
        q[i]=[q[i][0],q[i][1]-1]
        
    if q[i][0]>q[i][1]:
        del(q[i])
    return q
    

#procédure jouer

def jouer(c,q):
    i,p=c.split(":")
    i=int(i)
    if p=="G" or p=="D":
        q=jouerCote(i,p,q)
    else:
        q=jouerMilieu(i,q)
    return q





#programme principal
n=randint(5,15)
q=[[0,n-1]]

#interface graphique

#réglages de base
setup(2560, 1600,0,0)
tracer(0)
title("Jeu de quilles ninjas")
bgcolor("#E2CAB9")
speed(0)
hideturtle()



#sol
up()
goto(-700,-50)
down()
begin_fill()
color("black","#C59278")
forward(1400)
right(90)
forward(700)
right(90)
forward(1400)
right(90)
forward(700)
end_fill()


#bande grise
begin_fill()
color("black","#BAA799")
up()
home()
goto(-700,20)
down()
forward(1500)
left(90)
forward(100)
left(90)
forward(1500)
left(90)
forward(100)
up()
home()
end_fill()


#porte
begin_fill()
color("black","#3B1D03")
width(3)
up()
home()
goto(-550,-50)
down()
forward(200)
left(90)
forward(400)
left(90)
forward(200)
left(90)
forward(400)
end_fill()

up()
left(90)
forward(30)
down()
forward(140)
left(90)
forward(370)
left(90)
forward(140)
left(90)
forward(370)

up()
left(90)
forward(163)
left(90)
forward(200)
down()
begin_fill()
color("black")
circle(8)
end_fill()


#yingyang pendus
up()
goto(-250,400)
i=0
while i<=1:
    width(3)
    color("black")
    down()
    setheading(270)
    forward(70)
    x1=xcor()
    y1=ycor()

    setheading(180)
    width(2)
    fillcolor("white")
    begin_fill()
    circle(24, 180)
    end_fill()
    fillcolor("black")
    begin_fill()
    circle(24, 180)
    end_fill()

    #demicercle noir
    up()
    left(90)
    forward(48)
    left(90)
    down()
    begin_fill()
    circle(12, -180)
    end_fill()

    #demicercle blanc
    up()
    left(180)
    down()
    fillcolor("white")
    begin_fill()
    circle(12, 180)
    end_fill()

    #petits ronds
    up()
    left(90)
    forward(12)
    down()
    begin_fill()
    color("black")
    circle(3)
    end_fill()

    up()
    right(180)
    backward(24)
    down()
    begin_fill()
    color("white","white")
    circle(2)
    end_fill()

    up()
    goto(190,400)
    down()
    i=i+1


#tableau d'affichage
up()
goto(-210,350)
width(8)
color("black","#D5D5D5")
begin_fill()
setheading(0)
down()
forward(360)
right(90)
forward(200)
right(90)
forward(360)
right(90)
forward(200)
end_fill()
up()
goto(-30,315)
color("black")
down()
write("Tableau d'affichage",align="center",font=("Arial",20,"bold","underline"))




#bienvenu en chinois
up()
color("black")
home()
goto(x1,y1)
setheading(270)
forward(230)
setheading(180)
forward(500)
down()

i=0
while i<=3:
    width(2)
    setheading(0)
    forward(30)
    right(110)
    forward(25)
    x=xcor()
    y=ycor()
    forward(25)
    up()
    goto(x,y)
    down()
    right(115)
    forward(20)
    left(180)
    up()
    forward(20)
    down()
    forward(20)

    up()
    setheading(0)
    forward(10)
    x=xcor()
    y=ycor()
    left(75)
    down()
    forward(25)
    right(150)
    forward(25)
    left(20)
    forward(35)
    up()
    goto(x,y)
    down()
    right(70)
    forward(35)

    up()
    goto(x-2,y)
    setheading(90)
    forward(32)
    setheading(0)
    down()
    x=xcor()
    y=ycor()
    forward(30)
    right(130)
    forward(20)
    up()
    goto(x,y)
    setheading(0)
    left(70)
    forward(15)
    left(180)
    down()
    forward(35)

    setheading(90)
    up()
    forward(8)
    right(90)
    forward(60)
    down()
    forward(16)
    right(90)
    forward(43)
    x=xcor()
    y=ycor()
    right(60)
    forward(18)
    up()
    goto(x,y)
    setheading(270)
    down()
    left(60)
    forward(18)
    setheading(0)
    forward(60)

    up()
    goto(x,y)
    setheading(90)
    forward(50)
    left(45)
    down()
    forward(20)

    up()
    setheading(0)
    forward(30)
    right(90)
    forward(5)
    x=xcor()
    y=ycor()
    setheading(270)
    down()
    forward(48)
    left(135)
    forward(20)
    up()
    goto(x,y)
    setheading(90)
    right(45)
    down()
    forward(20)

    up()
    setheading(0)
    forward(5)
    right(90)
    forward(74)
    setheading(90)
    down()
    forward(67)
    right(90)
    forward(23)
    right(90)
    forward(47)
    right(90)
    forward(18)
    
    up()
    backward(18)
    setheading(90)
    forward(40)
    setheading(0)
    forward(60)
    down()
    
    i=i+1



#fenêtre
up()
goto(270,360)
width(10)
begin_fill()
color("black","#0F2990")
down()
forward(320)
right(90)
forward(220)
right(90)
x2=xcor()
y2=ycor()
forward(320)
right(90)
forward(220)
end_fill()



#lune
up()
goto(390,290)
width(1)
begin_fill()
color("#D5D5D5")
down()
circle(40)
end_fill()



    
#ninja
#support
up()
goto(x2-150,y2)
begin_fill()
color("black")
down()
setheading(90)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()

#pieds
up()
right(90)
forward(40)
right(90)
i=0
while i<=1:
    begin_fill()
    down()
    forward(4)
    down()
    forward(7)
    left(90)
    forward(13)
    left(90)
    forward(7)
    left(90)
    forward(13)
    up()
    setheading(0)
    forward(11)
    end_fill()
    i=i+1

#jambes
up()
goto(420,195)
begin_fill()
down()
right(55)
for loop in range(2):
    circle(20,90)
    circle(20/2,90)

up()
goto(465,187)
down()
left(35)
for loop in range(2):
    circle(20,90)
    circle(20/2,90)

end_fill()

#corps
up()
goto(439,250)
setheading(0)
begin_fill()
down()
x3=xcor()
y3=ycor()
forward(30)
y4=ycor()
x4=xcor()
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)

end_fill()


#bras
up()
goto(x3-6,y3)
setheading(180)
begin_fill()
down()
i=0
while i<=1:
    left(45)
    for loop in range(2):      
        circle(18,90)    
        circle(18/2,90)
    up()
    goto(x4-7,y4)
    setheading(180)
    down()
    i=i+1
end_fill()

#tête
up()
goto(x4+2,y4+13)
setheading(90)
begin_fill()
down()
circle(17)
end_fill()

#baton
up()
goto(x3,y3)
right(55)
begin_fill()
down()
forward(10)
left(90)
forward(50)
left(90)
forward(10)
left(90)
forward(50)
end_fill()



#table
up()
home()
goto(-400,0)
down()
begin_fill()
color("black","#673508")
width(3)

forward(800)
right(45)
forward(300)
x=xcor()
y=ycor()
setheading(180)
forward(1227)
x2=xcor()
y2=ycor()
right(135)
forward(300)

end_fill()


#pieds
begin_fill()
color("black","#4F2805")
up()
goto(x,y)
down()
setheading(270)
forward(150)
right(90)
forward(70)
right(90)
forward(120)
left(90)
forward(1087)
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(150)
right(90)
forward(1227)

end_fill()




             
    




#algorithme du jeu

quilleDebout(afficheQuilles(q,n))
update()

while q!=[]:
    q=jouer(joueurJoue(q),q)
    quilleTombée(afficheQuilles(q,n))
    update()
    if q==[]:
        up()
        goto(-30,250)
        write("Bravo, vous avez gagné !",align="center",font=("Arial",20,"bold"))
        update()
    else:
        q=jouer(ordiJoue(q),q)
        quilleTombée(afficheQuilles(q,n))
        time.sleep(1)
        update()
        if q==[]:
            up()
            goto(-30,250)
            write("Dommage, l'ordinateur a gagné !",align="center",font=("Arial",20,"bold"))
            update()
    















    
    
