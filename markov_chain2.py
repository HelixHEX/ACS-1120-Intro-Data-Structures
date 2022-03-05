from random import random
import sys
from typing import List
from dictogram import Dictogram
from listogram import Listogram
from text_list import text_list
import random
import sys
import time
from tokens import tokenize

class Markov_Chain():
  def __init__(self, tokens) -> None:
    self.markov_chain = {}
    self.hist = Dictogram()

    for index in range(len(tokens)-2):
      pair = (tokens[index], tokens[index+1])
      self.hist.add_count(pair)

      if pair not in self.markov_chain.keys():
        self.markov_chain[pair] = Dictogram()
      self.markov_chain[pair].add_count(tokens[index+2])

  def walk(self, length=20) -> str:
    sentence = ""
    pair = self.hist.sample()
    sentence += f"{pair[0]} {pair[1]} "
    for _ in range(length):
      pair = (pair[1], self.markov_chain[pair].sample())
      sentence += f"{pair[1]} "
      
    return sentence
    
if __name__ == '__main__':
  file_name = sys.argv[1]
  tokens = tokenize(file_name)
  chain = Markov_Chain(tokens)
  # print(chain.markov_chain)
  print(chain.walk())
