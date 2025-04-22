import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aerotur.settings')

    # Inicia métricas só quando for servidor (não em migrate, shell, etc)
    if os.getenv("DOCKER_ENV") == "true" and 'runserver' in sys.argv:
        from aerotur.metrics import start_metrics
        start_metrics()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
