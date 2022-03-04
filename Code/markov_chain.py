from random import random
import sys
from typing import List
from listogram import Listogram
from text_list import text_list
import random
import sys
import time


def generate_sentence():
    file_name = sys.argv[1]
    if file_name:
        start_time = time.time()
        char_limit = random.randint(75, 150)
        word_list = text_list(file_name)
        len_word_list = len(word_list)
        # hist = Listogram(word_list)
        chosen_word = random.choice(word_list)
        sentence = "" 
        # while len(sentence) < char_limit:
        #   print(chosen_word)
        #   temp_list = []
        #   for index in chosen_word[2]:
        #     if index < len_word_list - 1:
        #       temp_list.append(word_list[index])
        #   chosen_word = hist.sample()
        #   sentence += f"{chosen_word[0]} " 

        while len(sentence) <= char_limit:
            temp_list = []
            for index, word in enumerate(word_list):
                if word[0] == chosen_word[0] and index < len_word_list - 1:
                    temp_list.append(word_list[index+1])
            chosen_word = random.choice(temp_list)
            sentence += f"{chosen_word} "
        # else:
            # return "Cannot generate sentence"
        end_time = time.time()
        print(sentence)
        print(f"Code completed in: {end_time - start_time}")
    return "File name not given"


# if __name__ == '__main__':
generate_sentence()
