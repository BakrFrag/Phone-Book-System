

# Create your views here.
from rest_framework import viewsets
from rest_framework import mixins 
from contact.models import Contact 
           
from contact.serializers import ContactSerializer , ContactCreateSerializer

class ContactViewset(mixins.CreateModelMixin , mixins.ListModelMixin, mixins.RetrieveModelMixin , viewsets.GenericViewSet):
    """
    handle operation on model contact 
    create contact and associate with mulipli numbers 
    retrieve single object
    list of contacts with username and attached numbers
    """
    queryset = Contact.objects.all().prefetch_related("numbers")
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ContactSerializer
        return ContactCreateSerializer