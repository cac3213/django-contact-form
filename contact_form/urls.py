"""
Example URLConf for a contact form.

Because the ``contact_form`` view takes configurable arguments, it's
recommended that you manually place it somewhere in your URL
configuration with the arguments you want. If you just prefer the
default, however, you can hang this URLConf somewhere in your URL
hierarchy (for best results with the defaults, include it under
``/contact/``).

"""


from django.conf.urls.defaults import *
from django.views.generic import TemplateView

from contact_form.views import CaptchaContactFormView


urlpatterns = patterns('',
    url(r'^$',
       CaptchaContactFormView.as_view(),
       name='contact_form'),

    url(r'^sent/$',
        TemplateView.as_view(
           template_name='contact_form/contact_form_sent.html',
        ),
        name='contact_form_sent'),

    )

