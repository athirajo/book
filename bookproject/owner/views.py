from django.shortcuts import render, redirect
from owner.forms import BookForm
from django.views.generic import View
from owner.models import Books


# Create your views here.
# addd book
# list all book
# bookdetail
# edit book
# delete book
class AddBook(View):
    def get(selfs, request):
        form = BookForm()
        return render(request, "add_book.html", {"form": form})

    def post(self, request):
        form = BookForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return  redirect("listbook")

          #qs = Books(book_name=form.cleaned_data.get("book_name"),
           #        author=form.cleaned_data.get("author"),
             #      price=form.cleaned_data.get("price"),
             #      copies=form.cleaned_data.get("copies"))
          #qs.save()

        else:
          return render(request, "add_book.html", {"form": form})


class BookList(View):
    def get(self, request):
        qs = Books.objects.all()
        return render(request, "book_list.html", {"books": qs})


class BookDetail(View):
    def get(self, request, *args, **kwargs):
        # pass
        # kwargs={'id':3}
        qs = Books.objects.get(id=kwargs.get("id"))
        return render(request, "book_detail.html", {"book": qs})


class BookDelete(View):
    def get(self, request, *args, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("listbook")

class ChangeBook(View):
    def get(self, request, *args, **kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        form = BookForm(instance=qs)

        return render(request,"book_change.html",{"form":form})


    def post(self,request,*args,**kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        form = BookForm(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
          form.save()
          return redirect("listbook")