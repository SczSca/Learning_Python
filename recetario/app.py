from pathlib import Path
from Recetario import Recetario

recipeManager = Recetario(Path(__file__).parent.absolute())

recipeManager.start_manager()