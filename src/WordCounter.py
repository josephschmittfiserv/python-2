class WordCounter:
    count = 0

    def __init__(self, sentence):
        self.sentence = sentence
        self.count = 0

    def count_words(self):
        self.count = len(self.sentence.split(" "))
    
    def get_word_count(self):
        return self.count

    def get_shortest_word(self):

        new_list= self.sentence.split(" ")
        new_list = sorted(new_list,key=len)
        return len(new_list[0])
    
    def get_longest_word(self):
        new_list= self.sentence.split(" ")
        new_list = sorted(new_list,key=len)
        return len(new_list[len(new_list)-1])