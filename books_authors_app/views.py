from django.shortcuts import render, redirect
from books_authors_app.models import Book, Author
def add_a_book(request):
    print('*'*50)
    print('please add a book')
    print(Book.objects.all())
    print(request)
    context={
        'books_list': Book.objects.all(),
        'author_list': Author.objects.all(),
    }
    return render(request,'add_book.html',context)

def adding_a_book(request):
    print('*'*50)
    print('There is a new book inputed')
    print(f'Method:{request.method}')
    print(request.POST['title'])
    print(request.POST['desc'])
    if request.POST['title'] != "":
        Book.objects.create(title=f"{request.POST['title']}",desc=f"{request.POST['desc']}")
    return redirect('/')

def book_detail(request,x):
    selected_book=Book.objects.get(id=int(x))
    print('*'*50)
    print(f'Book title: {selected_book.title}')
    print(f'Authors: {selected_book.author.all()}')
    all_authors_list=Author.objects.all()
    selected_book_authors=selected_book.author.all()
    other_authors_list=[]
    for i in all_authors_list:
        if i not in selected_book_authors:
            other_authors_list.append(i)
    context={
        'book':selected_book,
        'author': selected_book.author.all(),
        'other_authors_list':other_authors_list,
    }
    return render(request,'book.html',context)

def updating_a_book(request,x):
    print('*'*50)
    print(f'Method:{request.method}')
    # print(request.POST['new_author'])
    authorID=int(request.POST['new_author'])
    sellected_book=Book.objects.get(id=x)
    sellected_author=Author.objects.get(id=authorID)
    sellected_book.author.add(sellected_author)
    print(f'updated-{sellected_book.title}')
    print(f'added an author-{sellected_author.first_name}')
    return redirect(f'/books/{int(x)}')

def add_an_author(request):
    print('*'*50)
    print('please add an author')
    print(Author.objects.all().values())
    print(request)
    context={
        'books_list': Book.objects.all(),
        'authors_list': Author.objects.all(),
    }
    return render(request,'add_author.html',context)

def adding_an_author(request):
    print('*'*50)
    print('There is a new author inputed')
    print(f'Method:{request.method}')
    print(request.POST['first_name']+" "+ request.POST['last_name'])
    print(request.POST['notes'])
    if request.POST['first_name'] != "" and request.POST['last_name'] != "":
        Author.objects.create(first_name=f"{request.POST['first_name']}",last_name=f"{request.POST['last_name']}",notes=f"{request.POST['notes']}")
    return redirect('/author')

def author_detail(request,x):
    selected_author=Author.objects.get(id=int(x))
    print('*'*50)
    print(f'Name: {selected_author.first_name}')
    print(f'Authors: {selected_author.book.all()}')
    all_books_list=Book.objects.all()
    selected_author_books=selected_author.book.all()
    other_books_list=[]
    for i in all_books_list:
        if i not in selected_author_books:
            other_books_list.append(i)
    context={
        'author':selected_author,
        'book': selected_author.book.all(),
        'other_books_list':other_books_list,
    }
    return render(request,'author.html',context)

def updating_an_author(request,x):
    print('*'*50)
    print(f'Method:{request.method}')
    # print(request.POST['new_author'])
    bookID=int(request.POST['new_book'])
    sellected_book=Book.objects.get(id=bookID)
    sellected_author=Author.objects.get(id=x)
    sellected_book.author.add(sellected_author)
    print(f'updated-{sellected_author.first_name}')
    print(f'added a book-{sellected_book.title}')
    return redirect(f'/authors/{int(x)}')

def clear_session(request):
    print('*'*50)
    request.session.clear()
    print('session cleared')
    return redirect('/')

# Create your views here.
