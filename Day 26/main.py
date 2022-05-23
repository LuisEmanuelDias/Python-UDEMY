import pandas
import bs4
name = input("Introduce your name: ").upper()
bs4.
data = pandas.read_csv("nato_phonetic_alphabet.csv")

NATO_name = [(data.code[data.letter == let]).to_string(index=False) for let in name]
print(NATO_name)
