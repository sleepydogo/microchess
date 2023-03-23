# ESTRUCTURA DE LA RED NEURONAL

ENTRADA         RED             SALIDA</br>
[0,&emsp;O-O-O-O-O-O-O-O-O&emsp;   [0,</br>
1,&emsp;O-O-O-O-O-O-O-O-O&emsp;    1,</br>
0,&emsp;O-O-O-O-O-O-O-O-O&emsp;    0,</br>
1,&emsp;O-O-O-O-O-O-O-O-O&emsp;    1,</br>
1,&emsp;O-O-O-O-O-O-O-O-O&emsp;    1,</br>
1,&emsp;O-O-O-O-O-O-O-O-O&emsp;    1,</br>
.&emsp;O-O-O-O-O-O-O-O-O&emsp;    .</br>
.&emsp;O-O-O-O-O-O-O-O-O&emsp;    .</br>
.&emsp;O-O-O-O-O-O-O-O-O&emsp;    .</br>
0,&emsp;O-O-O-O-O-O-O-O-O&emsp;    0,</br>
1]&emsp;O-O-O-O-O-O-O-O-O&emsp;    1]</br>

LA ENTRADA SERA UN VECTOR DE 64 POSICIONES QUE REPRESENTAN CADA POSICION DEL TABLERO. CON UN  VALOR DE 4 BITS EN CADA UNO DE LOS ELEMENTOS DE VECTOR. A ESTO HAY QUE SUMARLE

## INFO DE CONTROL

    * REY PUEDE ENRROCAR X4                 (4 BITS)
    * TORRE PUEDE ENRROCAR X4               (4 BITS)
    * PEON PUEDE SALTAR 2 CASILLEROS X16    (16 BITS)
    * TOTAL                                 (3 BYTES)

##PESO TOTAL DEL ARREGLO:

    64 * 4 BITS + 3 BYTES = 35 BYTES DE ENTRADA

## SALIDA DE LA RED:

    POSIBILIDADES:
    1) 35 BYTES QUE REPRESENTAN UN TABLERO FUTURO.
    2) MOVIMIENTO
            [A..H][1..8][A..H][1..8] = 
            1B  + 1B   + 1B   + 1B   = 4 BYTES

## (OPTIMIZACION A TENER EN CUENTA)

SE PODRIA OPTIMIZAR PARA QUE CADA CASILLERO LIBRE EN VEZ DE REPRESENTARLOS CON 4 BITS SE REPRESENTE EN BINARIO CON UN 0

## PROBLEMA: SABER DONDE TERMINA Y EMPIEZA LA POSICION DE UNA PIEZA. HABRIA QUE ANIADIR ALGUN TIPO DE INDICE

```sh

```
