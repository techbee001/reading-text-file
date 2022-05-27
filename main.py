 # Read text from a file, and count the occurence of words in that text
 # Example:
 # count_words("The cake is done. It is a big cake!") 
 # --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
 
def read_file_content(filename):
     # [assignment] Add your code here 
     with open(filename) as file:
         text = file.read()
         file.close()
     # return type(text) - the type text is a string therfore I will be returning the text
     return text
def count_words():
     text = read_file_content("./story.txt")
     # [assignment] Add your code here
     dic = {}
     for item in text.split():
         if item in dic:
             dic[item] += 1
         else:
             dic[item] = 1
     return dic
     # return {"as": 10, "would": 20}
 # print(count_words())   