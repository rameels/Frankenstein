#!/usr/bin/env python
import os
import sys
import csv
from frankapp.models import Stages, Events, EventsTimes, Actors, Roles, ActorsRoles, Crew, Responsibilities, CrewResponsibilities
from datetime import datetime
from django.utils import timezone

if __name__ == "__main__":
	sys.path.append('./Development/Frankenstein')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frank.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
