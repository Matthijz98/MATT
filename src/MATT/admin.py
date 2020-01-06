from django.contrib import admin
from .models import Printer, PrinterStatus, Job, File, JobDetail, SlicerProfile, SlicerProfileSetting, Material, MaterialProfile, MaterialProfileSetting


admin.site.register(Printer)
admin.site.register(PrinterStatus)
admin.site.register(Job)
admin.site.register(File)
admin.site.register(JobDetail)
admin.site.register(SlicerProfile)
admin.site.register(SlicerProfileSetting)
admin.site.register(Material)
admin.site.register(MaterialProfile)
admin.site.register(MaterialProfileSetting)