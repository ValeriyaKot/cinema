from json import JSONDecodeError

from rest_framework import views
import requests
from rest_framework.response import Response
from recognition_platform.serializers.auth import LoginSerializer
from recognition_platform.recognition_platform.settings.base import SMG_API_BASE_URL
from recognition_platform.apps.authentication import exceptions


class LoginView(views.APIView):

    def post(self, request):
        url = '{}/token'.format(SMG_API_BASE_URL)
        serializer = LoginSerializer(data=request.data)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if serializer.is_valid():
            try:
                res = requests.post(url=url, json=serializer.data, headers=headers, timeout=10)
                if res.status_code != 200:
                    if res.status_code == 500:
                        title = res.json()["title"]
                        if title == "Invalid credentials":
                            raise exceptions.SMGAuthError("Invalid credentials")
                        raise exceptions.SMGConnectionError('No "Invalid credentials" in title')
                    raise exceptions.SMGConnectionError("Status code is neither 200 or 500")
                return Response(res.content)
            except requests.exceptions.Timeout as e:
                raise exceptions.SMGProxyError(str(e))
            except (requests.exceptions.RequestException, JSONDecodeError, KeyError) as e:
                raise exceptions.SMGConnectionError(str(e))
