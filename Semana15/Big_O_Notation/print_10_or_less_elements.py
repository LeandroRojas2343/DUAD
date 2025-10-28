def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index]) 
		
    
#Complejidad: O(1)
#Crecimiento: Constante 
#Explicacion: Maximo 10 iteraciones, independiente del tamaño de la lista. 

		