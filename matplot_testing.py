# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [5, 2, 4, 2, 1, 4, 5, 2]
#
# plt.scatter(x, y, label='skitscat', color='g', s=25, marker="o")
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()




# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# X, Y, Z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 6, 2, 3, 13, 4, 1, 2, 4, 8], [2, 3, 3, 3, 5, 7, 9, 11, 9, 10]
# ax.plot_wireframe(X, Y, Z)
# plt.legend(['hello'])
#
# plt.show()






# 3D scatter plot code.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4]
y = [2019, 2020, 2021, 2022]
z = [4, 5, 6, 7]

x2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
y2 = [-5, -6, -7, -8, -2, -5, -6, -3, -7, -2]
z2 = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]

ax1.scatter(x, y, z, c='g', marker='o', label='hello')
ax1.scatter(x2, y2, z2, c='r', marker='o')

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.legend()

plt.show()







# Pie Chart code......very good.

import plotly.graph_objects as go

labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial'
                             )])
fig.show()
