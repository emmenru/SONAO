import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd

def readCSV(fileName):
    print("Reading the following file: ", fileName)
    df = pd.read_csv(fileName, sep=",")
    print(df.columns)
    return df


# array of x,y,z values
a = np.random.rand(2000, 3)*10
# array of time values?
t = np.array([np.ones(100)*i for i in range(20)]).flatten()
df = pd.DataFrame({"time": t ,"x" : a[:,0], "y" : a[:,1], "z" : a[:,2]})
# data frame with columns time, x, y, z

# try using your own df
emserdata=readCSV("/Users/emmafrid/Desktop/SONAO/Code/FormatMocapData_Python/data_formatted/sadness_clip-0048.csv")
df1 = emserdata[["Time", "AlejandroMask:HeadTopX7", "AlejandroMask:HeadTopY7", "AlejandroMask:HeadTopZ7"]]


def update_graph(num):
    data=df[df['time']==num]
    graph.set_data (data.x, data.y)
    graph.set_3d_properties(data.z)
    title.set_text('3D Test, time={}'.format(num))
    return title, graph,


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
title = ax.set_title('3D Test')

data=df[df['time']==0]
graph, = ax.plot(data.x, data.y, data.z, linestyle="", marker="o")

ani = matplotlib.animation.FuncAnimation(fig, update_graph,19,interval=120, blit=True)

plt.show()