from django.shortcuts import render, redirect
 
from .models import Videos
 
# Create your views here.
 
def upload_video(request):
  if request.method == 'POST': 
    title = request.POST['title']
    video = request.POST['video']
    print(video)
      
    content = Videos(title=title,video=video)
    content.save()
    return redirect('videos')
  return render(request,'upload.html')


def display(request):
  videos = Videos.objects.all()
  context ={
      'videos': videos,
  }
  for v in videos:
    print(v.video.url)
    if not v.video.url.startswith('/media/videos'):
      print("ADD")
      # v.video.url = v.video.url.replace('/media', 'media/videos')
    print(v.video.url)
  return render(request,'videos.html',context)