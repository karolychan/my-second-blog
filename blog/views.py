from django.shortcuts import render
#myviews
def post_list(request):
	return render(request, 'blog/post_list.html',{})
	