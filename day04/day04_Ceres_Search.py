# PART ONE

def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Directions: (row_delta, col_delta)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]

    def is_valid(r, c):
        """Check if a position is within the grid."""
        return 0 <= r < rows and 0 <= c < cols

    def check_direction(r, c, dr, dc):
        """Check if the word exists starting at (r, c) in the given direction."""
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check all directions from this cell
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count


# Main function to read input and process
def main():
    input_file = "puzzle_input.txt"
    
    with open(input_file, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    
    word = "XMAS"
    occurrences = find_word(grid, word)
    print(f"Occurrences of '{word}': {occurrences}")


if __name__ == "__main__":
    main()
