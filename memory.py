import os

MEMORY_FILE = "memory.txt"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return f.read().splitlines()
    return []

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        f.write("\n".join(memory))
