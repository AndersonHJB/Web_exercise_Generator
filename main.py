from uuid import uuid1


class Web_exercise_Generator():
	def __init__(self):
		self.path_list = ["template/template01.txt", "template/template02.txt"]
	
	def read(self):
		html_lst = []
		for path in self.path_list:
			with open(path, "r", encoding="utf-8")as f:
				# print(f.read())
				html_lst.append(f.read())
		return html_lst
	
	def parse_suffix(self, filename):
		filename_lst = filename.split(".")
		# print(filename_lst)
		suffix = filename_lst[-1].lower()
		# print(f"suffix:{suffix}")
		if suffix != "html":
			filename += ".html"
			return filename
		elif suffix == "html":
			return filename
		else:
			pass
	
	def generator(self, html_lst, question, save_filename):
		filename = self.parse_suffix(save_filename)
		r_html = html_lst[0] + question + html_lst[1]
		with open(filename, "w", encoding="utf-8")as f:
			f.write(r_html)


if __name__ == '__main__':
	html_content = input("Please enter your HTML:>>>")
	save_filename = input("Please enter the name of the file you want to save:>>>")
	
	web = Web_exercise_Generator()
	html_lst = web.read()
	web.generator(html_lst, html_content, save_filename)
