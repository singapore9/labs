import sys
filename = 'L1n1.txt'

def toStandart(word):
    import string
    line = word
    endSent = ['...', '.', '!!', '!?', '?!', '!', '?']
    for char in endSent:
        line = line.replace(char, '.')
    for char in string.punctuation.replace('.','—'):
        line = line.replace(char, ' ')
    for char in string.whitespace:
        line = line.replace(char, ' ')
    return line.lower()

def stat(text):
    st_text = toStandart(text).replace('.',' ')
    import string
    words = [word for word in st_text.split() if word not in string.whitespace]
    dict_words = {word:words.count(word) for word in words}
    print(dict_words)
    return dict_words

def listSent(text):
    listSent = [sent for sent in toStandart(text).split('.')]
    listSent = listSent[:-1]
    numSent = []
    for i in range(len(listSent)):
        s = 0
        d = stat(listSent[i])
        for item in d:
            s += d[item]
        numSent.append(s)
    return sorted(numSent)

def averSent(text):
    if listSent(text):
        return sum(listSent(text))//len(listSent(text))
    else:
        return sum(listSent(text))

def mediSent(text):
    arr = listSent(text)
    if len(arr)%2:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2] + arr[len(arr)//2 + 1])/2

def topK(text, K, N):
    num = stat(text)
    Dnum = {word:num[word] for word in num if len(word)>=N}
    Nnum = dict()
    if N>0:
        for word in Dnum:
            for offset in range(len(word) - N + 1):
                val = Nnum.get(word[offset:offset+N], 0)+Dnum[word]
                Nnum[word[offset:offset+N]] = val
    else:
        Nnum = Dnum
    top = []
    print(Nnum)
    while (K != 0) & (Nnum != dict()):
        val = max(Nnum.values())
        for item in Nnum:
            if (val == Nnum[item]):
                top.append({item:val})
                K -= 1
                Nnum.pop(item)
                break
    return top
    
def main(text = open(filename, 'r').read()):
    print('Text:\n', text)
    print('Words dictionary:\n', stat(text))
    print('Average num of words in sentence:', averSent(text))
    print('Median num of words in sentence:', mediSent(text))
    try:
        s = input('Enter K, N for top-K for n-letter words:\n')
        K, N = list(map(int, s.split()))
        print('top-{0} of most used words with {1} letters:\n'.format(K, N),\
              topK(text, K, N))
    except:
        print('invalid input data')



if __name__ == '__main__':
    try:
        if '-f' in sys.argv:
            filename = sys.argv[sys.argv.index('-f') + 1]
    except:
        filename = 'L1n1.txt'
    main()
with open(filename, 'r') as f:
    text = f.read()
