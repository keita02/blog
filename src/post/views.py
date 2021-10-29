from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Category, Author, PostView
from marketing.models import SignUp
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import CommentForm, PostForm
from django.views.generic import CreateView, DeleteView, UpdateView, ListView 
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import decorators

# RECUPERER L'EDITEUR DE L'ARTICLE

def get_author(user):
	qs = Author.objects.filter(user=user)
	if qs.exists():
		return qs[0]
	return None

#----------------------------------------------------------------------------------------------#
# FONCTION DE RECHERCHE
def search(request):

	queryset = Post.objects.all()
	query = request.GET.get('q')
	search_count = query.count

	if query:

		queryset = queryset.filter(Q(title__icontains=query) | Q(overview__icontains=query)  ).distinct()

	print(queryset.count)

	context = {

		'queryset' : queryset,

	}

	return render(request, 'search_results.html', context)



#----------------------------------------------------------------------------------------------#
# RECUPERER LE NOMBRE D'ARTICLE ASSOCIE A UNE CATEGORIE
def get_category_count():
	queryset = Post.objects.values('category__title').annotate(Count('category__title'))
	return queryset
#----------------------------------------------------------------------------------------------#

# PAGE D'ACCUEIL
def index(request):
	queryset = Post.objects.filter(featured=True).all()
	latest = Post.objects.order_by('-timestamp')[0:3]

	if request.method == 'POST':
		email = request.POST['email']
		new_signup = SignUp()
		new_signup.email = email
		new_signup.save()

		messages.success(request, 'Vous venez de souscrire à la Newsletter avec succès')

	context = {

		'object_list': queryset,
		'latest'     : latest,
	}

	return render(request, 'index.html', context)

#----------------------------------------------------------------------------------------------#
# PAGE DU BLOG
def blog(request):

	category_count   = get_category_count()
	per_page         = 4
	recent           = 3
	page_request_var = 'page'
	post_list        = Post.objects.all()
	paginator        = Paginator(post_list, per_page)
	most_recent      = Post.objects.order_by('-timestamp')[:recent]
	page             = request.GET.get(page_request_var)

	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)


	context = {
		'queryset'         : paginated_queryset,
		'page_request_var' : page_request_var,
		'most_recent'      : most_recent,
		'category_count'   : category_count,
	}

	return render(request, 'blog.html', context)



#----------------------------------------------------------------------------------------------#
# LISTE DE TOUS LES ARTICLES

def post(request, id):
	recent  = 3
	category_count   = get_category_count()
	post_detail      = get_object_or_404(Post, id=id)
	most_recent      = Post.objects.order_by('-timestamp')[:recent]
	form             = CommentForm(request.POST or None)


	if request.user.is_authenticated:
		PostView.objects.get_or_create(user=request.user, post=post_detail)

	form = CommentForm(request.POST or None)


	if request.method == 'POST':

		if form.is_valid():
			form.instance.user = request.user
			form.instance.post = post_detail
			form.save()

			return redirect(reverse('post', kwargs={'id':post_detail.pk}))


	context = {
	'post'           : post_detail,
	'most_recent'    : most_recent,
	'category_count' : category_count,
	'form'			 : form,

	}
	return render(request, 'post.html', context)


#----------------------------------------------------------------------------------------------#
# FORMULAIRE D'EDITION D'UN ARTICLE
def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	titre = 'Rediger un article'
	author = get_author(request.user)

	if request.method == 'POST':
		if form.is_valid():
			form.instance.author = author
			print(form.instance.author)
			form.save()
			return redirect(reverse('post', kwargs={'id':form.instance.id}))
	context = {
		'form':form,
		'titre': titre,
	}

	return render(request, 'post_create.html', context)

#----------------------------------------------------------------------------------------------#
# MODIFIER UN ARTICLE
@login_required
def post_update(request, id):

	post = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=post)
	titre = 'Modifier l\'article'
	author = get_author(request.user)

	if author == post.author:
		if request.method == 'POST':
			if form.is_valid():
				form.instance.author = author
				print(form.instance.author)
				form.save()
				return redirect(reverse('post', kwargs={'id':form.instance.id}))
	else:
		raise Http404

	context = {
		'form':form,
		'titre': titre,
	}

	return render(request, 'post_create.html', context)
#----------------------------------------------------------------------------------------------#
# SUPPRIMER UN ARTICLE
@login_required
def post_delete(request, id):
	post = get_object_or_404(Post, id=id)
	author = get_author(request.user)

	if author == post.author:
		post.delete()
		return redirect(reverse('blog'))
	else:
		raise Http404


# CREATION D'UN ARTICLE
# @login_required
# def post_create(request):

# 	title = 'Créer'
# 	form = PostForm(request.POST or None, request.FILES or None)

# 	if request.method == 'POST':
# 		if form.is_valid():
			
# 			form = form.save(commit=False)
# 			form.user = request.user
# 			print(form.user)
# 			form.save()
# 			return redirect(reverse('post', kwargs={'id':form.id}))
# 	else:
# 		form = PostForm()

# 	context = {
# 		'titre': title,
# 		'form':form,
# 	}

# 	return render(request, 'post_create.html', context)


#----------------------------------------------------------------------------------------------#
# MODIFICATION D'UN ARTICLE
# @login_required
# def post_update(request, id):

# 	post = get_object_or_404(Post, id=id)
# 	title = 'Modifier'
# 	form = PostForm(request.POST or None, request.FILES or None, instance=post)

# 	if request.user.id == 1:
# 		if request.method == 'POST':
# 			if form.is_valid():
# 				form.instance.author = author
# 				form.save()
# 				return redirect(reverse('post', kwargs={'id':form.instance.id}))
# 	else:
# 		raise Http404

# 	context = {
# 		'titre': title,
# 		'form':form,
# 	}

# 	return render(request, 'post_create.html', context)


#----------------------------------------------------------------------------------------------#
# SUPPRESSION D'UN ARTICLE
# @login_required
# def post_delete(request, id):
# 	post = get_object_or_404(Post, id=id)

# 	if request.user == post.user:
# 		post.delete()
# 		return redirect(reverse("blog"))
# 	else :
# 		raise Http404
	# post = get_object_or_404(Post, pk=id)
	# post.delete()
	# return redirect(reverse('blog')


#----------------------------------------------------------------------------------------------#

# def contact(request):
# 	form = ContactForm()

# 	context = {
# 	  'form' : form
# 	}
	
# 	return render(request, 'contact.html', context)