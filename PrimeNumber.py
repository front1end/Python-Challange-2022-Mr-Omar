import time
from multiprocessing import Pool
from math import sqrt

def asal_mi(sayi):
    if sayi < 2:
        return False
    ""
    if sayi % 2 == 0:
        return False

    bolunecekler = range(3, int(sqrt(sayi)), 2)
    for x in bolunecekler:
        if sayi % x == 0:
            return False
    return True

def sayilar_asal_mi(sayilar):
    return [i for i in sayilar if asal_mi(i)]

if __name__ == "__main__":

    p = Pool(processes = 4)
    eski = time.time()
    neticeler = p.map(sayilar_asal_mi, [range(2,625000),
                                       range(62500, 125000),
                                       range(125000, 187500),
                                       range(187000, 250000),
                                       range(250000, 312500),
                                       range(312500, 375000),
                                       range(375000, 437000),
                                       range(437000, 500000)])

    print(time.time() - eski)
    print(neticeler)
    alt_toplamlar = map(sum, neticeler)
    print("Rəqəmlərin Cəmi:", sum(alt_toplamlar)) 
