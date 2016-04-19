from django.contrib import admin

from .models import (Action, Function, PaperRecordArchiveRetentionPeriod, PaperRecordRetentionOrder,
                     PaperRecordWorkplaceRetentionPeriod, PersonalData, Phase, ProtectionClass, PublicityClass, Record,
                     RetentionCalculationBasis, RetentionPeriod, RetentionReason, SecurityPeriod,
                     SecurityPeriodCalculationBasis, SecurityReason, SocialSecurityNumber)

admin.site.register(Action)
admin.site.register(Record)
admin.site.register(Phase)

admin.site.register(PublicityClass)
admin.site.register(SecurityPeriod)
admin.site.register(SecurityReason)
admin.site.register(PersonalData)
admin.site.register(SocialSecurityNumber)
admin.site.register(RetentionPeriod)
admin.site.register(RetentionReason)
admin.site.register(ProtectionClass)
admin.site.register(RetentionCalculationBasis)
admin.site.register(PaperRecordRetentionOrder)
admin.site.register(PaperRecordArchiveRetentionPeriod)
admin.site.register(PaperRecordWorkplaceRetentionPeriod)
admin.site.register(SecurityPeriodCalculationBasis)


class FunctionAdmin(admin.ModelAdmin):
    list_display = ('function_id', 'name')
    ordering = ('function_id',)

admin.site.register(Function, FunctionAdmin)
