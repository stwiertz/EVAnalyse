from src.reader import main as reader_main
from src.analyser import main as analyser_main

# path = '250206_secret_frozen.mp4'
path = './local/video/arte.mp4'

def main():
    # Call the main function from reader.py
    reader_main.main(path)
    # You can also call other functions from reader if needed
    # reader('hello')
    analyser_main.main('boumba')

if __name__ == "__main__":
    main()
