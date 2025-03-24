import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.cluster import KMeans
from random_forest import model

# **1. Definieer een nieuwe plattegrond (voorbeeldinput)**
new_design = pd.DataFrame({
    "room_count": [5],        # Aantal kamers
    "total_area": [160],      # Totale oppervlakte (m²)
    "span_width": [7],        # Gemiddelde overspanning (m)
    "load_factor": [1.8]      # Gemiddelde belastingfactor
})

# **2. Voorspel het aantal benodigde palen**
predicted_piles = model.predict(new_design)[0]
print(f"&#x1f539; AI Advies: Gebruik ongeveer {round(predicted_piles)} palen voor dit ontwerp.")


# **1. Genereer een grid van mogelijke paalposities**
x_coords = np.random.uniform(0, 20, 100)  # X-coördinaten (voorbeeld)
y_coords = np.random.uniform(0, 20, 100)  # Y-coördinaten (voorbeeld)
possible_positions = np.column_stack((x_coords, y_coords))

# **2. Clustering uitvoeren om paallocaties te bepalen**
num_piles = round(predicted_piles)  # Gebruik voorspeld aantal palen
kmeans = KMeans(n_clusters=num_piles, random_state=42)
kmeans.fit(possible_positions)

# **3. Resultaten visualiseren**
plt.scatter(x_coords, y_coords, c='lightgrey', label="Mogelijke posities")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', label="AI-geplaatste palen")
plt.xlabel("X-coördinaat")
plt.ylabel("Y-coördinaat")
plt.title("AI-geoptimaliseerde paalstructuur")
plt.legend()
plt.show()