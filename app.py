



# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="wef", null=True, blank=True)
#     is_register = False
#
#     def __str__(self):
#         return self.user.username
#
#     def save(self, *args, **kwargs):
#         super().save()
#
#         img = Image.open(self.image.path)
#         if img.width > 300 or img.height > 300:
#             over = (300, 300)
#             img.thumbnail(over)
#             img.save(self.image.path)
#
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# @receiver(post_save, sender=User)
# def create_profile(sender, created, instance, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
# def ready(self):
#     import display.signal
#
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# import six
# class Token(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return six.text_type(user.id) + six.text_type(timestamp) + six.text_type(user.profile.is_register)
# verify_token = Token()
#
# from django import forms
#
# class Profile_Form(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["image"]
#
# from django.shortcuts import render, redirect
# from django.contrib import messages
# def profile(request):
#     p = Profile_Form()
#     if request.method == "POST":
#         p = Profile_Form(request.POST, request.FILES, instance=request.user)
#         if p.is_valid():
#             p.save()
#             messages.info(request, "wef")
#             return redirect("profile")
#
#     return render(request, "profile.html",
#                   {"profile": p})
#
#
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_text, force_str, force_bytes, DjangoUnicodeDecodeError
# from django.core.mail import EmailMessage
#
# def verify(request, user):
#     title = "hello"
#     site = get_current_site(request)
#     body = render_to_string("wef", {"id": urlsafe_base64_encode(force_bytes(user.id)),
#                                     "user":user,
#                                     "site":site,
#                                     "token": verify_token.make_token(user)})
#
#     e = EmailMessage(headers=title, body=body, from_email="mrkaungminnkhant@gmail.com", to=[user.email])
#     e.send()
#     messages.info(request, "wef")
#     return redirect("eewf")
#
# def registration(request):
#     email = request.POST["email"]
#     if User.objects.filter(email=email).exists():
#         return redirect("wef")
#     user = User.objects.create_user(email)
#     verify(request, user)
#
# from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings
#
# urlpatterns = [
#     path("verify.html/<str:id>/<str:token>", view.verify, name="verify")
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
#
# def verifyy(request, id, token):
#     try:
#         u_id = force_str(urlsafe_base64_decode(id))
#         user = User.objects.get(id=u_id)
#     except:
#         user = None
#
#     if user and verify_token.check_token(user, token):
#         user.profile.is_register = True
#         user.save()
#         messages.success(request, "verify")
#         return redirect("login")
#     return redirect("login")
# from datetime import datetime
# class Blog(models.Model):
#     user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
#     title = models.CharField(max_length=225, null=True, blank=True)
#     time = models.DateTimeField(default=datetime.now, blank=True)
#     time2 = models.DateTimeField(auto_now_add=True)
#
# class Blogform(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ["title", "time", "time2"]
#
#
# def create(request):
#     if request.method == "POST":
#         b = Blogform(request.POST, request.FILES)
#         if b.is_valid():
#             instance = b.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             messages.success(request, "wef")
#             return redirect("wef")
#         messages.info(request, "notvaild")
#         return redirect("wef")
#
#     b = Blogform()
#     return render(request, "wef",
#                   {"blog":b})
#
#
# def update(request, pk):
#     b = Blog.objects.get(id=pk)
#     bf = Blogform(instance=b)
#     if request.method == "POST":
#         bf = Blogform(request.POST, request.FILES, instance=b)
#         if bf.is_valid():
#             bf.save()
#             messages.success(request, "wef")
#             return redirect("wef")
#         messages.info(request, "wef")
#         return redirect("wef")
#
#     return render(request, "wef",
#                   {"bf":bf})
#
#
# def delete(request, pk):
#     if request.method == "POST":
#         b = Blog.objects.get(id=pk)
#         b.delete()
#         messages.info(request, "wef")
#     return redirect("wef")
#
# import os
# [os.path.join(BASE_DIR, "template")],
#
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]
#
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_URL = "/media/"


