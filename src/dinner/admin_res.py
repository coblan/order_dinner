from helpers.director.shortcut import ModelTable,TablePage,ModelFields,page_dc,director
from .models import ResourceType

class ResPage(TablePage):
    def get_label(self):
        return '原料管理'
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = ResourceType
        exclude =[]
        pop_edit_fields=['id']

class ResForm(ModelFields):
    class Meta:
        model = ResourceType
        exclude =[]
        
director.update({
    'res':ResPage.tableCls,
    'res.edit':ResForm,
})

page_dc.update({
    'res':ResPage
})