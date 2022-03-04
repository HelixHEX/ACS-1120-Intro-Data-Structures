import re, sys 

def split_on_whitespace(text):
    return re.split('\s+', text)

def tokenize(file_name):
    source = open(file_name).read()
    no_punc_text = remove_punctuation(source)
    tokens = split_on_whitespace(no_punc_text)
    return tokens

def remove_punctuation(text):
    no_punc_text = re.sub('[,.()…]', '', text)
    no_punc_text = re.sub('-', ' ', no_punc_text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
        print(tokens)