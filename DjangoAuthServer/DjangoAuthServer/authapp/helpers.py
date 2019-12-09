import logging

from django.contrib.auth import get_user_model

from DjangoAuthServer.authapp.forms import UserForm
from DjangoAuthServer.authapp.exceptions import UserException

User = get_user_model()


def check_user_auth(user):
    return user.is_authenticated


def base(request):
    """
    :param request:
    :return dict: return base context
    """
    context = dict()
    if not request.user.is_anonymous:
        user = User.objects.get(pk=request.user.pk)
        context.update({"user": user})
    else:
        context.update({"user": None})
    return context


def save_user_by_form(request, context):
    valid = False
    user_form = UserForm(request.POST, request.FILES)
    user_form.is_valid()

    if user_form.is_valid():
        valid = True
        try:
            user = user_form.save()
        except UserException as error:
            logging.error(f"Error occured while saving user from form: {error}")
            user_form.valid = False
            # add error to user form
            user_form.errors.update({"__all__": str(error)})
            return user_form, False

        context['user'] = user
    return user_form, valid
