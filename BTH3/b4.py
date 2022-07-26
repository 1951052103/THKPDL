from scipy.io import arff
from pandas import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


data = arff.loadarff(r'Clustering1-NoClass-Train.arff')
df = pd.DataFrame(data[0])

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)

clusters = df[['wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-size']]

kmeans.fit(clusters)
predicted_values = kmeans.predict(clusters)
print(kmeans.cluster_centers_)

plt.scatter(df['width'], df['height'], c=predicted_values, s=50, cmap='viridis')
plt.show()