menu = [ "Baleadas", "Pollo", "Tacos ", "Pizza" ]

def  imprimir_menu ():
	print( "Listar Menu")
	print( "2 Agregar Pedido")
	print( "3 Imprimir Pedido")
	print ( "4 Salir")
	valor =  input ( "Ingrese el numero de la accion que desea realizar: " )


def  Listar_menu ():
	print()
	print( " Listado de Menu " )
	for producto in  range ( len (menus)):
		print(" {0}  {1} " .format (producto.menus [producto])

def  agregar_pedido ():
	print()
	print( "Creando un pedido" )
	mesa =  entrada ( "Numero de mesa" )
	producto =  input ( "Nombre de platillo" )
	pedidos.append ("Meza No. {0} Platillo {1} " .format (mesa, producto)

def imprimir_pedidos ()
	if pedidos:
			for pedido in pedidos:
					print(pedido)
	else:
			print("No hay pedidos ingresados")

salir = True

While continuar:
	# _retornado = valor Retornado
	v_retornado  = imprimir_menu ()
	if int (v_retornado) == 1
		for producto in productos
			lista_menu()
	elsif int (v_retornado)== 2:
		agregar_pedido()
	elsif int(v_retornado) == 3:
		valor = input ("Ingrese el producto agregar:")
			imprimir_pedido(valor)
	elsif int(v_retornado) == 4:
		continuar = False
			eliminar_productos()
	else:
		print("Opcion no controlada")
