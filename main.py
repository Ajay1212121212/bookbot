def main():
    with open("books/frankenstein.txt", mode = "a") as text:
        rea = text.read()
        print(rea)
        
        
main()