import requests as r
import tkinter as tk
from tkinter import ttk

# Fetch data from the API
supriti = r.get('https://newsapi.org/v2/everything?q=tesla&from=2025-02-05&sortBy=publishedAt&apiKey=1613ce0ed54744078f27cba62aa91796')
jsdata = supriti.json()['articles']

# Initialize the Tkinter window
root = tk.Tk()
root.title('InstaNews')
root.geometry("600x800")

# Function to create a news card
def create_news_card(parent, headline, date, summary):
    # Create a frame for the card
    card_frame = tk.Frame(parent, bg="white", width=350, height=250, relief="solid", bd=2)
    card_frame.grid_propagate(False)  # Prevent resizing the frame based on contents

    # Add a headline (title) to the card
    headline_label = tk.Label(card_frame, text=headline, font=("Helvetica", 14, "bold"), bg="white", wraplength=320)
    headline_label.grid(row=0, column=0, pady=(10, 5), padx=10)

    # Add the date of publication to the card
    date_label = tk.Label(card_frame, text=date, font=("Helvetica", 10, "italic"), bg="white")
    date_label.grid(row=1, column=0, pady=(0, 5), padx=10)

    # Add a summary (brief description) to the card
    summary_label = tk.Label(card_frame, text=summary, font=("Helvetica", 11), bg="white", wraplength=320)
    summary_label.grid(row=2, column=0, pady=(0, 10), padx=10)

    return card_frame

# Header label
label = tk.Label(root, 
                 text="InstaNews App",
                 anchor=tk.CENTER,       
                 bg="lightblue",      
                 height=3,              
                 width=30,              
                 bd=3,                   
                 font=("Arial", 16, "bold"), 
                 cursor="hand2",   
                 fg="red",             
                 padx=15,               
                 pady=15,                
                 justify=tk.CENTER,    
                 relief=tk.RAISED,     
                 underline=0,           
                 wraplength=250         
                )

# Create a frame for the scrollbar and canvas
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Add a scrollbar to the frame
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a canvas to hold the news cards
canvas = tk.Canvas(frame, bg="lightgray", yscrollcommand=scrollbar.set)
canvas.pack(fill=tk.BOTH, expand=True)

# Link scrollbar with canvas
scrollbar.config(command=canvas.yview)

# Create a frame to place on the canvas to hold the news cards
cards_frame = tk.Frame(canvas, bg="lightgray")
canvas.create_window((0, 0), window=cards_frame, anchor="nw")

# Update the scroll region whenever the cards are added
def update_scroll_region():
    cards_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Place news cards using the grid system
row = 0  # Initial row for placing the news cards
for article in jsdata:
    headline = article.get("title", "No Title")
    date = article.get("publishedAt", "No Date")
    summary = article.get("description", "No Description")
    
    # Create and place each card using grid
    news_card = create_news_card(cards_frame, headline, date, summary)
    news_card.grid(row=row, column=0, pady=20, padx=10)  # Place the card in the grid
    row += 1  # Increment the row for the next card

# Update the scroll region to make sure the canvas scrolls correctly
update_scroll_region()

# Pack the header label
label.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
