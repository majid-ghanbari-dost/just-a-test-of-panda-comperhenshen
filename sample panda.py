import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter: row.code for (key, row) in data.iterrows()}
word = input("put it here!: ")
new_word = [n.upper() for n in word]
new_list = [data_dic[n] for n in new_word]
print(new_list)
