import graphene
from graphene_django import DjangoObjectType

from .models import User
from persona_app.models import Persona

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'created_at', 'updated_at')
    
class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona
        fields = '__all__'

class Query(graphene.ObjectType):
    all_users =graphene.List(UserType)
    all_personas = graphene.List(PersonaType)

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_personas(root, info):
        return Persona.objects.all()

schema = graphene.Schema(query=Query)