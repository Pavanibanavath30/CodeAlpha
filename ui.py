import tkinter as tk
from chatbot import FAQChatBot

bot = FAQChatBot('C:\\Users\\Banavath Pavani\\OneDrive\Desktop\\FAQChatBot_Project\\data\\faqs.csv')

def ask_bot():
    user_input = user_entry.get()
    response = bot.get_response(user_input)
    chat_log.insert(tk.END, "You: " + user_input + '\n')
    chat_log.insert(tk.END, "Bot: " + response + '\n\n')
    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("FAQ ChatBot")

chat_log = tk.Text(root, height=20, width=50)
chat_log.pack()

user_entry = tk.Entry(root, width=40)
user_entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=ask_bot)
send_button.pack()

root.mainloop()
