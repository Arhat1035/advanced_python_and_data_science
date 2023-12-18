
# from bs4 import BeautifulSoup as BS
# import requests as req
# import tkinter


# url = "https://www.businesstoday.in/latest/economy"
 
# webpage = req.get(url)
# trav = BS(webpage.content, "html.parser")
# M = 1
# for link in trav.find_all('a'):
   

#     if(str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
#        and len(link.string) > 35):
 
#         print(str(M)+".", link.string)
#         M += 1          



import tkinter as tk
import requests

class ApiDisplay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("API Output Display")
        self.label = tk.Label(self, text="API Output will appear here")
        self.label.pack()
        self.get_data_button = tk.Button(self, text="Get API Data", command=self.get_data)
        self.get_data_button.pack()

    def get_data(self):
        response = requests.get("hhttps://www.businesstoday.in/latest/economy")
        data = response.json()
        self.label.config(text=str(data))

if __name__ == "__main__":
    app = ApiDisplay()
    app.mainloop()