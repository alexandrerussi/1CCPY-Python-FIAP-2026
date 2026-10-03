from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREATE / READ / UPDATE / DELETE

# READ
def read_leads():
    return json.loads(DB_PATH.read_text(encoding="utf-8")) # desafio: try/except

# CREATE
def create_lead(lead_dict):
    leads = read_leads() # DESAFIO....
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

# READ com BUSCA
def read_leads_search(query):
    leads = read_leads()
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["email"]}".lower()
        # print(txt_lead)

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results

# EXPORT CSV
def export_csv():
    """Exportar leads para CSV e RETORNAR o caminho do arquivo"""
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for lead in leads:
                writer.writerow(lead)
        return path_csv
    except PermissionError:
        return None