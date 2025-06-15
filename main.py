from core import AGI

if __name__ == "__main__":
    agi = AGI()

    while True:
        user_input = input("👤 Kamu: ")
        if user_input.lower() in ["exit", "keluar"]:
            print("👶 BabyAGI: Sampai jumpa!")
            break

        response = agi.respond(user_input)
        print("👶 BabyAGI:", response)
