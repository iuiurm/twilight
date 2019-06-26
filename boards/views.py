from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import Streamer, Video, Data


@require_GET
def index(request):
    context = {
        'latest_question_list': "test",
    }
    return render(request, 'home2.html', context)

@require_GET
def streamer(request):
    streamers = Streamer.objects.all()
    context = {'streamers': streamers}
    return render(request, 'streamer.html', context)


# video 의 리스트
@require_GET
def video(request, streamer_sid):
    streamer_instance = Streamer.objects.get(sid=streamer_sid)
    videos = Video.objects.filter(streamer_id=streamer_instance.id)
    context = {'videos': videos, 'streamer': streamer_instance}
    return render(request, 'video_list.html', context)


@require_GET
def chat(request, streamer_sid, video_vid):
    # date time을 chat으로부터 가지고 와야함.
    #for 문을 돌려서 입력한 시간의 갯수만큼 버튼을 만들건데, for문을 def Data Table을 통해 돌릴 것이기 때문.
    # video로 돌릴경우 시간 값을 뽑을 수가없다. for문을 돌려서 걸리는 시간값만큼 button 생성.
    data_instance = Data.objects.all()
    streamer_instance = Streamer.objects.get(sid=streamer_sid)
    video = Video.objects.get(vid=video_vid)
    context = {'video': video, 'streamer': streamer_instance, 'datas' : data_instance}




    return render(request, 'chat.html', context)
