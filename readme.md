# Rapport sur la Calculatrice
## Introduction

Ce rapport présente la conception et l'implémentation d'une calculatrice en utilisant le langage de programmation Python et la bibliothèque Tkinter pour l'interface graphique. La calculatrice prend en charge des opérations basiques ainsi que des opérations scientifiques.
## Fonctionnalités Développées

### Interface Graphique

L'interface graphique de la calculatrice est construite en utilisant Tkinter. La fenêtre principale a une taille de 400x700 pixels et est divisée en deux parties. La partie supérieure affiche l'expression en cours d'évaluation, tandis que la partie inférieure contient les boutons pour les chiffres, opérateurs, et fonctions.

L'utilisateur peut basculer entre deux modes : "normal" et "scientifique". Le mode normal propose les opérations de base, tandis que le mode scientifique inclut des fonctions trigonométriques, logarithmiques, et d'autres fonctions mathématiques avancées.

### Évaluation des Expressions

La classe Calculator gère l'évaluation des expressions mathématiques. Elle prend en charge les opérations binaires telles que l'addition, la soustraction, la multiplication, la division, et l'exponentiation, ainsi que des opérations unaires comme les fonctions trigonométriques, logarithmiques, la racine carrée, etc.

Lorsqu'un bouton est cliqué dans l'interface graphique, la méthode button_click est appelée, mettant à jour l'expression en cours d'évaluation. Lorsque le bouton "=" est cliqué, la méthode evaluate_expression est appelée pour évaluer l'expression et afficher le résultat.

Pour les expressions binaires, elles sont sous la forme (x {operator} y), pour les unaires ({operator}x). Si vous rentrez plus que sous ces formes la, par exemple (3+2%), la calculatrice ne sortiras rien. Le pourcentage n'est pas pris en charge. 

### Tests

Des tests ont été effectués pour vérifier le bon fonctionnement de la calculatrice. Les cas de tests comprennent :

1. Opérations de base : Addition, soustraction, multiplication, et division.
2. Opérations avancées : Exponentiation, fonctions trigonométriques, logarithmiques, etc.
3. Gestion des erreurs : La calculatrice est conçue pour gérer les erreurs d'évaluation, par exemple, lorsque l'utilisateur entre une expression incorrecte.

Les tests ont été effectués en utilisant la calculatrice avec différentes expressions mathématiques pour s'assurer de sa précision et de sa robustesse.

## Conclusion

La calculatrice développée offre une interface utilisateur conviviale et prend en charge une variété d'opérations mathématiques. Les tests effectués ont confirmé que la calculatrice fonctionne correctement dans différentes situations. Des améliorations futures pourraient inclure l'ajout de fonctionnalités supplémentaires et l'amélioration de l'interface graphique.