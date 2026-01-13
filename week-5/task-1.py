import string
import os
from collections import Counter

def does_exist(fname):
    if not os.path.exists(fname):
        with open(fname, "w") as f:
            f.write("Code validation test")

def get_stats(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    n_lines = len(lines)
    words = []
    for line in lines:
        clean = line.translate(str.maketrans("", "", string.punctuation)).lower()
        words.extend(clean.split())
    return n_lines, len(words), Counter(words)

def save_stats(n_lines, n_words, counts):
    with open("analysis.txt", "w") as f:
        f.write(f"Lines: {n_lines}\nWords: {n_words}\n")
        for w, c in counts.items():
            f.write(f"{w}: {c}\n")

def main():
    file_name = "text.txt"
    does_exist(file_name)
    l, w, c = get_stats(file_name)
    save_stats(l, w, c)
    print("Analysis done. Saved to analysis.txt")

main()