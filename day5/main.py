"""
--- Day 5: Print Queue ---
"""

def part_one(filename):
    page_ordering_rules = {}
    updates = []
    
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                x, y = line.split('|')
                x = int(x)
                y = int(y)
                if x in page_ordering_rules:
                    page_ordering_rules[x].append(y)
                else:
                    page_ordering_rules[x] = [y]
            elif "," in line:
                updates.append([int(e) for e in line.split(',')])
                
    def is_correctly_ordered(page, history):
        if page in page_ordering_rules:
            for p in page_ordering_rules[page]:
                if p in history:
                    return False
        return True
            
    middle_pages = []
    for update in updates:
        history = []
        correct_order = True
        for page in update:
            if history == []:
                history.append(page)
                continue
            correct_order = is_correctly_ordered(page, history)
            if not correct_order:
                break
            history.append(page)
        if correct_order:
            middle_pages.append(update[len(update)//2])
    
    return sum(middle_pages)
            
print(f"Part 1: {part_one("input/puzzle.txt")}")