import tkinter as tk
from PIL import ImageTk, Image
from FlashCard import FlashCard


class FlashCardStack:

    def __init__(self):
        self.win = tk.Tk()
        self.win.title("FlashCard Maker")
        self.main_frame = tk.Frame(self.win)
        self.main_frame.pack()

        self.cards_list = []
        self.show_content()

        # self.add_card()

        tk.mainloop()

    def show_content(self):
        label_welcome = tk.Label(self.main_frame, text="Welcome to FlashCard Maker!")
        label_welcome.grid(row=0, column=0)
        label_welcome.pack()

        btn_add_card = tk.Button(self.main_frame, text="Add Card", command=lambda : self.on_click_add_card())
        btn_add_card.grid(row=1, column=0)
        btn_add_card.pack()

        btn_add_card = tk.Button(self.main_frame, text="Review Flashcards", command=lambda: self.on_click_review_flashcards())
        btn_add_card.grid(row=2, column=0)
        btn_add_card.pack()

        btn_add_card = tk.Button(self.main_frame, text="View All Flashcards", command=lambda: self.on_click_view_all_flashcards())
        btn_add_card.grid(row=3, column=0)
        btn_add_card.pack()

        background_image = ImageTk.PhotoImage(Image.open("wood2.png"))
        background_label = tk.Label(self.main_frame, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.pack()

    def on_click_add_card(self):
        pass

    def on_click_view_all_flashcards(self):
        pass

    def on_click_review_flashcards(self):
        pass



    """
    Functionality:
    -add/remove flashcards
    -view all flashcards in list format (term, definition)
    -use 
    
    """

flashcard_stack = FlashCardStack()
