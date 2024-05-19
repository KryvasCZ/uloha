import sys
import math
from itertools import combinations

def parse_input():
    airplanes = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            coords, name = line.split(':')
            x_str, y_str = coords.split(',')
            x, y = float(x_str), float(y_str)
            if not name:
                raise ValueError
            airplanes.append((x, y, name))
        except ValueError:
            print("Nespravny vstup.")
            sys.exit(1)
    return airplanes

def calculate_distance(plane1, plane2):
    x1, y1 = plane1[:2]
    x2, y2 = plane2[:2]
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def main():
    airplanes = parse_input()
    
    if len(airplanes) < 2:
        print("Nespravny vstup.")
        sys.exit(1)
    
    min_distance = float('inf')
    closest_pairs = []

    for plane1, plane2 in combinations(airplanes, 2):
        distance = calculate_distance(plane1, plane2)
        if distance < min_distance:
            min_distance = distance
            closest_pairs = [(plane1, plane2)]
        elif distance == min_distance:
            closest_pairs.append((plane1, plane2))
    
    print(f"Vzdalenost nejblizsich letadel: {min_distance:.6f}")
    print(f"Nalezenych dvojic: {len(closest_pairs)}")
    for plane1, plane2 in closest_pairs:
        print(f"{plane1[2]} - {plane2[2]}")

if __name__ == "__main__":
    main()
