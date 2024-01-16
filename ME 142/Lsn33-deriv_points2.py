import matplotlib.pyplot as plt

# velocity data
t = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
v = [15, 19, 19, 8, 12, 5, 3, 2, 1, 1, 0, 0.5, 1, 2.5, 4, 5, 10, 13, 15, 20, 25]

# calculate acceleration
a = []
for i in range(len(t)):
    if i == 0:
        deriv = (v[i+1]-v[i])/(t[i+1]-t[i])
        a.append(deriv)
    elif i == len(t)-1:
        deriv = (v[i]-v[i-1])/(t[i]-t[i-1])
        a.append(deriv)
    else:
        deriv = (v[i+1]-v[i-1])/(t[i+1]-t[i-1])
        a.append(deriv)

# print time, velocity, and acceleration
print('\nTime (s)  Velocity (ft/s)  Acceleration (ft/s^2)')
for i in range(len(t)):
    print(f'{t[i]:7.1f} {v[i]:18.1f} {a[i]:23.2f}')
print()

# plot velocity and acceleration vs time
plt.plot(t, v, '-bo', label='velocity (ft/s)')
plt.grid(True)
plt.plot(t, a, '-ro', label='acceleration (ft/s^2)')
plt.legend(loc='best')
plt.xlabel('Time (s)')
plt.title('Plot of velocity and acceleration over time')
plt.show()