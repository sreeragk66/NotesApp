from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,UpdateView,DeleteView
from notes.models import Note
from django.contrib import messages
from notes.forms import NoteCreationForm

# Create your views here.

class NoteCreateView(View):

    def get(self,request):
        form=NoteCreationForm()
        return render(request,"home.html",{"form":form})
    def post(self,request):
        form=NoteCreationForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Note saved")
            return redirect("display")
        else:
            messages.error(request,"Error while creating note..!")

class NoteDisplayView(TemplateView):
    template_name="display.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        notes = Note.objects.all()
        context["allnotes"]=notes
        return context

class NoteEditView(UpdateView):
    model=Note
    form_class=NoteCreationForm
    template_name="edit.html"
    success_url = reverse_lazy("display")
    pk_url_kwarg = "note_id"

    def form_valid(self, form):
        messages.success(self.request,"Note has been updated")
        self.object=form.save()
        return super().form_valid(form)

def DeleteNote(request,*args,**kwargs):
    note_id=kwargs.get("note_id")
    qs=Note.objects.get(id=note_id)
    qs.delete()
    messages.error(request, "Note has been deleted")
    return redirect("display")









