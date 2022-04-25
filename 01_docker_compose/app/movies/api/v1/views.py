from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from movies.models import Filmwork, PersonFilmwork, Role


class MoviesListApi(BaseListView):
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        return Filmwork.objects.prefetch_related('genres', 'person').values().all() \
                   .annotate(genres=ArrayAgg('genres__name', distinct=True),
                             actors=ArrayAgg('persons__full_name',
                                             filter=Q(personfilmwork__role__icontains=Role.ACTOR),
                                             distinct=True),
                             directors=ArrayAgg('persons__full_name',
                                                filter=Q(personfilmwork__role__icontains=Role.DIRECTOR),
                                                distinct=True),
                             writers=ArrayAgg('persons__full_name',
                                              filter=Q(personfilmwork__role__icontains=Role.WRITER),
                                              distinct=True)
                             )[:2]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'results': list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
