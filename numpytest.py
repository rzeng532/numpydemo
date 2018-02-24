import numpy as py

matrix_alcohol = py.array([["1986", "Western", "Viet Nam", "Wine", "0"]
                          , ["1986", "Americas", "Uruguay", "Other", "0"]
                          , ["1985", "Africa", "Cte d'Ivoire", "Wine", "1.62"]])

alcohol_comsume = matrix_alcohol[:, 4]
print(alcohol_comsume)
print(type(alcohol_comsume[0]))
alcohol_comsume_new = alcohol_comsume.astype(float)
print(alcohol_comsume_new)
print(alcohol_comsume)
print(matrix_alcohol)