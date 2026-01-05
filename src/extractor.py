from bs4 import BeautifulSoup


def extract_data_patient(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    def value_by_id(id_html):
        field = soup.find(id=id_html)
        return field.get("value", "").strip() if field else ""  # type: ignore

    return {
        "Nome": value_by_id("no_usuario"),
        "Cartao": value_by_id("nr_cns"),
        "Nascimento": value_by_id("dt_nascimento"),
        "DDD": value_by_id("end_ddd_celular"),
        "Celular": value_by_id("end_nr_fone_celular"),
    }
