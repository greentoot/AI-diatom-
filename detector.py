import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from detector_especes import espece
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tqdm import tqdm  
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data_dir = 'data_individual_images'
model_path = 'model_entrainer/recognitiondéchet.h5'
chemin = "DIATOMEES MORCHENE"

try:
    model = load_model(model_path)
except OSError:
    exit()

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=1,
    class_mode='categorical',
    shuffle=False
)

save = []

for dossier, sous_dossiers, fichiers in os.walk(chemin):
    save.append(dossier)

nombre_fichiers = 0

for fichier in fichiers:
    nombre_fichiers += 1

table = {}

for i in tqdm(range(nombre_fichiers), desc="Chargement des images"):
    img_path = os.path.join(save[0], fichiers[i]) 
    img = image.load_img(img_path, target_size=(128, 128))

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  
    img_array = img_array / 255.0  

    prediction = model.predict(img_array)

    predicted_class_indices = np.argmax(prediction, axis=1)  
    labels = test_generator.class_indices
    labels = dict((v, k) for k, v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices]
    if "diatom" in predictions[0]:
        table[img_path] = (espece(img_path))
    else : 
        pourcentage_prediction = np.max(prediction) * 100
        table[img_path] = ("détritu", pourcentage_prediction)

for key, value in table.items():
    print(value[0])

class App:
    def __init__(self, master):
        self.master = master
        master.title("Anthony Loiseau programme de résultat")

        self.master.attributes('-fullscreen', True)
        style = ttk.Style()
        style.configure("TNotebook.Tab", padding=(50, 20))
        self.tabControl = ttk.Notebook(self.master, style="TNotebook")

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text="RESULTAT")
        self.tabControl.add(self.tab2, text="ENVIRONNEMENT")
        self.tabControl.add(self.tab3, text="DIATOMS")

        self.tabControl.pack(expand=1, fill="both")

        result_label = tk.Label(self.tab1, text="Ici se trouvent les résultats 'bruts' du programme detector.py réalisé")
        result_label.pack(padx=20, pady=20)

        self.result_search_entry = tk.Entry(self.tab1, width=50)
        self.result_search_entry.pack(pady=10)
        self.result_search_button = tk.Button(self.tab1, text="Rechercher", command=self.perform_result_search)
        self.result_search_button.pack(pady=10)

        self.result_treeview = ttk.Treeview(self.tab1, columns=("Clé", "Valeur", "Prediction"), show="headings")
        self.result_treeview.heading("Clé", text="Image")
        self.result_treeview.heading("Valeur", text="Diatom correspondant(selon l'IA)")
        self.result_treeview.heading("Prediction", text='Prediction du machine learning')
        self.result_treeview.pack(expand=1, fill="both")

        for key, value in table.items():
            if isinstance(value, tuple):
                prediction = value[1]
            else:
                prediction = None

            self.result_treeview.insert("", "end", values=(key, str(value[0]), prediction))

        environment_label = tk.Label(self.tab2, text="Ceci est une estimation de la qualité de l'environnement en fonction de leur nombre ... ")
        environment_label.pack(padx=20, pady=20)

        diatoms_label = tk.Label(self.tab3, text="Ici se trouve des informations approfondies sur les diatomées")
        diatoms_label.pack(padx=20, pady=20)

        result_tree_scrollbar = ttk.Scrollbar(self.tab1, orient="vertical", command=self.result_treeview.yview)
        result_tree_scrollbar.pack(side="right", fill="y")
        self.result_treeview.configure(yscrollcommand=result_tree_scrollbar.set)


        self.diatoms_treeview = ttk.Treeview(self.tab3, columns=["Attribut"] +['Denomination_espece'], show="headings")
        self.diatoms_treeview.heading("Attribut", text="Attribut")
        for col in ['Denomination_espece'] :
            self.diatoms_treeview.heading(col, text=col)
        self.diatoms_treeview.pack(expand=1, fill="both")

        diatoms_tree_scrollbar = ttk.Scrollbar(self.tab3, orient="vertical", command=self.diatoms_treeview.yview)
        diatoms_tree_scrollbar.pack(side="right", fill="y")
        self.diatoms_treeview.configure(yscrollcommand=diatoms_tree_scrollbar.set)

        self.show_diatom_info()

        self.create_environment_graph()

        self.quit_button = tk.Button(self.master, text="Quitter", command=self.quit)
        self.quit_button.pack(side="top", anchor="ne", padx=10, pady=10)

    def perform_result_search(self):
        for item in self.result_treeview.get_children():
            self.result_treeview.delete(item)

        search_query = self.result_search_entry.get().lower()

        for key, value in table.items():
            if search_query in key.lower() or search_query in str(value[0]).lower():
                if isinstance(value, tuple):
                    prediction = value[1]
                else:
                    prediction = None

                self.result_treeview.insert("", "end", values=(key, str(value[0]), prediction))

    def show_diatom_info(self):
        for key, value in table.items():
            if len(value) > 2:
                values_list = [value[0]] + [value[2].get(col, "") for col in table[key][2].keys()]
                self.diatoms_treeview.insert("", "end", values=values_list)

    def create_environment_graph(self):
        diatoms_count = {}
        for diatom in table.values():
            diatoms_count[str(diatom[0])] = diatoms_count.get(str(diatom[0]), 0) + 1
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))
        ax1.bar(diatoms_count.keys(), diatoms_count.values())
        ax1.set_ylabel('Fréquence')
        ax1.set_xlabel('Diatomées')
        ax1.set_title('Répartition des Diatomées (Barres)')
        ax2.pie(diatoms_count.values(), labels=diatoms_count.keys(), autopct='%1.1f%%', startangle=90)
        ax2.axis('equal') 
        ax2.set_title('Répartition des Diatomées (Camembert)')
        canvas = FigureCanvasTkAgg(fig, master=self.tab2)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

    def quit(self):
        self.master.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()