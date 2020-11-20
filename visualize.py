"""
Visualization
"""
import matplotlib.pyplot as plt
import transform

# Plot 1


def plot_3d_scatter(filename: str):
    """
    dd
    """

    data = transform.final_data(filename)

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    y = [x for x in range(1990, 2017)]

    ax1.scatter(data[0][1], 1990, [1], c='g', marker='o', label=data[0][0])
    ax1.scatter(data[1][1], 1990, [2], c='r', marker='o', label=data[1][0])
    ax1.scatter(data[2][1], 1990, [3], c='b', marker='o', label=data[2][0])
    ax1.scatter(data[3][1], 1990, [4], c='g', marker='o', label=data[3][0])
    ax1.scatter(data[4][1], 1990, [5], c='g', marker='o', label=data[4][0])
    ax1.scatter(data[5][1], 1990, [6], c='g', marker='o', label=data[5][0])

    ax1.set_xlabel('x axis')
    ax1.set_ylabel('y axis')
    ax1.set_zlabel('z axis')
    plt.legend()

    plt.show()
