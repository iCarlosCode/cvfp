import tkinter as tk
from tkinter import ttk
 
 
window = tk.Tk()
 
window.title("Calculadora Vetorial Feita às Pressas")
window.maxsize(600,1000)
window.resizable(0,0)

def obterVetorDePontos(dotA = (0, 0, 0), dotB = (0, 0, 0)):
    return (dotB[0] - dotA[0], dotB[1] - dotA[1], dotB[2] - dotA[2])

def calcularProdutoEscalar(v = (0, 0, 0), u = (0, 0, 0)):
    return ((v[0]*u[0]) + (v[1]*u[1]) + (v[2]*u[2]))

def calcularProdutoVetorial(v = (0, 0, 0), u = (0, 0, 0)):
    return (((v[1] * u[2]) - (v[2] * u[1])), ((v[2] * u[0]) - (v[0] * u[2])), ((v[0] * u[1]) - (v[1] * u[0])))

def calcular():
  coordenada1 = (coordenada1x.get(), coordenada1y.get(), coordenada1z.get())
  coordenada2 = (coordenada2x.get(), coordenada2y.get(), coordenada2z.get())
  
  if(modo.get() == 'Vetor por dois pontos'):
    resultado_lbl.configure(text= f'O resultado é: {obterVetorDePontos(coordenada1, coordenada2)}.')
  elif(modo.get() == 'Produto Escalar'):
    resultado_lbl.configure(text= f'O resultado é: {calcularProdutoEscalar(coordenada1, coordenada2)}.')
  elif(modo.get() == 'Produto Vetorial'):
    resultado_lbl.configure(text= f'O resultado é: {calcularProdutoVetorial(coordenada1, coordenada2)}.')
  else:
    resultado_lbl.configure(text= 'Escolha um modo! :P')
 
c1_lbl = ttk.Label(window, text = "Preencha as coordenadas 1")
c1_lbl.grid(column = 0, row = 0)
 
x1_lbl = ttk.Label(window, text = "X:")
x1_lbl.grid(column = 0, row = 1)
coordenada1x = tk.IntVar()
coordenada1_entry_x = ttk.Entry(window, width = 15, textvariable = coordenada1x)
coordenada1_entry_x.grid(column = 1, row = 1)

y1_lbl = ttk.Label(window, text = "Y:")
y1_lbl.grid(column = 2, row = 1)
coordenada1y = tk.IntVar()
coordenada1_entry_y = ttk.Entry(window, width = 15, textvariable = coordenada1y)
coordenada1_entry_y.grid(column = 3, row = 1)

z1_lbl = ttk.Label(window, text = "Z:")
z1_lbl.grid(column = 4, row = 1)
coordenada1z = tk.IntVar()
coordenada1_entry_z = ttk.Entry(window, width = 15, textvariable = coordenada1z)
coordenada1_entry_z.grid(column = 5, row = 1)
 
# LINHA DOIS
c2_lbl = ttk.Label(window, text = "Preencha as coordenadas 2")
c2_lbl.grid(column = 0, row = 2)
 
x2_lbl = ttk.Label(window, text = "X:")
x2_lbl.grid(column = 0, row = 3)
coordenada2x = tk.IntVar()
coordenada2_entry_x = ttk.Entry(window, width = 15, textvariable = coordenada2x)
coordenada2_entry_x.grid(column = 1, row = 3)

y2_lbl = ttk.Label(window, text = "Y:")
y2_lbl.grid(column = 2, row = 3)
coordenada2y = tk.IntVar()
coordenada2_entry_y = ttk.Entry(window, width = 15, textvariable = coordenada2y)
coordenada2_entry_y.grid(column = 3, row = 3)

z2_lbl = ttk.Label(window, text = "Z:")
z2_lbl.grid(column = 4, row = 3)
coordenada2z = tk.IntVar()
coordenada2_entry_z = ttk.Entry(window, width = 15, textvariable = coordenada2z)
coordenada2_entry_z.grid(column = 5, row = 3)

escolha_lbl = ttk.Label(window, text = "Escolha uma operação:")
escolha_lbl.grid(column = 0, row = 4)

calcular_btn = ttk.Button(window, text = "Calcular", command = calcular)
calcular_btn.grid(column= 1, row = 4)

modo = tk.StringVar()
modos_cb = ttk.Combobox(window, width = 15 , textvariable = modo)
modos_cb['values'] = ('Vetor por dois pontos','Produto Escalar','Produto Vetorial')
modos_cb.grid(column = 2, row = 4, columnspan=4, sticky='WE')

resultado_lbl = ttk.Label(window, text = "")
resultado_lbl.grid(column = 0, row = 5)

window.mainloop()
