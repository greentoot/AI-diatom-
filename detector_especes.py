import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
from abre_race import dico
import requests
def espece(nomdelimage): 
    model = load_model('model_entrainer/diatom.h5')

    img = cv2.imread(nomdelimage)
    new_size = (128, 128)
    img_resized = cv2.resize(img, new_size)
    img_array = np.expand_dims(img_resized, axis=0)
    img_array = img_array / 255.0  

    data_dir = 'data_individual_images/individual_diatoms'
    test_datagen = ImageDataGenerator(rescale=1./255) 

    test_generator = test_datagen.flow_from_directory(
        data_dir,
        target_size=(128, 128),
        batch_size=1, 
        class_mode='categorical',
        shuffle=False 
    )

    rotation_angles = [90, 180, 270]
    predictions_per_class = {label: [] for label in test_generator.class_indices.keys()}

    for angle in rotation_angles:
        img_rotated = np.rot90(img, k=angle // 90)
        img_resized = cv2.resize(img_rotated, new_size)
        img_array = np.expand_dims(img_resized, axis=0)
        img_array = img_array / 255.0  

        prediction = model.predict(img_array)
        predicted_class_indices = np.argmax(prediction, axis=1)
        labels = test_generator.class_indices
        labels = {v: k for k, v in labels.items()}

        for idx, val in enumerate(predicted_class_indices):
            class_label = labels[val]
            predictions_per_class[class_label].append(prediction[idx])

    total_angles = len(rotation_angles)
    save = []
    for class_label, predictions_list in predictions_per_class.items():
        percentage = (len(predictions_list) / total_angles) * 100
        save.append(percentage)
    most_common_class = max(predictions_per_class, key=lambda x: len(predictions_per_class[x]))
    

    data = dico()
    if most_common_class in data: 
        return most_common_class, max(save), data[most_common_class]
    else:
        return most_common_class, max(save)
    
  

