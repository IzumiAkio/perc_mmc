import time
from percolation_stats import PercolationStats

def main():
    '''(None) -> None
    '''
    # leia a forma da grade do sistema
    n = int(input("Digite a dimensão da grade: "))
    # leia o número de experimentos
    t     = int(input("Digite o número de experimentos: "))
    
    #----------------------------------------------
    inicio = time.time()
    exps = PercolationStats(n, t);
    mean = exps.mean()
    stddev = exps.stddev()
    confidenceLow = exps.confidenceLow()
    confidenceHigh = exps.confidenceHigh()
    fim = time.time()
    #---------------------------------------------

    # relatorio
    print(f"mean()           = {mean:.6f}")
    print(f"stddev()         = {stddev:.6f}")
    print(f"confidenceLow()  = {confidenceLow:.6f}")
    print(f"confidenceHigh() = {confidenceHigh:.6f}")
    print(f"elapsed time     = {fim-inicio:.3f}s")

#--------------------------------------------------
if __name__ == '__main__':
    main()