import importlib
import subprocess


def test_pkg():
    {{slug_name}} = importlib.import_module("{{slug_name}}")
    assert {{slug_name}}.__name__ == "{{slug_name}}"

{% if cli %}
def test_cmd():
    subprocess.run(["{{slug_name}}", "--help"], check=True)
    subprocess.run(["{{slug_name}}", "-h"], check=True)
{% endif %}