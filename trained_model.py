import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# print(clf.predict([[8.1, 8.5, 8.4, 8.2]]))


# Save the trained model as an artifact
joblib.dump(clf, 'trained_model.pkl')
