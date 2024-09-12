"""
modular.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GPxxx
Integrantes:
    - Sergio Fernández
    - Liam Esgueva

Descripción:
Librería para la realización de cálculos y resolución de problemas de aritmética modular.
"""

from typing import Tuple, List, Dict

class IncompatibleEquationError(Exception):
    pass


""" Reciba un entero n y devuelva verdadero si es un número primo y falso en caso contrario

    Args:
        n (int): Entero
    
    Returns:
        true si el entero es un número primo.
        false en caso contrario.

    Raises: None
    
    Examples:
        es_primo(5)=true
        es_primo(4)=false
"""
def es_primo(n:int)->bool:
    pass

""" Recibe dos enteros a y b y devuelva la lista de números primos en el intervalo [a, b)

    Args:
        a (int): Elemento inicial del intervalo (incluido)
        b (int): Elemento final del intervalo (no incluido)
    
    Returns:
        List[int]: lista ordenada de primos mayores o iguales que a y menores que b.

    Raises: None
    
    Examples:
        lista_primos(1,11)=[2,3,5,7]
"""
def lista_primos(a,b)-> List[int]:
    pass


""" Recibe  un entero n y devuelve un diccionario cuyas claves son los primos que dividen a n y sus valores los
correspondientes exponentes en la descomposición en producto de factores primos de n.
    Args:
        n (int): Entero que se desea factorizar.
    
    Returns:
        Dict[int,int]: Diccionario en el que las claves son primos positivos p_i que dividen a n y, para cada p_i,
            su valor asociado es el máximo exponente e_i tal que p_i^(e_i) divide a n. Si n=0, devuelve un diccionario vacío.

    Raises: None

    Examples
        factorizar(12)={2: 2, 3: 1}
        factorizar(0)={}
"""
def factorizar(n:int)->Dict[int,int]:
    pass

""" Calcula el máximo común divisor de dos enteros a y b.
    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns:
        int: devuelve el máximo común divisor de a y b

    Raises: None

    Examples
        mcd(10,15)=5
"""
def mcd(a:int,b:int)->int:
    pass

""" Calcula el máximo común divisor d de dos enteros a y b junto con dos enteros x e y tales que
        d=ax+by

    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns: (d,x,y)
        d (int): Máximo común divisor.
        x (int): Coeficiente de a.
        y (int): Coeficiente de b.

    Raises: None

    Examples
        bezout(6,10)=(2,2,-1)
"""
def bezout(n:int, m:int) -> Tuple[int,int,int]:
    pass

""" Dada una lista de enteros, devuelve el máximo divisor común a todos ellos.
    Args:
        nList (List[int]): Lista de enteros.        
    
    Returns:
        int: devuelve el máximo entero que divide a todos los enteros de la lista.

    Raises: None

    Examples
        mcd([4,10,14])=2
"""
def mcd_n(nlist:List[int])->int:
    #Opcional
    pass

""" Dada una lista de enteros [a_1,...,a_n], devuelve el máximo divisor común d a todos ellos y una
lista de coeficientes [x_1,...,x_n] tal que
    d=a_1*x_1+...a_n*x_n

    Args:
        nList (List[int]): Lista de enteros.        
    
    Returns: (d,X)
        d (int): Máximo entero que divide a todos los enteros de la lista.
        X (List[int]): Lista de coeficientes [x_1,...,x_n].

    Raises: None

    Examples
        bezout_n([4,10,14])=(2,[-2,1,0])
"""
def bezout_n(nlist:List[int])->Tuple[int,List[int]]:
    #Opcional
    pass

""" Determina si dos enteros son coprimos.
    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns:
        bool: Verdadero si son coprimos y falso si no.

    Raises: None

    Examples
        coprimos(14,20)=false
        coprimos(14,15)=true
"""
def coprimos(n:int,m:int)->bool:
    pass

""" Calcula potencias módulo p.

    Args:
        base (int): Base de la potencia.
        exp (int): Exponente al que se eleva la base.
        p (int): Módulo.
    
    Returns:
        int: Resto de dividir base^exp módulo p.

    Raises:
        ZeroDivisionError: Si el módulo es 0.
"""
def potencia_mod_p(base:int, exp:int, p:int) -> int:
    pass

""" Calcula la inversa de un número n módulo p.

    Args:
        n (int): Número que se desea invertir
        p (int): Módulo.
    
    Returns:
        int: Entero x entre 0 y p-1 tal que n*x es congruente con 1 módulo p.

    Raises:
        ZeroDivisionError: Si el módulo es 0 o si n no es invertible módulo p.
"""
def inversa_mod_p(n:int,p:int)->int:
    pass

""" Calcula la función phi de Euler de un entero positivo n, es decir, cuenta cúantos enteros positivos
menores que n son coprimos con n.

    Args:
        n (int): Número entero positivo.
    
    Returns:
        int: Función phi de Euler de n.

    Raises: None
"""
def euler(n:int)->int:
    pass

""" Dado un entero n y un número primo p, calcula el símbolo de Legendre de n módulo p.

    Args:
        n (int): Número entero.
        p (int): Número primo.
    
    Returns:
        int: Símbolo de Legendre de Euler de n módulo p:
            0 si es múltiplo de p
            1 si es un cuadrado perfecto (distinto de 0), módulo p
            -1 en caso contrario.

    Raises:
        ZeroDivisionError: Si el módulo p es 0.
"""
def legendre(n:int,p:int)->int:
    pass

""" Dadas tres listas de números enteros [a_1,...,a_n], [b_1,...,b_n] y [p_1,...,p_n], resuelve el sistema de congruencias
    
    a_i * x = b_i (mod p_i)   i=1,...,n
    
    devolviendo un entero r y un módulo m tales que las soluciones del sistema corresponden a todos los enteros
    x congruentes con r módulo m.

    Args:
        alist (List[int]): Lista de coeficientes de la variable x, [a_1,...,a_n].
        blist (List[int]): Lista de términos independientes [b_1,...,b_n].
        plist (List[int]): Lista de módulos [p_1,...,p_n]
    
    Returns: (r,m)
        r (int): Entero entre 0 y m-1.
        m (int): Entero positivo, módulo de la solución.

    Raises:
        IncompatibleEquationError: Si no es posible resolver el sistema.
"""
def resolver_sistema_congruencias(alist:List[int],blist:List[int],plist:List[int])->Tuple[int,int]:
    pass

""" Encuentra, si existe, una raíz cuadrada para un entero n módulo un número primo p.

    Args:
        n (int): Entero del que se desea hallar la raíz.
        p (int): Módulo. Se asume que es un número primo.
    
    Returns:
        int: Entero x entre 0 y p-1 tal que x^2 = n (mod p).

    Raises:
        IncompatibleEquationError: Si no es posible hallar dicha raíz.
"""
def raiz_mod_p(n:int,p:int)->int:
    #Opcional
    pass

""" Halla, si es posible, las dos posibles soluciones de la ecuación cuadrática ax^2+bx+c=0 (mod p).
Devuelve una tupla con las dos raíces (distintas o una misma raíz repetida en caso de ser doble).

    Args:
        a (int): Coeficiente de x^2.
        b (int): Coeficiente de x.
        c (int): Término independiente.
        p (int): Módulo. Se asume que es un número primo.
    
    Returns: (x1,x2)
        x1 (int): Primera solución. Entero entre 0 y p-1.
        x2 (int): Segunda solución. Entero entre 0 y p-1.

    Raises:
        IncompatibleEquationError: Si no es posible resolver la ecuación.
"""
def ecuacion_cuadratica(a:int,b:int,c:int,p:int)->Tuple[int,int]:
    #Opcional
    pass



