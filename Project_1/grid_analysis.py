import json
import numpy as np

# Inladen van JSON-bestand
def load_floorplan(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Grid aanmaken en vullen met kolommen/muren
def create_grid(floorplan, grid_size=10):
    grid = np.full((grid_size, grid_size), "◯")  # Begin met lege cellen

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

        grid[y1, x1] = "▬"
        grid[y2, x2] = "▬"

    # Kolommen toevoegen aan het grid
    for column in floorplan["columns"]:
        x = min(int(column["position"][0] * scale_x), grid_size - 1)
        y = min(int(column["position"][1] * scale_y), grid_size - 1)
        grid[y, x] = "🔵"

    return grid

# Grid visualiseren
def print_grid(grid):
    print("\nGrid Weergave:")
    for row in grid:
        print(" ".join(row))
    print("\nLegenda: 🔵 = Kolom, ▬ = Muur, ◯ = Open Ruimte")

# Functie om grote open ruimtes te detecteren (incl. diagonale checks)
def detect_large_spans(grid, max_span=3):
    warnings = []
    size = grid.shape[0]

    # Horizontale check
    for y in range(size):
        open_count = 0
        for x in range(size):
            if grid[y, x] == "◯":
                open_count += 1
            else:
                if open_count > max_span:
                    warnings.append(f"⚠️ Grote overspanning (horizontaal) van {open_count} cellen op rij {y}")
                open_count = 0

    # Verticale check
    for x in range(size):
        open_count = 0
        for y in range(size):
            if grid[y, x] == "◯":
                open_count += 1
            else:
                if open_count > max_span:
                    warnings.append(f"⚠️ Grote overspanning (verticaal) van {open_count} cellen op kolom {x}")
                open_count = 0

    # Diagonale check (\ richting)
    for d in range(-size + 1, size):
        open_count = 0
        for i in range(size):
            x, y = i, i + d
            if 0 <= x < size and 0 <= y < size:
                if grid[y, x] == "◯":
                    open_count += 1
                else:
                    if open_count > max_span:
                        warnings.append(f"⚠️ Grote overspanning (diagonaal \\) van {open_count} cellen op diagonaal {d}")
                    open_count = 0

    # Diagonale check (/ richting)
    for d in range(-size + 1, size):
        open_count = 0
        for i in range(size):
            x, y = i, size - 1 - (i + d)
            if 0 <= x < size and 0 <= y < size:
                if grid[y, x] == "◯":
                    open_count += 1
                else:
                    if open_count > max_span:
                        warnings.append(f"⚠️ Grote overspanning (diagonaal /) van {open_count} cellen op diagonaal {d}")
                    open_count = 0

    return warnings

# Uitvoeren
if __name__ == "__main__":
    floorplan = load_floorplan("floorplan 2.json")  # JSON-bestand met plattegrond
    grid = create_grid(floorplan, grid_size=10)  # Gridgrootte instellen
    print_grid(grid)

    # Overspanningsdetectie uitvoeren
    warnings = detect_large_spans(grid, max_span=3)
    if warnings:
        print("\n⚠️ STRUCTURELE WAARSCHUWINGEN:")
        for warning in warnings:
            print(warning)
    else:
        print("\n✅ Geen grote overspanningen gedetecteerd.")
