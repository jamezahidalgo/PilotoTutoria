from sklearn.cluster import KMeans

class ModelKMeans:
    def __init__(self, name_model, n_clusters=5):
        self.name = name_model
        self.clusters = n_clusters
        self.kmeans = KMeans(n_clusters, random_state=29) 
        
    def get_name(self):
        return "<<" + self.name + ">>"

    def fit(self, X):
        self.kmeans.fit(X)
        self.centroids = self.kmeans.cluster_centers_ 

    def get_centroides(self):
        return self.centroids

    def predict(self, X):
        # Predicting the clusters
        return self.kmeans.predict(X)



    
