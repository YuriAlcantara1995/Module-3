import numpy as np


class KNN:
    """
    K-neariest-neighbor classifier using L1 ('manhattan') or L2 ('euclidean') loss
    """
    def __init__(self, k=1, metric=None):
        self.k = k
        self.metric = metric

    def fit(self, X, y):
        self.train_X = X
        self.train_y = y

    def predict(self, X, num_loops=0):
        '''
        Uses the KNN model to predict classes for the data samples provided
        
        Arguments:
        X, np array (num_samples, num_features) - samples to run
           through the model
        num_loops, int - which implementation to use

        Returns:
        predictions, np array of ints (num_samples) - predicted class
           for each sample
        '''
        if num_loops == 0:
            dists = self.compute_distances_no_loops(X)
        elif num_loops == 1:
            dists = self.compute_distances_one_loop(X)
        else:
            dists = self.compute_distances_two_loops(X)

        if self.train_y.dtype == np.bool:
            return self.predict_labels_binary(dists)
        else:
            return self.predict_labels_multiclass(dists)

    def compute_distances_two_loops(self, X):
        '''
        Computes distance from every sample of X to every training sample
        Uses simplest implementation with 2 Python loops

        Arguments:
        X, np array (num_test_samples, num_features) - samples to run
        
        Returns:
        dists, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample
        '''
        num_train = self.train_X.shape[0]
        num_test = X.shape[0]
        dists = np.zeros((num_test, num_train), np.float32)
        if self.metric == 'manhattan':
            for i_test in range(num_test):
                for i_train in range(num_train):
                    # TODO: Fill dists[i_test][i_train]
                    dists[i_test][i_train] = np.sum(abs(X[i_test] - self.train_X[i_train]))
                    pass
        elif self.metric == 'euclidean':
            for i_test in range(num_test):
                for i_train in range(num_train):
                    # TODO: Fill dists[i_test][i_train]
                    dists[i_test][i_train] = np.linalg.norm(X[i_test] - self.train_X[i_train])
                    pass

    def compute_distances_one_loop(self, X):
        '''
        Computes distance from every sample of X to every training sample
        Vectorizes some of the calculations, so only 1 loop is used

        Arguments:
        X, np array (num_test_samples, num_features) - samples to run
        
        Returns:
        dists, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample
        '''
        num_train = self.train_X.shape[0]
        num_test = X.shape[0]
        dists = np.zeros((num_test, num_train), np.float32)
        if self.metric == 'manhattan':
            for i_test in range(num_test):
                # TODO: Fill the whole row of dists[i_test]
                # without additional loops or list comprehensions
                dists[i_test] = np.sum(abs(self.train_X - X[i_test]), axis = 1)
        elif self.metric == 'euclidean':
            for i_test in range(num_test):
                # TODO: Fill the whole row of dists[i_test]
                # without additional loops or list comprehensions
                dists[i_test] = np.linalg.norm(self.train_X - X[i_test], axis = 1)

    def compute_distances_no_loops(self, X):
        '''
        Computes L1 distance from every sample of X to every training sample
        Fully vectorizes the calculations using numpy

        Arguments:
        X, np array (num_test_samples, num_features) - samples to run
        
        Returns:
        dists, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample
        '''
        num_train = self.train_X.shape[0]
        num_test = X.shape[0]
        # Using float32 to to save memory - the default is float64
        dists = np.zeros((num_test, num_train), np.float32)
        if self.metric == 'manhattan':
            # TODO: Implement computing all distances with no loops!
            dists = np.abs(X[:,None] - self.train_X).sum(-1)
            pass
        if self.metric == 'euclidean':
            # TODO: Implement computing all distances with no loops!
            dists = np.sqrt((X**2).sum(axis=1)[:, np.newaxis] + (self.train_X**2).sum(axis=1) - 2 * X.dot(self.train_X.T))
            pass

    def predict_labels_binary(self, dists):
        '''
        Returns model predictions for binary classification case
        
        Arguments:
        dists, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample

        Returns:
        pred, np array of bool (num_test_samples) - binary predictions 
           for every test sample
        '''
        num_test = dists.shape[0]
        pred = np.zeros(num_test, np.bool)
        for i in range(num_test):
            # TODO: Implement choosing best class based on k
            # nearest training samples
            pass
        return pred

    def predict_labels_multiclass(self, dists):
        '''
        Returns model predictions for multi-class classification case
        
        Arguments:
        dists, np array (num_test_samples, num_train_samples) - array
           with distances between each test and each train sample

        Returns:
        pred, np array of int (num_test_samples) - predicted class index 
           for every test sample
        '''
        num_test = dists.shape[0]
        num_test = dists.shape[0]
        pred = np.zeros(num_test, np.int)
        for i in range(num_test):
            # TODO: Implement choosing best class based on k
            # nearest training samples
            pass
        return pred
