import tkinter as tk
from tkinter import ttk, messagebox

def calculer_impot():
    try:
        salaire = float(entry_salaire.get())
        prime_montant = float(entry_prime.get())
        prime_placee = var_prime.get()
        plus_value = float(entry_crypto_gain.get())
        moins_value = float(entry_crypto_loss.get())
        opt_bar_progressif = var_barprog.get()

        seuil_exon_apprenti = 19744
        revenu_total = salaire + (0 if prime_placee else prime_montant)

        # Calcul prime d'intéressement
        if prime_placee:
            csg_prime = prime_montant * 0.097
            prime_net = prime_montant - csg_prime
            info_prime = (
                f"Prime placée : exonérée d'impôt\n"
                f"Soumise à 9,7 % CSG/CRDS = {csg_prime:.2f} €\n"
                f"Montant net perçu : {prime_net:.2f} €"
            )
        else:
            csg_prime = prime_montant * 0.172
            prime_net = prime_montant - csg_prime
            info_prime = (
                f"Prime encaissée : imposable\n"
                f"Soumise à 17,2 % de prélèvements sociaux = {csg_prime:.2f} €\n"
                f"Montant net perçu : {prime_net:.2f} €"
            )

        # Calcul crypto
        pv_nette = max(0, plus_value - moins_value)

        if opt_bar_progressif:
            if revenu_total <= seuil_exon_apprenti:
                impot_crypto = pv_nette * 0.172
                taux_crypto = "17,2 % (CSG/CRDS uniquement, IR = 0 %)"
            else:
                impot_crypto = pv_nette * 0.284  # Exemple : 11,2 % IR + 17,2 %
                taux_crypto = "28,4 % (11,2 % IR + 17,2 % prélèvements sociaux)"
        else:
            impot_crypto = pv_nette * 0.30
            taux_crypto = "30 % (PFU : 12,8 % IR + 17,2 % sociaux)"

        message = (
            f"Revenu d’apprenti déclaré : {salaire:.2f} €\n"
            f"{info_prime}\n\n"
            f"Plus-value crypto nette : {pv_nette:.2f} €\n"
            f"Taux appliqué : {taux_crypto}\n"
            f"Impôt total crypto : {impot_crypto:.2f} €"
        )

        messagebox.showinfo("Simulation Fiscale Complète", message)

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des montants numériques valides.")

# Interface graphique
root = tk.Tk()
root.title("Simulation Impôt - Apprenti / Crypto / Prime")

# Entrée salaire
ttk.Label(root, text="Salaire annuel brut (€)").grid(row=0, column=0, sticky="e")
entry_salaire = ttk.Entry(root)
entry_salaire.grid(row=0, column=1)

# Entrée prime
ttk.Label(root, text="Montant de la prime (€)").grid(row=1, column=0, sticky="e")
entry_prime = ttk.Entry(root)
entry_prime.insert(0, "4000")
entry_prime.grid(row=1, column=1)

# Check prime placée
var_prime = tk.BooleanVar(value=True)
ttk.Label(root, text="Prime placée (PEE / PER) ?").grid(row=2, column=0, sticky="e")
ttk.Checkbutton(root, variable=var_prime, text="Oui (décocher = encaissée)").grid(row=2, column=1, sticky="w")

# Gains crypto
ttk.Label(root, text="Gains crypto bruts (€)").grid(row=3, column=0, sticky="e")
entry_crypto_gain = ttk.Entry(root)
entry_crypto_gain.grid(row=3, column=1)

# Pertes crypto
ttk.Label(root, text="Pertes crypto (€)").grid(row=4, column=0, sticky="e")
entry_crypto_loss = ttk.Entry(root)
entry_crypto_loss.grid(row=4, column=1)

# Option PFU vs Barème
var_barprog = tk.BooleanVar(value=True)
ttk.Label(root, text="Barème progressif pour crypto ?").grid(row=5, column=0, sticky="e")
ttk.Checkbutton(root, variable=var_barprog, text="Oui (décocher = PFU 30%)").grid(row=5, column=1, sticky="w")

# Bouton de calcul
ttk.Button(root, text="Calculer", command=calculer_impot).grid(row=6, column=0, columnspan=2, pady=15)

root.mainloop()

