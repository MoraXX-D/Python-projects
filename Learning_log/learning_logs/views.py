from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """ show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    """ show a single topic and all its entry """
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries': entries}
    return render(request,'learning_logs/topic.html',context)

def new_topic(request):
    """ Add a new topic """
    if request.method != 'POST':
        # No data is submitted; create a blank form
        form = TopicForm()

    else:
        # POST data submitted; process data
        form = TopicForm(request.Post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request,'learning_logs/new_topic.html',context)



