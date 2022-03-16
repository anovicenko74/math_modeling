import lab_3_1 as const
import math 

h = 100

u = (const._g_of_earth * h * ( math.tan( const._pi/6 )**2 ) / 2 * math.cos( const._pi/3 )**2 * ( 1 - math.tan( const._pi / 6 ) * math.tan( const._pi/3 ) ))**0.5 

T = 200
e = 300

N = (( 2 / const._pi**0.5 ) * ( const._planck_constant / ( T * const._boltzmann_constant )**(3/2) )) * const._euler_number**( -e / T * const._boltzmann_constant ) * e**( T / 2 )

print("u =", u);

print("N =", N)