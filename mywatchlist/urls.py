from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_json_by_id #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_xml_by_id #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_item_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/<int:id>', show_item_by_id, name='show_watchlist'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]