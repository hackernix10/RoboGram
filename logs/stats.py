import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 30, 1)
number_followers = []
gain = []
date = 0
log = open("followerNum.txt", "r")
for line in log:
    buf = int(((line.split())[0])[len((line.split())[0])-2:])
    if ( buf != date):
        date = buf
        number_followers.append((line.split())[2])
#number of followers
if (len(number_followers) < 30):
    plt.plot(days[0:len(number_followers)], number_followers, 'ro')
else:
    plt.plot(days, number_followers[len(number_followers)-30:], 'ro')
    
plt.xlabel('day')
plt.ylabel('number of followers')
plt.show()
#gain per day
for i in range(0, len(number_followers)-1):
    gain.append(int(number_followers[i+1]) - int(number_followers[i]))
if (len(gain) < 30):
    plt.plot(days[0:len(gain)], gain, 'ro', [1, len(gain)], [0, 0])
else:
    plt.plot(days, gain[len(gain)-30:], 'ro', [1, 30], [0, 0])
    
plt.xlabel('day')
plt.ylabel('gain per day')
plt.show()

log.close()