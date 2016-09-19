import urllib

def read_text():
    quotes = open("/Users/admin/Files/고진텍기나파이루/IT/_Study/Study_Python/Udacity/Programming_Foundations/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    # print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no course words!")
    else:
        print ("could not scan the document properly.")

read_text()
    
