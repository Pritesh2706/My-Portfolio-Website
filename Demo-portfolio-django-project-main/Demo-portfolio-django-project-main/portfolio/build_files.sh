echo "BUILD START"
python3.13.3 -m pip install -requirements.txt
python3.13.3 manage.py collectstatic --noinput --clear
echo "BUILD END"
