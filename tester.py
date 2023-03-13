import pyautogui
import time

# Chemin du fichier contenant les chaînes de caractères à coller
filename = "output.txt"

# Position du champ de texte dans lequel coller les chaînes de caractères
x, y = 500, 500

# Temps d'attente avant d'appuyer sur la touche Entrée (en secondes)
wait_time = 1

# Ouvre le fichier en lecture
with open(filename, "r") as f:
    # Lit chaque ligne du fichier
    for line in f:
        # Supprime les caractères de fin de ligne
        line = line.rstrip("\n")

        # Sélectionne le champ de texte
        pyautogui.click(x, y)

        # Coller la chaîne de caractères
        pyautogui.hotkey("command", "v")
        
        # Attendre avant d'appuyer sur la touche Entrée
        time.sleep(wait_time)
        
        pyautogui.hotkey("command", "a")

        # Attendre avant d'appuyer sur la touche Entrée
        time.sleep(wait_time)

        # Simule la pression de la touche Entrée
        pyautogui.press("enter")

