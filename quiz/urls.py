from django.conf.urls import url

from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.TakeView.as_view(), name='take'),
    url(r'^edit/$', views.EditView.as_view(), name='edit'),
    url(r'^(?P<problem_id>[0-9]+)/choose/$', views.choose, name='choose'),
    url(r'^(?P<pk>[0-9]+)/results/', views.ResultsView.as_view(), name='results'),
    url(r'^edit/add_problem/$', views.AddProblemView.as_view(), name='add_problem'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EditProblemView.as_view(), name='edit_problem'),
    url(r'^(?P<problem_id>[0-9]+)/delete_problem/$', views.deleteProblem, name='delete_problem'),
    url(r'^edit/add_problem/add_logic$', views.addLogic, name='add_logic')
]