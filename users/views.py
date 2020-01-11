from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from blog.models import Post,Answer
from django.contrib.auth.models import User
from users.models import Follow


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request,pk):

    if pk == request.user.username:

        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'following': Follow.objects.filter(following=request.user),
            'follower': Follow.objects.filter(follower=request.user)
        }

        return render(request, 'users/profile.html', context)

    else:

        pk_user=User.objects.filter(username=pk).first()

        context={
            'posts':Post.objects.all(),
            'answers':Answer.objects.filter(author=pk_user.id),
            'user_profile':User.objects.filter(username=pk).first(),
            'following': Follow.objects.filter(following=pk_user),
            'follower': Follow.objects.filter(follower=pk_user)
        }

        return render(request,'users/not_logged_in_user_profile.html',context)

@login_required
def followers(request,pk):

    pk_user=User.objects.filter(username=pk).first()

    context={

            'follower':Follow.objects.filter(follower=pk_user),
            'following':Follow.objects.filter(following=pk_user),
            'context_user':pk_user
    }

    return render(request,'users/followers.html',context)

@login_required
def following(request,pk):

    pk_user=User.objects.filter(username=pk).first()

    context={

            'follower':Follow.objects.filter(follower=pk_user),
            'following':Follow.objects.filter(following=pk_user),
            'context_user':pk_user
    }

    return render(request,'users/following.html',context)           
                    
