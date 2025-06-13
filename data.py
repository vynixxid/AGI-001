import os

def load_all_articles():
    data_folder = "data"
    articles = []
    if os.path.exists(data_folder):
        for filename in sorted(os.listdir(data_folder)):
            if filename.endswith(".txt"):
                with open(os.path.join(data_folder, filename), "r", encoding="utf-8") as f:
                    articles.append(f.read())
    return articles
