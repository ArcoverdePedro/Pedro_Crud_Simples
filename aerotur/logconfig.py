import os
import sys
import logging
from pathlib import Path
from loguru import logger

def setup_loguru():
    # Define o caminho dos logs
    LOG_DIR = Path("logs")
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Remove o handler padrão do loguru para evitar duplicação
    logger.remove()

    # Adiciona handler para arquivos de log
    logger.add(
        LOG_DIR / "app_{time:YYYY-MM-DD}.log",
        format="| {level} | {name}:{function}:{line} | {message}",
        level="INFO",
        rotation="00:00",
        retention="30 days", # Mantém logs por 30 dias
        encoding="utf-8"
    )
    #aparecer no terminal
    logger.add(sys.stdout, level="DEBUG")

    for log_file in LOG_DIR.glob("app_*.log"):
        os.chmod(log_file, 0o664)

class InterceptHandler(logging.Handler):
    """
    Handler para interceptar logs do módulo de logging padrão do Python
    e redirecioná-los para o Loguru.
    """
    def emit(self, record):
        # Obtém os logs enviados com o logging para o loguru automaricamente
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())

def get_logging_config():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "loguru": {
                "class": "aerotur.logconfig.InterceptHandler",  # classe do interceptador
            },
        },
        "root": {
            "handlers": ["loguru"],
            "level": "INFO",
        },
        "loggers": {
            "django": {
                "handlers": ["loguru"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["loguru"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.server": {
                "handlers": ["loguru"],
                "level": "ERROR",
                "propagate": False,
            },
        },
    }