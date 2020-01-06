from django.db import models
from django.conf import settings


class Printer(models.Model):
    printer_name = models.CharField(max_length=255)
    printer_description = models.TextField(blank=True, null=True)
    printer_img = models.ImageField(blank=True, null=True)
    printer_ip = models.GenericIPAddressField(blank=True, null=True)
    printer_apikey = models.CharField(max_length=255, blank=True, null=True)
    printer_username = models.CharField(max_length=255, blank=True, null=True)
    printer_password = models.CharField(max_length=255, blank=True, null=True)


class PrinterStatus(models.Model):
    printer_status_printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE)
    printer_status_from = models.DateTimeField()
    printer_status_until = models.DateTimeField(blank=True, null=True)


class File(models.Model):
    file_name = models.CharField(max_length=255)
    file_added_date = models.DateTimeField()
    file_added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=128)
    file_size = models.IntegerField()


class Job(models.Model):
    job_name = models.CharField(max_length=255)
    job_added = models.DateTimeField()
    job_started = models.DateTimeField()
    job_finished = models.DateTimeField()


class JobDetail(models.Model):
    job_detail_job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    job_detail_file = models.ForeignKey(File, on_delete=models.CASCADE)
    job_detail_ammount = models.IntegerField()


class Material(models.Model):
    material_name: models.CharField(max_length=255)
    material_description = models.TextField()


class MaterialProfile(models.Model):
    material_profile_name = models.CharField(max_length=255)
    material_profile_description = models.TextField(blank=True, null=True)
    material_profile_material = models.ForeignKey(Material, on_delete=models.CASCADE)


class MaterialProfileSetting(models.Model):
    material_profile = models.ForeignKey(MaterialProfile, on_delete=models.CASCADE)
    material_profile_setting_key = models.CharField(max_length=128)
    material_profile_setting_value = models.CharField(max_length=128)


class SlicerProfile(models.Model):
    slicer_profile_name = models.CharField(max_length=255)
    slicer_profile_description = models.TextField(blank=True, null=True)
    slicer_profile_printer = models.ForeignKey(Printer, on_delete=models.CASCADE)


class SlicerProfileSetting(models.Model):
    slicer_profile = models.ForeignKey(SlicerProfile, on_delete=models.CASCADE)
    slicer_profile_setting_key = models.CharField(max_length=128)
    slicer_profile_setting_value = models.CharField(max_length=128)

