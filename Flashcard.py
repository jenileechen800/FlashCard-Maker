import tkinter as tk


class FlashCard:
    def __init__(self, win):
        self.word = None
        self.definition = None

        root = win
        global flashcard_frame
        flashcard_frame = tk.Frame(root)
        flashcard_frame.pack()
        self.new_card()

    def new_card(self):
        label_new_card = tk.Label(flashcard_frame, text="Create New Card").grid(row=0)
        self.set_word()
        self.set_definition()

        btn_add_card = tk.Button(flashcard_frame, text="Add Card", command=lambda: self.btn_click_add_card())
        btn_add_card.grid(row=3, column=1)

    def set_word(self):
        global enter_word
        enter_word = tk.Entry(flashcard_frame)
        label_word = tk.Label(flashcard_frame, text="Enter Word:")

        enter_word.grid(row=1, column=1)
        label_word.grid(row=1)

    def set_definition(self):
        global enter_def
        enter_def = tk.Entry(flashcard_frame)
        label_def = tk.Label(flashcard_frame, text="Enter Definition:")

        enter_def.grid(row=2, column=1)
        label_def.grid(row=2)

    def btn_click_add_card(self):
        self.word = enter_word.get()
        self.definition = enter_def.get()
        print("word: " + self.word)
        print("def: " + self.definition)





