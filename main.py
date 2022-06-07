import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import time


matrix = []
def main():
    user_input = -1

    while(user_input != 0):
        try:
            user_input = int(input("1: Scatter plot\n2: Hierarchical Clustering dendrogram\n3: Agglomerative Clustering"
                                "\n4: Show your data\n0: To exit\n"))
            if(user_input == 1): scatter_plotter(data())

            elif(user_input == 2):

                matrix = data()
                orientation = str(input("Direction of clustering: (top,bottom,left,right): "))
                link = str(input("Linkage type: (single, complete, average, centroid): "))

                while (orientation != 'top' and orientation != 'bottom' and orientation != 'left'
                    and orientation != 'right') or (link != 'single' and link != 'complete' and link != 'average'
                     and link !='centroid'):

                        print("Enter only one of the given options")
                        orientation = str(input("Direction of clustering: (top,bottom,left,right): "))
                        link = str(input("Linkage type: (single, complete, average, centroid): "))

                Hierarchical_Clustering(matrix,orientation,link)
            elif(user_input == 3):
                matrix = data()
                cluster_num = int(input("The number of clusters k: "))
                link = str(input("Linkage type: (single, complete, average, centroid): "))

                while (link != 'single' and link != 'complete' and link != 'average'
                    and link !='centroid'):
                        print("Enter only one of the given options")
                        link = str(input("Linkage type: (single, complete, average, centroid): "))

                Agglomerative_Clustering(matrix,cluster_num,link)

            elif user_input == 4:
                show_data()
            else:
                if(user_input != 0):raise ValueError()
        except ValueError or TypeError:
            print("Choose a number between 0-3")


def scatter_plotter(matrix):
    X = matrix

    label = range(1,len(X)+1)

    plt.figure(figsize=(8,8))
    plt.xlabel("x-axis")
    plt.ylabel('y-axis')
    plt.title('Scatter')
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(X[:,0], X[:,1])

    for label,X,y in zip(label,X[:,0],X[:,1]):
        plt.annotate(label,xy=(X,y),xytext = (-3,3),
                    textcoords="offset points", ha="right", va="bottom")

    plt.show()

def Hierarchical_Clustering(matrix,direction,link):

    linked = linkage(matrix, link)
    label = np.array(range(1,len(matrix)+1))
    plt.figure(figsize = (8,8))
    plt.xlabel("x-axis")
    plt.ylabel('y-axis')
    plt.title('Hierarchical Clustering')
    
    dendrogram(linked, labels=label, orientation=direction, show_leaf_counts=True)
    plt.show()

def Agglomerative_Clustering(matrix, n,link):
    X = matrix
    cluster = AgglomerativeClustering(n_clusters=n, affinity='euclidean', linkage=link)
    cluster.fit_predict(X)

    plt.xlabel("x-axis")
    plt.ylabel('y-axis')
    plt.title('Agglomerative Clustering. The cluster is '+ str(cluster.labels_))
    labels = np.array(range(1, len(matrix) + 1))
    
    plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow', label=labels)

    plt.show()


def data():
    data.matrix = []
    if len(matrix) == 0:
        try:
            while(True):
                row_col = int(input("Enter the number of points: "))
                for i in range(row_col):
                    x_axis = float(input("Enter x value: "))
                    y_axis = float(input("Enter y value: "))
                    matrix.append([x_axis, y_axis])
                if row_col <= 0:
                    print("Enter positive numbers of points.")
                else:
                    return np.array(matrix)

        except TypeError and ValueError:
            print("Enter positive numbers (integer for number of points, float otherwise.")
    else:
        empty = input("To set a new data and points type only 'yes': ")
        if empty == 'yes':
            matrix.clear()
            data()
        else:
            return np.array(matrix)

def show_data():
    if(len(matrix) != 0):
        for i in matrix: print(i)
    else:
        print("No data provided")
    time.sleep(2)

if __name__ == '__main__':
    main()


