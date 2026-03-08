from app.io import input_from_console, read_file_python, read_file_pandas, write_into_console, write_into_file_python

def main():
    text1 = input_from_console()
    text2 = read_file_python()
    text3 = read_file_pandas()

    write_into_console(text1)
    write_into_console(text2)
    write_into_console(text3)

    write_into_file_python(text1)
    write_into_file_python(text2)
    write_into_file_python(text3)

if __name__ == '__main__':
    main()