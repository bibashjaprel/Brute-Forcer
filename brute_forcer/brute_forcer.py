#
# Author: Bibash Japrel (github.com/bibashjaprel)

# A simple yet fast tool for finding web directories.

import requests
import re, sys, argparse, os
import concurrent.futures
from urllib.parse import urljoin

''' Colors '''
BLUE = '\033[0;38;5;12m'
RED = '\033[1;31m'
END = '\033[0m'
BOLD = '\033[1m'

# -------------- Arguments & Usage -------------- #
parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="Use -u or --url followed by a url")
parser.add_argument("-w", "--wordlist", help="Use -w or --wordlist followed by wordlist")
parser.add_argument("-i", "--include_404", action="store_true", help="Include 404 not found in the output")
parser.add_argument("-t", "--threads", type=int, default=20, help="Number of threads to use (default is 20)")
args = parser.parse_args()  # arguments to be parsed

if not args.url:
    print('''%s┓          ┏         
┣┓┏┓┓┏╋┏┓━━╋┏┓┏┓┏┏┓┏┓
┗┛┛ ┗┻┗┗   ┛┗┛┛ ┗┗ ┛
   by @bibashjaprel <3 %s''' % (RED, END))
    print()
    print('''%s * 💻 web app directory brute forcer.%s''' % (BLUE, END))
    sys.exit(1)
else:
    url = args.url

# Function to Check the Url is Valid or Invalid 
def url_checker(url):
    url_regex = r'^https?:\/\/'
    if url and not re.match(url_regex, url):
        print("Invalid URL. Please provide a URL with http or https scheme.")
        sys.exit(1)  
    return url

# Function to check if a directory exists on the target website
def check_directory(session, url, directory, include_404):
    try:
        response = session.get(urljoin(url, directory), timeout=10)
        if response.status_code == 200:
            print(f"\033[92m[+] [200] Found directory: {urljoin(url, directory)}\033[0m")
        elif include_404:
            print(f"[+] [404] NOT Found : {urljoin(url, directory)}")
    except requests.RequestException as e:
        pass

# Function to brute force directories using multiple threads
def brute_force_directories(url, wordlist, include_404, num_threads):
    with open(wordlist, 'r') as f:
        directories = f.read().splitlines()

    with requests.Session() as session:
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(check_directory, session, url, directory, include_404) for directory in directories]
            try:
                for future in concurrent.futures.as_completed(futures):
                    future.result()
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt received. Terminating...")
                for future in futures:
                    future.cancel()
                executor.shutdown(wait=False)

if __name__ == "__main__":
    url = args.url
    target_url = url_checker(url)

    # Get the script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    default_wordlist_path = os.path.join(script_dir, '..', 'wordlists', 'common_directories.txt')

    wordlist_path = args.wordlist if args.wordlist else default_wordlist_path
    include_404 = args.include_404
    num_threads = args.threads
    brute_force_directories(target_url, wordlist_path, include_404, num_threads)
