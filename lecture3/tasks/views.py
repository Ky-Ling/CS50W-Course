from django.urls import reverse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == 'POST':
        # Process the result of that request 
        #   --> request.POST contains all of the data that the user submitted when they submitted the form
        form = NewTaskForm(request.POST)
        
        # Server-Side
        if form.is_valid():
            # Isolate the task from the "cleaned" version of form data
            task = form.cleaned_data["task"]

            # Add this task to the list of tasks
            request.session["tasks"] += [task]

            # The user will be redirected back to the index page of my tasks application
            return HttpResponseRedirect(reverse("tasks:index"))
        else:

            # We render the user to the add page but we pass in the form that they submitted so that they can see all the errors
            #   they made, they can make modifications to their own submission if they would like to 

            # If the form is invalid, re-render the page with existing information. 
            return render(request, "tasks/add.html", {
                "form": form
            })



    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
    