from django.http import HttpResponse
from django.shortcuts import render
from view.home import view_home
from view.order import view_order, view_orders
from view.post import view_post, view_posts
from view.user import view_user, view_users, view_user_add


# home

def home(request):
    return view_home.home(request)


# user

def users(request):
    return view_users.users(request)


def user(request, user_id):
    return view_user.user(request, user_id)


def user_add(request):
    return view_user_add.user_add(request)


# post

def posts(request):
    return view_posts.posts(request)


def post(request):
    pass


# order

def orders(request):
    return view_orders.orders(request)


def order(request):
    pass
