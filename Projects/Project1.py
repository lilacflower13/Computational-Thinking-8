###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("purplebackground")
q1 = codesters.Square(100, 100, 200, 'purple')
q2 = codesters.Square(-100, 100, 200, 'pink')
q3 = codesters.Square(-100, -100, 200, 'violet')
q4 = codesters.Square(100, -100, 200, 'magenta')

s1 = codesters.Sprite("mountain",-85,-160)
s1.set_size(0.4)
s2 = codesters.Sprite("Lilac",100,100)
s2.set_size(0.7)
s3 = codesters.Sprite("sun",-145,-45)
s3.set_size(0.7)
s4 = codesters.Sprite("headphones",-100,100)
s4.set_size(0.7)
s5 = codesters.Sprite("doggie",110,-100)
s5.set_size(0.7) 
s6 = codesters.Sprite("star",40,-50)
s6.set_size(0.2) 



message1 = codesters.Text("Lila Mae Vail",0,230,"purple") 
message2 = codesters.Text("'Being fearless isn't being 100% not fearful,",0,-220,"black")
message3 = codesters.Text("it's being terrified but you jump anyway'",0,-240,"black")