pip install pandas


import json
import pandas as pd

def process_json(json_data):
    # Process the nested data
    processed_data = []

    def process_section(section):
        section_data = {"sectionName": section["sectionName"]}
        books_data = []

        for book in section["books"]:
            book_data = {
                "title": book["title"],
                "author": book["author"],
                "price": book["price"],
                "isAvailable": book["isAvailable"]
            }
            books_data.append(book_data)

        section_data["books"] = books_data
        processed_data.append(section_data)

    for section in json_data["sections"]:
        process_section(section)

    return processed_data

def convert_to_excel(data, output_file="output.xlsx"):
    # Convert data to Excel format
    df = pd.json_normalize(data, "books", ["sectionName"])
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Read JSON file
    try:
        with open("sample.json", "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print("Error: JSON file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Incorrect JSON format.")
        exit(1)

    # Process the nested data
    processed_data = process_json(json_data)

    # Convert to Excel format
    convert_to_excel(processed_data)

    print("Conversion successful. Excel file created.")
