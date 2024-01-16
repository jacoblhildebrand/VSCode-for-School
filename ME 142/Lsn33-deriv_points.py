"""





"""
import matplotlib.pyplot as plt

#define
x = [1,2.5,4,5,8,10,11.5,15]
y = [5,8,13.5,17,21,22.5,24.5,26]

slope=[]
#approximate
for i in range(len(x)):
    if i == 0:
        deriv = (y[i+1]-y[i])/(x[i+1]-x[i])
        slope.append(deriv)
    elif i == len(x)-1:
        deriv = (y[i]-y[i-1])/(x[i]-x[i-1])
        slope.append(deriv)
    else:
        deriv = (y[i+1]-y[i-1])/(x[i+1]-x[i-1])
        slope.append(deriv)

#print
print('\nTime (s)  Position (ft)  Velocity (ft/s)')
for i in range(len(x)):
    print(f'{x[i]:5.1f} {x[i]:11.1f} {slope[i]:14.2f}')
print()

#plot
plt.plot(x,y,'-bo',label = 'position (ft)')
plt.grid(True)
plt.plot(x,slope,'-ro',label = 'Velocity (ft/s)')
plt.legend(loc = 'right')
plt.xlabel('Time (s)')
plt.title('Plot of position and velocity over time')
plt.xlim(0,16)
plt.ylim(0.30)
plt.show()