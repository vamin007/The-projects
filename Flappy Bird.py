{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 app.stepsPerSecond = 60\
\
\
#BackGround and ground\
app.background='lightSkyBlue'\
Rect(0,345,400,55, fill = 'paleGoldenrod')\
Rect(0,330,400,15, fill = 'limeGreen')\
line2 = Line(500,330,1000,330, fill='forestgreen', dashes=True,lineWidth=25)\
line1 = Line(0,330,500,330, fill = 'forestGreen', dashes=True,lineWidth=25)\
Line(0,345,400,345, fill = 'sandyBrown')\
\
\
#Clouds\
def drawClouds(x,y):\
    Circle(x,y,35, fill='floralWhite', border='black', borderWidth=0.5)\
    Circle(x+50,y,25, fill='floralWhite', border='black', borderWidth=0.5)\
\
drawClouds(20,258)\
drawClouds(130,258)\
drawClouds(230,258)\
drawClouds(270,258)\
drawClouds(370,258)\
Rect(0,258,400,70, fill='floralWhite')\
\
\
#Pipes\
LowPipes1=Group(\
Rect(570,285,50,45, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(563,265,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(570,0,50,115, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(563,115,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
MidPipes1=Group(\
Rect(320,255,50,75, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(313,235,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(320,0,50,93, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(313,93,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
HighPipes1=Group(\
Rect(445,215,50,115, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(438,195,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(445,0,50,75, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(438,75,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
LowPipes2=Group(\
Rect(690,285,50,45, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(683,265,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(690,0,50,115, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(683,115,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
MidPipes2=Group(\
Rect(930,255,50,75, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(923,235,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(930,0,50,93, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(923,93,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
HighPipes2=Group(\
Rect(810,215,50,115, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(803,195,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(810,0,50,75, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(803,75,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
LowPipes3=Group(\
Rect(1050,285,50,45, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1043,265,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1050,0,50,115, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1043,115,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
MidPipes3=Group(\
Rect(1170,255,50,75, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1163,235,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1170,0,50,93, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1163,93,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
HighPipes3=Group(\
Rect(1290,215,50,115, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1283,195,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1290,0,50,75, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1283,75,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
LowPipes4=Group(\
Rect(1530,285,50,45, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1523,265,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1530,0,50,115, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1523,115,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
MidPipes4=Group(\
Rect(1410,255,50,75, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1403,235,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1410,0,50,93, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1403,93,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
HighPipes4=Group(\
Rect(1657,215,50,115, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1650,195,63,25, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1657,0,50,75, fill = 'limeGreen',borderWidth = 2, border='black'),\
Rect(1650,75,63,25, fill = 'limeGreen',borderWidth = 2, border='black'))\
\
\
#Pipes being put into groups\
Sequence1 = Group(\
    LowPipes1,\
    MidPipes1,\
    HighPipes1,\
    )\
\
Sequence2 = Group(\
    LowPipes2,\
    MidPipes2,\
    HighPipes2)\
\
Sequence3 = Group(\
    LowPipes3,\
    MidPipes3,\
    HighPipes3)\
    \
Sequence4 = Group(\
    LowPipes4,\
    MidPipes4,\
    HighPipes4)\
\
\
#Groups of Pipes being put into a group\
Sequence1and2= Group(\
    Sequence1,\
    Sequence2)\
    \
Sequence3and4 = Group(\
    Sequence3,\
    Sequence4)\
\
\
#Bird\
birdie = Group(\
    Rect(212,208,16,12, fill='white'),\
    Rect(216,204,8,4, fill='white'),\
    Rect(216,220,20,4,fill='white'),\
    Rect(228,212,4,8, fill='white'),\
    Rect(200,200,24,4),\
    Rect(200,204,8,4, align= 'top-right'),\
    Rect(192,208,4,4,align = 'top-right'),\
    Rect(180,212,16,4),\
    Rect(180,216,4,12,align='top-right'),\
    Rect(180,228,4,4),\
    Rect(184,232,12,4),\
    Rect(184,236,4,4),\
    Rect(188,240,8,4),\
    Rect(196,244,20,4),\
    Rect(216,244,24,20, align='bottom-left'),\
    Rect(224,204,4,4, align='top-left'),\
    Rect(228,208,4,4),\
    Rect(232,212,4,12),\
    Rect(196,216,4,4),\
    Rect(200,220,4,8),\
    Rect(196,232,4,4, align='bottom-left'),\
    Rect(228,212,4,8,align='top-right'),\
    Rect(212,204,4,4),\
    Rect(212,208,4,12, align='top-right'),\
    Rect(212,220,4,4,align='top-left'),\
    Rect(212,228,4,4),\
    Rect(208,232,4,4),\
    Rect(212,236,4,4),\
    Rect(212,232,4,4,fill='tomato'),\
    Rect(216,236,20,4,fill='tomato'),\
    Rect(216,228,24,4,fill='tomato'),\
    Rect(240,228,4,4),\
    Rect(180,228,4,4,align='bottom-left',fill='yellow'),\
    Rect(184,232,12,4,align='bottom-left', fill='yellow'),\
    Rect(196,228,4,4,align='bottom-left', fill='yellow'),\
    Rect(196,212,12,4,fill='yellow'),\
    Rect(200,208,8,4,fill='yellow'),\
    Rect(200,216,8,4,fill='yellow'),\
    Rect(204,220,8,4,fill='yellow'),\
    Rect(204,224,12,4,fill='yellow'),\
    Rect(200,228,12,4,fill='yellow'),\
    Rect(196,232,12,4,fill='orange'),\
    Rect(188,236,24,4,fill='orange'),\
    Rect(196,240,20,4,fill='orange'),\
    Rect(180,216,16,8,fill='white'),\
    Rect(184,224,12,4,fill='white'),\
    Rect(196,220,4,4, fill='white'),\
    Rect(192,208,8,4, fill='white'),\
    Rect(200,204,12,4,fill='white')\
)\
\
#counters for Scoring\
counter1 = Label(0,0,0, visible = False)\
\
counter2 = Label(0,200,20,size = 30,visible=True)\
\
\
#endScreen\
endScreen = Group (\
    Rect(0,0,400,400, fill='lightCoral', border='fireBrick', borderWidth = 6),\
    Label('You Lost!',200,200, size =50,fill= 'fireBrick',font='orbitron'), \
    Label('Skill Issue??', 200,270, size =20, fill='fireBrick',font='orbitron'),\
    Label('Score:',200,70, size = 30, fill='fireBrick', font='orbitron'),\
    visible= False\
) \
\
\
#StartScreen\
startScreen = Group(\
    Rect(0,0,400,400, fill='lightGreen', border='forestGreen', borderWidth = 6),\
    Label('Press r to start',200,200, size = 42, fill='forestGreen',font='orbitron'),\
    Label('Press space to jump',200,300, size = 20, fill='forestGreen',font='orbitron')\
    )\
    \
    \
#placement, and shape of bird\
birdie.centerY=150\
\
birdie.width-=26\
birdie.height-=20\
\
birdie.dy1 = 0\
birdie.dy2 = 0\
\
\
#onStep\
def onStep():\
    \
    \
    #Gravity of Bird\
    birdie.centerY += birdie.dy1\
    birdie.dy1+= birdie.dy2\
\
\
    #Movement of Pipes and 'Ground'\
    if(startScreen.visible ==False):\
        Sequence1and2.centerX-=3\
        Sequence3and4.centerX-=3\
        line1.centerX -=3\
        line2.centerX-=3\
        \
        if(line2.centerX <=200):\
            line1.left = line2.right\
        \
        if(line1.centerX <=200):\
            line2.left = line1.right\
            \
    #Used to loop the pipes so the game seems infinite\
    if(Sequence1and2.right <=0):\
        Sequence1and2.left = Sequence3and4.right +60\
\
    elif(Sequence3and4.right <=0):\
        Sequence3and4.left = Sequence1and2.right +60\
        \
        \
    #Score(Increases every second)\
    if(endScreen.visible ==False and startScreen.visible ==False):\
        counter1.value+=1\
        \
        if(counter1.value == 60):\
            counter2.value +=1\
            counter1.value=0\
    \
    \
    #If the Bird hits the ground, stop movement of bird\
    if(birdie.bottom >= 330):\
        birdie.dy1=0\
        birdie.dy2=0\
        birdie.dr1=0\
        \
        \
    #If bird hits the pipes or ground, display the endscreen\
    if(birdie.bottom >=330 or birdie.hitsShape(Sequence1and2) or birdie.hitsShape(Sequence3and4)):\
        endScreen.toFront()\
        endScreen.visible =True\
        counter2.toFront()\
        counter2.centerY = 110\
        counter2.fill = 'fireBrick'\
    \
    \
#Used for player to game interaction\
def onKeyPress(key):\
    \
    \
    #When the startscreen is visible, click 'r' to start and start gravity of Bird\
    if(key == 'r' and startScreen.visible==True):\
        startScreen.visible=False\
        birdie.dy1 = .1\
        birdie.dy2 = .2\
\
\
    #If space is clicked, the bird will 'jump' up\
    if(key == 'space' and birdie.bottom <=330 and startScreen.visible ==False):\
        birdie.dy1= -3\
    \
        \
}