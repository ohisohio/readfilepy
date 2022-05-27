# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    f = open('story.txt','r')
    contents = f.read()
    return contents



def count_words():
    text=read_file_content("./story.txt")
    count = dict()
    wordcount = text.split()
   
    for word in wordcount:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1
    return count


# print(read_file_content('./story.txt'))
print (count_words())
