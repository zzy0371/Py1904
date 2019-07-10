import xadmin
from .models import *
xadmin.site.register(Category)
xadmin.site.register(Tag)
class ArticleAdmin:
    # 模型字段想要使用ueditor 样式冲注册模型管理类
    style_fields = {"body": "ueditor"}

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Ads)