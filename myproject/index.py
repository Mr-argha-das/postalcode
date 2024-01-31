
    
    
import csv

def find_row(csv_file_path, target_value):
    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Check if the target value is in the current row
            if target_value in row:
                return row  # Return the first matching row

    return None  # Return None if the target value is not found


