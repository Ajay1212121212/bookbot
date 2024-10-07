def main():
    book_name = "frankenstein"
    with open("books/frankenstein.txt", mode = "r") as book:
        
        read = book.read()
        letter_counter = {}
        word_counter = read.split()
        word_counter = len(word_counter)
        
        lower = read.lower()
        
        for i in range(0, len(lower)-1):
            if lower[i] in letter_counter:
                letter_counter[lower[i]]+=1
                
            elif lower[i].isalpha():
                letter_counter.update({lower[i]:1})
                
        print(letter_counter)
        
        print(f"--- Begin report of books/{book_name}.txt ---")
        print(f"{word_counter} words found in the document\n")
        
        sorted_array = list(letter_counter.keys())
        sorted_array.sort()
        
        
        for i in sorted_array:
            print(f"The '{i}' character was found {letter_counter[i]} times ")
            
        print("--- End report ---")
main()