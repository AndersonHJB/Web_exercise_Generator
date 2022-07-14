class Web_exercise_Generator():
	def read(self):
		with open("./template_html/template_html.html", "r", encoding="utf-8")as f:
			print(f.read())

if __name__ == '__main__':
	web = Web_exercise_Generator()
	web.read()