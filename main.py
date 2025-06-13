from core import think
from memory import load_memory

if __name__ == "__main__":
    memory = load_memory()
    while True:
        try:
            user_input = input("Kamu: ")
            response = think(user_input, memory)
            print("AGI:", response)
        except KeyboardInterrupt:
            print("\n[!] Keluar...")
            break
