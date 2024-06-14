import json
from django.shortcuts import render
from datetime import datetime as dtime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken

def token(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token

    # Mengatur waktu kedaluwarsa access token menjadi 3 hari dari sekarang
    access_token.set_exp(lifetime=timedelta(days=3))

    # Mengatur waktu kedaluwarsa refresh token jika diperlukan
    refresh.set_exp(lifetime=timedelta(days=3))  # Misalnya 3 hari

    # Mendapatkan waktu expired dari access token
    access_token_exp = dtime.fromtimestamp(access_token['exp'])

    # Mendapatkan waktu expired dari refresh token
    refresh_token_exp = dtime.fromtimestamp(refresh['exp'])
    
    access_token = str(access_token)

    response = {
                'id': user.id,
                'username': user.username,
                'jwt': access_token,
                'access_token_exp': access_token_exp,
                'refresh_token_exp': refresh_token_exp,
                'message': "Succes Login!",
            }


    return render(request, "extoken.html", locals())
