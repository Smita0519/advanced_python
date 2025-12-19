 # word to find

def counting_words(target):
    try:
        with open("python.txt", "r") as file:
            content = file.read()
            # # python. is not same as python so replace with empty space
            # content = content.replace(".", "").replace(",", "")
            # Convert to lowercase
            words = content.lower().split()
            count = words.count(target)  #count
            
            print(f"The word '{target}' is repeated {count} times.")

    except FileNotFoundError:
        print(f"Error: The file was not found. Please check the name.")

target = "python"
counting_words(target)
    