#!/usr/bin/env python3
# lesson04 trigrams
import re
import sys
import random
from collections import defaultdict

__author__ = "Wieslaw Pucilowski"

# global variables:
list_words = []
tridict = defaultdict(list)
story = []


def parse_text():
    if len(sys.argv) != 2:
        print("""
        Wrong number of script arguments!
        Script execcution: {} <file to parse>
        """.format(sys.argv[0]))
        sys.exit()
    p = re.compile('([\w]+)')
    with open(sys.argv[1], 'r') as f:
        content = f.read()
        for word in content.split():
            m = p.match(word)
            if m:
                list_words.append(m.groups()[0])


def build_tridict():
    for i in range(len(list_words)-2):
        tridict[(list_words[i],
                 list_words[i+1])].append(list_words[i+2])


def create_story():
    words_num = len(list_words)
    list_tridict_keys = list(tridict.keys())
    key = random.choice(list_tridict_keys)
    story.extend(key)
    while len(story) <= words_num:
        next_word = random.choice(tridict[key])
        story.append(next_word)
        key = tuple(story[-2:])
        if key not in tridict.keys():
            key = random.choice(list_tridict_keys)


def write_story_to_file():
    text = ''
    for i, j in enumerate(story):
        if i % 20 == 0:
            text += "\n"
        else:
            text += """{} """.format(j)
    with open(sys.argv[1].split('.')[0]+'_trigrams.txt', 'w') as f:
        f.write(text)

if __name__ == "__main__":
    parse_text()
    build_tridict()
    create_story()
    write_story_to_file()
