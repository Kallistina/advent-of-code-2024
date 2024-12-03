# Function to read a 2D array from a file
def read_array_from_file(filename):
    """
    Reads a 2D array with exactly 2 columns and many rows from a file.
    
    :param filename: Name of the file containing the array
    :return: 2D array as a list of lists
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # Parse lines into a 2D array
    array_2d = [list(map(int, line.split())) for line in lines]

    # Ensure each row has exactly 2 columns
    for row in array_2d:
        if len(row) != 2:
            raise ValueError("Each row must contain exactly 2 columns.")
    
    return array_2d

#PART ONE
# Function to process the 2D array
def calculate_distance(array_2d):
    """
    Function to process a 2D array with multiple rows and 2 columns.
    It sorts the elements of each column, calculates the absolute difference
    between the corresponding values in the left and right columns,
    and returns the total sum of these differences.

    :param array_2d: List of lists (2D array) with multiple rows and 2 columns
    :return: Integer sum of the absolute differences between the left and right columns
    """
    distance = 0

    # Step 1: Transpose the array (swap rows with columns)
    transposed = list(zip(*array_2d))
    
    # Step 2: Sort each column (now a row after transposing)
    sorted_transposed = [sorted(col) for col in transposed]
    
    # Step 3: Transpose back to get the sorted array
    sorted_array_2d = list(zip(*sorted_transposed))

    # Step 4: Calculate the distance between the two points
    for row in sorted_array_2d:
        left_col, right_col = row
        distance += abs(left_col - right_col)  # Add the absolute difference to the total
       
    return distance

def calculate_similarity_score(array_2d):
    """
    Function to process a 2D array with multiple rows and 2 columns.
    It calculates the similarity score between the corresponding values
    in the left and right columns, and returns the total sum of these scores.
    The similarity score is based on how many times the left column value
    appears in the entire right column.
    
    :param array_2d: List of lists (2D array) with multiple rows and 2 columns
    :return: Integer sum of the similarity scores between the left and right columns
    """
    score = 0

    # Step 1: Extract all values in the right column
    right_column = [row[1] for row in array_2d]

    # Step 2: Iterate through each row in the 2D array
    for row in array_2d:
        left_col = row[0]

        # Step 3: Count how many times the left column value appears in the right column
        count = right_column.count(left_col)

        # Step 4: Add the score for this row
        score += count * left_col  # Multiply the count by the left column value

    return score

# Main function
def main():
    """
    Main function 
    """
    # File containing the 2D array
    input_file = "puzzle_input.txt"

    try:
        # Read the array from the file
        array_2d = read_array_from_file(input_file)

        # Process the array
        result = calculate_distance(array_2d)
        
        # print("Input 2D array from file:")
        # for row in array_2d:
        #     print(row)

        print("\n** The puzzle answer is: %d. **" % result)

        score = calculate_similarity_score(array_2d)

        print("\n** The similarity score is: %d. **\n" %score)
    
    except Exception as e:
        print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    main()