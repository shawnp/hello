from django.shortcuts import render

# Create your views here.
def index(request):
	#this is our new def def view
	return render(request, 'index.html')
