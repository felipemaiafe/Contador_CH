from PyPDF2 import PdfReader
import re

def extract_numbers_from_pdf(pdf_path):
    numbers = []

    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)

        for page_number in range(num_pages):
            text = reader.pages[page_number].extract_text()

            # Use regex to find all continuous numbers
            numbers.extend(re.findall(r'\b\d+\b', text))

    return numbers

def main():
    pdf_path = input("Enter the path to the PDF file: ").strip()
    numbers = extract_numbers_from_pdf(pdf_path)

    # Filter numbers to exclude single digits and numbers with 4 or more digits
    filtered_numbers = [int(number) for number in numbers if 10 <= int(number) <= 999]

    # Main numbers that must always be printed
    main_numbers = [90, 100, 105, 135, 150, 157, 175, 180, 200, 210]

    # Count the occurrence of each number
    numbers_count = {number: filtered_numbers.count(number) for number in set(filtered_numbers)}

    # Print the main numbers first
    print("Main Numbers")
    print("Number\t\tCount")
    print("====================")
    for number in main_numbers:
        count = numbers_count.get(number, 0)
        print(f"{number}\t\t{count}")
    print("====================")

    # Print other numbers that appeared
    print("\nOther Numbers")
    print("Number\t\tCount")
    print("====================")
    for number, count in sorted(numbers_count.items()):
        if number not in main_numbers:
            print(f"{number}\t\t{count}")

if __name__ == "__main__":
    main()