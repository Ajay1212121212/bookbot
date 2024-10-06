def main():
    with open("books/frankenstein.txt", mode = "r") as frankenstein:
        read = frankenstein.read()
        print(read)
        
        
main()