from django.urls import path
from . import views
urlpatterns=[
    path('',views.add_a_book),
    path('reset',views.clear_session),
    path('adding_a_book',views.adding_a_book),
    path('books/<x>',views.book_detail),
    path('books/<x>/updating_a_book',views.updating_a_book),
    path('authors/<x>',views.author_detail),
    path('authors/<x>/updating_an_author',views.updating_an_author),
    path('author',views.add_an_author),
    path('adding_an_author',views.adding_an_author),
]