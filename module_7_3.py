# Задача "Найдёт везде"

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = ''
                for line in file:
                    signs = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for sign in signs:
                        line = line.replace(sign, '').lower()
                    lines = lines + line
                all_words[file_name] = lines.split()
        return all_words

    def find(self, word):
        finds = {}
        for key, values in self.get_all_words().items():
            if word.lower() in values:
                finds.update({key:values.index(word.lower())+1})
        return finds
    def count(self, word):
        finds = {}
        for key, values in self.get_all_words().items():
            i = 0
            for value in values:
                if word.lower() == value:
                    i = i + 1
            finds.update({key: i})
        return finds

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего