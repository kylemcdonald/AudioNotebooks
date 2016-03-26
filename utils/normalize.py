def normalize(X):
    X -= X.min(axis=0)
    X /= X.max(axis=0)
    return X