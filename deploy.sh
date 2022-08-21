echo 'Starting deployment process...'
echo 'Pulling changes from github repo...'
git pull origin main
curl -X POST -H "Content-Type: application/json" https://www.pythonanywhere.com/user/mraklord/webapps/mraklord.pythonanywhere.com/reload
