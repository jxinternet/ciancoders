from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from sales import views 

router = routers.DefaultRouter()
router.register(r'sales', views.TaskView, 'sales')
urlpatterns = [
    path("api/1", include(router.urls))
    path('docs/', include_docs_urls(title="Cian Coders API"))
]
