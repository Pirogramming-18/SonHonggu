from django.shortcuts import render, redirect
from server.apps.ideas.models import Idea, Devtool

def ideas_list(request, *args, **kwargs):
    search_mode = request.GET.get('search_mode')
    context = {
        'option_list' : ['기본', '찜하기순', '이름순', '등록순', '최신순']
    }
    if search_mode:
        if search_mode == '기본':
            ideas = Idea.objects.all()
            default_option = '기본'
        # elif search_mode == '찜하기순':
        #     ideas = Idea.objects.order_by('title')
        #     default_option = '찜하기순'
        elif search_mode == '이름순':
            ideas = Idea.objects.order_by('title')
            default_option = '이름순'
        elif search_mode == '등록순':
            ideas = Idea.objects.order_by('-created_at')
            default_option = '등록순'
        elif search_mode == '최신순':
            ideas = Idea.objects.order_by('-updated_at')
            default_option = '최신순'
    else:
        ideas = Idea.objects.all()
        default_option = '기본'
        
    context['ideas'] = ideas
    context['default_option'] = default_option
    return render(request, "ideas/ideas_list.html", context=context)

def ideas_create(request, *args, **kwargs):
    if request.method == "POST":
        devtool_id = request.POST["devtool"]
        Idea.objects.create(
            title=request.POST["title"],
            image=request.FILES.get("image"),
            content=request.POST["content"],
            interest=request.POST["interest"],
            devtool=Devtool.objects.get(id=devtool_id),
        )
        new = Idea.objects.last()
        return redirect("/ideas/{}".format(new.id))
    
    devtools = Devtool.objects.all()
    
    context = {
        'devtools' : devtools,
    }
    
    return render(request, "ideas/ideas_create.html",context=context)

def ideas_read(request, pk, *args, **kwargs):
    idea = Idea.objects.get(id=pk)
    
    context = {
        'idea' : idea,
    }
    
    return render(request, "ideas/ideas_read.html", context=context)

def ideas_update(request, pk, *args, **kwargs):
    idea = Idea.objects.get(id=pk)
    devtools = Devtool.objects.all()
    
    context = {
        'idea' : idea,
        'devtools' : devtools,
    }
    
    if request.method == "POST":
        devtool_id = request.POST["devtool"]
        
        idea.title=request.POST["title"]
        if request.FILES.get("image"):
            idea.image=request.FILES["image"]
        if request.POST.get("check"):
            idea.image = None
        idea.content=request.POST["content"]
        idea.interest=request.POST["interest"]
        if devtool_id:
            idea.devtool=Devtool.objects.get(id=devtool_id)
        idea.save()
        return redirect("/ideas/{}".format(idea.id))
    
    return render(request, "ideas/ideas_update.html", context=context)

def ideas_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("/")

##############################################################################################################

def devtools_list(request, *args, **kwargs):
    devtools = Devtool.objects.all()
    
    context = {
        "devtools" : devtools,
    }
    
    return render(request, "devtools/devtools_list.html", context=context)
    
def devtools_create(request, *args, **kwargs):
    if request.method == "POST":
        Devtool.objects.create(
            name=request.POST["name"],
            kind=request.POST["kind"],
            content=request.POST["content"],
        )
        new_devtool = Devtool.objects.last()
        return redirect("/devtool/{}".format(new_devtool.id))
    return render(request, "devtools/devtools_create.html")
    
def devtools_read(request, pk, *args, **kwargs):
    devtool = Devtool.objects.get(id=pk)
    all_ideas = devtool.idea_devtool.all()
    context = {
        'devtool' : devtool,
        'all_ideas' : all_ideas
    }
    
    return render(request, "devtools/devtools_read.html", context=context)

def devtools_update(request, pk, *args, **kwargs):
    devtool = Devtool.objects.get(id=pk)
    
    context = {
        'devtool' : devtool,
    }
    
    if request.method == "POST":
        devtool.name = request.POST["name"]
        devtool.kind = request.POST["kind"]
        devtool.content = request.POST["content"]
        devtool.save()
        return redirect("/devtool/{}".format(devtool.id))
        

    return render(request, "devtools/devtools_update.html", context=context)

def devtools_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        devtool = Devtool.objects.get(id=pk)
        devtool.delete()
    return redirect("/devtool")