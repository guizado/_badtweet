from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from math import floor
from random import choice
import json



def cleanText(text):
	t = ''
	for c in text:
		if ord(c) > 657:
			text = text.replace(c, ' ')
	if len(text) > 139:
	    text += ' ...'
	text = text.split()
	while text[0][0] == '@':
		text.pop(0)
	for word in text:
		if 'https://' not in word:
			t += word + ' '
	return t



class Library():
	
	def __init__(self, lpath, bpath):
		self.BPATH = bpath
		with open(lpath) as f:	
			self.library = json.load(f)
	
		
	def getTemplate(self):
		with open(self.BPATH) as f:
			b = json.load(f)
		if len(b) == 0:
			b = [i for i in range(0, len(self.library))]
		rt = choice(b)
		b.remove(rt)
		with open(self.BPATH, 'w') as f:
			json.dump(b, f)
		return self.library[rt]

		
	def showBag(self):
		with open(self.BPATH) as f:
			b = json.load(f)
		print(b)



class TemplateProccessor():
	'''
	Receives a text string, and writes that text on a given image,
	also known as a template.
	'''

	def __init__(self, text, template):
		self.text = text
		self.MIN_FONT_SIZE = 6
		self.template = template


	def getCPL(self, font_size):
		'''font size -> character per line'''
		return floor(self.template['comprimento'] / (font_size * 0.8125))


	def insertNewline(self, font_size):
		'''
		Transforms initial text into a list of lines, inserting '\n'
		where appropriate, depending on the given font size and size
		of the template
		'''
		t = ''
		cpl = self.getCPL(font_size)
		char_left = cpl

		for palavra in self.text.split(' '):

			#Word too long
			if len(palavra) > cpl:
				#Insert word until line ends
				t += palavra[:char_left-1] + '_\n'
				char_palavra = len(palavra) - char_left + 1
				for i in range(char_palavra // cpl):
					# Fill up the following line(s) depending on the word's lenght
					cp = len(palavra) - char_palavra
					t += palavra[cp : cp+cpl-1] + '_\n'
					char_palavra -= cpl - 1
				#Insert the rest of the word and return to normal
				t += palavra[len(palavra) - char_palavra:] + ' '
				char_left = cpl - char_palavra - 1

			# No space left for the word in the current line
			elif len(palavra) > char_left:
				t += '\n' + palavra + ' '
				char_left = cpl - len(palavra) - 1

			# Default case, there's enough space for the word in the current line
			else:
				t += palavra + ' '
				char_left = char_left - len(palavra) - 1
		return t.split('\n')


	def findFontSize(self):
		'''Finds the adequate font size for a given template and text'''
		f = self.MIN_FONT_SIZE #MIN
		desvios = {}

		#MAX
		while True:
			f += 1
			t = self.insertNewline(f)
			if (len(t) > self.template['altura'] / (f*1.2) or self.getCPL(f) < 10):
				f -= 1
				break
			desvios[f] = self.desvioMaximo(t, f)

		# Find the font size with the minimum deviation
		min_desvio = desvios[self.MIN_FONT_SIZE + 1]
		for k, v in desvios.items():
			if v <= min_desvio:
				min_desvio = v
				f = k
		return f


	def tupleCPL(self, ltext, font_size):
		'''
		Takes a list of lines and a font_size and returns a tuple
		with the number of characters in each line
		'''
		tcpl = ()
		for line in ltext:
			i = 0
			for c in line:
				if c != ' ':
					i += 1
			tcpl += ((i),)
		return tcpl


	def desvioMaximo(self, ltext, font_size):
		'''Returns the maximum character deviance from a list of lines'''
		cpl = self.getCPL(font_size)
		tcpl = self.tupleCPL(ltext, font_size)
		desvios = ()
		for i in tcpl:
			desvios += (abs(i - cpl),)
		return max(desvios)


	def drawText(self, ltext, font_size):
		'''Draws the lines of text onto the image'''
		draw = ImageDraw.Draw(self.img)
		font = ImageFont.truetype("joystix.ttf", font_size)
		y = self.template['altura'] - len(ltext)*font_size*1.2
		p = (self.template['p1'][0], self.template['p1'][1] + (y/2))
		i = 1
		for line in ltext:
			draw.text(p, line, fill='black', font=font)
			p = (p[0], p[1] + font_size*i*1.2)


	def info(self, ltext, font_size):
		'''Prints relevant information'''
		for line in ltext:
			print(line)
		print("\nfont size:", font_size)
		print("\n=========================\n")


	def proccess(self, out, info=False):
		'''Main method'''
		self.img = Image.open(self.template['img_path'])
		f = self.findFontSize()
		t = self.insertNewline(f)
		self.drawText(t, f)
		self.img.save("sample-out/out" + str(out) + ".jpg")
		if info:
			self.info(t, f)



if __name__ == "__main__":
	
	lib = Library("lib.json", "lib_q.json")
	t = lib.getTemplate()
	TemplateProccessor("KKKKK GENTE SABIA QUE SE VC TWITTAR UM OS ABACATES DO MEXICO TE RESPONDEM NA HORA", t).proccess(0)
	
		


