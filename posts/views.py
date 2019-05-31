from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.http import HttpResponse, HttpResponseNotFound

from users.models import ForumUser as User

from .models import *

@login_required
def create_post(request):

    context = {}
    try:
        # Get data from request
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
    except KeyError:
        return render(request, 'posts/create_post.html', context)
    else:
        username = request.user.username
        user = User.objects.get(username=username)
        new_question = Question.create(title=title, description=description, tags=tags, user=user)
        return redirect("/post/"+str(new_question.id))

def post(request,id_post):

    question = Question.read(id_post)
    if (question == None):
        return HttpResponseNotFound('<h1>Pergunta '+str(id_post)+' não encontrada</h1>')

    question_tags = QuestionTag.search(question = id_post)
    tags = [Tag.read(qt.tag.id) for qt in question_tags]
    
    answers = Answer.objects.filter(question=id_post).order_by("creation_date")

    # Verificação de usuário
    username = request.user.username
    user_id = request.user.id
    if (user_id == None):
        context = {
                "question": question,
                "tags": tags,
                "answers": answers,
                "loged_user": {"id": 0}
        }

    else:
        user = User.objects.get(username=username)
        context = {
                "question": question,
                "tags": tags,
                "answers": answers,
                "loged_user": user
        }
    
    try:
        # Get data from request
        description = request.POST['message']
    except (KeyError):
        return render(request, 'posts/post.html', context)
    else:
        if (user_id == None):
            context['error_message'] = "Você não está logado"
            return render(request, 'posts/post.html', context)
        user = User.objects.get(username=username)
        answer = Answer(description=description, user=user, question=question)
        answer.save()
        # return redirect("/post/"+str(question.id))
        return render(request, 'posts/post.html', context)
        

class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Question, pk=kwargs['id_post']) #questao clicada pelo usuario        
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.upvote.all():
                obj.upvote.remove(user)
            else:
                if user in obj.downvote.all():
                    obj.downvote.remove(user)
                obj.upvote.add(user)
        return url_


class PostDislikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Question, pk=kwargs['id_post']) #questao clicada pelo usuario        
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.downvote.all():
                obj.downvote.remove(user)
            else:
                if user in obj.upvote.all():
                    obj.upvote.remove(user)
                obj.downvote.add(user)
        return url_


class AnswerLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Answer, pk=kwargs['id_post']) #questao clicada pelo usuario   
        obj2 = get_object_or_404(Question, pk=obj.get_question().id)      
        url_ = obj2.get_absolute_url()  
        user = self.request.user
        if user.is_authenticated:
            if user in obj.upvote.all():
                obj.upvote.remove(user)
            else:
                if user in obj.downvote.all():
                    obj.downvote.remove(user)
                obj.upvote.add(user)
        return url_


class AnswerDislikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Answer, pk=kwargs['id_post']) #questao clicada pelo usuario  
        obj2 = get_object_or_404(Question, pk=obj.get_question().id)      
        url_ = obj2.get_absolute_url()  
        user = self.request.user
        if user.is_authenticated:
            if user in obj.downvote.all():
                obj.downvote.remove(user)
            else:
                if user in obj.upvote.all():
                    obj.upvote.remove(user)
                obj.downvote.add(user)
        return url_


def edit_post(request, post_id):
    question = Question.read(post_id)
    if (question == None):
        return HttpResponseNotFound('<h1>Pergunta '+str(post_id)+' não encontrada</h1>')
    
    question_tags = QuestionTag.search(question = post_id)
    tags = [Tag.read(qt.tag.id).name for qt in question_tags]
        
    context = {
        'title': 'Editar pergunta',
        'question': question,
        'tags': tags
    }
    
    # Verificação de usuário
    user_id = request.user.id
    if(user_id != question.user.id):
        context['error_message'] = "Usuário atual não é o criador da pergunta"
        return redirect("/all-posts")
    
    try:
        # Get data from request
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
    except (KeyError):
        return render(request, 'posts/edit_post.html', context)
    else:
        Question.update(id=post_id, title=title, description=description, tags=tags)
        return redirect("/post/"+str(question.id))


def delete_post(request, post_id):
    question = Question.read(post_id)
    if (question == None):
        return HttpResponseNotFound('<h1>Pergunta '+str(post_id)+' não encontrada</h1>')

    question_tags = QuestionTag.search(question = post_id)
    tags = [Tag.read(qt.tag.id).name for qt in question_tags]
    
    answers = Answer.objects.filter(question=post_id).order_by("creation_date")
    
    context = {
        "title": "Excluir pergunta",
        "question": question,
        "answers": answers,
        "tags": tags
    }
    
    # Verificação de usuário
    user_id = request.user.id
    if(user_id != question.user.id):
        context['error_message'] = "Usuário atual não é o criador da resposta"
        return redirect("/post/"+str(question.id))
    
    try:
        # Get data from request
        hidden_confirm = request.POST['hidden_confirm']
    except (KeyError):
        return render(request, 'posts/delete_post.html', context)
    else:
        Question.remove(post_id)
        return redirect("/all-posts")

def tag(request,tag_id):
    tag = Tag.read(post_id)
    if (tag == None):
        return HttpResponseNotFound('<h1>Tag '+str(tag_id)+' não encontrada</h1>')
    question_tags = QuestionTag.search(tag=tag_id)
    questions = [Question.read(qt.question.id) for qt in question_tags]
    
    context = {
        "questions": questions,
        "tag": tag.name
    }


    return render(request, 'tags/tag.html', context)

def edit_answer(request,answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    # question = Question.objects.get(id=answer.question.id)
    question = Question.read(answer.question.id)
    question_tags = QuestionTag.search(question = answer.question.id)
    tags = [Tag.read(qt.tag.id).name for qt in question_tags]
    
    
    context = {
        "title": "Editar resposta",
        "question": question,
        "tags": tags,
        "answer": answer
    }
    
    # Verificação de usuário
    user_id = request.user.id
    if(user_id != answer.user.id):
        context['error_message'] = "Usuário atual não é o criador da resposta"
        return redirect("/post/"+str(question.id))
    
    try:
        # Get data from request
        description = request.POST['description']
    except (KeyError):
        return render(request, 'answers/edit_answer.html', context)
    else:
        answer.description = description
        answer.save()
        return redirect("/post/"+str(question.id))
        

def delete_answer(request,answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    # question = Question.objects.get(id=answer.question.id)
    question = Question.read(answer.question.id)
    question_tags = QuestionTag.search(question = answer.question.id)
    tags = [Tag.read(qt.tag.id).name for qt in question_tags]
    
    context = {
        "title": "Excluir resposta",
        "question": question,
        "tags": tags,
        "answer": answer
    }
    
    # Verificação de usuário
    user_id = request.user.id
    if(user_id != answer.user.id):
        context['error_message'] = "Usuário atual não é o criador da resposta"
        return redirect("/post/"+str(question.id))
    
    try:
        # Get data from request
        hidden_confirm = request.POST['hidden_confirm']
    except (KeyError):
        return render(request, 'answers/delete_answer.html', context)
    else:
        answer.delete()
        return redirect("/post/"+str(question.id))