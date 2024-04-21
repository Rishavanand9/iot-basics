import os
import face_recognition
import numpy as np
import pickle

def train_recognizer(directory):
    known_encodings = []
    known_names = []

    # Loop over the image paths
    for label in os.listdir(directory):
        person_dir = os.path.join(directory, label)
        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(label)

    # Save the encodings and names
    with open('trained_model.pkl', 'wb') as f:
        pickle.dump({'encodings': known_encodings, 'names': known_names}, f)

if __name__ == "__main__":
    train_recognizer('labeled_images')  # path to your labeled images
