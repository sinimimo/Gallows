import requests, random     # Import libraries

def vis():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)      # We make a request to a site with a list of words.
    words = response.text.split()           
    
    word = words[random.randint(0,len(words))]      # Saves a random word from a variable [words]
    wordHidden = ['-'] * len(word)
    attempt = 0

    while True:
        print('Word:', ''.join(wordHidden))
        dataInput = str(input('Enter a letter:'))       # User input
        if word.find(dataInput) != -1:
            for i in range(len(word)):
                if dataInput == word[i]:
                    wordHidden[i] = word[i]
        else:
            attempt += 1
        if '-' not in wordHidden:
            return print('Congratulations, you guessed the word [' + ''.join(wordHidden) + '] and saved the man!')
        
        if attempt == 8:
            return print('You failed to guess the word [' + word + '] YOU LOST!')
        print()
        print('attempts:', str(8-attempt) + '/' + str(8))

def main():
    vis()
    
if __name__ == '__main__':
    main()
