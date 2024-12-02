# Function to read a 2D array from a file
def read_array_from_file(filename):
    """
    Reads a 2D array with any number of rows and columns from a file.
    
    :param filename: Name of the file containing the array
    :return: 2D array as a list of lists
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # Parse lines into a 2D array
    array = [list(map(int, line.split())) for line in lines if line.strip()]  # Ignore empty lines
    
    # Ensure the array is not empty
    if not array:
        raise ValueError("The file does not contain any valid data.")
    
    return array

# #PART ONE
# # Function to process the array
# def calculate_reports(array):
#     """
#     Calculates the number of rows in which the numbers are in strictly increasing
#     or decreasing order, with consecutive differences between 1 and 3.
    
#     :param array: 2D array (list of lists)
#     :return: Count of valid rows
#     """
#     reports = 0

#     # Iterate over each row
#     for row in array:
#         is_increasing = all(1 <= row[i + 1] - row[i] <= 3 for i in range(len(row) - 1))
#         is_decreasing = all(1 <= row[i] - row[i + 1] <= 3 for i in range(len(row) - 1))
        
#         # Increment reports if the row satisfies either condition
#         if is_increasing or is_decreasing:
#             reports += 1

#     return reports

#PART TWO
# Problem Dampener
# Function to process the array with the ability to remove at most one number
def calculate_reports(array):
    """
    Calculates the number of rows in which the numbers are in strictly increasing
    or decreasing order with differences between 1 and 3, allowing the removal
    of at most one number per row.
    
    :param array: 2D array (list of lists)
    :return: Count of valid rows
    """
    reports = 0

    # Helper function to check if a row is valid (strictly increasing or decreasing)
    def is_valid_row(row):
        is_increasing = all(1 <= row[i + 1] - row[i] <= 3 for i in range(len(row) - 1))
        is_decreasing = all(1 <= row[i] - row[i + 1] <= 3 for i in range(len(row) - 1))
        return is_increasing or is_decreasing

    # Iterate over each row
    for row in array:
        if is_valid_row(row):
            # Row is already valid
            reports += 1
            continue

        # Check if the row can be made valid by removing at most one element
        for i in range(len(row)):
            # Remove the i-th element and check if the row becomes valid
            new_row = row[:i] + row[i + 1:]
            if is_valid_row(new_row):
                reports += 1
                break  # Stop checking further as we can remove only one element

    return reports

# Main function
def main():
    """
    Main function to demonstrate the usage of process_2d_array.
    """
    # File containing the 2D array
    input_file = "day2 puzzle input.txt"

    try:
        # Read the array from the file
        array = read_array_from_file(input_file)
        
        print("Input array from file:")
        for row in array:
            print(row)

        reports = calculate_reports(array)

        print("\n** The number of the safe reports is: %d. **\n" % reports)
    
    except Exception as e:
        print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    main()