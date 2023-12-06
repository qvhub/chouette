echo "Waiting for database to be ready"
sleep 20
echo "Migrate database"
python manage.py migrate
echo "Flushing database"
python manage.py flush --noinput
echo "Filling database"
python manage.py shell < /scripts/fill_database.py
echo "Database ready"
echo "Launching server"
python manage.py runserver 0.0.0.0:8000