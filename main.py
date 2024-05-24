# main.py
from sklearn.linear_model import Perceptron
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Załadowanie danych
iris = load_iris()
X, y = iris.data, iris.target

# Podział na zestaw treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Utworzenie i trenowanie modelu perceptron
model = Perceptron()
model.fit(X_train, y_train)

# Predykcja na zestawie testowym
y_pred = model.predict(X_test)

# Wyświetlenie dokładności
accuracy = accuracy_score(y_test, y_pred)
print(f'Dokładność modelu: {accuracy:.2f}')