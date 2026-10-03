# LinVT StarLight Cards

Pequeño proyecto de cartas con Pygame. Contiene la lógica del juego, recursos de cartas y utilidades para desarrollo.

## Estructura relevante
- `src/main.py`: entrypoint (lanza `GameApp`).
- `src/game_app.py`: clase `GameApp` (bucle principal, UI, eventos).
- `src/card.py`: definición de cartas y `cards_info`.
- `src/utils.py`: utilidades (carga de imágenes con manejo de errores).
- `src/check_images_exist.py`: comprobación rápida de que los ficheros de imagen existen.
- `src/check_resources.py`: comprobación de imágenes usando Pygame (requiere `pygame`).
- `src/watcher.py`: reinicio automático del juego durante el desarrollo.
- `requirements.txt`: dependencias del proyecto.

## Requisitos
- Python 3.8+ (se recomienda usar el entorno virtual del proyecto).

## Instalación rápida (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Nota: la instalación de `pygame` puede requerir herramientas de compilación en Windows. Si `pip install -r requirements.txt` falla, instala una rueda precompilada apropiada o consulta la documentación de Pygame.

## Ejecutar el juego
```powershell
python src\main.py
```

El juego resuelve los recursos desde la raíz del repositorio, por lo que el
comando funciona aunque se ejecute desde otra carpeta. Durante el desarrollo
se puede usar:

```powershell
python src\watcher.py
```

## Tests y comprobaciones de recursos
- Comprobar que las rutas de imagen listadas en `cards_info` existen (no requiere Pygame):
```powershell
python src\check_images_exist.py
```
- Comprobar que las imágenes funcionan con Pygame (prueba headless con driver `dummy`):
```powershell
# En PowerShell
$env:SDL_VIDEODRIVER='dummy'
python src\check_resources.py
```

## Notas de diseño y próximos pasos
- `main.py` ahora es un entrypoint que crea `GameApp` en `src/game_app.py`.
- La partida usa una pila compartida sin duplicar objetos de carta y cachea las imágenes escaladas.
- Las cartas se crean por partida y cargan sus imágenes después de inicializar Pygame.
- `load_image` en `src/utils.py` resuelve recursos de forma independiente del
  directorio actual y devuelve un placeholder si la carga falla.

---
Creado automáticamente por el asistente de refactorización.
