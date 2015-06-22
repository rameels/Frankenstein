#!/usr/bin/env python
import os
import sys
from frankapp.models import Stages, Events, EventsTimes, Actors, Roles, ActorsRoles, Crew, Responsibilities, CrewResponsibilities

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frank.settings")

	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
