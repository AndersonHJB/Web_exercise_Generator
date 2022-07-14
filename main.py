import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

class Web_exercise_Generator():
	def read(self):
		with open("./template_html/template_html.html", "r", encoding="utf-8")as f:
			# print(f.read())
			return f.read()
	def generator(self, html, question):
		html = html.format(content=question)
		with open("")
	
if __name__ == '__main__':
	web = Web_exercise_Generator()
	html = web.read()
	web.generator(html)