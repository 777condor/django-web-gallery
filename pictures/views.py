from django.shortcuts import render, redirect
from .models import Album,Picture

# Create your views here.

def home(request):
	album = request.GET.get('album')

	if album == None:
		pictures = Picture.objects.all()

	else:
		pictures = Picture.objects.filter(album__name=album)

	albums = Album.objects.all()
	
	context = {'albums':albums,'pictures':pictures}
	return render(request, 'pictures/home.html', context)

def addPicture(request):
	albums = Album.objects.all()

	if request.method == 'POST':
		data = request.POST
		image = request.FILES.get('image')

		if data['album'] != 'none':
			album = Album.objects.get(id=data['album'])

		elif data['new_album'] != '':
			album, created = Album.objects.get_or_create(name=data['new_album'])

		else:
			album = None

		picture = Picture.objects.create(
			album = album,
			about = data['about'],
			image = image,
			)

		return redirect('home')

	context = {'albums':albums}
	return render(request, 'pictures/add_picture.html',context)

def viewPicture(request, pk):
	picture = Picture.objects.get(id=pk)
	context = {'picture':picture}
	return render(request, 'pictures/view_picture.html', context)