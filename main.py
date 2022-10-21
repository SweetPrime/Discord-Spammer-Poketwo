from webserver import keep_alive
import requests

channelID = 942823381760352269
headers = {
    "authorization":
    "MTAzMzAyMjkzODUyNzU4NDMyNg.GJLVgl.ECMSLIlOwWNt5y2cuI_iLy2fRNucQp4bozUb3Y"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
