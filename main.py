import pandas as pd
import colorama
import nltk
import math
import sys
import os

nltk.download('punkt')

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def info_retrieval():
    query = nltk.word_tokenize(input("Search:\n=>"))

    matrix = pd.read_csv("matrix.csv")
    docs = pd.read_csv("data.csv")

    matrix["query"] = 0
    for token in query:
        try:
            matrix.loc[matrix["Words"] == token, "query"] = 1
        except:
            pass

    matrix["idf"] = 0
    for idx, _ in enumerate(matrix["Words"]):
        matrix.loc[idx, "idf"] = math.log10(len(docs["docID"])/matrix.loc[idx, "df"])

    doc_cols = list(matrix.filter(like='Doc'))[:1460] + ['query']
    df_modified = matrix[doc_cols].mul(matrix['idf'], axis=0)

    docs["cos"] = 0
    for idx, _ in enumerate(docs["docID"]):
        docs.loc[idx, "cos"] = sum(df_modified["Doc " + str(idx+1)] * df_modified["query"])/math.sqrt(sum(df_modified["Doc " + str(idx+1)]**2))*math.sqrt(sum(df_modified["query"]**2))

    df_sorted = docs.sort_values(by="cos", ascending=False)
    os.system('cls' if os.name == 'nt' else 'clear')
    for _, row in df_sorted.head(10).iterrows():
        for word in query:
            row['docData'] = row['docData'].replace(word, f"{colorama.Fore.RED}{word}{colorama.Style.RESET_ALL}")
        print(f"Document number {row['docID']} - Title: {row['docTitle']}")
        print(f"\n{row['docData']}")
        print("-" * 30)

if not os.path.exists("matrix.csv"):
    print("matrix.csv Not Found!\nPlease Run data_to_matrix.py First!")
    sys.exit()

info_retrieval()