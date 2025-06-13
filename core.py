from memory import load_memory, save_memory
from data import load_all_articles

def think(input_text, memory):
    articles = load_all_articles()
    context = "\n".join(articles)
    response = f"[Belajar dari data...]\nKamu berkata: {input_text}\nJawaban berdasarkan konteks:\n{context[:300]}..."
    memory.append(f"User: {input_text}")
    memory.append(f"AGI: {response}")
    save_memory(memory)
    return response
