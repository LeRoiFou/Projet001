# Test projet n°001

Date :19/11/2025 <br>
Editeur : Laurent Reynaud

## Arborescence

L'arborescence doit comprendre à la racine :

- un répertoire "app", comprenant :
  - le fichier principal python (main.py ou app.py...)
  - le fichier vide \_\_init\_\_.py
  - des sous-répertoires (assets, treatments, data, templates, static...)
- le fichier README.md
- le fichier Dockerfile
- le fichier .dockerignore

---

## Fichier requirements.txt

- Construire le fichier requirements.txt à la racine du programme dans le terminal : <br>
  `pip freeze > requirements.txt`
- Vérifier qu'il n'y a pas de conflit de versions entre les librairies en saisissant dans le terminal : <br>
  `pip install -r requirements.txt`
- Saisir ceci dans le terminal pour vérifier que le type d'encodage appliqué sur le fichier requirements.txt (normalement encodage UTF-8) : <br>
  `python -c "import chardet; raw=open('requirements.txt','rb').read(); print(chardet.detect(raw))"`
- Si le résultat n'est pas un encodage de type UTF-8 (plutôt de l'encodage UTF-16 qui ressort), saisir ceci dans le terminal pour convertir le fichier requirements.txt en encodage UTF-8, afin que le build de docker puisse bien interpréter ce fichier .txt : <br>
  `Get-Content requirements.txt | Set-Content -Encoding UTF8 requirements-utf8.txt
Remove-Item requirements.txt
Rename-Item requirements-utf8.txt requirements.txt
`
- Pour installer de nouvelles librairies, <font color='yellow'>on risque de retomber sur un encodage UTF-16 de notre fichier requirements.txt</font>. Pour éviter cela, à chaque nouvelles librairies à rajouter dans le fichier requirements.txt, au lieu de saisir ceci dans le terminal : <br>
  `pip freeze > requirements.txt` <br>
  Saisir ceci : <br>
  `pip freeze | Out-File -Encoding utf8 requirements.txt`

---

## Docker (en local)

- Créer le fichier Dockerfile
- Créer le fichier .dockerignore
- Ouvrir l'application Docker Desktop
- Dans le terminal, saisir l'instruction suivante pour construire (build) l'image python :
  `docker build --no-cache -t nomImage .` (nomImage : nom de l'image donné à l'application -> ici c'est <font color="yellow">dash-analyse</font>)
- Toujours dans le terminal, saisir ensuite l'instruction suivante pour lancer l'image dockerisée : `docker run -p 8050:8050 nomImage`
- Tester l'application en saisissant en URL d'une page web : `http://localhost:8050`
