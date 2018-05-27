# -*- coding: utf-8 -*-
# Copyright (C) 2016 o.s. Auto*Mat
from django.contrib import admin

from import_export.admin import ImportExportMixin

from related_admin import RelatedFieldAdmin

from . import models
import smmapdfs.actions

class PdfSandwichAdmin(ImportExportMixin, RelatedFieldAdmin):
    list_display = (
        'pdfsandwich_type',
        'pdf',
        'pdfsandwich_type',
        'sent_time',
    )
    actions = (smmapdfs.actions.send_pdfsandwich,)


class PdfSandwichFieldAdmin(ImportExportMixin, RelatedFieldAdmin):
    list_display = (
        'field',
        'x',
        'y',
        'font',
        'font_size',
    )
    list_editable = (
        'x',
        'y',
        'font',
        'font_size',
    )