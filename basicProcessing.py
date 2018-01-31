from urllib import request
url = "http://www.gutenberg.org/files/11/11.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

def basic_info(s):
    n = 50
    #use , to pass different strings to print function
    print("Type of the content: ",type(raw))
    #need to convert int to string
    print("Length of the content: "+str(len(raw)))
    #print first 50 character. python substring method - [start:end]
    print("The first %d characters %s are," %(n,raw[:50]))


def word_count(s):
    counts = dict()
    words = str.split(s)

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

s = 'the quick brown fox jumps over the lazy dog.'
print("---basic information---")
print(basic_info(raw))
print( word_count(raw))