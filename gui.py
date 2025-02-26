import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_faq_answer  # Ensure chatbot.py is in the same folder

def on_send_click():
    # Get input from the user
    user_input = user_input_field.get()
    print("DEBUG: User input:", user_input)  # Debug print in the console
    if user_input.strip():  # Only proceed if input is not empty
        # Enable chat_display to update it
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "You: " + user_input + "\n")
        try:
            # Get the answer from the chatbot logic
            answer = get_faq_answer(user_input)
        except Exception as e:
            answer = "Error occurred: " + str(e)
        chat_display.insert(tk.END, "Bot: " + answer + "\n\n")
        # Disable editing of chat_display again
        chat_display.config(state=tk.DISABLED)
        # Clear the input field and scroll to the bottom
        user_input_field.delete(0, tk.END)
        chat_display.yview(tk.END)
    else:
        print("DEBUG: No input provided.")

# Create the main window
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("450x550")

# Create a scrolled text area to display the conversation
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED, font=("Arial", 10))
chat_display.pack(padx=10, pady=10)

# Create an entry widget for user input
user_input_field = tk.Entry(root, width=35, font=("Arial", 12))
user_input_field.pack(padx=10, pady=10)

# Create a send button to trigger the on_send_click function
send_button = tk.Button(root, text="Send", width=15, height=2, font=("Arial", 12), bg="lightblue", command=on_send_click)
send_button.pack(padx=10, pady=10)

# Insert an initial greeting from the bot
chat_display.config(state=tk.NORMAL)
chat_display.insert(tk.END, "Bot: Hello, how can I help you?\n\n")
chat_display.config(state=tk.DISABLED)

# Start the Tkinter event loop
root.mainloop()
