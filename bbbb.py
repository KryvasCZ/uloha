import math
def get_coordinates(label):
    try:
        x, y = input(f"{label}: ").split()
        return float(x), float(y)
    except ValueError:
        print("Chyba: Zadávejte pouze čísla oddělená mezerou.")
        exit()

def main():
    print("Zadejte souřadnice bodů A, B, C:")
    ax, ay = get_coordinates("Bod A")
    bx, by = get_coordinates("Bod B")
    cx, cy = get_coordinates("Bod C")
    AB = math.sqrt((bx-ax)**2 + (by-ay)**2)
    BC = math.sqrt((cx-bx)**2 + (cy-by)**2)
    AC = math.sqrt((cx-ax)**2 + (cy-ay)**2)
    print(AB)
    print(BC)
    print(AC)
    if AB==0 or AC == 0 or BC == 0:
        print("Dva nebo všechny tři zadané body splývají.")
    else:
        if AB+BC==AC:
            print("Body leží na jedné přímce.")
            print("B je uprostřed")
        else:
            if BC+AC==AB:
                print("Body leží na jedné přímce.")
                print("C je uprostřed")
            else:

                if AC+AB==BC:
                    print("A je uprostřed")
                    print("Body leží na jedné přímce.")
                else:
                    print("body nelezi na prmice xd")
        

if __name__ == "__main__":
    main()
