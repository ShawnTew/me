"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
it will create lists from the words
some_words = ['what', 'does', 'this', 'line', 'do', '?']
it will put the word from the list in the terminal
for word in some_words:
    print(word)
it will do the same as lines 16-17
for x in some_words:
    print(x)
it will print the list
print(some_words)
it will print 'some_words contains more than 3 words' because some words has more than 3 words
if len(some_words) > 3:
    print('some_words contains more than 3 words')
it creates a function called usefulFunction 
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """this will print the plantform
    print(platform.uname())

usefulFunction()
