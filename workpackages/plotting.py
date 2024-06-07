import matplotlib.pyplot as plt

def scatter_plot(group1, group2, labelx, labely, title):

    plt.scatter(group1, group2)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.show()
