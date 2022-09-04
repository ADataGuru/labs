
# Environnement d'écution principal à python
if __name__ == '__main__':

    # Kesako une variable et les types

    un_string: str = "titi"  # Et non 1_string les chiffres ne sont pas acceptés en préfix de nom de variable
    un_entier: int = 1
    un_decimal: float = 1.4

    from typing import List, Dict, Union  # From le nom du package python importer ce qu'on veut du package/fichier

    une_liste: List = ["1", 2]
    un_dict_d_utilisateur: Dict = {
        "user1": {
            "nom": "cam",
            "prenom": "lolo",
            "age": 27
        },
        "user2": {
            "nom": "benz",
            "prenom": "soufiane",
            "age": None
        }
    }

    # Kesako des loops

    for el in un_dict_d_utilisateur:
        message = """
        Hello, 
        Le prénom de l'user est : {prenom}
        Son nom est : {nom}
        Son age est : {age}
        """.format(prenom=un_dict_d_utilisateur.get(el).get("prenom"), nom=un_dict_d_utilisateur.get(el).get("nom"),
                   age=un_dict_d_utilisateur.get(el).get("age"))
        print(message)


    # Kesako les fonctions

    def ajoute(premier_nombre: Union[float, int], deuz_nombre: Union[float, int]) -> Union[float, int]:
        return premier_nombre + deuz_nombre


    print(ajoute(4.3, 3))


    # Kesako les classes:
    class Utilisateur:
        prenom: str
        nom: str

        def __init__(self, prenom: str, nom: str):
            self.prenom = prenom
            self.nom = nom

        def get_nom_complet(self) -> str:
            return f"{self.prenom} {self.nom}"

    user1 = Utilisateur("Loïc", "Caminale")
    nom_entier = user1.get_nom_complet()
    print(nom_entier)

    user2 = Utilisateur("titi", "toto")