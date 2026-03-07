# Aide Google Colab

## Démarrage Rapide

### Ouvrir un Notebook
1. Cliquez sur le badge "Open in Colab" en haut du notebook
2. Ou: [colab.research.google.com](https://colab.research.google.com) → Fichier → Ouvrir → GitHub → `maclandrol/cours-ia-med`

### Sauvegarder Votre Travail
**⚠️ IMPORTANT:** Colab ne sauvegarde PAS automatiquement!
- Fichier → Enregistrer une copie dans Drive
- Utilisez `Ctrl+S` régulièrement

### Exécuter du Code
- Cliquez sur ▶️ ou `Shift+Enter`
- Exécutez les cellules dans l'ordre

---

## Problèmes Courants

### "Module not found" ou "No module named..."

```python
!pip install -q nom_du_module
```

Exemples:
```python
!pip install -q torchxrayvision
!pip install -q transformers
```

### Session Déconnectée ou Expirée

**Cause:** Inactivité ou dépassement de temps (12h max)

**Solution:**
1. Exécution → Redémarrer l'environnement
2. Exécution → Tout exécuter
3. Réexécutez vos cellules depuis le début

### Cellule Qui Tourne Indéfiniment

1. Exécution → Interrompre l'exécution
2. Vérifiez votre code (boucles infinies?)
3. Essayez avec moins de données pour tester

### Erreur de Mémoire (Out of Memory)

**GPU/RAM pleine:**
1. Exécution → Redémarrer l'environnement
2. Réduisez la taille de batch
3. Libérez la mémoire: `del variable_name`

### Fichiers Perdus Après Reconnexion

**Cause:** Les fichiers uploadés sont temporaires

**Solution:**
- Sauvegardez vos données importantes sur Google Drive
- Ou téléchargez-les avant de fermer:
```python
from google.colab import files
files.download('mon_fichier.csv')
```

### Impossible de Télécharger un Fichier

```python
from google.colab import files
uploaded = files.upload()
# Sélectionnez votre fichier dans la fenêtre
```

Pour plusieurs fichiers:
```python
!mkdir -p data
# Puis glissez-déposez dans le dossier "Files" à gauche
```

### Code Qui Fonctionnait Hier Ne Fonctionne Plus

**Causes possibles:**
1. Nouvelles versions de librairies
2. Variables non définies (cellules non exécutées)
3. Ordre d'exécution des cellules incorrect

**Solution:**
- Exécution → Redémarrer et tout exécuter
- Vérifiez les versions:
```python
import torch
print(torch.__version__)
```

---

## Raccourcis Utiles

| Raccourci | Action |
|-----------|--------|
| `Shift+Enter` | Exécuter la cellule et passer à la suivante |
| `Ctrl+Enter` | Exécuter la cellule sans changer de cellule |
| `Ctrl+S` | Sauvegarder |
| `Ctrl+M B` | Ajouter une cellule en dessous |
| `Ctrl+M A` | Ajouter une cellule au-dessus |
| `Ctrl+M D` | Supprimer la cellule |

---

## Activer le GPU

Pour les cours 5-8 (images médicales):

1. Exécution → Modifier le type d'exécution
2. Accélérateur matériel → **GPU**
3. Enregistrer

Vérifier l'activation:
```python
import torch
print(torch.cuda.is_available())  # Doit afficher True
```

---

## Obtenir de l'Aide

### Pendant le Cours
- Levez la main ou posez vos questions
- Utilisez le forum du cours

### En Dehors du Cours
- Consultez d'abord cette aide
- Regardez les erreurs dans le notebook
- Heures de permanence (voir syllabus)

### Messages d'Erreur
**Lisez toujours la dernière ligne de l'erreur en premier!**

Exemple:
```
ValueError: expected 2D input (got 3D input)
```
Cherchez "ValueError" et "expected 2D input" dans la documentation.
