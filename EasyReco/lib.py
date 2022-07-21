from keras.datasets import mnist
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn import svm
import numpy as np
import joblib

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X = np.concatenate([X_train, X_test])
y = np.concatenate([y_train, y_test])

X_flat = X.reshape(X.shape[0], -1)
X_scaled = scale(X_flat)

non_linear_model_rbf = svm.SVC(kernel='rbf')
non_linear_model_rbf.fit(X_scaled, y)

joblib.dump(non_linear_model_rbf,'svc.gz',compress=('gzip',3))