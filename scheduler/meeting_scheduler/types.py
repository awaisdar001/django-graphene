"""
Custom scheduler app nodes
"""
import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from .models import Booking, Availability, UserModel


class UserType(DjangoObjectType):
    """User Object Type Definition"""

    class Meta:
        model = UserModel
        fields = ("id", "username", "email",)


class AvailabilityType(DjangoObjectType):
    """Availability Object Type Definition"""
    interval_mints = graphene.String()
    user = graphene.Field(UserType)

    class Meta:
        model = Availability
        interfaces = (graphene.relay.Node,)
        filter_fields = ['user__username']

    @classmethod
    def resolve_interval_mints(cls, availability, info):
        """Resolves interval mints choice field."""
        return availability.get_interval_mints_display()


class BookingType(DjangoObjectType):
    """Booking Object Type Definition"""
    user = graphene.Field(UserType)

    class Meta:
        model = Booking
        interfaces = (relay.Node,)
