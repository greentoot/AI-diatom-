# Author :  Anthony Loiseau / Vincent Lafargue / Noé Cazanova et le reste ( sorry etienne et maya)

# Projet pour Notre chère Vincent
Je crois que cela va servir pour un projet de biologie, j'espère que vincent tu va lire ceci

# info
- pour lancer le fichier, il faut juste utiliser detector.py, cela proposera un input dans lequel vous pourrez y mettre votre image (l'endroit ou elle se trouve) et c'est tout 
- les models sont déjà entrianer mais vous pouvez très bien agrandir la base de donné et faire votre propre nombre d'Epoch

# exemple : 
- "cd /lecheminduprojet/vincent"
- "python detector.py"
ensuite : 
- "exemple/test1.jpg"
et paf le result

# requirements : 
- os 
- numpy
- tensorflow
- keras 
- cv2


# pourcentage d'erreur : 
sortie de la console pour déterminer si oui ou non c'est un débris ou un diatomée (2 classes : 10 Epoch ) le modèle génèrera une accuracy de : 98% et un loss finale de : ?: 



sortie de la console pour l'espèce (166 classes pour 100 Epoch) ce qui n'est pas énorme pour la quantité d'image provenant de la base et, le détail nécessaire pour les identifier, mais il a fallut plus de 15h d'apprentissage avant que le modèle générer ai une accuracy égale a : 74% et un loss finale de : 3.83 : 
Epoch 100/100
247/247 [==============================] - 103s 417ms/step - loss: 5.1146e-08 - accuracy: 1.0000 - val_loss: 3.8373 - val_accuracy: 0.7436

On double pour le recto verso 
Epoch 300/300
494/494 [==============================] - 204s 1.253s/step - loss: 8.1146e-12 - accuracy: 1.0000 - val_loss: 1.4789 - val_accuracy: 0.8586
