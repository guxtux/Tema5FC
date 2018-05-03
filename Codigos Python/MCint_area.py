import random
import time
import numpy as np
import matplotlib.font_manager as font_manager

#font_path = 'C:\Windows\Fonts\consola.ttf'
#font_prop = font_manager.FontProperties(fname=font_path, size=12)

def MCint_area(f, a, b, n, m):
    porDebajo = 0  
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            porDebajo += 1
    area = porDebajo/float(n)*m*(b-a)
    return area


def MCint_area_vec(f, a, b, n, m):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, m, n)
    porDebajo = np.sum(y < f(x))
    area = porDebajo/float(n)*m*(b-a)
    return area

def MCint3_area(f, a, b, n, m, N=1000):
    
    I_valores = []
    k_valores = []
    porDebajo = 0
    
    for k in range(1, n+1):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        
        if y <= f(x):
            porDebajo += 1
        
        area = porDebajo/float(k)*m*(b-a)
        
        if k % N == 0:
            I = area
            I_valores.append(I)
            k_valores.append(2*k)
    
    return k_valores, I_valores


def f1(x):
    return 2 + 3*x

a = 1; b = 2; n = 1000000; N = 10000; fmax = f1(b)

t0 = time.clock()
print (MCint_area(f1, a, b, n, fmax))
t1 = time.clock()
print (MCint_area_vec(f1, a, b, n, fmax))
t2 = time.clock()
print ('fraccion bucle/vectorizada:', (t1-t0)/(t2-t1))

k, I = MCint3_area(f1, a, b, n, fmax, N)
print (I[-1])

error = 6.5 - np.array(I)

plt.plot(k, error)
plt.xlabel('Número de muestras')
plt.ylabel('Error')
plt.title('Integración Monte Carlo por puntos')
plt.axhline(y=0, color = 'k')
plt.savefig('integracionPuntos.eps')
plt.show()
