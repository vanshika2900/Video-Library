from django.shortcuts import render
from posts.models import Post
from searches.models import SearchQuery

def search_view(request):
	query = request.GET.get('q', None)
	user = None
	context = None
	#if request.user.is_authenticated:
	user=request.user
	context = {"query": query}
	#if query is not None:
		#SearchQuery.objects.create(user=user,query=query)
		#blog_list = Post.objects.search(query=query)
		#context['blog_list'] = blog_list
	
	return render(request,'view.html',context)
