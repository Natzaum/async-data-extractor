import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

login_url = os.getenv("LOGIN_URL")
patient_url = os.getenv("PATIENT_URL")


async def login(session, username, password):
    async with session.post(
        login_url,
        data={"usuario": username, "senha": password},
        timeout=aiohttp.ClientTimeout(total=10),
    ) as response:
        await response.text()
        return


async def get_patient_page(session, patient_id):
    async with session.get(
        patient_url.format(patient_id), timeout=aiohttp.ClientTimeout(total=10)  # type: ignore
    ) as response:
        return await response.text()


def is_session_valid(text):
    text = text.lower()
    return not (
        "sua sessão expirou" in text
        or "fazer login novamente" in text
        or ("alert(" in text and "sessão" in text)
    )
