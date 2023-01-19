from percolation import Percolation
import numpy as np
import random
import math
                 
class PercolationStats:
    '''Classe utilizada para estimar o limiar de percolação.
    '''

    def __init__(self, shape, T):
        
        self.T = T
        
        if type(shape) == int:
            self.nlin, self.ncol = shape, shape
        elif type(shape) == tuple:
            self.nlin, self.ncol = shape[0], shape[1]
            
        self.exp = []  #lista de experimentos

        for i in range(T):
            a = Percolation(shape)
            while a.percolates() == False:
                a.open(random.randint(0, self.nlin-1), 
                       random.randint(0, self.ncol-1))
            self.exp.append(a)
                
#------------------------------------------------------------------------------
                
    def no_abertos(self):
        lista = []
        
        for i in range(self.T):
            lista.append(self.exp[i].no_open())
            
        return np.array(lista)
    
#------------------------------------------------------------------------------
        
    def mean(self):
        
        T = self.T
        no_sitios = self.nlin * self.ncol * T
        soma_abertos = 0
        array_abertos = self.no_abertos()
        
        for i in range(T):
            soma_abertos += array_abertos[i]
            
        return soma_abertos/no_sitios
    
#------------------------------------------------------------------------------
        
    def stddev(self):
        
        x_barra = self.mean()
        no_sitios = self.nlin * self.ncol
        T = self.T
        soma = 0
        
        for i in range(T):
            x_i = self.exp[i].no_open() / no_sitios  #limiar no experimento i
            dif = (x_i - x_barra)
            dif = dif**2
            soma += dif
            
        return (soma/(T - 1))**(1/2)
    
#------------------------------------------------------------------------------
        
    def confidenceLow(self):
        
        x_barra = self.mean()
        s = self.stddev()
        raiz_T = math.sqrt(self.T)
        
        return x_barra - (1.96*s/raiz_T)
        
#------------------------------------------------------------------------------
        
    def confidenceHigh(self):
        
        x_barra = self.mean()
        s = self.stddev()
        raiz_T = math.sqrt(self.T)
        
        return x_barra + (1.96*s/raiz_T)