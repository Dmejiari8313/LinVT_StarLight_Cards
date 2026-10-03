import logging
import sys
from pathlib import Path

import pygame

logger = logging.getLogger(__name__)


def resource_path(path):
    """Devuelve una ruta de recurso válida desde el proyecto o PyInstaller."""
    relative_path = Path(path)
    if relative_path.is_absolute():
        return relative_path

    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path

    return Path(__file__).resolve().parent.parent / relative_path


def load_image(path):
    """Carga una imagen con manejo de errores y compatibilidad PyInstaller.

    Devuelve una Surface válida incluso si la carga falla (placeholder).
    """
    resolved_path = resource_path(path)
    try:
        img = pygame.image.load(str(resolved_path))
        try:
            return img.convert_alpha()
        except Exception:
            return img.convert()
    except Exception as e:
        logger.exception("Fallo cargando imagen %s: %s", resolved_path, e)
        w, h = 100, 150
        surf = pygame.Surface((w, h), pygame.SRCALPHA)
        surf.fill((100, 100, 100))
        return surf