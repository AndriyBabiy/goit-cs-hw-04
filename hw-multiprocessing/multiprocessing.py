import multiprocessing
from collections import defaultdict
from pathlib import Path
import timeit
import os

def search_in_file(file_path, keywords, results_queue):
  with open(file_path, 'r') as file:
    content = file.read()
    for keyword in keywords:
      if keyword in content:
        results_queue.put((keyword, file_path))

def process_task(files, keywords, results_queue):
  for file in files:
    search_in_file(file, keywords, results_queue)

def main_multiprocessing(file_paths, keywords): 
  num_processes = os.cpu_count()

  processes = []
  results_queue = multiprocessing.Queue()
  results = defaultdict(list)

  for i in range(num_processes):
    processes.append(process)
    process.start()

  for process in processes:
    process.join()

  while not results_queue.empty():
    keyword, file_path, = results_queue.get()
    results[keyword].append(file_path)

  return results


if __name__ == '__main__':
  file_paths = list(Path("input").glob("*.py"))
  print(f"File paths: [file_paths]\n")
  keywords = []
  results = main_multiprocessing(file_paths, keywords)
  print(results)