import tkinter as tk
import tktable


class FlashCardTable:
    def __init__(self, flashcard_dict):
        global root
        root = tk.Tk()
        root.title("Flashcard Table")

        self.create_table()
        self.flashcard_dict = flashcard_dict
        self.show_all_flashcards()

        root.mainloop()

    def show_all_flashcards(self):
        for flashcard in self.flashcard_dict:
            self.show(flashcard)

    def show(self, flashcard):
        word = flashcard.word
        definition = flashcard.definition

        index = "%i,%i" % (row_count, 0)
        self.var[index] = str(word)

        index = "%i,%i" % (row_count, 1)
        self.var[index] = str(definition)

    def create_table(self):
        global tb
        global var
        global flashcard_frame
        global row_count

        row_count = 0

        flashcard_frame = tk.Frame(root)
        flashcard_frame.pack()

        tb = tktable.Table(flashcard_frame,
                           width=50,
                           rows=80,
                           cols=2,
                           titlerows=1,
                           colwidth=40)
        var = tktable.ArrayVar(flashcard_frame)
        tb['variable'] = var
        tb.pack()


flashcard_table = FlashCardTable({"hi": "hi"})
