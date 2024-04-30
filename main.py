from api_lib import *
import json

def main() -> None:
    team_number = 8293

    respuesta = get_team_info(team_number)
    print(type(respuesta))
    respuesta = json.dumps(respuesta, indent = 4)

    print(respuesta)

if __name__ == "__main__":
    main()