from django.shortcuts import render
from projects.forms import CommentForm,ProjectForm
# Create your views here.

def projectView(request):
    if request.method == "POST":
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.owner = request.user
            project.save()
    else:
        project= ProjectForm(prefix="project")
        comment= CommentForm(prefix="comment")
        return render(request,"projects/index.html",{
            "commentForm":comment,
            "projectForm":project
        })



def commentView(request):
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.owner = request.user
            comment.save()
    else:
        project= ProjectForm(prefix="project")
        comment= CommentForm(prefix="comment")
        return render(request,"projects/index.html",{
            "commentForm":comment,
            "projectForm":project
        })
