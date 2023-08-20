from ninja import NinjaAPI
from .models import Task

api = NinjaAPI()

@api.get('task/')
def list(request):
    task = Task.objects.all()
    response = [{'title': i.title, 'status': i.status, } for i in task]
    return response

