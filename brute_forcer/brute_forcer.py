import requests
import re,sys,argparse
import concurrent.futures
from urllib.parse import urljoin
#Check and parse the Argument
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Use -u or --url followed by a url")
parser.add_argument("-w", "--wordlist", help="Use -w or --wordlist followed by wordlist")
args = parser.parse_args()
if not args.url:
    print(f"\033[0;31mPlease Provide a url use -h or --help to get the help message\033[0m")
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
def check_directory(url, directory):
    try:
        response = requests.get(urljoin(url, directory))
        if response.status_code == 200:
            print(f"\033[92m[+] [200] Found directory: {urljoin(url, directory)}\033[0m")
        else:
            print(f"[+] [404] NOT Found : {urljoin(url, directory)}")
    except Exception as e:
        pass

# Function to brute force directories using multiple threads
def brute_force_directories(url, wordlist, num_threads=10):
    with open(wordlist, 'r') as f:
        directories = f.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(check_directory, url, directory) for directory in directories]
        try:
            for future in concurrent.futures.as_completed(futures):
               future.result()
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt received. Terminating...")
            for future in futures:
                future.cancel()
            executor.shutdown(wait=False)

if __name__ == "__main__":
    url=args.url
    target_url = url_checker(url)
    wordlist_path = args.wordlist if args.wordlist else '../wordlist/common_directories.txt'
    brute_force_directories(target_url, wordlist_path)

