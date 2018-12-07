import matplotlib.pyplot as plt 
import numpy as np  
a=10
b=1
l=0.1
k=1
w=25       
def fR(t,R,F):
   return -w*F
def fF(t,R,F):
   return  R

print("=========================================================================================")
print(" ")
print("========== HARMONIC OSCILLATOR PHASE SPACE DIAGRAM ============")
print(" ")
print("=========================================================================================")

t=input("Initial time value : ")
h=input('Enter time step, eg:0.01 : ')
R=input("Initial velocity : ")
F=input("Initial position : ")
N=input('Enter the number of iterations ,i.e , number of points that should be on your plot : ')
R1=[]
F1=[]
T=[]
T.append(t)
R1.append(R)
F1.append(F)
for i in range(1,N+1,1):
       k1R=fR(t,R,F)
       k1F=fF(t,R,F)
       k2R=fR(t+h/2,R+k1R*h/2,F+k1F*h/2)
       k2F=fF(t+h/2,R+k1R*h/2,F+k1F*h/2)
       k3R=fR(t+h/2,R+k2R*h/2,F+k2F*h/2)
       k3F=fF(t+h/2,R+k2R*h/2,F+k2F*h/2)
       k4R=fR(t+h,R+k3R*h,F+k3F*h)
       k4F=fF(t+h,R+k3R*h,F+k3F*h)
       R=R+(k1R+2*k2R+2*k3R+k4R)*h/6
       R1.append(R)
       F=F+(k1F+2*k2F+2*k3F+k4F)*h/6
       F1.append(F)
       t=t+h
       T.append(t)
plt.plot(R1, F1, color='green', linestyle='dashed', linewidth = 1,markersize=12) 
plt.ylim(-100,100) 
plt.xlim(-100,100) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis')  
plt.title('simple harmonic oscillator') 
plt.show() 
