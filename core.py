from data import knowledge_base
from memory import Memory

class AGI:
    def __init__(self):
        self.memory = Memory()

    def respond(self, input_text):
        self.memory.store("user", input_text)

        # Basic knowledge search
        response = knowledge_base.get(input_text.lower(), "Maaf aku belum tahu tentang itu.")

        # Tanya balik
        follow_up = self.generate_follow_up(input_text)

        final_response = f"{response} {follow_up}"
        self.memory.store("agi", final_response)
        return final_response

    def generate_follow_up(self, input_text):
        if "kamu" in input_text or "nama" in input_text:
            return "Ngomong-ngomong, kamu siapa ya?"
        elif "cuaca" in input_text:
            return "Kamu suka cuaca seperti itu?"
        else:
            return "Ada hal lain yang kamu ingin tahu?"
