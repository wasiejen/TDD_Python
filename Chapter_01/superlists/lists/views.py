from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse("<html>\
		<title>To-Do lists</title>\
		<p>This is my first line.\
		<br>This is my second line.</p>\
		<p>This is a new paragraph</p>\
		</html>")


