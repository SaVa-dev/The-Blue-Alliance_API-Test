import constants as cons
import requests

def get_team_info(team_number: int) -> dict | None:
    url = f"{cons.URL}/team/frc{team_number}"

    headers = {
        "X-TBA-Auth-Key": cons.READ_KEY
    }

    respuesta = requests.get(url, headers = headers)

    print(respuesta.status_code)

    if respuesta.status_code == 200:
        return respuesta.json()
    return None