from django.core.management.templates import TemplateCommand
from django.utils.crypto import get_random_string


class Command(TemplateCommand):
    def handle(self, project_name=None, target='.', *args, **options):
        self.validate_name(project_name, "project")

        options['extensions'] = ['.py', '.env']
        options['template'] = 'boilerplate/conf/project_template'

        # Create a random SECRET_KEY hash to put it in the main settings.
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        options['local_secret_key'] = get_random_string(50, chars)
        options['dev_secret_key'] = get_random_string(50, chars)
        options['prod_secret_key'] = get_random_string(50, chars)

        super(Command, self).handle('project', project_name, target, **options)
