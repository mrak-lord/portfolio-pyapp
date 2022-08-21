echo 'Starting deployment process...'
echo 'Pulling changes from github repo...'
git pull origin main
curl -X POST -H "Content-Type: application/json" -H "X-CSRFToken: AlqsGgZykYrpRiEZqcunvmdOlgpC9rnDU55urCVoxzkb2p04UyuoIHrR7uazCyxT" https://www.pythonanywhere.com/user/mraklord/webapps/mraklord.pythonanywhere.com/reload
