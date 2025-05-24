import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

def index(request):
    aticles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': aticles})


def create_article(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        article = Article.objects.create(
            titre=['title'],
            contenu=['content'],
            auteur=['author'],
        )
        return JsonResponse({
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'author': article.author,
            'date': article.date_creation.strftime('%y/%m/%d'),
        })
    


def update_article(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            article = Article.object.get(id=id)
            article.titre= data['title']
            article.contenu = data['content']
            article.auteur = data['author']
            article.save()
            return JsonResponse({
                'id': article.id,
                'title': article.title,
                'content': article.content,
                'author': article.author,
            })
        except Article.DoesNotExist:
            return JsonResponse({'error': 'Article non trouve'}, status=404)
        
    
def delete_article(request, id):
    if request.method == 'POST':
        try:
            article = Article.object.get(id=id)
            article.delete()
            return JsonResponse({'message': 'Article supprime avec succes'})
        except Article.DoesNotExist:
            return JsonResponse({'error': 'Article non trouve'}, status=404)
        

def get_article(request, id):
    try:
        article = Article.object.get(id=id)
        return JsonResponse({
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'author': article.author,
        })
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article non trouve'}, status=404)
    
