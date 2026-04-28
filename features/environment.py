import os
import re
from datetime import datetime
from pathlib import Path

from selenium import webdriver

from pages.practice_form_page import PracticeFormPage


# Diretórios base
ROOT_DIR = Path.cwd()
SCREENSHOTS_DIR = ROOT_DIR / "screenshots_behave"


def _slugify(text: str) -> str:
    """
    Converte texto para formato seguro para nome de arquivo.
    Ex: "Fluxo Completo" -> "Fluxo_Completo"
    """
    text = text.strip()
    text = re.sub(r"[^a-zA-Z0-9_-]+", "_", text)
    return text.strip("_")


def before_all(context):
    """
    Executa antes de toda a suíte.
    Cria pasta de screenshots.
    """
    SCREENSHOTS_DIR.mkdir(exist_ok=True)


def before_scenario(context, scenario):
    """
    Executa antes de cada cenário.
    Inicializa o driver e o Page Object.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(options=options)
    context.page = PracticeFormPage(context.driver)

    # Guardar nomes organizados
    feature_name = getattr(getattr(scenario, "feature", None), "name", "feature")
    context.feature_name = _slugify(feature_name)
    context.scenario_name = _slugify(scenario.name)


def after_step(context, step):
    """
    Executa após CADA step (independente de sucesso ou falha).

    👉 Aqui salvamos screenshot de TODOS os steps
    """

    if not hasattr(context, "driver") or not context.driver:
        return

    # Status do step (passed, failed, skipped)
    status = getattr(step.status, "name", str(step.status)).lower()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Estrutura de pastas:
    # screenshots_behave/feature/scenario/
    feature_dir = SCREENSHOTS_DIR / context.feature_name
    scenario_dir = feature_dir / context.scenario_name
    scenario_dir.mkdir(parents=True, exist_ok=True)

    # Nome do arquivo inclui status
    step_name = _slugify(step.name)
    filename = f"{step_name}_{status}_{timestamp}.png"

    filepath = scenario_dir / filename

    # Salva screenshot
    context.driver.save_screenshot(str(filepath))

    print(f"[SCREENSHOT] {status.upper()} - {filepath}")


def after_scenario(context, scenario):
    """
    Executa após cada cenário.
    Fecha o navegador.
    """
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()