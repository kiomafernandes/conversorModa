from tkinter import *
from tkinter import Tk, ttk
import requests
import json
import string


#cores

branco = '#FFFFFF'
preto = '#333333'
azulEscuro = '#38576b'

#janela

janela = Tk()
janela.geometry('300x320')
janela.title('Conversor de moeda')
janela.config(bg=branco)

style = ttk.Style(janela)
style.theme_use('clam')
janela.resizable(width=FALSE, height=FALSE)


#Função
def converter():
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrada = valor.get()

    response = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
    dados = json.loads(response.text)
    cambio = dados['rates'][moeda_para]
    resultado = float(valor_entrada) * float(cambio)

    if moeda_para == 'USD':
        simbolo = '$'
    elif moeda_para == 'EUR':
        simbolo = '€'
    elif moeda_para == 'INR':
        simbolo = '₹'
    elif moeda_para == 'BRL':
        simbolo = 'R$'
    else:
        simbolo = 'Kz'

    moeda_equivalente = simbolo + '{:,.2f}'.format(resultado)
    app_conversor['text'] = moeda_equivalente


#divisão da janela

frame_titulo = Frame(janela, width=300, height=60, padx=0, pady=0, bg=azulEscuro, relief='flat')
frame_titulo.grid(row=0, column=0, columnspan=2)
frame_corpo = Frame(janela, width=300, height=260, padx=0, pady=5, bg=branco, relief='flat')
frame_corpo.grid(row=1, column=0, sticky=NSEW)

app_nome = Label(frame_titulo, text=' $ Conversor de Moedas € ', height=5, pady=20, padx=13, relief=RAISED, anchor=NW, font='Ivy 16 bold', bg=azulEscuro, fg=branco)
app_nome.place(x=0, y=0)

app_conversor = Label(frame_corpo, text='', width=16, height=2, relief='solid', anchor=CENTER, font='Ivy 15 bold', bg=branco, fg=preto)
app_conversor.place(x=50, y=10)

moeda = ['USD', 'BRL', 'EUR', 'INR', 'AOA']

app_de = Label(frame_corpo, text='De', width=8, height=2, relief='flat', anchor=NW, font='Ivy 10 bold', bg=branco, fg=preto)
app_de.place(x=48, y=90)
combo_de = ttk.Combobox(frame_corpo, width=8, justify=CENTER,font=('Ivy 12 bold'))
combo_de.place(x=50, y=115)
combo_de['values'] = (moeda)

app_para = Label(frame_corpo, text='Para', width=8, height=2, relief='flat', anchor=NW, font='Ivy 10 bold', bg=branco, fg=preto)
app_para.place(x=158, y=90)
combo_para = ttk.Combobox(frame_corpo, width=8, justify=CENTER,font=('Ivy 12 bold'))
combo_para.place(x=160, y=115)
combo_para['values'] = (moeda)

valor = Entry(frame_corpo, width=22, justify=CENTER,font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50, y=155)

botao = Button(frame_corpo, command=converter, text='Converter', width=19, padx=5, height=1, bg=azulEscuro, fg=branco, font=('Ivy 12 bold'), relief='raised', overrelief=RIDGE)
botao.place(x=50, y=210)


janela.mainloop()
