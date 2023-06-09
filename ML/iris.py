from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
test_idx=[0,55,100]
iris=load_iris()

train_target=np.delete(iris.target,test_idx)
train_data=np.delete(iris.data,test_idx,axis=0)

test_target=iris.target[test_idx]
test_data=iris.data[test_idx]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(train_data,train_target)
print (clf.predict(test_data))
print (test_target)