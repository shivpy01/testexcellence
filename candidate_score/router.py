from candidate.viewsets import CandidateViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('candidate/',CandidateViewSet, basename='Candidate')