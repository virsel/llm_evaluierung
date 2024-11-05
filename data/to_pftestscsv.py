import pandas as pd
import json
import ast

def transform_csv(input_file, output_file):
    """
    Transform CSV from QA format to promtfoo testing format.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
    """
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Function to safely extract text from answers column
    def extract_answer_text(answer_str):
        try:
            # Convert string representation of dict to actual dict
            cleaned_string = (answer_str.replace("array", "").replace("dtype=object", "").replace("dtype=int32", ""))
            data = ast.literal_eval(cleaned_string)
            return data['text'][0][0]
        except:
            return ""
    
    # Create new dataframe with transformed data
    transformed_df = pd.DataFrame({
        'query': df['question'],
        'context': df['context'],
        'fact': df['answers'].apply(extract_answer_text)
    })
    
    # Write to new CSV file
    transformed_df.to_csv(output_file, index=False)
    
    # Print sample of transformed data
    print("\nTransformed data sample:")
    print(transformed_df.head())
    
if __name__ == "__main__":
    # Example usage
    input_file = "GermanQuAD_small.csv"
    output_file = "tests_qanda_lazy_context.csv"
    
    transform_csv(input_file, output_file)