#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.suptitle('All in One')
plt.subplots_adjust(wspace=0.5, hspace=1)

plt.rc('axes', titlesize='x-small')
plt.rc('axes', labelsize='x-small')
plt.rc('legend', fontsize='x-small')

# Graph #0
plot1 = plt.subplot(321)
plot1.set_xlim(0, 10)
plot1.set_yticks(np.arange(0, 1500, step=500))
plot1.set_xticks(np.arange(0, 11, step=2))
plot1.plot(y0, c='r')

# Graph #1
plot2 = plt.subplot(322)
plot2.set_title("Men's Height vs Weight")
plot2.set_xlabel("Height (in)")
plot2.set_ylabel('Weight (lbs)')
plot2.scatter(x1, y1, s=10, c='m')

# Graph #2
plot3 = plt.subplot(323)
plot3.set_title('Exponential Decay of C-14')
plot3.set_xlabel('Time (years)')
plot3.set_ylabel('Fraction Remaining')
plot3.set_yscale('log')
plot3.set_xlim(0, 28650)
plot3.plot(x2, y2)

# Graph #3
plot4 = plt.subplot(324)
plot4.set_title("Exponential Decay of Radioactive Elements")
plot4.set_xlabel('Time (years)')
plot4.set_ylabel('Fraction Remaining')
plot4.set_xlim(0, 20000)
plot4.set_ylim(0, 1)
plot4.plot(x3, y31, c='r', linestyle='dashed', label='C-14')
plot4.plot(x3, y32, c='g', label='Ra-226')
plot4.legend()

# Graph #4
plot5 = plt.subplot(313)
plot5.set_title('Project A')
plot5.set_xlabel('Grades')
plot5.set_ylabel('Number of Students')
plot5.set_xlim(0, 100)
plot5.set_ylim(0, 30)
plot5.hist(student_grades, bins=10, edgecolor='black', range=(0, 100))
plot5.set_xticks(np.arange(0, 110, step=10))
plot5.set_yticks(np.arange(0, 40, step=10))

plt.show()
