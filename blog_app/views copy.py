from django.shortcuts import render, redirect
from django.views import View
from blog_app.models import Category, Blog, About, Comment
from portfolio.models import graphics
from django.db.models import Q
from django.contrib import messages
from blog_app.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


class Product(View):
    def get(self, request):
        # Get all published blogs
        all_blogs = Blog.objects.filter().order_by("-updated_at")
        
        # Paginate the blogs, with 8 blogs per page
        paginator = Paginator(all_blogs, 8)  # Show 8 blogs per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, "product.html", context={"page_obj": page_obj})




class GetPostBySlug(View):
    def get(self, request, slug):
        post = graphics.objects.get(slug=slug)
        return render(
            request,
            "product_detail.html",
            context={
                "post": post,

            },
        )

    # def post(self, request, slug):
    #     if request.user.is_authenticated:
    #         comment = request.POST.get("comment")
    #         if comment.strip() == "":
    #             messages.error(request, "Please fill the required field")
    #             return redirect("post_by_slug", slug=slug)
    #         post = Blog.objects.get(slug=slug)
    #         comment_obj = Comment.objects.create(
    #             comment_text=comment, blog_post=post, commented_by=request.user
    #         )
    #         messages.success(request, "comment saved successfully")
    #         return redirect("post_by_slug", slug=slug)
    #     else:
    #         return redirect("login_user")


class PostsByCategory(View):
    def get(self, request, id):
        try:
            blogs = Blog.objects.filter(status="Published", category_id=id).order_by(
                "-updated_at"
            )
            category = blogs[0].category if blogs else Category.objects.get(id=id)
        except Exception:
            return redirect("home")
        return render(
            request,
            "category_post.html",
            context={"category": category, "blogs": blogs},
        )


class SearchCategory(View):
    def get(self, request):
        searched_posts = []
        keyword = request.GET.get("keyword")
        if keyword and keyword.strip() != "":
            searched_posts = Blog.objects.filter(
                Q(title__icontains=keyword)
                | Q(short_description__icontains=keyword)
                | Q(blog_body__icontains=keyword),
                status="Published",
            )
        else:
            searched_posts = Blog.objects.filter(status="Published")
        return render(
            request,
            "searched_posts.html",
            context={"searched_posts": searched_posts, "keyword": keyword},
        )


class Contact(View):
    def get(self, request):
        context={}
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                message = form.cleaned_data['message']

                form.save()
                messages.success(request,"New Contact Alert!!. ")
                return redirect('contact')
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    