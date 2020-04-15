calification = int(input('Calification: '))
color = None
if calification >= 7 and calification <= 10:
    color = 'green'
elif calification < 7 and calification >= 0:
    color = 'red'
else:
	print('There was an error, please try again.')
# =============================================
# Assignation on one line
color = 'green' if calification >= 7 else 'red'
if color is not None:
    print(calification, color)

''' Values Python takes as falses
    - False
    - None
    - []
    - ()
    - {}
    - ' '
    - 0
    - 0.0 '''