import re


def translate(text):
    pig_text = []
    regex = re.compile('^(x(?!r)|y(?!t)|[^aeiouqxy]*(?:qu?)?)(.+)$')
    for word in text.split():
        match = re.search(regex, word)
        pig_word = match.expand(r"\2\1ay")
        pig_text.append(pig_word)
    return " ".join(pig_text)
