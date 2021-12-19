from math import *
from sympy import *

e = radians(11.36) #angulo de la cercha
a = atan(0.3348/0.83333)
b= atan(2*0.3348/0.83333)
c=b
d= atan(3*0.3348/0.83333)

AB,AC,BC,BD,CD,CE,DE,DF,EF,EG,FG,FH,GH,GI,HI,HJ,IJ,IK,JK = symbols('AB,AC,BC,BD,CD,CE,DE,DF,EF,EG,FG,FH,GH,GI,HI,HJ,IJ,IK,JK')
Va, Ha, Vk = symbols('Va, Ha, Vk')

ec1=[]

#Nodos A-J

#Horizontales en A
ec1.append((Ha+AC+AB*cos(e)))
#Verticales en A
ec1.append((Va+AB*sin(e)-0.5))


#Horizontales en B
ec1.append((BD*cos(e)+BC*cos(a)-AB*cos(e)))
#Verticales en B
ec1.append((BD*sin(e)-AB*sin(e)-BC*sin(a)-1))


#Horizontales en C
ec1.append((CE-AC+CD*cos(b)-BC*cos(a)))
#Verticales en C
ec1.append((BC*sin(a)+CD*sin(b)))


#Horizontales en D
ec1.append((DF*cos(e)+DE*cos(c)-BD*cos(e)-CD*cos(b)))
#Verticales en D
ec1.append((DF*sin(e)-DE*sin(c)-CD*sin(b)-BD*sin(e)-1))


#Horizontales en E
ec1.append((EG-CE+EF*cos(d)-DE*cos(c)))
#Verticales en E
ec1.append((EF*sin(d)+DE*sin(c)))


#Horizontales en F
ec1.append((FH*cos(e)+FG*cos(d)-EF*cos(d)-DF*cos(e)))
#Verticales en F
ec1.append((-FH*sin(e)-FG*sin(d)-EF*sin(d)-DF*sin(e)-1))


#Horizontales en G
ec1.append((GI-EG+GH*cos(c)-FG*cos(d)))
#Verticales en G
ec1.append((GH*sin(c)+FG*sin(d)))


#Horizontales en H
ec1.append((HJ*cos(e)+HI*cos(b)-GH*cos(c)-FH*cos(e)))
#Verticales en H
ec1.append((FH*sin(e)-GH*sin(c)-HI*sin(b)-HJ*sin(e)-1))


#Horizontales en I
ec1.append((IK-GI+IJ*cos(a)-HI*cos(b)))
#Verticales en I
ec1.append((HI*sin(b)+IJ*sin(a)))


#Horizontales en J
ec1.append((JK*cos(e)-IJ*cos(a)-HJ*cos(e)))
#Verticales en J
ec1.append((HJ*sin(e)-IJ*sin(a)-JK*sin(e)-1))


#Horizontales en K
ec1.append((-JK*cos(e)-IK))
#Verticales en K 
ec1.append((JK*sin(e)+Vk-0.5))


X=[Va, Ha, Vk, AB,AC,BC,BD,CD,CE,DE,DF,EF,EG,FG,FH,GH,GI,HI,HJ,IJ,IK,JK]

print(solve(ec1,X))


#CORDON INFERIOR
ec2=[]

#Nodos A-J

#Horizontales en A
ec2.append((Ha+AC+AB*cos(e)))
#Verticales en A
ec2.append((Va+AB*sin(e)-0.5))


#Horizontales en B
ec2.append((BD*cos(e)+BC*cos(a)-AB*cos(e)))
#Verticales en B
ec2.append((BD*sin(e)-AB*sin(e)-BC*sin(a)))


#Horizontales en C
ec2.append((CE-AC+CD*cos(b)-BC*cos(a)))
#Verticales en C
ec2.append((BC*sin(a)+CD*sin(b)-1))


#Horizontales en D
ec2.append((DF*cos(e)+DE*cos(c)-BD*cos(e)-CD*cos(b)))
#Verticales en D
ec2.append((DF*sin(e)-DE*sin(c)-CD*sin(b)-BD*sin(e)))


#Horizontales en E
ec2.append((EG-CE+EF*cos(d)-DE*cos(c)))
#Verticales en E
ec2.append((EF*sin(d)+DE*sin(c)-1))


#Horizontales en F
ec2.append((FH*cos(e)+FG*cos(d)-EF*cos(d)-DF*cos(e)))
#Verticales en F
ec2.append((-FH*sin(e)-FG*sin(d)-EF*sin(d)-DF*sin(e)))


#Horizontales en G
ec2.append((GI-EG+GH*cos(c)-FG*cos(d)))
#Verticales en G
ec2.append((GH*sin(c)+FG*sin(d)-1))


#Horizontales en H
ec2.append((HJ*cos(e)+HI*cos(b)-GH*cos(c)-FH*cos(e)))
#Verticales en H
ec2.append((FH*sin(e)-GH*sin(c)-HI*sin(b)-HJ*sin(e)))


#Horizontales en I
ec2.append((IK-GI+IJ*cos(a)-HI*cos(b)))
#Verticales en I
ec2.append((HI*sin(b)+IJ*sin(a)-1))


#Horizontales en J
ec2.append((JK*cos(e)-IJ*cos(a)-HJ*cos(e)))
#Verticales en J
ec2.append((HJ*sin(e)-IJ*sin(a)-JK*sin(e)))


#Horizontales en K
ec2.append((-JK*cos(e)-IK))
#Verticales en K 
ec2.append((JK*sin(e)+Vk-0.5))


print(solve(ec2,X))

