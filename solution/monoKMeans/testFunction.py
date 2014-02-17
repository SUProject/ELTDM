# -*-coding:Latin-1 -*

#########################################################
# Test functions
# ELADM Project
#########################################################

#####
# Modulus part for import in the main
#####
def bissextile():
        annee = input("Enter a year: ") # On attend que l'utilisateur fournisse l'année qu'il désire tester
        try:
                annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
                assert annee > 0
        except ValueError:
                print("Input is not a number.")
        except AssertionError:
                print("Input not a positive year.")
                
        if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
                print("L'année saisie est bissextile.")
        else:
               	print("L'année saisie n'est pas bissextile.")
        



#####
# Modulus part for test here
#####
if __name__ == "__main__":
        bissextile()

        fruits = {"pommes":21, "melons":3, "poires":31}
        print(fruits.keys())
