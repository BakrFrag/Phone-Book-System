

# Create your views here.
from rest_framework import viewsets
from rest_framework import mixins 
from rest_framework.response import Response
from contact.models import Contact , PhoneNumber 
           
from contact.serializers import ContactSerializer

class ContactViewsets(mixins.CreateModelMixin , mixins.ListModelMixin, mixins.RetrieveModelMixin , viewsets.GenericViewSet):
    """
    handle operation on model contact 
    create contact and associate with mulipli numbers 
    retrieve single object
    list of contacts with username and attached numbers
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer