# job-analysis-sn
# Analyse du marché de l’emploi au Sénégal (EmploiDakar – Avril/Mai 2025)

## 📌 Description
Le marché de l’emploi au Sénégal évolue rapidement. Ce projet vise à identifier les secteurs porteurs, les types de contrats et les profils recherchés à partir d’un scraping de 259 annonces publiées sur EmploiDakar.com.
  
**Objectif :** 
- Démontrer mes compétences en data collection, cleaning, analysis et visualisation.
- Créer un dashboard interactif pour explorer le marché par secteur, niveau hiérarchique et type de contrat.

---

## 🛠️ Stack technique
- **Python** : BeautifulSoup, Pandas, Matplotlib, Seaborn
- **Power BI** : visualisations interactives
- **IA** : catégorisation des secteurs et niveaux (ChatGPT, DeepSeek)
---

## 📂 Structure du projet
data:
jobs.csv (données brutes scrappées)
enriched_jobs_cleaned.csv (données nettoyées et enrichies)

scraping:
scraping.ipynb

visuals:
dashboard_overview.png
wordcloud_title.png
wordcloud_description.png
3D_scatter.png

dashboard:
job-analysis.pbix

---

## 🔍 Méthodologie

**Collecte des données**
- Source : EmploiDakar.com
- Méthode : Scraping Python (BeautifulSoup)
- Champs extraits : poste, entreprise, localisation, type de contrat, date
- Final count : 259 annonces → 258 après nettoyage


**Nettoyage et structuration**
- Objectif : garantir fiabilité des analyses
- Suppression des doublons et valeurs aberrantes
- Standardisation des formats et dates
- Enrichissement des données
- Ajout de colonnes : secteur, niveau hiérarchique, mots-clés
- Catégorisation assistée par IA pour plus de précision

**Résultats et Insights**

*1. Vue d’ensemble*
- 152 entreprises, 16 secteurs
- Marché concentré : certaines entreprises publient plusieurs annonces, beaucoup restent ponctuelles.
- Insight général: marché actif mais opportunités limitées dans certaines niches.

*2. Types de contrats*
- 74% CDD, 9% stages, 7% CDI, 3% freelance
- Insight : les contrats à durée limités dominent ce qui signifie flexibilité pour les entreprises et insécurité pour les candidats. Stages très limités ce qui met en évidence le manque d'opportunité pour étudiants et jeunes diplômés.

*3. Niveaux hiérarchiques*
- 38% Junior, 31% Senior, 30% Mid, <1% Intern
- Insight : une demande présente de profils juniors mais les postes expérimentés dominent et le type de contrat le plus récurrent pour chaque niveaux est le CDD.

*4. Répartition sectorielle*
- Top secteurs : Technologie, ONG, Recrutement, Finance, Commerce
- Insight : la tech domine, suivi par ONG et finance. Marché numérique en croissance.

*5. Analyse sémantique*
- Mots-clés fréquents : commerce, marketing, gestion, tech
- Insight : convergence entre intitulés et descriptions les compétences clés recherchées sont généralement dans les domaines du commerce, de la gestion et de la tech.

*6. Tendances temporelles*
- Pic de publication entre 11–18 mai
- Insight : certaines entreprises publient en lot → impact sur les tendances journalières.

*7. Interactions secteur / niveau / type de contrat*
Senior en CDD : Finance et ONG → missions spécialisées temporaires
Junior : Tech et Recrutement/Intérim → insertion rapide
Mid : moins dominant → polarisation jeunes entrants vs expérimentés

**Conclusion & Recommandations**
Marché dynamique mais concentré
Contrats majoritairement temporaires → flexibilité pour employeurs mais instabilité pour les candidats
Profils experimentés dominent, les stages se font rares → manque d'opportunités pour étudiants
Dashboard interactif : permet une exploration facile et actionnable pour candidats et recruteurs
Perspectives : étendre la collecte, ajouter variables comme salaire, localisation précise, compétences → insights plus stratégiques


---

## 👩‍💻 Auteur
**Nafissatou LY** – Data Analyst Junior  
💼 [LinkedIn]([https://www.linkedin.com/](https://www.linkedin.com/in/nafissatouly/)) | 📧 lynafi0000@gmail.com
