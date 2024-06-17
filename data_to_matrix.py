import pandas as pd
import nltk
import csv
import os

nltk.download('punkt')

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def make_matrix(output_filename):
    data = pd.read_csv("data.csv")
    fieldnames = ["Words"]
    token_list = {}

    for id in data["docID"]:
        fieldnames.append("Doc "+str(id))

    fieldnames.append("df")

    for idx, sentence in enumerate(data["docData"]):
        new_tokens = nltk.word_tokenize(sentence)
        for token in new_tokens:
            if token not in token_list.keys():
                token_list[token] = [idx+1]
            else:
                token_list[token].append(idx+1)


    with open(output_filename, "w", newline="") as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for token in (token_list.keys()):
            sum = 0
            row = {"Words": token}
            for doc in data["docID"]:
                if doc in token_list[token]:
                    row["Doc "+str(doc)] = 1
                    sum += 1
                else:
                    row["Doc "+str(doc)] = 0
            row["df"] = sum
            writer.writerow(row)
    
        print(f"CSV file created: {output_filename}")

make_matrix("matrix.csv")