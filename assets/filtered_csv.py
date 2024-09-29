import csv


def filter_and_select_columns_csv(input_file, output_file, selected_columns):

    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            if not set(selected_columns).issubset(reader.fieldnames):
                raise ValueError("Some selected columns do not exist in the input file.")

            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=selected_columns)
                writer.writeheader()

                for row in reader:
                    filtered_row = {col: row[col] for col in selected_columns}
                    writer.writerow(filtered_row)

        print(f"Filtered and selected columns CSV created: {output_file}")

    except Exception as e:
        print(f"Error processing CSV: {str(e)}")



columns_to_include = ['Target Longitude', 'Target Latitude','Target Priority','Target Industry','Target Type','Target City','Target Country','Target ID']

filter_and_select_columns_csv('operations.csv', 'new_csv.csv',  columns_to_include)