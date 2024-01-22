import math

def idkneco(x1, y1, z1, x2, y2, z2):
    trubkys_length = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
    hadic_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    return trubkys_length, hadic_length

def main():
    
        room_size = 300  

        x1, y1, z1 = 130, 100, 0  #nefunguje 3. jsou naproti sobe
        x2, y2, z2 = 200, 280, 300

        trubkys_length, hadic_length = idkneco(x1, y1, z1, x2, y2, z2)

        print(f"Delka potrubi: {hadic_length}")
        print(f"Delka hadce: {trubkys_length:.6f}")

    

main()
