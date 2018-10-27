import tkinter as tk
    
def write_slogan(num):
    print("Boton ", num)

# configuracion de ventana
root = tk.Tk()
root.geometry("250x250")
frame = tk.Frame(root)
frame.pack()

#creacion de matriz de botones
i=0
fila = 30
for f in range(8):
    columna = 1
    for c in range(8): 
        fondo = "white"       
        if i==2 or i==4 or i==7 or i==9 or i==21 or i==22 or i==24 or i==26 or i==28 or i==38 or i==40 or i==44 or i==47 or i==53 or i==57 or i==58:
            fondo = "black"        
        slogan = tk.Button(frame, width=2, height=1, bg = fondo, command = lambda idx = i: write_slogan(idx))
        slogan.grid(row=fila, column=columna)
        columna+=1
        i+=1
    fila+=30




# button = tk.Button(frame, width=2, height=1, bg = "black", command=quit)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame, text="Hi", command = lambda idx = 4: write_slogan(idx))
# slogan.pack(side=tk.LEFT)

root.mainloop()