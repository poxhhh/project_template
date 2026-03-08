def write_into_console(text):
    """
    writes the output to the console
    """
    print(text)

def write_into_file_python(text):
    """
    writes the output using python's built-in capabilities
    """
    with open("data/text.txt", "a", encoding="utf-8") as fb:
        fb.write("\n" + text)