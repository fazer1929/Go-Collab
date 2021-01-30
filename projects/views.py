from django.shortcuts import render
import json
from projects.forms import CommentForm,ProjectForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from projects.models import Project,Comment
# Create your views here.

# Static Pages
def projects(request):
    projects=Project.objects.order_by('-created_at')
    return render(request,'ui/project.html',{
        "projects":projects
    })

def contact(request):
    return render(request,"ui/contact.html")





def index(request):
    projects = Project.objects.order_by('-created_at')[:3]
    return render(request,"ui/index.html",{
        "projects":projects
    })

def projectCreateView(request):
    if request.method == "POST":
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.owner = request.user
            project.save()
    else:
        project= ProjectForm(prefix="project")
        comment= CommentForm(prefix="comment")
        return render(request,"ui/index.html",{
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
# Sample: EXPECTED JSON data
# {
#     'cmd':"add_appr"/"rem_appr",
#     "project_id":1,
#     "user_id":3
# }
@csrf_exempt
def addUserAproval(request):
    if request.method=="POST":
        data = json.loads(request.body)
        try:
            project_id = int(data['project_id'])
            user_id = int(data['user_id'])
            cmd = data['cmd']
            project = Project.objects.filter(id=project_id)[0]
            user = User.objects.filter(id=user_id)[0]
            if(cmd=="add_appr"):
                project.members_not_approved.add(user)
            elif(cmd=="rem_appr"):
                if(project.members_not_approved.filter(id=user.id) != None):
                    project.members_not_approved.remove(user)
        except:
            return JsonResponse({
                "err":"Bad Request"
            })
        return JsonResponse({
                "message":"Success"
            })


# Sample: EXPECTED JSON data
# {
#     'cmd':"add"/"rem",
#     "project_id":1,
#     "user_id":3
# }
@csrf_exempt
def addUserMember(request):
    if request.method=="POST":
        data = json.loads(request.body)
        try:
            project_id = int(data['project_id'])
            user_id = int(data['user_id'])
            cmd = data['cmd']
            project = Project.objects.filter(id=project_id)[0]
            user = User.objects.filter(id=user_id)[0]
            if(cmd=="add"):
                project.members_present.add(user)
            elif(cmd=="rem"):
                if(project.members_present.filter(id=user.id) != None):
                    project.members_present.remove(user)
        except:
            return JsonResponse({
                "err":"Bad Request"
            })
        return JsonResponse({
                "message":"Success"
            })

# Sample: EXPECTED JSON data
# {
#     "text":"Comment Text",
#     "project_id":3
# }
@csrf_exempt
def addComments(request):
    if request.method=="POST":
        data = json.loads(request.body)
        try:
            project_id = int(data['project_id'])
            text=data['text']
            user = request.user
            project=Project.objects.filter(id=project_id)
            comment = Comment(text=text,owner=user,project=project)
            comment.save()
        except:
            return JsonResponse({
                "err":"Bad Request"
            })
        return JsonResponse({
                "message":"Success"
            })
