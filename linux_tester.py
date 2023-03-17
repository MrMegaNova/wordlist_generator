import pyautogui
import time

time.sleep(3)

filename = "output.txt"

x, y = 500, 500

wait_time = 1

with open(filename, "r") as f:
    for line in f:
        # Supprime les caractères de fin de ligne
        line = line.rstrip("\n")

        # Sélectionne le champ de texte
        #pyautogui.click(x, y)

        # Attendre avant d'appuyer sur la touche Entrée
        time.sleep(0.01)
        
        pyautogui.hotkey("ctrlleft", "a")

        # Attendre avant d'appuyer sur la touche Entrée
        time.sleep(0.01)
        
        pyautogui.write(line)

        # Simule la pression de la touche Entrée
        pyautogui.press("enter")

