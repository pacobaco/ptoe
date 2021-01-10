import pickle

class PTOE:
	def __init__(self, AtomicNumber, Element, Symbol, AtomicMass, NumberofNeutrons, NumberofProtons, NumberofElectrons, Period, Group, Phase, Radioactivity, Natural, Metal, Nonmetal, Metalloid, Type, AtomicRadius, Electronegativity, FirstIonization, Density, MeltingPoint, BoilingPoint, NumberofIsotopes, Discoverer, Year, SpecificHeat, NumberofShells, NumberofValence):
		self.AtomicNumber = AtomicNumber
		self.Element = Element
		self.Symbol = Symbol
		self.AtomicMass = AtomicMass
		self.NumberofNeutrons = NumberofNeutrons
		self.NumberofProtons = NumberofProtons
		self.NumberofElectrons = NumberofElectrons
		self.Period = Period
		self.Group = Group
		self.Phase = Phase
		self.Radioactivity = Radioactivity
		self.Natural = Natural
		self.Metal = Metal
		self.Nonmetal = Nonmetal
		self.Metalloid = Metalloid
		self.Type = Type
		self.AtomicRadius = AtomicRadius
		self.Electronegativity = Electronegativity
		self.FirstIonization = FirstIonization
		self.Density = Density
		self.MeltingPoint = MeltingPoint
		self.NumberofIsotopes = NumberofIsotopes
		self.Discoverer = Discoverer
		self.Year = Year
		self.SpecificHeat = SpecificHeat
		self.NumberofShells = NumberofShells
		self.NumberofValence = NumberofValence
        
i = open('ptoe.csv')
q = i.read()
w = q.split('\n')
a = []
for x in w[1:]:
    r = x.split(',')
    print r
    a.append(PTOE(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18], r[19], r[20], r[21], r[22], r[23], r[24], r[25], r[26], r[27]))
    
objs = ''
for x in a:
    objs = objs + pickle.dumps(x) + '\n'
    
o = open('opie.sql', 'w')
o.write(objs)
o.close()
    
