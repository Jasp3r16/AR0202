from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Simulatie van 1000 mogelijke kolomlocaties met 5 kenmerken
np.random.seed(42)
X = np.random.rand(1000, 5)  # 1000 mogelijke plekken, met 5 kenmerken
y = np.random.rand(1000)  # Score tussen 0 en 1 (geschiktheid)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train een Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Voorspellingen maken
y_pred = model.predict(X_test)

# Model evalueren
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")



#toepassen op nieuwe plattegrond

new_building = np.random.rand(50, 5)  # 50 plekken met kenmerken
predictions = model.predict(new_building)  # Geschiktheidsscore voor elke plek

# Sorteer de plekken van meest naar minst geschikt
best_locations = np.argsort(-predictions)[:5]  # Top 5 locaties voor kolommen

print(f"Beste locaties voor kolommen: {best_locations}")
