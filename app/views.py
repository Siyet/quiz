from django.shortcuts import render
from .models import Team, Question, Category

# Create your views here.
def startPage(request):
    return render(request, 'app/start.html', {})

def teams(request):
    if request.POST:
        Team.create(title=request.POST['title'], order_num=int(request.POST['order_num']))
    teams = Team.objects.all()
    return render(request, 'app/teams.html', {'teams': teams})

def question(request, cat_id):
    team = Team.objects.all()[0]
    answer_id = None
    # raise Exception(request.GET)
    if request.GET.get('a_id'):
        question = Question.objects.get(id=int(request.GET['q_id']))
        question.is_public = False
        question.save()
        if request.GET['correctly'] == 'true':
            team.points += 1
        team.games_num += 1
        team.save()
        answer_id = request.GET['a_id']
    else:     
        question = Question.objects.filter(category__id=cat_id, is_public=True)[0] if Question.objects.filter(category__id=cat_id, is_public=True).count() else None
    return render(request, 'app/question.html', { 'cat_id':cat_id, 'question': question, 'team': team, 'answer_id': answer_id})

def question1(request, cat_id = 42):
    # team = Team.objects.all()[0]
    answer_id = None
    # raise Exception(request.GET)
    if request.GET.get('a_id'):
        question = Question.objects.get(id=int(request.GET['q_id']))
        question.is_public = False
        question.save()
        if request.GET['correctly'] == 'true':
            # team.points += 1
            pass
        # team.games_num += 1
        # team.save()
        answer_id = request.GET['a_id']
    else:     
        question = Question.objects.filter(category__id=cat_id, is_public=True)[0] if Question.objects.filter(category__id=cat_id, is_public=True).count() else None
    return render(request, 'app/question1.html', { 'cat_id':cat_id, 'question': question, 'answer_id': answer_id})

def categories(request):
    team = Team.objects.all()[0]
    categories = Category.objects.filter(is_public=True)
    return render(request, 'app/categories.html', {'categories': categories, 'team': team})