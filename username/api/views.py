from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from username.models import Username
from username.api.serializers import UsernameSerializer
from message.models import Messages
from datetime import datetime

def DelateMessages(id, date, time):
    day_format = "%Y-%m-%d"
    today = datetime.today()
    create_day = datetime.strptime(str(date), day_format)
    current_date = datetime.strptime(str(today.date()), day_format)
    day_difference = current_date - create_day

    if(day_difference.days >= 1):
        if (day_difference.days > 1):
            message_delate = Messages.objects.get(id=id)
            message_delate.delete()
        if (today.hour >= time.hour):
            if(today.minute >= today.minute):
                message_delate = Messages.objects.get(id=id)
                message_delate.delete()


class UserNameViewSet(ViewSet):
    def retrieve(self, request , pk):
        user = UsernameSerializer(Username.objects.get(username=pk))
        for i in Messages.objects.values_list('id','created'):
            date = i[1].date()
            id = i[0]
            time = i[1].time()
            DelateMessages(id, date, time)
        return Response(status=status.HTTP_200_OK, data=user.data)

    def create(self, request):
        username = UsernameSerializer(data=request.data)
        username.is_valid(raise_exception=True)
        username.save()
        return Response(status=status.HTTP_200_OK, data=username.data)