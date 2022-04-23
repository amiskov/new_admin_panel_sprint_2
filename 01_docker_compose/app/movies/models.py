import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True, null=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
        constraints = (
            models.UniqueConstraint(fields=['name'], name='genre_name_idx'),
        )

    def __str__(self):
        return self.name


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField('full_name', max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('person')
        verbose_name_plural = _('persons')


class Filmwork(UUIDMixin, TimeStampedMixin):
    class Type(models.TextChoices):
        MOVIE = "movie", _('movie')
        TV_SHOW = "tv_show", _('tv_show')

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    file_path = models.TextField(_('file_path'), max_length=512, blank=True, null=True)
    rating = models.FloatField(_('rating'), blank=True, null=True,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100)])
    type = models.CharField(
        _('type'),
        max_length=128,
        choices=Type.choices,
        default=Type.MOVIE,
    )
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    persons = models.ManyToManyField(Person, through='PersonFilmwork')
    creation_date = models.DateField(_('creation_date'), blank=True, null=True)

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('filmwork')
        verbose_name_plural = _('filmworks')
        indexes = [
            models.Index(fields=['creation_date', 'rating'], name='film_work_creation_date_idx'),
        ]

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        constraints = (
            models.UniqueConstraint(fields=['genre_id', 'film_work_id'], name='genre_film_work_idx'),
        )


class Role(models.TextChoices):
    ACTOR = "actor", _('actor')
    WRITER = "writer", _('writer')
    DIRECTOR = "director", _('director')


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        _('role'),
        max_length=255,
        choices=Role.choices,
        default=Role.ACTOR,
        null=True
    )

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _('person')
        verbose_name_plural = _('persons')
        constraints = (
            models.UniqueConstraint(fields=['film_work_id', 'person_id', 'role'], name='film_work_person_role_idx'),
        )
