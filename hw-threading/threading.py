import threading
from collections import defaultdict
from pathlib import Path
import timeit

def search_in_file(file_path, keywords, results_queue):
  with open(file_path, 'r') as file:
    content = file.read()
    for keyword in keywords:
      if keyword in content:
        results_queue.put((keyword, file_path))

def thread_task(files, keywords, results_queue):
  for file in files:
    search_in_file(file, keywords, results_queue)

def main_threading(file_paths, keywords):
  num_threads = 4
  threads = []
  results = defaultdict(list)

  for i in range(num_threads):
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  return results

if __name__ == '__main__':
  file_paths = list(Path("input").glob("*.py"))
  print(f"File paths: [file_paths]\n")
  keywords = []
  results = main_threading(file_paths, keywords)
  print(results)