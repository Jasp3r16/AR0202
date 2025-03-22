import json
import numpy as np

# JSON-bestand inlezen
def load_floorplan(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

# Functie om de overspanningen te berekenen
def calculate_spans(floorplan):
    columns = [np.array(col["position"]) for col in floorplan["columns"]]
    walls = [(np.array(wall["start"]), np.array(wall["end"])) for wall in floorplan["walls"]]

    spans = []

    # Sorteer kolommen op hun X-coördinaat (vereenvoudiging)
    columns.sort(key=lambda x: x[0])

    for i in range(len(columns) - 1):
        span = np.linalg.norm(columns[i + 1] - columns[i])
        spans.append(span)

    return spans

# Uitvoeren
if __name__ == "__main__":
    floorplan = load_floorplan("floorplan 2.json")
    spans = calculate_spans(floorplan)

    print("\nGevonden overspanningen tussen kolommen:")
    for i, span in enumerate(spans):
        print(f"  Overspanning {i+1}: {span:.2f} meter")

    # Controleer of overspanningen groter zijn dan 5 meter (voorbeeldregel)
    for span in spans:
        if span > 5:
            print(f"⚠️ Waarschuwing: Overspanning van {span:.2f} meter is te groot!")
