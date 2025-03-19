import json
import numpy as np

# Inladen van JSON-bestand
def load_floorplan(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Grid aanmaken en vullen met kolommen/muren
def create_grid(floorplan, grid_size=10):
    grid = np.full((grid_size, grid_size), "O")  # Begin met lege cellen

    # Maximale afmetingen van de plattegrond berekenen
    max_x = max(max(wall["start"][0], wall["end"][0]) for wall in floorplan["walls"])
    max_y = max(max(wall["start"][1], wall["end"][1]) for wall in floorplan["walls"])

    # Schaalfactor berekenen om plattegrond naar het grid te mappen
    scale_x = (grid_size - 1) / max_x
    scale_y = (grid_size - 1) / max_y

    # Muren toevoegen aan het grid
    for wall in floorplan["walls"]:
        x1 = min(int(wall["start"][0] * scale_x), grid_size - 1)
        y1 = min(int(wall["start"][1] * scale_y), grid_size - 1)
        x2 = min(int(wall["end"][0] * scale_x), grid_size - 1)
        y2 = min(int(wall["end"][1] * scale_y), grid_size - 1)

        grid[y1, x1] = "="
        grid[y2, x2] = "="

    # Kolommen toevoegen aan het grid
    for column in floorplan["columns"]:
        x = min(int(column["position"][0] * scale_x), grid_size - 1)
        y = min(int(column["position"][1] * scale_y), grid_size - 1)
        grid[y, x] = "+"

    return grid

# Grid visualiseren
def print_grid(grid):
    print("\nGrid Weergave:")
    for row in grid:
        print(" ".join(row))
    print("\nLegenda: + = Kolom, = = Muur, O = Open Ruimte")

# Uitvoeren
if __name__ == "__main__":
    floorplan = load_floorplan("floorplan.json")  # JSON-bestand met plattegrond
    grid = create_grid(floorplan, grid_size=10)  # Gridgrootte instellen
    print_grid(grid)
