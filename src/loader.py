import os
from config import IDS_FILE


def load_patient_ids():
    if not os.path.exists(IDS_FILE):
        raise SystemExit("ids.txt não encontrado.")

    patients = []

    with open(IDS_FILE, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()

            if len(parts) != 2:
                raise SystemExit(
                    f"Linha invalida em ids.txt: '{line}'. Esperado: ID data"
                )

            patient_id, exam_date = parts
            patients.append((patient_id, exam_date))

    if not patients:
        raise SystemExit("Sem IDS válidos em ids.txt")

    return patients
