from django.conf.urls import patterns, include, url
from django.views.generic.list_detail import object_list
from django.views.generic.create_update import create_object

from microblog.models import Note
from microblog.views import post_note
from microblog.forms import NoteForm


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'post_note/$', post_note, name='post_note'),
    url(r'$', object_list, dict(queryset=Note.objects.all().order_by('-id').select_related(depth=1),
                            paginate_by=20, extra_context=dict(form=NoteForm())), 'microblog_home'),
    # Examples:
    # url(r'^$', 'manoush2.views.home', name='home'),
    # url(r'^manoush2/', include('manoush2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
