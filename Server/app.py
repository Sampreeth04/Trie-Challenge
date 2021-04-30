# app.py
class trie:

    def __init__(self):
        self.stored_trie = {}
        
    def get_trie():
        return self.stored_trie

    #Function to insert a list of words into the trie
    def insert_words(self, word_list):
        for word in word_list:
            current_trie = self.stored_trie
            for char in word:
                    if char not in current_trie:
                        current_trie[char] = {}
                    current_trie = current_trie[char]
            current_trie['end_of_word'] = 'True' 
        return self.stored_trie

    #Function to search for a word in the stored trie
    def search_word(self, word):
        current_trie = self.stored_trie
        for char in word:
            if (char not in current_trie) or (char == word[-1] and 'end_of_word' not in current_trie[char]):
                return False
            current_trie = current_trie[char]
        print(self.stored_trie)
        return True

    #Functions to remove a particular word from the stored trie
    #Decided to use recursion as when I attempted to use an iterative method, there were empty dictionaries that occupy unecessary memory and were tedious to remove
    def remove_word(self, current_trie, word, char_index):
        print(char_index)
        condition = 0
        if char_index == len(word):
            if 'end_of_word' in current_trie:
                current_trie.pop('end_of_word')
                if len(current_trie) == 0:
                    return 0
                elif len(current_trie) != 0:
                    return -1
            elif 'end_of_word' not in current_trie:
                return -1
        else:
            if word[char_index] in current_trie and self.remove_word(current_trie[word[char_index]], word, char_index+1) == 0:
                if len(current_trie[word[char_index]]) == 0:
                    current_trie.pop(word[char_index])
                    return 0
                elif len(current_trie[word[char_index]]) != 0:
                    return -1
            else:
                return -1

#using recursion is the most efficient method for deletion in my opinion because when I attempted it iteratively, several empty dictionaries remained which occupied unecessary memory

    def delete_word(self, word):
        current_trie = self.stored_trie
        for char in word:
            if (char not in current_trie) or (char == word[-1] and 'end_of_word' not in current_trie[char]):
                return 'No word found'
            current_trie = current_trie[char]
        current_trie = self.stored_trie
        self.remove_word(current_trie, word, 0)

    #Function to output a list of autocomplete suggestions
    def autocomplete_suggestions(self, word):
        current_trie = self.stored_trie
        global autocomplete_suggestions_list
        global autocomplete_stems
        autocomplete_suggestions_list = []
        autocomplete_stem = ''
        for char in word:
            if char not in current_trie:
                return 'No Matches'
            autocomplete_stem += char
            current_trie = current_trie[char]
        if 'end_of_word' in current_trie:
            autocomplete_suggestions_list.append(autocomplete_stem)
            #Checks if current trie has no children
            if len(current_trie) == 1:
                return autocomplete_suggestions_list
        autocomplete_stems = [autocomplete_stem]
        autocomplete_suggestions_list = self.autocomplete(current_trie, autocomplete_stem)
        print(autocomplete_suggestions_list)
        print(self.stored_trie)
        return autocomplete_suggestions_list

    def autocomplete(self, current_trie, autocomplete_word):
        for char in current_trie.keys():
            print('Stems: ', autocomplete_stems)
            print(char)
            if char == 'end_of_word':
                continue
            autocomplete_word = autocomplete_stems[-1]
            autocomplete_word += char
            autocomplete_stems.append(autocomplete_word)
            print(autocomplete_word)
            next_trie = current_trie[char]
            if 'end_of_word' in next_trie:
                print('here')
                autocomplete_suggestions_list.append(autocomplete_word)
                print(autocomplete_suggestions_list)
                #Checks if trie has no children
                if len(next_trie) == 1:
                    autocomplete_stems.pop(-1)
                    continue
            self.autocomplete(next_trie, autocomplete_word)
            autocomplete_stems.pop(-1)  
            print('Stems1: ', autocomplete_stems)  
        return autocomplete_suggestions_list

    def display_trie(self):
        print(self.stored_trie)

trie = trie()
trie.insert_words(['car', 'house', 'cars', 'hou', 'houses'])

#condition, trie = trie.search_word('house')
#print(condition)
#print(trie)
print("=====");
print(trie.search_word('car'));
print(trie.delete_word('car'))
print(trie.search_word('car'));
print("=====");

trie.display_trie()

trie.autocomplete_suggestions('hou')

import threading
import time
from flask import Flask, request, jsonify

app = Flask(__name__)
sem = threading.Semaphore()

#Defining routes to each trie function
@app.route('/search/', methods=['GET'])
def search():
    sem.acquire()
    word = request.args.get('word');
    print(trie.search_word(word))
    sem.release()
    return jsonify(trie.search_word(word));

@app.route('/insert/', methods=['GET'])
def insert():
        sem.acquire()
        word_str = request.args.get('word');
        words = word_str.split(",");
        sem.release()
        return trie.insert_words(words);

@app.route('/delete/', methods=['GET'])
def delete():
        sem.acquire()
        word = request.args.get('word');
        print(trie.delete_word(word))
        sem.release()
        return jsonify(trie.delete_word(word));

@app.route('/suggest/', methods=['GET'])
def auto_suggest():
        sem.acquire()
        word = request.args.get('word');
        print(trie.search_word(word))
        suggestions = trie.autocomplete_suggestions(word)
        sem.release()
        return jsonify(suggestions);
'''
@app.route('/print/', method=['GET'])
def print_trie():
        sem.acquire()
        trie_data = trie.get_trie();
        sem.release()
        return jsonify(trie_data);
'''
#Using threaded to allow multiple user support
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
