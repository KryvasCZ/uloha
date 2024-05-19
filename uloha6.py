import sys
import re

class Shelf:
    def __init__(self):
        self.items = []

class ShoppingItem:
    def __init__(self, name, shelf, actual_name):
        self.name = name
        self.shelf = shelf
        self.actual_name = actual_name

def read_input():
    lines = sys.stdin.read().splitlines()
    return lines

def parse_input(lines):
    shelves = []
    i = 0
    current_shelf = None
    
    while i < len(lines):
        line = lines[i].strip()
        if line == '':
            if current_shelf is None:
                break
            current_shelf = None
        else:
            if current_shelf is None:
                try:
                    shelf_number = int(line)
                    if shelf_number != len(shelves):
                        raise ValueError("Invalid shelf sequence.")
                    current_shelf = Shelf()
                    shelves.append(current_shelf)
                except ValueError:
                    print("Invalid shelf number.")
                    sys.exit(1)
            else:
                current_shelf.items.append(line)
        i += 1
    
    if i == len(lines) or len(shelves) == 0:
        print("Invalid input: missing shelves or empty shelves.")
        sys.exit(1)
    
    if lines[i].strip() != '':
        print("Invalid input: missing blank line after shelves.")
        sys.exit(1)
    
    i += 1
    shopping_lists = []
    current_list = []

    while i < len(lines):
        line = lines[i].strip()
        if line == '':
            if current_list:
                shopping_lists.append(current_list)
                current_list = []
        else:
            current_list.append(line)
        i += 1
    
    if current_list:
        shopping_lists.append(current_list)
    
    return shelves, shopping_lists

def find_item(shelves, item):
    item_lower = item.lower()
    for shelf_num, shelf in enumerate(shelves):
        for shelf_item in shelf.items:
            if shelf_item.lower() == item_lower:
                return ShoppingItem(item, shelf_num, shelf_item)
            if item_lower in shelf_item.lower():
                return ShoppingItem(item, shelf_num, shelf_item)
    return ShoppingItem(item, -1, item)

def optimize_shopping_list(shelves, shopping_list):
    optimized_list = []
    remaining_items = []
    
    for item in shopping_list:
        shopping_item = find_item(shelves, item)
        if shopping_item.shelf == -1:
            remaining_items.append(shopping_item)
        else:
            optimized_list.append(shopping_item)
    
    optimized_list.sort(key=lambda x: x.shelf)
    
    return optimized_list + remaining_items

def main():
    lines = read_input()
    shelves, shopping_lists = parse_input(lines)
    
    for shopping_list in shopping_lists:
        optimized_list = optimize_shopping_list(shelves, shopping_list)
        for item in optimized_list:
            if item.shelf == -1:
                print(f"{item.name} not found")
            else:
                print(f"{item.shelf} {item.actual_name}")
        print()

if __name__ == "__main__":
    main()
