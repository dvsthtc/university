# 
# Hangman game
#


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord = '', lettersGuessed = []):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += lettersGuessed.count(letter)   
            if count == len(secretWord):
                return True
        else:
            return False




def getGuessedWord(secretWord = '', lettersGuessed = []):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    guessed = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessed += '_ '
              
        if letter in lettersGuessed:
            guessed += letter
            
    return guessed
                                    
            

def getAvailableLetters(lettersGuessed = [],):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    available = ''
    for letter in string.ascii_lowercase:
        if letter in lettersGuessed:
           available += ''
        if letter not in lettersGuessed:
            available += letter
        
    return available
        

    

def hangman(secretWord = ''):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
        
    secretWord = random.choice(wordlist)
    line = '___________________' 
    guesses = 8 
    lettersGuessed = '' 
    print 'Welcome to the game, Hangman' 
    print 'I am thinking of a word that is ',len(secretWord),' letters long.' 
    while True: 
        print line 
        print 'You have ' ,str(guesses),' guesses left.' 
        print 'Aviable letters ',getAvailableLetters(lettersGuessed) 
        guess = raw_input('Please guess a letter: ') 
        if guess in lettersGuessed and guess in secretWord: 
            print 'Oops, you have already guessed that letter' 
            guess = '' 
        elif guess in lettersGuessed and guess not in secretWord: 
            print 'Oops, you have already tried that letter' 
            guess = '' 
        lettersGuessed += guess 
        if guess in secretWord: 
            print 'Good guess! :',getGuessedWord(secretWord, lettersGuessed) 
        else: 
            print 'Oops! That letter is not in my word: ' ,getGuessedWord(secretWord, lettersGuessed) 
            guesses -= 1 
        if isWordGuessed(secretWord, lettersGuessed): 
            print 'Congratulations, you won!' 
            break 
        if guesses == 0: 
            print 'Sorry, you ran out of guesses. The word was',secretWord 
            break 
    
        

    
        
            
            
    

        
    

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
