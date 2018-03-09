#Denver Wydermyer
#Computer Programming
#3/6/18

def longw():
    f = open('alice.txt', 'r')
    results=[]
    for line in f:
        for word in line.split():
            word_length = len(word)
            results.append(word_length)
            if word_length > word:
                print(results)

longw()
