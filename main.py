import requests
import json
import tkinter as tk

def words():
    word = word_entry.get()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    r = requests.get(url)
    dict = json.loads(r.text)
    try:
        data = dict[0]["meanings"][0]["definitions"][0]["definition"]
        output_lable.config(text=f"{data}")
    except Exception:
        output_lable.config(text="Error Enter the correct word")


window = tk.Tk()
window.title("Dictionary")

word_lable = tk.Label(window,text="Enter the word")
word_lable.pack()

word_entry = tk.Entry(window)
word_entry.pack()

word_search = tk.Button(window,text="Search",command=words)
word_search.pack()

output_lable = tk.Label(window,text="")
output_lable.pack()
window.mainloop()