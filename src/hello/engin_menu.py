from helpers.director.engine import BaseEngine,page
from helpers.director.base_data import inspect_dict
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine, page, fa, can_list, can_touch
from django.contrib.auth.models import User, Group
from helpers.func.collection.container import evalue_container

from django.utils.translation import ugettext as _
from django.conf import settings
from helpers.director.access.permit import has_permit
from helpers.mobile.base_data import mb_page_dc


class PcMenu(BaseEngine):
    url_name = 'Job'
    title = 'x' #''
    brand = 'x' #''
    mini_brand = 'XCL'
    menu_search=False
    need_staff=True
    access_from_internet=True
    @property
    def menu(self):
        crt_user = self.request.user
        menu = [
            #{'label': 'HOME', 'url': page('home'), 'icon': fa('fa-home'), 'visible': True},
         
            {'label': '菜单管理', 'icon': fa('fa-truck'), 'visible': True,
             'submenu': [
                {'label':'菜','url':page('dish')},
                {'label':'原料','url':page('res')},
             ]},
        
            {'label': '系统管理', 'icon': fa('fa-gear'), 'visible': True,
             'submenu': [
                 #{'label': '微信用户', 'url': page('wxuserinfo'), 'visible': can_touch(Group, crt_user)},
                 {'label': '账号管理', 'url': page('jb_user'), 'visible': can_touch(User, crt_user)},
                 #{'label': '权限分组', 'url': page('jb_group'), 'visible': can_touch(Group, crt_user)},
             ]},

        ]

        return menu

    #def custome_ctx(self, ctx):
        #ctx['js_stamp'] = js_stamp
        #ctx['fast_config_panel'] = True
        #if 'extra_js' not in ctx:
            #ctx['extra_js'] = []
        #ctx['extra_js'].append(ctx['js_config']['js_lib']['maindb'])

        #return ctx


PcMenu.add_pages(page_dc)

# 移动页面
#mb_page={}
#inspect_dict['mb_page']= mb_page


#class MBpageEngine(BaseEngine):
    #url_name='mb_page'
    #need_login=True
    #access_from_internet=True
    #login_url='/mb/login'
    #menu=[
        #{'label':'user_info','url':page('user_buyrecord')},
          #{'label':'user_washrecord','url':page('user_washrecord')},
          #{'label':'user_info','url':page('user_info')},
          
          #]
    #def custome_ctx(self, ctx):
        #if 'extra_js' not in ctx:
            #ctx['extra_js'] = []
        #if 'job' not in ctx['extra_js']:
            #ctx['extra_js'].append('job')
        #ctx['extra_js'].append('moment')
        #ctx['extra_js'].append('moment_zh_cn')
        
        
        ##ctx['extra_js'].append('moment')
        #return ctx

#MBpageEngine.add_pages(mb_page)
#MBpageEngine.add_pages(mb_page_dc)