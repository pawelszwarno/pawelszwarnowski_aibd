# Pawel Szwarnowski - rysowanie wykresow funkcji kwadratowej w zadanym przedziale
import matplotlib.pyplot as plt
import numpy as np

def sqr_func(x):
	return x**2+5

def show_sqr_func_for_x_in_range(x_min,x_max,step=100):
	x_lst = np.linspace(x_min,x_max,step,endpoint=False)
	y_lst = [sqr_func(x) for x in x_lst]
	plt.plot(x_lst,y_lst)
	plt.xlabel('oś x')
	plt.ylabel('oś y')
	plt.legend(labels=["przebieg"])
	plt.title(f"Wykres funkcji x^2+5 w przedziale: {x_min} {x_max}")
	plt.show()


show_sqr_func_for_x_in_range(-1,1,100)
show_sqr_func_for_x_in_range(-6,6,100)
show_sqr_func_for_x_in_range(0,5,100)
