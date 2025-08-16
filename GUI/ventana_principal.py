from tkinter import ttk
import tkinter as tk


ventana_principal = tk.Tk()
ventana_principal.title("Gestión de Tranferencias")
#ventana_principal.geometry("800x500")
ventana_principal.iconbitmap("img/iconoGestor.ico")

# Dimensiones deseadas de la ventana
ancho_ventana = 1265
alto_ventana = 300

# Obtener dimensiones de la pantalla
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()

# Calcular coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

# Establecer tamaño y posición
ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

transacciones = []

# Funcion agregar Transacción
def agregarTransaccion():
    ventana_agregarMonto = tk.Toplevel(ventana_principal)
    ventana_agregarMonto.title("Agregar Monto")
    ventana_agregarMonto.geometry("175x100")
    
    def guardar_transaccion():
        entryMonto = entry_agregarMonto.get()
        entryCantidad = entry_agregarCantidad.get()
        
        try:
            monto = float(entryMonto)
            cantidad = float(entryCantidad)
            transacciones.append({"monto": monto, "cantidad": cantidad})
            print("transacciones:", transacciones)
            ventana_agregarMonto.destroy()
        except ValueError:
            tk.messagebox.showerror("ERROR", "Ingresa valores validos")
    
    #Entrada Agregar Monto
    lbl_agregarMonto = tk.Label(ventana_agregarMonto, text="Monto: ").grid(row = 0, column = 0, padx=15)
    entry_agregarMonto = tk.Entry(ventana_agregarMonto, width=10)
    entry_agregarMonto.grid(row=0, column=1, sticky="w") 
    
    #Entrada Agregar Cantidad
    lbl_agregarCantidad = tk.Label(ventana_agregarMonto, text="Cantidad: ").grid(row = 1, column = 0, padx=15)
    entry_agregarCantidad = tk.Entry(ventana_agregarMonto, width= 10)
    entry_agregarCantidad.grid(row=1, column=1, pady=10, sticky="w") 
    
    btn_agregarTransaccion= tk.Button(ventana_agregarMonto, text= "Agregar transacción", command=guardar_transaccion)
    btn_agregarTransaccion.grid(row=2, column=0, columnspan=2)
    
    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Labels
lbl_titulo = ttk.Label(text="Gestión de Transferencias", font=("Arial", "36"))
lbl_titulo.grid(row = 0, column = 0, columnspan=5, pady=15)

# Botones
btn_recargas = ttk.Button(ventana_principal, text="Transacción Recargas", width=35, command=agregarTransaccion)
btn_recargas.grid(row=1, column=0, padx=20, pady=25)

btn_tarjetaSimert = ttk.Button(ventana_principal, text="Transacción Tarjetas Simert", width=35, command=agregarTransaccion)
btn_tarjetaSimert.grid(row=1, column=1, padx=20, pady=25)

btn_copias = ttk.Button(ventana_principal, text="Transacción Copias", width=35, command=agregarTransaccion)
btn_copias.grid(row=1, column=2, padx=20, pady=25)

btn_productosPapeleria = ttk.Button(ventana_principal, text="Transacción Productos de Papeleria", width=35, command=agregarTransaccion)
btn_productosPapeleria.grid(row=1, column=3, padx=20, pady=25)

btn_tejidos = ttk.Button(ventana_principal, text="Transacción Tejidos", width=30, command=agregarTransaccion)
btn_tejidos.grid(row=1, column=4, padx=20, pady=25)

ventana_principal.mainloop()