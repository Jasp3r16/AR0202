import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# **1. Laad de dataset**
# Vervang dit met je eigen dataset vanuit Grasshopper / Karamba 3D
# Voorbeeld dataset met fictieve features
data = {
    "room_count": [3, 4, 5, 6, 3, 5, 4, 6, 7, 3],
    "total_area": [80, 120, 150, 200, 90, 140, 130, 210, 250, 85],
    "span_width": [5, 6, 7, 8, 5, 6, 7, 9, 10, 5],
    "load_factor": [1.2, 1.5, 1.8, 2.0, 1.3, 1.6, 1.7, 2.2, 2.5, 1.2],
    "optimal_pile_count": [6, 8, 10, 12, 7, 9, 8, 13, 15, 6]  # Dit is de output
}

df = pd.DataFrame(data)

# **2. Splits de dataset in trainings- en testsets**
X = df.drop(columns=["optimal_pile_count"])  # Input features
y = df["optimal_pile_count"]  # Output: voorspelde paalposities

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# **3. Train het Random Forest model**
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# **4. Voorspellingen maken**
y_pred = model.predict(X_test)

# **5. Model evalueren**
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# **6. Visualiseer de werkelijke vs. voorspelde waarden**
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Werkelijke Paalstructuur")
plt.ylabel("Voorspelde Paalstructuur")
plt.title("Werkelijke vs. Voorspelde Aantallen Palen")
plt.show()
