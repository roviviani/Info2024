import tkinter as tk

ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200')

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Principal', menu=menu_principal)

submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label='Opciones', menu=submenu)
submenu.add_command(label='Opción 1')
submenu.add_command(label='Opción 2')

lista_menu = tk.Menu(menu_principal)
menu_principal.add_cascade(label='Lista de Menú', menu=lista_menu)
lista_menu.add_command(label='Ensalada')
lista_menu.add_command(label='Sopa')
lista_menu.add_command(label='Pasta')
lista_menu.add_command(label='Postre')

plato_principal = tk.Menu(menu_principal)
menu_principal.add_cascade(label='Plato Principal de la Casa', menu=plato_principal)
plato_principal.add_command(label='Paella')
plato_principal.add_command(label='Lasaña')
plato_principal.add_command(label='Pollo al Horno')

ventana.mainloop()

