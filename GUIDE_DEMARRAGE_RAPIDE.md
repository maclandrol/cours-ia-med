# Guide de Démarrage Rapide

## Commencer en 5 Minutes

### 1. Ouvrir Google Colab
- Allez sur [colab.research.google.com](https://colab.research.google.com)
- Connectez-vous avec votre compte Google

### 2. Ouvrir un Notebook
- Cliquez sur le badge "Open in Colab" en haut du notebook
- Ou: Fichier → Ouvrir → GitHub → `maclandrol/cours-ia-med`

### 3. Sauvegarder
- Fichier → Enregistrer une copie dans Drive
- Vos modifications seront sauvegardées

### 4. Exécuter le Code
- Cliquez sur ▶️ ou `Shift+Enter`
- Suivez les instructions

---

## Raccourcis Clavier

| Raccourci | Action |
|-----------|--------|
| `Shift+Enter` | Exécuter la cellule |
| `Ctrl+S` | Sauvegarder |
| `Ctrl+M B` | Ajouter une cellule |

---

## Activer le GPU (Optionnel)

Pour accélérer les calculs (cours 5-6):
1. Exécution → Modifier le type d'exécution
2. Accélérateur → **GPU**
3. Enregistrer

---

## Télécharger des Fichiers

```python
from google.colab import files
uploaded = files.upload()
```

---

## Résolution de Problèmes

**"Module not found"**
```python
!pip install -q nom_du_module
```

**Session déconnectée**
- Exécution → Redémarrer l'environnement
- Réexécuter toutes les cellules

**Cellule qui tourne indéfiniment**
- Exécution → Interrompre
- Vérifier le code

---

## Obtenir de l'Aide

- Forum du cours
- Heures de permanence (voir syllabus)
- Documentation dans chaque notebook
