import unittest
import HtmlTestRunner
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Define o diretório onde o relatório será salvo
report_dir = 'src/test/reports'
os.makedirs(report_dir, exist_ok=True)  # Cria a pasta se ela não existir

# Carrega os testes do diretório `src/test`
loader = unittest.TestLoader()
suite = loader.discover('test')

# Configura o HtmlTestRunner para gerar o relatório HTML
runner = HtmlTestRunner.HTMLTestRunner(output=report_dir)
runner.run(suite)

