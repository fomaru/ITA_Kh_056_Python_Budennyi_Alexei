from django.views.generic import UpdateView, ListView, DetailView, FormView, CreateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
from . import models
from .forms import SignUpForm
from django.db.models import Q
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'django_books_app.add_book'
    model = models.Book
    fields = ['title', 'authors', 'cover_img', 'description']
    template_name = 'book_create.html'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        form.save()
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'django_books_app.delete_book'
    model = models.Book
    success_url = reverse_lazy('main_page')
    template_name = 'book_confirm_delete.html'


class BookListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = models.Book
    template_name = 'book_list.html'

    def get_queryset(self):
        return models.Book.objects.filter(added_by=self.request.user).prefetch_related('authors')


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'django_books_app.change_book'
    model = models.Book
    fields = ['title', 'authors', 'cover_img', 'description']
    template_name = 'book_update.html'

    def get_success_url(self):
        return reverse('main_page')


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'django_books_app.add_author'
    model = models.Author
    fields = ['name']
    template_name = 'author_create.html'
    success_url = reverse_lazy('author_create')


class MainPageView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = models.Book
    template_name = 'main_page.html'
    paginate_by = 10


class SearchResultsView(LoginRequiredMixin, ListView):
    model = models.Book
    template_name = 'search_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = models.Book.objects.filter(Q(authors__name__icontains=query) | Q(title__icontains=query)).\
            prefetch_related('authors').distinct()
        return queryset.order_by('-rating')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class BookDetailedView(LoginRequiredMixin, DetailView):
    model = models.Book
    template_name = 'book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = models.Review.objects.filter(book__id__exact=self.kwargs['pk'])
        return context


class CommentFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'django_books_app.add_comment'
    form_class = CommentForm
    template_name = 'review_detail.html'

    def form_valid(self, form):
        form.instance.review = get_object_or_404(models.Review, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.save()
        return super(CommentFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('review_detail', kwargs={'pk': self.kwargs['pk']})


class ReviewView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = ReviewDetailedView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        return view(request, *args, **kwargs)


class ReviewCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'django_books_app.add_review'
    model = models.Review
    fields = ['title', 'review_text']
    template_name = 'review_create.html'

    def get_success_url(self):
        return reverse('review_per_book_list', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form, **kwargs):
        form.instance.book = models.Book.objects.get(pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data()
        contex['book'] = get_object_or_404(models.Book, pk=self.kwargs['pk'])
        return contex


class ReviewDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'django_books_app.delete_review'
    model = models.Review
    success_url = reverse_lazy('review_list')
    template_name = 'review_confirm_delete.html'


class ReviewListView(LoginRequiredMixin, ListView):
    model = models.Book
    template_name = 'review_list.html'

    def get_queryset(self):
        return models.Review.objects.filter(author=self.request.user)


class ReviewUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'django_books_app.change_review'
    model = models.Review
    fields = ['title', 'review_text']
    template_name = 'review_update.html'

    def get_success_url(self):
        return reverse('main_page')


class ReviewListPerBookView(LoginRequiredMixin, ListView):
    model = models.Review
    template_name = 'review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = get_object_or_404(models.Book, pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        query = models.Review.objects.filter(book=get_object_or_404(models.Book, pk=self.kwargs['pk'])).select_related()
        return query


class ReviewDetailedView(LoginRequiredMixin, DetailView):
    model = models.Review
    template_name = 'review_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = models.Comment.objects.filter(review__id__exact=self.kwargs['pk']).select_related().\
            order_by('create_date')
        return context


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        self.object.groups.add(Group.objects.get(pk=2))
        return response


class UserDetailedView(DetailView):
    model = models.User
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = models.Review.objects.filter(author=self.kwargs['pk']).select_related()
        return context
