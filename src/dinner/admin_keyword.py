from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director
from .models import KeyWord

class KeyWordPage(TablePage):
    def get_label(self):
        return '关键字管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = KeyWord
        exclude = []

class KeyWordForm(ModelFields):
    class Meta:
        model = KeyWord
        exclude =[]

director.update({
    'keyword':KeyWordPage.tableCls,
    'keyword.edit':KeyWordForm
})

page_dc.update({
    'keyword':KeyWordPage
})
 