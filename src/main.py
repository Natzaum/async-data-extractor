import os
import csv
import asyncio
import getpass
import aiohttp

from config import CSV_FILE
from loader import load_patient_ids
from extractor import extract_data_patient
from client import login, get_patient_page, is_session_valid
from writer import get_next_queue_number, write_header_if_needed


def get_credentials():
    username = input("Usuário: ").upper()
    password = getpass.getpass("Senha: ")
    return username, password


async def process_patient(semaphore, session, patient, queue_number):
    patient_id, exam_date = patient

    async with semaphore:
        print(f"Processando ID: {patient_id}")

        html = await get_patient_page(session, patient_id)

        if not is_session_valid(html):
            raise RuntimeError("Sessão inválida ou login incorreto.")

        patient_data = extract_data_patient(html)

        return [
            "",
            queue_number,
            patient_data.get("Nome", ""),
            patient_data.get("Cartao", ""),
            patient_data.get("Nascimento", ""),
            f"({patient_data.get('DDD', '')}){patient_data.get('Celular', '')}",
            exam_date,
        ]


async def main():
    username, password = get_credentials()

    patients = load_patient_ids()
    start_queue_number = get_next_queue_number()
    is_new_file = not os.path.exists(CSV_FILE)

    semaphore = asyncio.Semaphore(10)

    async with aiohttp.ClientSession() as session:
        await login(session, username, password)

        tasks = [
            process_patient(semaphore, session, patient, start_queue_number + i)
            for i, patient in enumerate(patients)
        ]

        try:
            results = await asyncio.gather(*tasks)
        except RuntimeError as error:
            print(error)
            print("Processamento interrompido para evitar dados incorretos.")
            return

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        write_header_if_needed(writer, is_new_file)
        writer.writerows(results)


if __name__ == "__main__":
    asyncio.run(main())
