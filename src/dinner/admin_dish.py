from helpers.director.shortcut import TablePage,ModelTable,ModelFields,director,page_dc
from .models import Dish,DishRes,ResourceType,KeyWord
from django.db.models import Sum,Count
from . admin_res import ResPage

class DishPage(TablePage):
    def get_label(self):
        return 'dish 管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    def get_context(self):
        ctx = super().get_context()
        ctx.update({
            'named_ctx':{
                'dish.table':[
                    {'name': 'res',
                     'label': '原料表',
                     'com': 'com-tab-table',
                     'pre_set':'rt={dish:scope.par_row.pk}',
                     'table_ctx': DishResTab().get_head_context(),
                     },
                ]
            }
        })
        return ctx
      
    
    class tableCls(ModelTable):
        model = Dish
        exclude =[]
        pop_edit_fields=['id']
        
        def getExtraHead(self):
            return [
                {'name':'res_count','label':'原料数','editor':'com-table-switch-to-tab','ctx_name':'dish.table','tab_name':'res'}
            ]
        
        def inn_filter(self, query):
            return query.annotate(res_count=Count('dishres'))
        
        def dict_row(self, inst):
            return {
                'res_count':inst.res_count
            }
        

class DishForm(ModelFields):
    class Meta:
        model = Dish
        exclude =[]
    
    def dict_head(self, head):
        if head['name'] =='price':
            head['suffix'] = '元'
        if head['name'] =='key_word':
            head['editor'] = 'com-field-split-text'
            head['options'] = [{'value':x.content,'label':x.content} for x in KeyWord.objects.all()]
        return head
    
    def dict_row(self, inst):
        return {
            'res_count':inst.dishres_set.count()
        }
    
class ResPicker(ResPage.tableCls):
    
    def dict_head(self, head):
        head = super().dict_head(head)
        if head['name'] =='label':
            head['editor'] ='com-table-click'
            head['action']='scope.ps.vc.$emit("finish",scope.row)'
        return head

class DishResTab(ModelTable):
    model = DishRes
    exclude = ['id']
    hide_fields=['dish']
    pop_edit_fields=['res']
    
    def dict_head(self, head):
        if head['name'] =='res':
            head['inn_editor'] = 'com-table-label-shower'
        return head
    
    def inn_filter(self, query):
        return query.filter(dish_id = self.kw.get('dish'))

    def get_operation(self):
        return [
            {'name':'add_res','editor':'com-op-btn',
             'label':'添加原料',
             'fields_ctx':DishResForm().get_head_context(),
             'action':'''scope.head.fields_ctx.row = {dish:scope.ps.vc.par_row.pk,_director_name:"dish.restab.edit"};
             cfg.pop_vue_com("com-form-one",scope.head.fields_ctx).then(row=>{scope.ps.update_or_insert(row);ex.refresh_row(scope.ps.vc.par_row)})'''},
            {'action':'scope.ps.delete_selected().then(resp=>{ ex.refresh_row(scope.ps.vc.par_row) })',
             'editor':'com-op-btn',
             'label':'删除',
             'style': 'color:red',
             'icon': 'fa-times',
             'disabled':'!scope.ps.has_select', 
             'visible': self.permit.can_del(),},
        ]

class DishResForm(ModelFields):
    hide_fields=['dish']
    class Meta:
        model = DishRes
        exclude = []
    
    def dict_head(self, head):
        if head['name'] =='res':
            head.update({
                'editor':'com-field-pop-table-select',
                'table_ctx':ResPicker().get_head_context(),
                'options':[]
            })
        return head
        
director.update({
    'dish':DishPage.tableCls,
    'dish.edit':DishForm,
    'dish.select_res':ResPicker,
    'dish.restab':DishResTab,
    'dish.restab.edit':DishResForm,
})

page_dc.update({
    'dish':DishPage
})