import os
import time
from datetime import datetime
import subprocess

# Chemin absolu des répertoires à nettoyer
directories = [
    "/Users/33760/Documents/test-Nettoyage",
    "/Users/33760/Desktop"
]

# Chemin absolu du fichier journal
journal_file = "/Users/33760/Documents/journal.txt"

# Suppression des fichiers en double
hashes = {}
for dirpath, dirnames, filenames in os.walk("/Users/33760/Documents/test-Nettoyage"):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        with open(file_path, "rb") as f:
            file_hash = hash(f.read())
        if file_hash in hashes:
            file_size = os.path.getsize(file_path)
            os.remove(file_path)
            with open(journal_file, "a") as journal:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                journal.write(f" {now}: {file_path} (Taille :{file_size} octets) a été supprimé car il est en double.\n")
        else:
            hashes[file_hash] = file_path

# Suppression des dossiers vides
for directory in directories:
    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            if not os.listdir(dir_full_path):
                os.rmdir(dir_full_path)
                with open(journal_file, "a") as journal:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    journal.write(f"{now}: {dir_full_path} a été supprimé car il est vide.\n")

# Suppression des fichiers temporaires et en cache
for directory in directories:
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if file_path.endswith('.tmp'):
                try:
                    file_size = os.path.getsize(file_path)
                    os.remove(file_path)
                    with open(journal_file, "a") as journal:
                        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        journal.write(f"{now}: {file_path} ({file_size} octets) a été supprimé car il est temporaire et en cache.\n")
                except:
                    with open(journal_file, "a") as journal:
                        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        journal.write(f"{now}: {file_path} n'a pas pu être supprimé.\n")

# Attente de 5 secondes avant la fin du script
time.sleep(5)
print("Le nettoyage est terminé.")

# Afficher une notification
subprocess.call(['osascript', '-e', 'display notification "Vous venez d\'effectuer un nettoyage sur votre répertoire" with title "Nettoyage terminé"'])
