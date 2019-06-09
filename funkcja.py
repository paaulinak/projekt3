# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:11:52 2019

@author: Paulina
"""

from math import sin, cos, sqrt, tan, pi, degrees, atan, floor
from moje_metody import decimalDeg2dms

def Vincenty(fi_a,la_a,fi_b,la_b,a = 6378137.000, e2 = 0.00669438002290):
    """
    #INPUT:
         fi_a [rad]
         la_a [rad]
         fi_b [rad]
         la_b [rad]
    #OUTPUT:
        s_AB [m]
    """
    
    if fi_a == fi_b and la_a == la_b: #ta sama szerokosc i dlugosc
        s_AB = 0
    elif fi_a == fi_b and la_a != la_b: #ta sama szerokosc
        N = a/sqrt(1-e2*(sin(fi_a))**2)
        dL = abs(la_a - la_b)  
        s_AB = dL*N*cos(fi_a)
#    elif la_a == la_b and fi_a != fi_b:
#        M = a*(1-e2)/sqrt((1-e2*(sin(fi_a))**2)**3) #??? KTORE FI
#        dB = abs(fi_a - fi_b)
#        s_AB = dB*M
    else: #rozne szerokosci i dlugosci
        b = a*sqrt(1-e2)
        f = 1 - (b/a)
        delta_la = la_b - la_a
        U_a = atan((1-f)*tan(fi_a))
        U_b = atan((1-f)*tan(fi_b))
        L = delta_la
        while True:
            sin_sigma = sqrt((cos(U_b)*sin(L))**2 + (cos(U_a)*sin(U_b) - sin(U_a)*cos(U_b)*cos(L))**2)
            cos_sigma = sin(U_a)*sin(U_b) + cos(U_a)*cos(U_b)*cos(L)
            sigma = atan(sin_sigma/cos_sigma)
            sin_alfa = (cos(U_a)*cos(U_b)*sin(L))/(sin_sigma)
            cos2_alfa = 1 - (sin_alfa)**2
            cos2_sigma_m = cos_sigma - (2*sin(U_a)*sin(U_b))/(cos2_alfa)
            C = (f/16)*cos2_alfa*(4+f*(4-3*cos2_alfa))
            Ls = L
            L = delta_la + (1-C)*f*sin_alfa*(sigma + C*sin_sigma*(cos2_sigma_m + C*cos_sigma*(-1+2*(cos2_sigma_m)**2)))
            if (L-Ls)<(0.000001/206265):
                break
        u2 = ((a**2 - b**2)/b**2)*cos2_alfa
        A = 1 + (u2/16384)*(4096 + u2*(-768 + u2*(320 - 175*u2)))
        B = (u2/1024)*(256 + u2*(-128 + u2*(74 - 47*u2)))
        delta_sigma = B*sin_sigma*(cos2_sigma_m + (1/4)*B*(cos_sigma*(-1 + 2*(cos2_sigma_m)**   2) - (1/6)*B*cos2_sigma_m*(-3 + 4*(sin_sigma)**2)*(-3 + 4*(cos2_sigma_m)**2)))
        s_AB = b*A*(sigma - delta_sigma)
#    A_AB = atan((cos(U_b)*sin(L))/(cos(U_a)*sin(U_b) - sin(U_a)*cos(U_b)*cos(L)))
#    A_BA = atan((cos(U_a)*sin(L))/(-sin(U_a)*cos(U_b) + cos(U_a)*sin(U_b)*cos(L))) + pi
    return s_AB