import pandas as pd

data = pd.read_csv( "xyz.txt" )

for key in data:
	for i in range( len( data[ key ])):
		val = 0 if data[ key ][ i ] < 0 else data[ key ][ i ]
		data[ key ][ i ] = val

print( data )