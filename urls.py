import datetime
from views import Index, About, Contact, Register, Students


# front controller
def first_front(request):
    request['datetime'] = datetime.datetime.now()


def second_front(request):
    request['key'] = 'key'


fronts = [first_front, second_front]


routes = {
    '/': Index(),
    '/about/': About(),
    '/contact/': Contact(),
    '/students/': Students(),
    '/register/': Register(),
}
