import pandas as pd

DATA_PATH = "data/GermanQuAD.csv"


# Read the CSV file
df = pd.read_csv(DATA_PATH)

def get_var(var_name, prompt, other_vars):
    question = other_vars["query"]
    # find context of question in df 
    context_text = df.loc[df['question'] == question, 'context'].values[0]

    return {
        "output": context_text,
    }
