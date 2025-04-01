from cook_framework.templator import render


class Index:
    def __call__(self, request, *args, **kwargs):
        return '200 OK', render('index.html',
                                datetime=request.get('datetime', None))


class About:
    def __call__(self, request):
        return '200 OK', render('about.html', datetime=request.get('datetime', None))


class Students:
    def __call__(self, request):
        return '200 OK', render('students.html', datetime=request.get('datetime', None))


class Register:
    def __call__(self, request):
        return '200 OK', render('register.html', datetime=request.get('datetime', None))


class Contact:
    def __call__(self, *args, **kwargs):
        return '200 OK', render('contact.html')
