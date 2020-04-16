from helpers.director.base_data import js_tr_list, js_lib_list
from django.utils.translation import ugettext as _
from helpers.maintenance.update_static_timestamp import js_stamp_dc,static_url
from django.conf import settings

def get_lib(request): 

    dc ={
        'order_dinner': static_url( 'js/order_dinner.pack.js?t=%s'%js_stamp_dc.get('order_dinner_pack_js') ),
    }
    return dc

js_lib_list.append(get_lib)