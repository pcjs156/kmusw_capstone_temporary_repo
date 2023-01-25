import graphene
from graphene_django import DjangoObjectType

from .models import Persona

class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona
        fields = '__all__'
    
class Query(graphene.ObjectType):
    related_personas = graphene.List(PersonaType)

    def resolve_related_personas(root, info):
        print(info.context)
        return Persona.filter(user=info.context.id)

schema = graphene.Schema(query=Query)