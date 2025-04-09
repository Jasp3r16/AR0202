import json

# JSON-bestand inlezen
def load_floorplan(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

# Test de functie
if __name__ == "__main__":
    floorplan = load_floorplan("floorplan.json")
    
    print("Muren:")
    for wall in floorplan["walls"]:
        print(f"  Start: {wall['start']}, End: {wall['end']}, Dikte: {wall['thickness']}")

    print("\nKolommen:")
    for column in floorplan["columns"]:
        print(f"  Positie: {column['position']}, Grootte: {column['size']}")

    print("\nOpeningen:")
    for opening in floorplan["openings"]:
        print(f"  Positie: {opening['position']}, Breedte: {opening['width']}")
