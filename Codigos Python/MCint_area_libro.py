import random
import time
import numpy as np
import matplotlib.pyplot as plt

title_font = {'fontname':'Roboto', 'size':'14', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Roboto', 'size':'12', 'color':'blue'}


def MCint_area(f, a, b, n, m):
    below = 0  # counter for no of points below the curve
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            below += 1
    area = below/float(n)*m*(b-a)
    return area



def MCint_area_vec(f, a, b, n, m):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, m, n)
    below = np.sum(y < f(x))
    area = below/float(n)*m*(b-a)
    return area

def MCint3_area(f, a, b, n, m, N=1000):
    # Store every N intermediate integral approximations in an
    # array I and record the corresponding k value.
    I_values = []
    k_values = []
    valor_xabajo=[]
    valor_yabajo=[]
    valor_xarriba=[]
    valor_yarriba=[]
    below = 0  # counter for no of points below the curve
    for k in range(1, n+1):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            below += 1
            valor_xabajo.append(x)
            valor_yabajo.append(y)
        else: 
            valor_xarriba.append(x)
            valor_yarriba.append(y)
        area = below/float(k)*m*(b-a)
        if k % N == 0:
            I = area
            I_values.append(I)
            k_values.append(2*k)
            
    return k_values, I_values, valor_xabajo, valor_yabajo, \
            valor_xarriba, valor_yarriba


def f1(x):
    return 2 + 3*x

a = 1; b = 2; n = 1000000; N = 10000; fmax = f1(b)

t0 = time.clock()
print (MCint_area(f1, a, b, n, fmax))
t1 = time.clock()
print (MCint_area_vec(f1, a, b, n, fmax))
t2 = time.clock()
print ('fraccion bucle/vectorizado', (t1 - t0)/(t2 - t1))

k, I, xabajo, yabajo, xarriba, yarriba = MCint3_area(f1, a, b, n, fmax, N)

print (I[-1])
#from scitools.std import plot
error = 6.5 - np.array(I)

x = np.linspace(a,b,100)
plt.plot(x, f1(x))
plt.plot(xarriba, yarriba, '^g')    
plt.plot(xabajo, yabajo, '+r')
plt.xlim([1,2])
#plt.plot(k, error)
#plt.title('Error estimado contra el valor exacto', **title_font)
#plt.ylabel('Error', **axis_font)
#plt.xlabel('Número de muestras', **axis_font)
#plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

plt.title('Gráfica incorporando $n=10^{6}$ puntos aleatorios', **title_font)
plt.xlabel('Eje x', **axis_font)
plt.ylabel('Función $f(x)$', **axis_font)
plt.show()
