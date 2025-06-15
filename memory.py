class Memory:
    def __init__(self):
        self.history = []

    def store(self, speaker, text):
        self.history.append({"speaker": speaker, "text": text})

    def recall(self):
        return self.history[-5:]  # Ambil 5 obrolan terakhir
