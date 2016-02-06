from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from .models import Problem, Answer
from django.views import generic
from django.utils import timezone
from .forms import ProblemForm

#VIEW STUFF
class IndexView(generic.ListView):
	template_name = 'quiz/index.html'
	context_object_name = 'problem_list'
	def get_queryset(self):
		return Problem.objects.all()

class TakeView(generic.DetailView):
	model = Problem
	template_name = 'quiz/take.html'
	def get_queryset(self):
		return Problem.objects.all()

class EditView(generic.ListView):
	template_name = 'quiz/edit.html'
	context_object_name = 'problem_list'
	def get_queryset(self):
		return Problem.objects.all()

class ResultsView(generic.DetailView):
	model = Problem
	template_name = 'quiz/results.html'

class AddProblemView(generic.ListView):
	template_name = 'quiz/add_problem.html'
	context_object_name = 'problem_list'
	def get_queryset(self):
		return Problem.objects.all()

class EditProblemView(generic.DetailView):
	model = Problem
	template_name = 'quiz/edit_problem.html'


#Delete function. Since the Answer objects are related to Problem, they get deleted too.
def deleteProblem(request, problem_id):
	problem = get_object_or_404(Problem, pk=problem_id)
	problem.delete()
	return HttpResponseRedirect(reverse('quiz:edit'))

#This function is called when the user selects the 'Add Question' button on add_question.html
#Checks to make sure the information was filled in correctly and gives an error message if otherwise
def addLogic(request):
	problem = None
	problemCanBeMade = False
	if len(request.POST['problem_value']) < 1:
		return render(request, 'quiz/add_problem.html', {
			'error_message': "You didn't provide a question.",
		})
	for i in range(1,5):
		if len(request.POST['answer_value'+str(i)]) > 0:
			print request.POST.get('is_correct', 0)
			if request.POST.get('is_correct', 0) > 0:
				problemCanBeMade = True
				break
	if problemCanBeMade:
		problem = Problem(problem_text=request.POST['problem_value'])
		problem.save()
		for i in range(1,5):
			if len(request.POST['answer_value'+str(i)]) > 0:
				answer = Answer(answer_text=request.POST['answer_value'+str(i)])
				if int(request.POST.get('is_correct', 0)) == i:
					answer.is_correct = True
				answer.save()
				problem.answer_set.add(answer)
				problem.save()
			elif int(request.POST.get('is_correct', 0)) == i:
				problem.delete()
				return render(request, 'quiz/add_problem.html', {
					'error_message': "The correct answer did not have a value.",
				})
		return HttpResponseRedirect(reverse('quiz:edit'))
	else:
		return render(request, 'quiz/add_problem.html', {
			'error_message': "You didn't provide a correct answer.",
		})


#This function is called when the user selects the 'Next Question' button on take.html
#It adds up the score and number of problems as it goes
def choose(request, problem_id):
	problem = get_object_or_404(Problem, pk=problem_id)
	min_id = problem.id

	for p in Problem.objects.all():
		if p.id < min_id:
			min_id = p.id
	if problem.id == min_id:
		problem.cur_score = 0
		problem.num_problems = 1
	try:
		selected_answer = problem.answer_set.get(pk=request.POST['answer'])
	except (KeyError, Answer.DoesNotExist):
		return render(request, 'quiz/take.html', {
			'problem': problem,
			'error_message': "You didn't select an answer.",
		})
	else:
		if selected_answer.is_correct:
			if problem.id > min_id:
				last_problem = Problem.objects.filter(id__lt=problem.id).order_by("-id")[0:1].get()
				problem.cur_score = last_problem.cur_score + 1
				#problem.cur_score = Problem.objects.get(id=(problem.id - 1)).cur_score + 1
			else:
				problem.cur_score = 1
		else:
			if problem.id > min_id:
				last_problem = Problem.objects.filter(id__lt=problem.id).order_by("-id")[0:1].get()
				problem.cur_score = last_problem.cur_score
				#problem.cur_score = Problem.objects.get(id=(problem.id - 1)).cur_score
		if problem.id > min_id:
			last_problem = Problem.objects.filter(id__lt=problem.id).order_by("-id")[0:1].get()
			problem.num_problems = last_problem.num_problems + 1
		try:
			next_problem = Problem.objects.filter(id__gt=problem.id).order_by("id")[0:1].get()
			return HttpResponseRedirect(reverse('quiz:take', args=(next_problem.id,)))
		except Problem.DoesNotExist:
			next_problem = problem
			return HttpResponseRedirect(reverse('quiz:results', args=(next_problem.id,)))