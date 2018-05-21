# -*- coding: utf8 -*-
import discord
import requests
import sqlite3
import re

client = discord.Client()

@client.event
async def on_ready():
	print("-"*20)
	print("ユーザー名：", client.user.name)
	print("ユーザーID：", client.user.id)
	print("-"*20)

@client.event
async def on_message(message):
	if not message.author.id == client.user.id:
		atsumori = r".*[あアｱ].*[つツﾂ].*[もモﾓ].*"
	
		if message.content == "ustlist":
			con = sqlite3.connect("ustl_twi.db")
			cur = con.cursor()
			cur.execute("select * from ch where etc = 'twitch' order by name")
			cnt = 0
			for row in cur:
				url = "https://api.twitch.tv/kraken/streams/" + row[1]
				# Twitch API key を入れる
				data = {"client_id": ""}
				r = requests.get(url, params=data)
				
				if not re.compile('"stream":null').search(r.text):
					await client.send_message(message.channel, row[0])
					await client.send_message(message.channel, "https://www.twitch.tv/" + row[1])
					cnt = cnt + 1
					
				print("リクエストURL：", url)
			cur.close()
			if cnt == 0:
				await client.send_message(message.channel, "だれも配信してないよ")
			else:
				await client.send_message(message.channel, str(cnt) + "人配信してるね！すごーい！")
		
		
		elif message.content == "tubelist":
			con = sqlite3.connect("tubelist,db")
			cur = con.cursor()
			cur.execute("select * from ch")
			cnt = 0
			for row in cur:
				url = "https://"
			
			cur.close()
		
		
		if message.content.find("プニキ") != -1:
			await client.send_message(message.channel, "https://kids.yahoo.co.jp/games/sports/013.html")
			
		if message.content.find("ちょっと") != -1:
			await client.send_message(message.channel, "ちょっとだけに")
			
		if re.match(r".*[あアｱ].*[つツﾂ].*[もモﾓ].*", message.content):
			await client.send_file(message.channel, "atsumori.png")
			
		if re.match(r".*[うウｳ].*[さサｻ].*[みミﾐ].*[んンﾝ].*", message.content):
			await client.send_file(message.channel, "usamin.mp4")
		
	print("投稿者：", message.author)
	print("メッセージ：", message.content)

# Discord API key を入れる
client.run("")
