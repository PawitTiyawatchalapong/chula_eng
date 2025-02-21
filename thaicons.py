import tkinter as tk
import random

# List of Thai consonants and their names
thai_consonants = [
    ("ก", "gor gai"), ("\u0e02", "khor khai"), ("\u0e03", "khor khuad"),
    ("\u0e04", "khor khwai"), ("\u0e05", "khor khon"), ("\u0e06", "khor ra-khang"),
    ("\u0e07", "ngor ngu"), ("\u0e08", "jor jaan"), ("\u0e09", "chor ching"),
    ("\u0e0a", "chor chang"), ("\u0e0b", "sor so"), ("\u0e0c", "chor choe"),
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief="ridge", bd=3)
        self.card_frame.pack(pady=20)
        
        self.consonant_label = tk.Label(self.card_frame, text="", font=("Arial", 50))
        self.consonant_label.pack(expand=True)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack()
        
        self.current_card = None
        self.show_new_card()
    
    def show_new_card(self):
        self.current_card = random.choice(thai_consonants)
        self.consonant_label.config(text=self.current_card[0])
        self.flipped = False
    
    def flip_card(self):
        if self.current_card:
            if not self.flipped:
                self.consonant_label.config(text=self.current_card[1])
            else:
                self.consonant_label.config(text=self.current_card[0])
            self.flipped = not self.flipped
    
    def next_card(self):
        self.show_new_card()

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()