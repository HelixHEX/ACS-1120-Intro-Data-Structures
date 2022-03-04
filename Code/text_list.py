def text_list(file_name):
  punc = '''!"#$%&'()…*+,-./:;<=>?@[\]^—_`{|}~'''
  words_list = []
  with open(file_name) as f:
      for line in f:
          words_list += line.translate(str.maketrans('','', punc)).lower().split()
  return words_list