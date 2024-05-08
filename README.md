# Directory Brute Forcer

Directory Brute Forcer is a Python script for brute forcing directories on a target website using a wordlist of common directory names. It provides a simple yet effective way to discover potential directories on a web server.

## Features

- Brute forces directories on a target website using a wordlist of common directory names.
- Prints found directories with their HTTP response status codes.
- Supports multi-threading for faster directory discovery.
- Customizable wordlist for directory brute forcing.

## Getting Started

### Installation

1. Clone this repository:

```bash
git clone https://github.com/your_username/directory_brute_forcer.git
```
2.Navigate to the directory_brute_forcer directory:
```bash
cd directory_brute_forcer
```
3.Install dependencies:
```bash
pip install -r requirements.txt
```
### Usage
Run the `brute_forcer.py` script with the target URL as an argument:
```bash
python brute_forcer/brute_forcer.py
```
You will be prompted to enter the target URL and wordlist file path. The script will then attempt to brute force directories on the target website and print the results.

### Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch (git checkout -b feature/your-feature-name).

3. Make your changes.

4. Commit your changes (git commit -am 'Add new feature').

5. Push to the branch (git push origin feature/your-feature-name).

6. Create a new pull request.

### Wordlist
The wordlist/ directory contains common directory names. You can customize the `common_directories.txt` file or add your own wordlist files for directory brute forcing.

## Disclaimer
This tool is intended for ethical hacking and security testing purposes only. Use it responsibly and only on websites you have permission to test.

### License

This project is licensed under the [MIT License](LICENSE).