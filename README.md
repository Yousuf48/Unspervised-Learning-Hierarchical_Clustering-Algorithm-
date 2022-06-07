# Unspervised-Learning-Hierarchical_Clustering-Algorithm-

**Hierarchical Clustering** is an algorithm that groups similar points together in the same cluster. It has two ways to create a cluster hierarchy:
 - Agglomerative
 - Divisive

main.py shows you two different graphs of clustering. i.e. Dendrogram and Agglomerative Clustering.

## Equations and explanation:
NOTE: The only used distance in the above code is euclidean: i.e 
$$d(p,q)=\sqrt (\sum_{i=1}^n (q_i-p_i)^2)$$

* Direction of clustering for the dendrogram:
* 
** **Top**: the root at the top and leaves at the bottom.

** **Bottom**: the root at the bottom and leaves at the top.

** **Right**: the root at the right and leaves at the leaft.

** **Left**: the root at the left and the leaves at the right.


* Link between the data type:

P.S "dist" is euclidean distance.

** **Single**: 
$$d(u,v) = min(dist(u[i],v[i]))$$

** **Complete**:
$$d(u,v) = max(dist(u[i],v[i]))$$


** **Average**:
$$d(u,v) = \sum_{i,j} (dist(u[i],v[i]) / (|u| * |v|))$$

	Note: |u| and |v| is the cardinality(size) of set u and v.
** **Centroid**
$$d(s,t) = ||C_s - C_t ||$$

	Note: C is the centroid of a cluster
  
  
## Number options (0-3):
**0**: Exits

**1**: Shows a  scatter plot graph.

**2**: Shows dendrogram graph.

**3**: shows Agglomerative graph with each piont assign to a cluster and a colour in the grapth.

**4**: Shows your dataset.


## Resources:

https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/

https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

