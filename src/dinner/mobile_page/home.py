from hello.engin_menu import mb_page
from django.conf import settings
from helpers.director.kv import get_value
from helpers.maintenance.update_static_timestamp import static_url
from helpers.director.shortcut import ModelTable,director,RowSearch
from dinner.models import Dish

class Home(object):
    need_login =False
    def __init__(self, request, engin):
        self.request =request
    
    def get_template(self):
        return 'mobile/live_show.html'
    
    def get_context(self):
        return {
            'editor':'live_layout',
             'editor_ctx':{
                 'layout_editors':[
                     #{'editor':'com-top-swiper','items':banners,},
                     {'editor':'com-top-dish-header'},
                     {'editor':'com-top-sidebar-ctn','class':'my-sidebar','css':'.my-sidebar{ height: calc( var( --app-height) - 1rem );}',
                      'tabs':[
                          {'editor':'com-ti-dinner-list','label':'热菜','kind':1},
                          {'editor':'com-ti-dinner-list','label':'冷菜','kind':2},
                          {'editor':'com-ti-dinner-list','label':'其他','kind':0},
                          ],
                      },
                     { 'editor':'com-top-dish-submit'}
                     
                     #{'editor':'com-top-caption',
                      #'image_url':static_url('mobile/python.jpg'),
                      #'class':'white-bg material-wave',
                      #'css':'.white-bg{background-color:white;margin:.4rem 0}',
                      #'title':'点菜系统',
                      #'sub_title':'Python+Django+Vuejs技术架构，非前后端分离的全栈式开发,1-2天快速响应'},
     
                    ],
                 #'footer':self.get_footer(0)
                 }
             }
    #def get_footer(self,index):
        #return {
            #'editor':'com-top-footer-btn-pannel',
            #'active':index,
            #'items':[
                #{'label':'首页','icon':'home-o','action':'location = "/mb/home" '},
                #{'label':'示例','icon':'gem-o','action':'location = "/mb/example"'},
                #{'label':'资讯','icon':'description','action':'location = "/mb/article"'}
            #]
        #}


class DishTab(ModelTable):
    nolimit = True
    model = Dish
    exclude =[]
    simple_dict = True
    
    def inn_filter(self, query):
        if self.kw.get('kind'):
            return query.filter(kind = self.kw.get('kind'))
        #elif self.search_args.get('_q'):
            #return query.filter(label__icontains = self.search_args.get('_q'))
        else:
            return query
    
    class search(RowSearch):
        names = ['label']
        
director.update({
    'dish.user':DishTab
})

mb_page.update({
    'home':Home
})