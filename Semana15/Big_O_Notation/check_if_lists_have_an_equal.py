def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False


#Complejidad: O(n x m)
#Crecimiento: Cuadratico 
#Explicacion: Dos bucles anidados, compara cada elemento de una lista con los de la otra. 

