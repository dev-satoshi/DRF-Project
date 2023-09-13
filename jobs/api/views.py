from rest_framework import generics

from jobs.api.serializers import JobOfferSerializer
from jobs.models import JobOffer


class ListView(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all().order_by("-id")
    serializer_class = JobOfferSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
