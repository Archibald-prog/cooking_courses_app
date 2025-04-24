import datetime
from views import Index, CategoryList, CreateCategory, Contact, StudyPrograms, \
    CourseList, CreateCourse, TeachersList


# front controller
def first_front(request):
    request['datetime'] = datetime.datetime.now()


def second_front(request):
    request['key'] = 'key'


fronts = [first_front, second_front]


routes = {
    '/': Index(),
    '/category-list/': CategoryList(),
    '/create-category/': CreateCategory(),
    '/contact/': Contact(),
    '/study-programs/': StudyPrograms(),
    '/course-list/': CourseList(),
    '/create-course/': CreateCourse(),
    # '/students/': Students(),
    '/teachers-list/': TeachersList(),
}
