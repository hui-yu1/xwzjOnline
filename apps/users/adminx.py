import xadmin
from xadmin import views

class BaseSetting(object):
    enabel_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '学无止境'
    site_footer = 'Powered By HuiYu -2020'

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

