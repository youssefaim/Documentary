from Documantaire2 import Documantaire, exemplaire

Doc0 = Documantaire("Lenovo","sep 8-9")
Doc1 = Documantaire("LenovoT480","sep")

print(Doc0.ToString())
print(Doc1.ToString())
print(Doc0.Equals(Doc1))

Ex1 = exemplaire("Lenv","Sep 9","Sep 7",)
Ex2 = exemplaire("lenvd","sep 30","Sep 10",234)
print(Ex1.ToString())
print(Ex2.ToString())
print(Ex1.Equals(Ex2))



