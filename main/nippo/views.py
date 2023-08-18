from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from .models import NippoModel
from .forms import NippoFormClass, NippoModelForm
from django.urls import reverse, reverse_lazy

# Create your views here.
class NippoListView(ListView):
    template_name = "nippo/nippo-list.html"
    model = NippoModel
    def get_queryset(self):
        qs = NippoModel.objects.all()
        if self.request.user.is_authenticated:
            qs = qs.filter(Q(public=True)|Q(user=self.request.user))
        else:
            qs = qs.filter(public=True)
        qs = qs.order_by("-timestamp")
        return qs


class NippoDetailView(DetailView):
    template_name = "nippo/nippo-detail.html"
    model = NippoModel


class NippoCreateModelFormView(CreateView):
    template_name = "nippo/nippo-form.html"
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")
    
    
class NippoUpdateModelFormView(UpdateView):
    template_name = "nippo/nippo-form.html"
    model = NippoModel
    form_class = NippoModelForm
    success_url = reverse_lazy("nippo-list")


class NippoDeleteView(DeleteView):
    template_name = "nippo/nippo-delete.html"
    model = NippoModel
    success_url = reverse_lazy("nippo_list")



















class NippoCreateFormView(FormView):
    template_name = "nippo/nippo-form.html"
    form_class = NippoFormClass
    success_url = reverse_lazy("nippo-list")
    def form_valid(self, form):
        data = form.cleaned_data
        obj = NippoModel(**data)
        obj.save()
        return supre().form_valid(form)

def nippoListView(request):
    template_name = "nippo/nippo-list.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs
    return render(request, template_name, ctx)


def nippoDetailView(request,pk):
    template_name = "nippo/nippo-detail.html"
    ctx = {}
    q = get_object_or_404(NippoModel, pk=pk)
    ctx["object"] = q
    return render(request, template_name, ctx)


def nippoCreateView(request):
    template_name = "nippo/nippo-form.html"
    form = NippoFormClass(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        title = request.POST["title"]
        content = request.POST["content"]
        obj = NippoModel(title=title,content=content)
        obj.save
        return redirect("nippo-list")
    return render(request, template_name, ctx)


def nippoUpdateFormView(request, pk):
    template_name = "nippo/nippo-form.html"
    obj = get_object_or_404(NippoModel, pk=pk)
    initial_values = {"title": obj.title, "content": obj.content}
    form = NippoFormClass(request.POST or initial_values)
    ctx = {"form": form}
    ctx["object"] = obj
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj.title = title
        obj.content = content
        obj.save()
        if request.POST:
            return redirect("nippo-list")
    return render(request, template_name, ctx)


def nippoDeleteView(request, pk):
    template_name = "nippo/nippo-delete.html"
    obj = get_object_or_404(NippoModel, pk=pk)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("nippo-list")
    return render(request, template_name, ctx)

