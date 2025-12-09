import tkinter as tk
# aqui definimos las funciones 
def mostrar_ventana2():
    ventana1.withdraw()#oculte pantalla 1
    ventana2.deiconify()#muestre panatalla 2
    
def regresar():
    ventana2.withdraw()#oculta ventana2
    ventana1.deiconify()# muestra ventana1

# creacion de ventana 1 
ventana1 = tk.Tk()
label1 =tk.Label(ventana1, text="estas en mi ventana 1 ")
ventana1.geometry("600x400")
label1.pack()
btn1=tk.Button(ventana1,text="ir a ventana 2",command=mostrar_ventana2)
btn1.pack()

#creacion de la ventana 2
ventana2 = tk.Tk()
label2 =tk.Label(ventana2, text="estas en mi ventana 2 ")
ventana2.geometry("600x400")
label2.pack()
btn2=tk.Button(ventana2,text="ir a ventana 1",command=regresar)
btn2.pack()

ventana2.withdraw()

#creacion de la ventana 
ventana1.mainloop()
