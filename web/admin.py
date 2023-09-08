from django.contrib import admin
from .models import NFTWalletForm
import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str

def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # Add BOM to support Excel
    writer.writerow([
        smart_str(modeladmin.model._meta.fields[i].verbose_name) for i in range(len(modeladmin.list_display))
    ])
    for obj in queryset:
        writer.writerow([smart_str(getattr(obj, field)) for field in modeladmin.list_display])
    return response

export_as_csv.short_description = "Export selected records as CSV"

class NFTWalletFormAdmin(admin.ModelAdmin):
    list_display = ('wallet_address',)  # Define the fields to display in the admin list view, note the comma
    actions = [export_as_csv]

# Register the NFTWalletForm model and its admin class
admin.site.register(NFTWalletForm, NFTWalletFormAdmin)
