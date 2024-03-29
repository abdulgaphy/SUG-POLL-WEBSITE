from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from vote.models import User, Vote, VoteCategory, Candidate
from import_export import resources
from .models import User


@admin.register(Vote, Candidate, VoteCategory, User)

class ViewAdmin(ImportExportModelAdmin):
    pass
