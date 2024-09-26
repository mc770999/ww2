import csv


def filter_and_select_columns_csv(input_file, output_file, filter_function, selected_columns):
    """
    Filters rows from the input CSV file based on a given filter function and writes the specified columns to a new CSV file.

    Parameters:
    input_file (str): The path to the input CSV file.
    output_file (str): The path to the output CSV file where the filtered rows and selected columns will be saved.
    filter_function (function): A function that takes a row (as a dictionary) and returns True if the row should be included.
    selected_columns (list): A list of column names to be included in the output CSV.
    """

    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)  # Reads the CSV into a dictionary format

            # Ensure that the selected columns exist in the input file's header
            if not set(selected_columns).issubset(reader.fieldnames):
                raise ValueError("Some selected columns do not exist in the input file.")

            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=selected_columns)  # Write using only selected columns
                writer.writeheader()  # Write the header of the selected columns

                for row in reader:
                    #if filter_function(row):  # Apply filter function
                        # Write only the selected columns from the filtered row
                    filtered_row = {col: row[col] for col in selected_columns}
                    writer.writerow(filtered_row)

        print(f"Filtered and selected columns CSV created: {output_file}")

    except Exception as e:
        print(f"Error processing CSV: {str(e)}")


# Example usage:
# Filter for rows where age is greater than 30, and only include 'name' and 'city' in the new CSV.

def age_filter(row):
    return int(row['age']) > 30


# Specify the columns you want in the new CSV file
columns_to_include = ['Target Longitude', 'Target Latitude','Target Priority','Target Industry','Target Type','Target City','Target Country','Target ID']

# Call the function
filter_and_select_columns_csv('operations.csv', 'new_csv.csv', age_filter, columns_to_include)