# Employee Profile Validator
A Python script developed as part of the freeCodeCamp Python Certificate course. 
This project demonstrates fundamental string manipulation and validation techniques in Python.
The *Employee Profile Validator* processes and cleans mock employee records (names, emails, phone numbers, and IDs), demonstrating real-world data standardisation and validation techniques in Python.

## Features
* **Email Parsing & Validation:** Extracts usernames from emails using slicing and the `.find()` method.
* **String Cleaning:** Utilizes `.strip()`, `.lower()`, `.upper()`, and `.title()` to format untidy text inputs (names and emails).
* **Text Replacement:** Replaces specific characters in strings, such as formatting phone numbers and transforming email components into display names.
* **Splitting & Joining:** Breaks down and reassembles structured address strings using `.split()` and `.join()`.
* **Prefix/Suffix & Counting Checks:** Validates codes and domains using `.startswith()`, `.endswith()`, and counts specific characters using `.count()`.

## Code Overview
The script processes various employee data attributes sequentially:
* **Email Handling:** Validates and slices email strings to isolate usernames.
* **Name Formatting:** Cleans up messy string inputs for consistent naming conventions.
* **Phone & Address Operations:** Sanitizes phone numbers and handles delimited text data.
* **Validation Checks:** Performs logical checks on employee codes and email formats.

## 💻 How to Run
1. Make sure you have Python installed on your system.
2. Clone this repository or download the `Employee_Profile_Validator.py` script.
3. Run the script using your terminal or command prompt:
   ```bash
   python Employee_Profile_Validator.py