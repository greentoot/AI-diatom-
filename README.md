# Author :  Anthony Loiseau / Vincent Lafargue / Noé Cazanova

# Projet 
This project is intended for a biology project. Vincent, we hope you find this helpful.
# info
- To launch the file, simply use detector.py. It will prompt an input where you can specify the location of your image, and that's it.
- The models are already trained, but you can expand the database and customize the number of epochs according to your needs.

#Usage Example
  -Navigate to the project directory.
  -Run python detector.py.
Voila! Get the result.

# requirements : 
- os 
- numpy
- tensorflow
- keras 
- cv2


# pourcentage d'erreur : 
Console output for determining whether it's debris or a diatom (2 classes: 10 Epochs): The model achieves an accuracy of 98% and a final loss of ?:.


Console output for species identification (166 classes for 100 Epochs): Given the substantial amount of images from the database and the necessary detail for identification, it took over 15 hours of training for the model to achieve an accuracy of 74% and a final loss of 3.83.

For double-sided detection:

Epoch 300/300
Final loss: 1.4789
Final accuracy: 85.86%
Feel free to adjust parameters and further optimize the models for your specific needs. 
Epoch 100/100

247/247 [==============================] - 103s 417ms/step - loss: 5.1146e-08 - accuracy: 1.0000 - val_loss: 3.8373 - val_accuracy: 0.7436

On double pour le recto verso 
Epoch 300/300
494/494 [==============================] - 204s 1.253s/step - loss: 8.1146e-12 - accuracy: 1.0000 - val_loss: 1.4789 - val_accuracy: 0.8586
