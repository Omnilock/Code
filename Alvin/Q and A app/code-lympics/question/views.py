from django.shortcuts import render_to_response
question_prompts = [
	"What are the color of apples?\n(a) Red\Green\n(b) Purple\n(c) Orange\n\n",
	"What are the color of Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
	"What are the color of strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]



class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer
		
def test(request):
	questions = [
		Question(question_prompts[0], "a"),
		Question(question_prompts[1], "c"),
		Question(question_prompts[2], "b"),	

	]		
	context = {	
	'questions' : questions,
	}

	
	return render_to_response(questions,'question/index.html',context)	

