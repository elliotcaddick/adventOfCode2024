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
            
# print(f"Part 1: {part_one("input/puzzle.txt")}")

def part_two(filename):
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
            
    to_correct = []
    for update in updates:
        history = []
        correct_order = True
        for page in update:
            if history == []:
                history.append(page)
                continue
            correct_order = is_correctly_ordered(page, history)
            if not correct_order:
                to_correct.append(update)
                break
            history.append(page)
    
    middle_pages = []
    for update in to_correct:
        i = 0
        history = []
        while i < len(update):
            correct_order = True
            if history == []:
                history.append(update[i])
                i += 1
            else:
                if update[i] in page_ordering_rules:
                    has_swaped = False
                    for p in page_ordering_rules[update[i]]:
                        if p in history:
                            correct_order = False
                            swap = update[i]
                            update[i] = p
                            update[update.index(p)] = swap
                            has_swaped = True
                            break
                    if has_swaped:
                        correct_order = True
                        history = []
                        i = 0
                    else:
                        history.append(update[i])
                        i += 1
                else:
                    history.append(update[i])
                    i += 1
    
    for update in to_correct:
        middle_pages.append(update[len(update)//2])        
    
    return sum(middle_pages)

# print(f"Part 2: {part_two("input/puzzle.txt")}")