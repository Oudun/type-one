import sys
import os
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "type_one.settings")
execute_from_command_line(sys.argv)