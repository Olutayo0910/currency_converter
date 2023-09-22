#!/usr/bin/python3
from tkinter import Tk, ttk
from tkinter import *
import requests
import json

#colors
cor0 = "#FFFFFF" # white
cor1 = "#333333" # black
cor2 = "#EB5D51" # red

window = Tk()
window.geometry('300x320')
window.title('Converter')
window.configure(bg=cor0)
window.resizable(height=FALSE, width=FALSE)


top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)


main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    # Define a dictionary to map currency codes to symbols
    currency_symbols = {
        'USD': '$',
        'AED': 'د.إ',  # United Arab Emirates Dirham
        'AUD': 'A$',  # Australian Dollar
        'BRL': 'R$',  # Brazilian Real
        'CAD': 'C$',  # Canadian Dollar
        'CHF': 'CHF',  # Swiss Franc
        'CNY': '¥',  # Chinese Yuan
        'EUR': '€',  # Euro
        'GBP': '£',  # British Pound Sterling
        'HKD': 'HK$',  # Hong Kong Dollar
        'INR': '₹',  # Indian Rupee
        'JPY': '¥',  # Japanese Yen
        'KRW': '₩',  # South Korean Won
        'MXN': 'Mex$',  # Mexican Peso
        'NGN': '₦',  # Nigerian Naira
        'NZD': 'NZ$',  # New Zealand Dollar
        'RUB': '₽',  # Russian Ruble
        'TRY': '₺',  # Turkish Lira
        'ZAR': 'R',  # South African Rand
        'SEK': 'kr',  # Swedish Krona
        'NOK': 'kr',  # Norwegian Krone
        'DKK': 'kr',  # Danish Krone
        'SGD': 'S$',  # Singapore Dollar
        'MYR': 'RM',  # Malaysian Ringgit
        'IDR': 'Rp',  # Indonesian Rupiah
        'THB': '฿',  # Thai Baht
        'SAR': '﷼',  # Saudi Riyal
        'QAR': '﷼',  # Qatari Riyal
        'EGP': '£',  # Egyptian Pound
        # Add more currencies and symbols as needed
    }

    # Check if currency_2 is in the dictionary, and if so, assign the symbol
    symbol = currency_symbols.get(currency_2, '')

    # If currency_2 is not found in the dictionary, symbol will be an empty string

    headers = {
        "X-RapidAPI-Key": "a2c1afb430mshf70b4fc77aade4dp18b7c6jsnc78446223cda",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)

    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result['text'] = formatted

    print(converted_amount, formatted)


# top frame

app_name = Label(top,
                 compound=LEFT,
                 text="Currency Converter",
                 height=1,
                 padx=40,
                 pady=10,
                 anchor=CENTER,
                 font=("Arial", 16, "bold"),
                 bg=cor2,
                 fg=cor0,

                 )
app_name.place(x=0, y=0)

result = Label(main,
               text=" ",
               width=16,
               height=2,
               pady=7,
               anchor=CENTER,
               font=("Ivy", 16, "bold"),
               bg=cor0,
               fg=cor1,
               relief="solid"
            )
result.place(x=50, y=10)

from_label = Label(main,
               text="From",
               width=8,
               height=1,
               pady=0,
               padx=0,
               anchor=CENTER,
               font=("Ivy", 10, "bold"),
               bg=cor0,
               fg=cor1,
               relief="flat"
            )
from_label.place(x=48, y=90)

currency = [
    'USD',    # United States Dollar
    'AED',    # United Arab Emirates Dirham
    'AUD',    # Australian Dollar
    'BRL',    # Brazilian Real
    'CAD',    # Canadian Dollar
    'CHF',    # Swiss Franc
    'CNY',    # Chinese Yuan
    'EUR',    # Euro
    'GBP',    # British Pound Sterling
    'HKD',    # Hong Kong Dollar
    'INR',    # Indian Rupee
    'JPY',    # Japanese Yen
    'KRW',    # South Korean Won
    'MXN',    # Mexican Peso
    'NGN',    # Nigerian Naira
    'NZD',    # New Zealand Dollar
    'RUB',    # Russian Ruble
    'TRY',    # Turkish Lira
    'ZAR',    # South African Rand
    'SEK',    # Swedish Krona
    'NOK',    # Norwegian Krone
    'DKK',    # Danish Krone
    'SGD',    # Singapore Dollar
    'MYR',    # Malaysian Ringgit
    'IDR',    # Indonesian Rupiah
    'THB',    # Thai Baht
    'SAR',    # Saudi Riyal
    'QAR',    # Qatari Riyal
    'EGP',    # Egyptian Pound
    # Add more currencies as needed
]

combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy", 12, "bold"))
combo1['values'] = currency
combo1.place(x=50, y=115)

to_label = Label(main,
               text="To",
               width=8,
               height=1,
               pady=0,
               padx=0,
               anchor=CENTER,
               font=("Ivy", 10, "bold"),
               bg=cor0,
               fg=cor1,
               relief="flat"
            )

to_label.place(x=160, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy", 12, "bold"))
combo2['values'] = currency
combo2.place(x=165, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Ivy", 12, "bold"), relief="solid")
value.place(x=50, y=155)

button = Button(main, text="Converter", width=19, padx=5, height=1, bg=cor2, fg=cor0, font=("Ivy", 12, "bold"), command = convert)
button.place(x=50, y=210)

window.mainloop()

