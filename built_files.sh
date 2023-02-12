echo "built start"
python3.9 -m pip install -r requirements.text
python3.p manage.py collectstatic --noinput --clear
echo "End built"