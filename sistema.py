# Ler o arquivo CSV usando Pandas.
# Processar os dados usando NumPy.
# Gerar gráficos usando Matplotlib.
# Exibir a interface gráfica com Tkinter.
# Crie 5 botões 
# Em cada botão precisa mostrar um tipo de grafico
# Mostre a estatistica também

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

canvas = None
estatisticas = None

def grafico_1():
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    dados = pd.read_csv('dados.csv')

    vendedores = dados['vendedor'].values
    vendas = dados['vendas'].values

    fig, grafico = plt.subplots()
    grafico.plot(vendedores, vendas, marker='o', linestyle='-', color='b')

    grafico.set_xlabel('Vendedores')
    grafico.set_ylabel('Vendas')
    grafico.set_title('Vendas por Vendedor')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def grafico_2():
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    dados = pd.read_csv('dados.csv')

    vendedores = dados['vendedor'].values
    vendas = dados['vendas'].values

    fig, grafico = plt.subplots()
    grafico.bar(vendedores, vendas)

    grafico.set_xlabel('Vendedores')
    grafico.set_ylabel('Vendas')
    grafico.set_title('Vendas por Vendedor')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def grafico_3():
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    dados = pd.read_csv('dados.csv')

    vendedores = dados['vendedor'].values
    vendas = dados['vendas'].values

    fig, grafico = plt.subplots()
    grafico.pie(vendas, labels=vendedores, autopct='%1.1f%%')

    grafico.set_title('Vendas por Vendedor')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def grafico_4():
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    dados = pd.read_csv('dados.csv')

    vendedores = dados['vendedor'].values
    vendas = dados['vendas'].values

    fig, grafico = plt.subplots()
    grafico.scatter(vendedores, vendas)

    grafico.set_xlabel('Vendedores')
    grafico.set_ylabel('Vendas')
    grafico.set_title('Vendas por Vendedor')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def grafico_5():
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    dados = pd.read_csv('dados.csv')

    vendedores = dados['vendedor'].values
    vendas = dados['vendas'].values

    fig, grafico = plt.subplots()
    grafico.hist(vendas, bins=20, color='b')

    grafico.set_xlabel('Vendas')
    grafico.set_ylabel('Frequência')
    grafico.set_title('Vendas por Vendedor')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)



janela = tk.Tk()
janela.geometry('800x600')
janela.title('Gráfico de Vendas')

frame = tk.Frame(janela)
frame.pack(side=tk.TOP, fill=tk.X, expand=True)

botao1 = tk.Button(frame, text='Grafico de Linhas', command=grafico_1)
botao1.pack(side=tk.TOP, padx=10)

botao2 = tk.Button(frame, text='Grafico de Barras', command=grafico_2)
botao2.pack(side=tk.TOP, padx=10)

botao3 = tk.Button(frame, text='Grafico de pizza', command=grafico_3)
botao3.pack(side=tk.TOP, padx=10)

botao4 = tk.Button(frame, text='Grafico de dispersao', command=grafico_4)
botao4.pack(side=tk.TOP, padx=10)

botao5 = tk.Button(frame, text='Grafico de Histograma', command=grafico_5)
botao5.pack(side=tk.TOP, padx=10)

dados = pd.read_csv('dados.csv')
np_vendas = np.array(dados['vendas'])

maior = np.max(np_vendas)
menor = np.min(np_vendas)
media = np.mean(np_vendas)
mediana = np.median(np_vendas)
desvio_padrao = np.std(np_vendas)

estatisticas = tk.Label(janela, text=f"Maior: {maior}\nMenor: {menor}\nMedia: {media}\nMediana: {mediana}\nDesvio Padrao: {desvio_padrao}")
estatisticas.pack(side=tk.RIGHT, padx=10)

janela.mainloop()


