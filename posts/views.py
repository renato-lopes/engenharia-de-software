from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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
        new_question = Question(title=title, description=description, user=user)
        new_question.save()
        for tag_name in tags.split(','):
            if(len(tag_name) == 0):
                continue
            tag_name = tag_name.strip()
            tag_res = Tag.objects.filter(name=tag_name)
            if (len(tag_res) == 0):
                new_tag = Tag(name=tag_name)
                new_tag.save()
            else:
                new_tag = tag_res[0]
            new_question_tag = QuestionTag(question=new_question, tag=new_tag)
            new_question_tag.save()
        return redirect("/post/"+str(new_question.id))

def post(request,id_post):

    question = get_object_or_404(Question, pk=id_post) #questao clicada pelo usuario
    
    question_tags = QuestionTag.objects.filter(question=id_post)
    tags = []
    for el in question_tags:
        tags.append(el.tag.name)
    
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

def edit_post(request, post_id):
    question = get_object_or_404(Question, pk=post_id)
    
    question_tags = QuestionTag.objects.filter(question=post_id)
    tags = []
    for el in question_tags:
        tags.append(el.tag.name)
        
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
        question.title = title
        question.description = description
        question.save()
        
        QuestionTag.objects.filter(question=post_id).delete()
        
        for tag_name in tags.split(','):
            if(len(tag_name) == 0):
                continue
            print (tag_name)
            tag_name = tag_name.strip()
            tag_res = Tag.objects.filter(name=tag_name)
            if (len(tag_res) == 0):
                new_tag = Tag(name=tag_name)
                new_tag.save()
            else:
                new_tag = tag_res[0]
            new_question_tag = QuestionTag(question=question, tag=new_tag)
            new_question_tag.save()
        return redirect("/post/"+str(question.id))

def delete_post(request, post_id):
    question = get_object_or_404(Question, pk=post_id) #questao clicada pelo usuario
    
    question_tags = QuestionTag.objects.filter(question=post_id)
    tags = []
    for el in question_tags:
        tags.append(el.tag.name)
    
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
        question.delete()
        return redirect("/all-posts")

def tag(request,tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    # tag = Tag.objects.get(id=tag_id)
    print(tag.name)
    
    question_tags = QuestionTag.objects.filter(tag=tag_id)
    questions = []
    for el in question_tags:
        questions.append(Question.objects.get(id=el.question.id))
    
    context = {
        "questions": questions,
        "tag": tag.name
    }


    return render(request, 'tags/tag.html', context)

def edit_answer(request,answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = Question.objects.get(id=answer.question.id)
    question_tags = QuestionTag.objects.filter(question=question.id)
    tags = []
    for el in question_tags:
        tags.append(el.tag.name)
    
    
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
    question = Question.objects.get(id=answer.question.id)
    question_tags = QuestionTag.objects.filter(question=question.id)
    tags = []
    for el in question_tags:
        tags.append(el.tag.name)
    
    
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