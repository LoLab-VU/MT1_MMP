"""This is reaction between molecule a and b to produce ab"""
#a + c <-> ac

from pysb import * #calling all pysb classes
import pysb.bng
Model() # calling Model class. We don't have to put arguments inside since it all has default in it (in core file)

Monomer('a',['b']) #calling monomer class in core file
Monomer('c',['b'])

##Diffusion
#default: diffusion constant is zero#
#Parameter('Da', 1)
#Parameter('Dc', 1)
#Diffusion('a(b=None), Da') #(species, value or parameter)
#Diffusion('a(c=None), Dc')

Parameter('k',1)
Parameter('l',1e-10)

Rule('d', a(b=None) + c(b=None) <> a(b=1)%c(b=1), k, l)

Parameter('ao',100)
Parameter('co',200)
Initial(a(b=None),ao)
Initial(c(b=None),co)

Observable('AC_complex', a(b=1)%c(b=1))
Observable('A_free', a(b=None))
Observable('C_free', c(b=None)) 
Observable('A_tot', a())
Observable('C_tot', c())

pysb.bng.generate_equations(model)

####
#To know the list of species that included in the obs
print model.observables[3].species
####

for i,ode in enumerate(model.odes):
    print i,':', ode
    print
print '%%%%%%%'
print type(model.odes[0])
w = model.odes[0]+model.odes[1]

#r = model.odes[0] - __s2*l #???
print model.species