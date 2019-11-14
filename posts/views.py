from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

class FileView(APIView):

	parser_classes = (MultiPartParser, FormParser)

	def file(self,request,*args,**kwargs):
		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data,status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def home_page(request):
	context = {"title": " Video Library"}
	return render(request,"home.html",context)


def Post_list_view(request):
	
	qs = Post.objects.all()
	template_name='Post_list.html'
	context={'object_list' : qs}
	return render(request,template_name,context)


def display_record(request,title):
	
	obj = get_object_or_404(Post,title=title)
	my_dict={'object':obj}
	template_name='display_record.html'
	return render(request,template_name,my_dict)
	
@staff_member_required
def model_form_upload(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = PostForm()
	context={'form':form}
	return render(request,'form_upload.html',context)








