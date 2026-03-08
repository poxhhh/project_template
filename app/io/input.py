import pandas as pd

def input_from_console():
    """
    reads text from the console
    """
    text = input("Enter text: ")
    return text

def read_file_python():
    """
    reads text from file using python's built-in capabilities
    """
    with open("data/text.txt", "r", encoding="utf-8") as fb:
        text = fb.read()
    return text

def read_file_pandas():
    """
    reads text from file using pandas
    """
    df = pd.read_csv("data/text.txt", header=None, names=['text'])
    return '\n'.join(df['text'])