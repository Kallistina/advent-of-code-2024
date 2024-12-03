import re

# PART ONE
# def extract_and_calculate_sum(file_path):
#     with open(file_path, 'r') as file:
#         data = file.read()
    
#     # Regular expression to match "mul(number1, number2)"
#     pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
#     matches = re.findall(pattern, data)
    
#     # Convert matches to tuples of integers
#     number_pairs = [(int(num1), int(num2)) for num1, num2 in matches]
    
#     # Calculate the sum of the products
#     total_sum = sum(num1 * num2 for num1, num2 in number_pairs)
    
#     return total_sum

# PART TWO
def extract_and_calculate(file_path):   
    # Read the program from the given file
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()

    # Initialize the state where multiplications are enabled by default
    mul_enabled = True
    total_sum = 0

    # Regular expression for detecting valid mul instructions: mul(num1,num2)
    mul_pattern = r'mul\((-?\d+),(-?\d+)\)'
    i = 0
    n = len(corrupted_memory)

    while i < n:
        # Debug print to track what is being processed
        #print(f"Processing: {corrupted_memory[i:i+10]}...")

        # Check for "do()" instruction to enable multiplication
        if corrupted_memory.startswith("do()", i):
            #print("do() - Multiplications enabled")
            mul_enabled = True  # Enable multiplication
            i += 4  # Skip "do()"
        
        # Check for "don't()" instruction to disable multiplication
        elif corrupted_memory.startswith("don't()", i):
            #print("don't() - Multiplications disabled")
            mul_enabled = False  # Disable multiplication
            i += 7  # Skip "don't()"
        
        # Look for valid mul(X,Y) instructions
        else:
            mul_match = re.match(mul_pattern, corrupted_memory[i:])
            if mul_match:
                x, y = int(mul_match.group(1)), int(mul_match.group(2))
                if mul_enabled:
                    #print(f"Multiplying: {x} * {y} = {x * y}")
                    total_sum += x * y
                #else:
                    #print(f"Skipping: {x} * {y} (multiplications disabled)")
                i += len(mul_match.group(0))  # Skip the matched mul instruction
            else:
                i += 1  # Move to the next character if no match

    return total_sum

# Main function
def main():
    """
    Main function
    """

    input_file = "puzzle_input.txt"

    try:
        result = extract_and_calculate(input_file)

        print("\n** The result of the multiplications is: %d. **\n" % result)
    
    except Exception as e:
        print(f"Error: {e}")

# Entry point
if __name__ == "__main__":
    main()