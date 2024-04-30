# The Blue Alliance API Testing

This is a project made as a scouting tool for FIRST Robotics Competition.
The project uses [The Blue Alliance](https://www.thebluealliance.com/) information to get the data for the scouting.

## Dependencies needed for the program to work:

### Python Libraries:
- Requests

**Windows systems:**
```bash
pip install requests
```

**UNIX systems:**
```bash
pip3 install requests
```

**Arch Linux repositories (Extra)**
```bash
pacman -S python-requests
```


### API Keys for getting the requests for The Blue Alliance:

For getting the API keys, you need to create an account at https://www.thebluealliance.com/account.<br>
You will need to generate a key at the *Read API Keys* section.

After that, you can either replace the line at constants to put your read key, or the reccomended way, to save it as a *Enviroment Variable* at your system.