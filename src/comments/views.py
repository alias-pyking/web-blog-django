from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Comment
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from .forms import CommentForm
# Create your views here.
def comment_thread(request,abc):
    obj = get_object_or_404(Comment, id = abc)
    initial_data = {
        'content_type':
        ''
    }
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        # if the form is valid the getting the content_type from the comment_form
        # getting the object id from the comment_form
        # getting the content from the comment_form
        # form that data from form creating the whole comment (Comment model) 
        c_type = comment_form.cleaned_data.get('content_type')
        obj_id = comment_form.cleaned_data.get('object_id')
        content_type = ContentType.objects.get(model=c_type)
        content_data = comment_form.cleaned_data.get('content')
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id = parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()
       
        new_comment,created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            comentText=content_data,
            parent = parent_obj
            )
    context = {
        'comment':obj,
        'comment_form':comment_form,
    }
    return render(request,'comment_thread.html',context)
