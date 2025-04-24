from datetime import date
from cook_framework.templator import render
from components.models import Engine

site = Engine()


class Index:
    def __call__(self, request, *args, **kwargs):
        return '200 OK', render('index.html',
                                datetime=request.get('datetime', None))


class StudyPrograms:
    def __call__(self, request):
        return '200 OK', render('study-programs.html',
                                date=date.today())


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class CourseList:
    def __call__(self, request):
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name, id=category.id)
        except KeyError:
            return 'No courses have been added yet'


class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render('course_list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create_course.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return 'No categories have been added yet'


class CategoryList:
    def __call__(self, request):
        return '200 OK', render('category_list.html',
                                objects_list=site.categories)


class CreateCategory:
    def __call__(self, request):

        if request['method'] == 'POST':
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render('category_list.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html',
                                    categories=categories)


# class Students:
#     def __call__(self, request):
#         return '200 OK', render('students.html', datetime=request.get('datetime', None))


class TeachersList:
    def __call__(self, request):
        return '200 OK', render('teachers_list.html', datetime=request.get('datetime', None))


class Contact:
    def __call__(self, *args, **kwargs):
        return '200 OK', render('contact.html')
