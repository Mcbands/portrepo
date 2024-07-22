from django.shortcuts import render, redirect
from django.views import View
from portfolio.models import graphics
from django.db.models import Q
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            send_mail(
                subject=f'Contact Form Submission from {name}, Subject: {subject}',
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )
            
            return redirect('index')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})





class Index(View):
    def get(self, request):
        # Fetching only the featured graphics and ordering them by the most recent
        featured_graphics = graphics.objects.filter(is_featured=True).order_by('-id')[:3]
        return render(request, 'index.html', {'featured_graphics': featured_graphics})


class About(View):
    def get(self, request):
        return render(request, "about.html")




class Services(View):
    def get(self, request):
        return render(request, "services.html")



class Terms(View):
    def get(self, request):
        return render(request, "terms.html")


class Faq(View):
    def get(self, request):
        return render(request, "faq.html")

class Contact(View):
    def get(self, request):
        return render(request, "contact.html")


class Products(View):
    def get(self, request):
        # Get all published products
        graphs = graphics.objects.all()
        # print(graphs)
        paginator = Paginator(graphs, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "products.html", {"page_obj": page_obj})


# class Products(View):
#     def get(self, request):
#         blogs = Blog.objects.filter(status="Published").order_by("-updated_at")
#         return render(request, "products.html", context={"blogs": blogs})



class GetPostBySlug(View):
    def get(self, request, slug):
        try:
            post = graphics.objects.get(status="Published", slug=slug)
        except graphics.DoesNotExist:
            return HttpResponseRedirect("/404/")  # Redirect or handle the 404 error appropriately

        return render(
            request,
            "product-detail.html",
            context={
                "post": post
            },
        )

