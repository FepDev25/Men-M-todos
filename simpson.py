import matplotlib.pyplot as plt

x = [1, 2, 3.25, 4.5, 6, 7, 8, 9, 9.5, 10]
y = [5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5]

plt.plot(x, y, linestyle='-', color='green', marker='o', label='Línea')  
plt.scatter(x, y, color='blue', label='Puntos') 


plt.title('Gráfica de puntos unidos con línea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()  

plt.xlim(0, max(x) + 1) 
plt.ylim(0, max(y) + 5) 

plt.grid(True)  
plt.show()
