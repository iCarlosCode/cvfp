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
def calcularProdutoMisto(v = (0, 0, 0), u = (0, 0, 0), w = (0, 0, 0)):
    return calcularProdutoEscalar(w, calcularProdutoVetorial(v, u))
def calcularSoma(v = (0, 0, 0), u = (0, 0, 0)):
    return (v[0] + u[0], v[1] + u[1], v[2] + u[2])
def calcularSubtração(v = (0, 0, 0), u = (0, 0, 0)):
    return (v[0] - u[0], v[1] - u[1], v[2] - u[2])
def checarParalelismo(v = (0, 0, 0), u = (0, 0, 0)):
    return (calcularProdutoVetorial(v, u) == (0, 0, 0))
def checarPerpedincularismo(v = (0, 0, 0), u = (0, 0, 0)):
    return (calcularProdutoEscalar(v, u) == 0)
def calcularMultEscalar(e = 1, v = (0, 0, 0)):
    return ((v[0]*e), (v[1]*e), (v[2]*e))

def calcular():
  coordenada1 = (coordenada1x.get(), coordenada1y.get(), coordenada1z.get())
  coordenada2 = (coordenada2x.get(), coordenada2y.get(), coordenada2z.get())
  coordenada3 = (coordenada3x.get(), coordenada3y.get(), coordenada3z.get())
  coordenada4 = (coordenada4x.get(), coordenada4y.get(), coordenada4z.get())
  
  if(modo.get() == modos[0]):
    resultado_lbl.configure(text= f'O resultado é: {obterVetorDePontos(coordenada1, coordenada2)}.')
  elif(modo.get() == modos[1]):
    resultado_lbl.configure(text= f'O resultado é: {calcularProdutoEscalar(coordenada1, coordenada2)}.')
  elif(modo.get() == modos[2]):
    resultado_lbl.configure(text= f'O resultado é: {calcularProdutoVetorial(coordenada1, coordenada2)}.')
  elif(modo.get() == modos[3]):
    resultado_lbl.configure(text= f'O resultado é: {calcularProdutoMisto(coordenada1, coordenada2, coordenada3)}.')
  elif(modo.get() == modos[4]):
    resultado_lbl.configure(text= f'O resultado é: {calcularSoma(coordenada1, coordenada2)}.')
  elif(modo.get() == modos[5]):
    resultado_lbl.configure(text= f'O resultado é: {calcularSubtração(coordenada1, coordenada2)}.')
  elif(modo.get() == modos[6]):
    resultado_lbl.configure(text= '{}, pois v x u = {}.'.format('São paralelos' if checarParalelismo(coordenada1, coordenada2) else 'Não são paralelos', calcularProdutoVetorial(coordenada1, coordenada2)))
  elif(modo.get() == modos[7]):
    resultado_lbl.configure(text= '{}, pois v • u = {}.'.format('São Perpendiculares' if checarPerpedincularismo(coordenada1, coordenada2) else 'Não são perpendiculares', calcularProdutoEscalar(coordenada1, coordenada2)))
  elif(modo.get() == modos[8]):
    resultado_lbl.configure(text= f'O resultado é: {calcularMultEscalar(coordenada4e.get(), coordenada4)}') 
  else:
    resultado_lbl.configure(text= 'Escolha um modo! :P')

def habilitarC3():
    print(modo.get())
    if (modo.get() == modos[3]):
        c3_lbl.configure(text='Preencha as coordenadas 3')
        coordenada3_entry_x.configure(state='enabled')
        coordenada3_entry_y.configure(state='enabled')
        coordenada3_entry_z.configure(state='enabled')
    else:
        c3_lbl.configure(text='Para habilitar as coordenadas 3, escolha a operação "Produto Misto"')
        coordenada3_entry_x.configure(state='disabled')
        coordenada3_entry_y.configure(state='disabled')
        coordenada3_entry_z.configure(state='disabled')

    if (modo.get() == modos[8]):
        c4_lbl.configure(text='Preencha o escalar e as coordenadas')
        c4_lbl.grid_configure(sticky='W')
        coordenada1_entry_x.configure(state='disabled')
        coordenada1_entry_y.configure(state='disabled')
        coordenada1_entry_z.configure(state='disabled')
        coordenada2_entry_x.configure(state='disabled')
        coordenada2_entry_y.configure(state='disabled')
        coordenada2_entry_z.configure(state='disabled')
        coordenada3_entry_x.configure(state='disabled')
        coordenada3_entry_y.configure(state='disabled')
        coordenada3_entry_z.configure(state='disabled')
        coordenada4_entry_e.configure(state='enabled')
        coordenada4_entry_x.configure(state='enabled')
        coordenada4_entry_y.configure(state='enabled')
        coordenada4_entry_z.configure(state='enabled')
    else:
        c4_lbl.configure(text='Para habilitar a opção abaixo, escolha a operação "Multiplicação Por Escalar"')
        c4_lbl.grid_configure(sticky='E')
        coordenada1_entry_x.configure(state='enabled')
        coordenada1_entry_y.configure(state='enabled')
        coordenada1_entry_z.configure(state='enabled')
        coordenada2_entry_x.configure(state='enabled')
        coordenada2_entry_y.configure(state='enabled')
        coordenada2_entry_z.configure(state='enabled')
        coordenada4_entry_e.configure(state='disabled')
        coordenada4_entry_x.configure(state='disabled')
        coordenada4_entry_y.configure(state='disabled')
        coordenada4_entry_z.configure(state='disabled')
    window.after(10, habilitarC3)

padding_up = 15
c1_lbl = ttk.Label(window, text = "Preencha as coordenadas 1")
c1_lbl.grid(column = 0, row = 0, columnspan = 2, padx = (5, 5), stick='E')
 
x1_lbl = ttk.Label(window, text = "X:")
x1_lbl.grid(column = 0, row = 1, sticky='E')
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
c2_lbl.grid(column = 0, row = 2, columnspan = 2, pady= (padding_up,0), padx = (5, 5), stick='E')
 
x2_lbl = ttk.Label(window, text = "X:")
x2_lbl.grid(column = 0, row = 3, sticky='E')
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

# LINHA 4
c3_lbl = ttk.Label(window, text = "Preencha as coordenadas 3")
c3_lbl.grid(column = 0, row = 4, columnspan=6, sticky='W', pady= (padding_up,0), padx = (5, 5))

#LINHA 5
x3_lbl = ttk.Label(window, text = "X:")
x3_lbl.grid(column = 0, row = 5, sticky='E')
coordenada3x = tk.IntVar()
coordenada3_entry_x = ttk.Entry(window, width = 15, textvariable = coordenada3x)
coordenada3_entry_x.grid(column = 1, row = 5)

y3_lbl = ttk.Label(window, text = "Y:")
y3_lbl.grid(column = 2, row = 5)
coordenada3y = tk.IntVar()
coordenada3_entry_y = ttk.Entry(window, width = 15, textvariable = coordenada3y)
coordenada3_entry_y.grid(column = 3, row = 5)

z3_lbl = ttk.Label(window, text = "Z:")
z3_lbl.grid(column = 4, row = 5)
coordenada3z = tk.IntVar()
coordenada3_entry_z = ttk.Entry(window, width = 15, textvariable = coordenada3z)
coordenada3_entry_z.grid(column = 5, row = 5)

# LINHA 6
c4_lbl = ttk.Label(window, text = "Preencha as coordenadas 4")
c4_lbl.grid(column = 0, row = 6, columnspan=6, sticky='E', pady= (padding_up,0), padx = (5, 5))

#LINHA 7

e4_lbl = ttk.Label(window, text = "Escalar:")
e4_lbl.grid(column = 0, row = 7, padx = (5, 5), stick='E')
coordenada4e = tk.IntVar()
coordenada4_entry_e = ttk.Entry(window, width = 15, textvariable = coordenada4e)
coordenada4_entry_e.grid(column = 1, row = 7, columnspan=5, sticky='WE')

#LINHA 8
x4_lbl = ttk.Label(window, text = "X:")
x4_lbl.grid(column = 0, row = 8, sticky='E')
coordenada4x = tk.IntVar()
coordenada4_entry_x = ttk.Entry(window, width = 15, textvariable = coordenada4x)
coordenada4_entry_x.grid(column = 1, row = 8)

y4_lbl = ttk.Label(window, text = "Y:")
y4_lbl.grid(column = 2, row = 8)
coordenada4y = tk.IntVar()
coordenada4_entry_y = ttk.Entry(window, width = 15, textvariable = coordenada4y)
coordenada4_entry_y.grid(column = 3, row = 8)

z4_lbl = ttk.Label(window, text = "Z:")
z4_lbl.grid(column = 4, row = 8)
coordenada4z = tk.IntVar()
coordenada4_entry_z = ttk.Entry(window, width = 15, textvariable = coordenada4z)
coordenada4_entry_z.grid(column = 5, row = 8)

#LINHA 9
escolha_lbl = ttk.Label(window, text = "Escolha uma operação:")
escolha_lbl.grid(column = 0, row = 9, columnspan = 2, pady= (padding_up,0), padx = (5, 5), stick='E')

modo = tk.StringVar()
modos = ('Vetor por dois pontos','Produto Escalar','Produto Vetorial', 'Produto Misto', 'Soma', 'Subtração', 'Checar se são paralelos', 'Checar se são perpendiculares', 'Multiplicação Por Escalar')
modos_cb = ttk.Combobox(window, width = 15 , textvariable = modo)
modos_cb['values'] = modos
modos_cb.grid(column = 2, row = 9, columnspan=5, sticky='WE', pady= (padding_up,0), padx = (5, 5))

#LINHA 10
resultado_lbl = ttk.Label(window, text = "")
resultado_lbl.grid(column = 0, row = 10, columnspan=3, sticky='E', pady= (padding_up-5,0), padx = (5, 5))

calcular_btn = ttk.Button(window, text = "Calcular", command = calcular)
calcular_btn.grid(column= 3, row = 10, columnspan=3, sticky='WE', pady= (padding_up-5,0), padx = (5, 5))

window.after(10, habilitarC3)
window.mainloop()
