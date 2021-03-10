import graphene

from graphene_django.types import DjangoObjectType

from .models import Student,Faculty

class StudentType(DjangoObjectType):
    class Meta:
        model = Student

class FacultyType(DjangoObjectType):
    class Meta:
        model = Faculty
        
class Query(graphene.AbstractType):
    all_student = graphene.List(StudentType)
    all_faculty = graphene.List(FacultyType)

    def resolve_all_student(self, args):
        return Student.objects.all()

    def resolve_all_faculty(self, args):
        return Faculty.objects.all()