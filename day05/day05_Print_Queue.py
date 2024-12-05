from collections import defaultdict, deque

def parse_input(input_data):
    with open(file_path, "r") as file:
        input_data = file.read()

    rules_section, updates_section = input_data.strip().split("\n\n")
    
    # Parse ordering rules
    rules = []
    for line in rules_section.splitlines():
        x, y = map(int, line.split("|"))
        rules.append((x, y))
    
    # Parse updates
    updates = []
    for line in updates_section.splitlines():
        updates.append(list(map(int, line.split(","))))
    
    return rules, updates

def is_update_correct(rules, update):
    # Build a directed graph of the rules that apply to the update
    graph = defaultdict(list)
    in_update = set(update)
    for x, y in rules:
        if x in in_update and y in in_update:
            graph[x].append(y)
    
    # Perform a topological sort on the update
    # Map pages to their positions in the update
    pos = {page: i for i, page in enumerate(update)}
    for x, neighbors in graph.items():
        for y in neighbors:
            if pos[x] > pos[y]:
                return False
    return True

def get_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

#PART ONE

# def main(input_data):
#     rules, updates = parse_input(input_data)
    
#     middle_sum = 0
#     for update in updates:
#         if is_update_correct(rules, update):
#             middle_sum += get_middle_page(update)
    
#     print("Sum of middle page numbers:", middle_sum)


# PART TWO

def sort_update(rules, update):
    # Build a graph for the update
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    in_update = set(update)
    for x, y in rules:
        if x in in_update and y in in_update:
            graph[x].append(y)
            in_degree[y] += 1
    
    # Topological sort using Kahn's algorithm
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def main(file_path):
    rules, updates = parse_input(file_path)
    
    middle_sum = 0
    for update in updates:
        if not is_update_correct(rules, update):
            corrected_update = sort_update(rules, update)
            middle_sum += get_middle_page(corrected_update)
    
    print("Sum of middle page numbers (incorrect updates):", middle_sum)

file_path = "puzzle_input.txt" 
main(file_path)