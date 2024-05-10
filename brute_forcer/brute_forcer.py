import requests
import concurrent.futures
from urllib.parse import urljoin

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
    target_url = input("Enter the target URL: ")
    wordlist_path = '../wordlist/common_directories.txt'


    brute_force_directories(target_url, wordlist_path)
