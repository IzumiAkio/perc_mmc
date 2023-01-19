import numpy as np

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

class Percolation:
    '''
    Representa uma grade com todos os sítios inicialmente bloqueados.
    '''
    def __init__(self, shape):
        
        if type(shape) == int:
            array = []
            lin = [BLOCKED] * shape
            for i in range(shape):
                array.append(lin[:])
            self.grade = np.array(array)
            self.shape = (shape, shape)
        else:
            array =[]
            lin = [BLOCKED] * shape[1]
            for i in range(shape[0]):
                array.append(lin[:])
            self.grade = np.array(array)
            self.shape = shape
            
#-------------------------------------------------------------------------- 
            
    def __str__(self):
        
        s = ''
        ref = self.get_list() #contem os simbolos [' ', 'o', 'x'] nas posicoes
        n_lin = len(ref)
        n_col = len(ref[0])
        
        
        for i in range(n_lin):
            for j in range(n_col):
                if self.grade[i][j] == BLOCKED:
                    ref[i][j] = ' '
                elif self.grade[i][j] == OPEN:
                    ref[i][j] = 'o'
                elif self.grade[i][j] == FULL:
                    ref[i][j] = 'x'
        
        
        for i in range(n_lin):
            s += '+'
            s += '---+' * n_col
            s += '\n|'
            for j in range(n_col):
                s += f' {ref[i][j]} |'
            s += '\n'
               
        s += '+'
        s += '---+' * n_col
        s += '\n'
        
        
        s += f'grade de dimensão: {self.shape[0]}x{self.shape[1]}\n'
        s += f'no. sítios abertos: {self.no_open()}\n'
        s += f'percolou: {self.percolates()}'
        
        return s

#-------------------------------------------------------------------------- 
        
    def is_open(self, lin, col):
        
        if lin not in range(self.shape[0]) or col not in range(self.shape[1]):
            print(f'is_open() : posição [{lin},{col}] está fora da grade')
            return None
        
        return self.grade[lin][col] == OPEN or self.grade[lin][col] == FULL
    
#-------------------------------------------------------------------------- 
        
    def is_full(self, lin, col):
        
        if lin not in range(self.shape[0]) or col not in range(self.shape[1]):
            print(f'is_full() : posição [{lin},{col}] está fora da grade')
            return None
            
        return self.grade[lin][col] == FULL
    
#-------------------------------------------------------------------------- 
        
    def percolates(self):
        
        for i in range(self.shape[0]):
            if FULL not in self.grade[i]:
                return False
            
        return True
    
#-------------------------------------------------------------------------- 
    
    def no_open(self):
        cont = 0
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.grade[i][j] == OPEN or self.grade[i][j] == FULL:
                    cont += 1
                    
        return cont
    
#-------------------------------------------------------------------------- 
        
    def open(self, lin, col):
        
        if lin not in range(self.shape[0]) or col not in range(self.shape[1]):
            print(f'open() : posição [{lin},{col}] está fora da grade')
            return None
        
        
        self.grade[lin][col] = OPEN      # abre a posicao escolhida
        nlin = self.shape[0]
        ncol = self.shape[1]
        fila = []
        
        for j in range(ncol):            # preenche a primeira linha
            if self.is_open(0, j):
                self.grade[0][j] = FULL
                fila.append([0, j])
            elif self.is_full(0,j):
                fila.append([0,j])
                
        for i in range(nlin):            # reseta os FULL para OPEN
            for j in range(ncol):
                if self.grade[i][j] == FULL:
                    self.grade[i][j] = OPEN
                
        
        while fila != []:                # processa todos os OPEN
            sitio = fila.pop(0)
            s_lin = sitio[0]
            s_col = sitio[1]
            
            DOWN = min(s_lin + 1, nlin - 1)
            UP = max(s_lin - 1, 0)
            LEFT = max(s_col - 1, 0)
            RIGHT = min(s_col + 1, ncol - 1)
            
            #-----------------------------------------
            
            if self.grade[DOWN , s_col] == OPEN:
                self.grade[DOWN, s_col] = FULL
                fila.append([DOWN, s_col])
                
            if self.grade[UP, s_col] == OPEN:
                self.grade[UP, s_col] = FULL
                fila.append([UP, s_col])
                
            if self.grade[s_lin, LEFT] == OPEN:
                self.grade[s_lin, LEFT] = FULL
                fila.append([s_lin, LEFT])
                
            if self.grade[s_lin, RIGHT] == OPEN:
                self.grade[s_lin, RIGHT] = FULL
                fila.append([s_lin, RIGHT])
    
            #-----------------------------------------
            
            
            
#-------------------------------------------------------------------------- 
    
    def get_grid(self):
        
        clone = []
        
        for i in range(self.shape[0]):
            linha = []
            for j in range(self.shape[1]):
                linha.append(self.grade[i][j])
            clone.append(linha)
            
        return np.array(clone)
    
#--------------------------------------------------------------------------
        
    def get_list(self):
        
        clone = []
        
        for i in range(self.shape[0]):
            linha = []
            for j in range(self.shape[1]):
                linha.append(self.grade[i][j])
            clone.append(linha)
            
        return clone