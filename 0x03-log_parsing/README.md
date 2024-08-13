# 0x03. Log Parsing

## Description
This project involves creating a Python script that reads log entries from standard input (stdin) in real-time, parses the log data, and computes key metrics. The script is designed to handle large volumes of log data, aggregate important information such as status codes and file sizes, and print these statistics periodically or when the script is interrupted.

## Concepts and Resources

### Key Concepts:
- **File I/O**: Reading from stdin line by line.
- **Signal Handling**: Gracefully handling keyboard interruptions (e.g., `CTRL + C`).
- **Data Processing**: Parsing strings to extract specific data points and aggregating data.
- **Regular Expressions**: Validating and parsing the format of each log entry.
- **Dictionaries**: Using dictionaries to count occurrences of status codes and accumulate file sizes.
- **Exception Handling**: Managing potential exceptions during file reading and data processing.

### Resources:
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python Signal Handling](https://docs.python.org/3/library/signal.html)
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## Requirements

- Python 3.4.3 or higher
- The script will be executed on Ubuntu 20.04 LTS
- All files must end with a new line
- The first line of your Python file must be exactly `#!/usr/bin/python3`
- Your code should conform to [PEP 8 style guidelines](https://pep8.org/)
- All your files must be executable

## How to Run

1. **Clone the repository** (if applicable):

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory**:

    ```bash
    cd 0x03-log_parsing
    ```

3. **Make the Python script executable**:

    ```bash
    chmod +x log_parser.py
    ```

4. **Run the script**:

    ```bash
    cat <log_file> | ./log_parser.py
    ```

    - Replace `<log_file>` with the path to your log file.
    - The script will process the log file line by line and print the statistics every 10 lines or when interrupted.

## Example Usage

Here’s an example of how the output might look:

```bash
$ cat sample_log.txt | ./log_parser.py
File size: 5000
200: 30
301: 5
404: 2
File size: 10200
200: 60
301: 10
404: 4

