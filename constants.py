import os

URL: str = 'https://www.thebluealliance.com/api/v3'
READ_KEY: str = os.getenv('TBA_KEY') # KEY FOR READING AT TBA


# Zona de testing
def main() -> None:
    print(READ_KEY)

if __name__ == '__main__':
    main()