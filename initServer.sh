rm -rf venv
virtualenv --always-copy venv
source venv/bin/activate
pip install -r requeriments.txt
deactivate
