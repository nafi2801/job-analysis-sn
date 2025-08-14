import pandas as pd
import re
import unicodedata

df = pd.read_csv('enriched_jobs.csv')

# Utility: normalize text
def normalize_text(txt):
    if pd.isna(txt):
        return ""
    txt = txt.lower().strip()
    txt = unicodedata.normalize("NFD", txt).encode("ascii", "ignore").decode("utf-8")
    return txt

# Mapping: French labels
sector_patterns = [
    (r"banque|assurance|finance", "Finance et Assurance"),
    (r"call|televent|relation client|centre d'appel", "Service Client et Centres d'Appels"),
    (r"sant[eé]|pharma|clinic|hopital", "Santé et Pharmaceutique"),
    (r"\bong\b|cooperation|unicef|wfp|humanitaire", "ONG et Développement International"),
    (r"tech|informatique|developer|digital|data", "Technologie et Numérique"),
    (r"recrutement|int[ée]rim|cabinet rh", "Recrutement et Ressources Humaines"),
    (r"education|professeur|formation", "Éducation et Formation"),
    (r"agro|laiterie|agriculture|alimentaire", "Agriculture et Agroalimentaire"),
    (r"transport|logist|chauffeur", "Transport et Logistique"),
    (r"btp|batiment|construction", "BTP et Génie Civil"),
    (r"commerce|vente|retail", "Commerce et Vente"),
    (r"marketing|communication|graphiste", "Marketing et Communication"),
    (r"hotel|h[ôo]tel|restaur", "Hôtellerie et Tourisme"),
    (r"manufactur|usine|industrie", "Industrie et Fabrication"),
    (r"energie|mines|petrol", "Énergie et Mines"),
    (r"consult|audit|deloitte", "Conseil et Services Professionnels"),
    (r"immobilier|immo", "Immobilier"),
    (r"securit[yé]", "Sécurité"),
    (r"ambassade|minister|government|public", "Secteur Public et Gouvernemental"),
]

def classify_sector(row):
    search_text = " ".join([
        normalize_text(row.get("sector", "")),
        normalize_text(row.get("description", "")),
        normalize_text(row.get("title", "")),
        normalize_text(row.get("company", "")),
    ])

    for pattern, label in sector_patterns:
        if re.search(pattern, search_text):
            return label
    return "Autre"

# Example integration after scraping
# df = ...  # your scraped DataFrame
df["Secteur_Nettoyé"] = df.apply(classify_sector, axis=1)

# Save cleaned dataset for Power BI
df.to_csv("enriched_jobs_cleaned.csv", index=False, encoding="utf-8-sig")

print("Nettoyage terminé. Colonnes disponibles :", df.columns.tolist())
print(df["Secteur_Nettoyé"].value_counts())
