pkill -f vite
sudo ufw status
cd ~/sports-frontend/sports-frontend && npm run dev
cd ~/sports-frontend/sports-frontend && npm ls sass
cd /root
cd ~/sports-frontend/sports-frontend && npm uninstall sass node-sass && rm -rf node_modules package-lock.json && npm install -D sass@latest && npm install
cd /root
cd ~/sports-frontend/sports-frontend && node -v && npm ls sass
cd /root
cd ~/sports-frontend/sports-frontend && npm run dev
cd ~/sports-frontend/sports-frontend && rm -rf node_modules package-lock.json && npm install
cd /root
cd ~/sports-frontend/sports-frontend && npm run dev
cd ~/sports-frontend/sports-frontend && npm install -D path
cd /root
cd ~/sports-frontend/sports-frontend && npm run dev
cd ~/sports-frontend/sports-frontend && npm ls sass && node -v
cd /root
cd ~/sports-frontend/sports-frontend && rm -rf node_modules package-lock.json && npm uninstall sass && npm install -D sass@latest && npm install
cd /root
cd ~/sports-frontend/sports-frontend && npm run dev
cd /root
cd ~/sports-frontend/sports-frontend && npm list quasar @quasar/extras
cd /root
cd ~/sports-frontend/sports-frontend && pkill -f vite && npm run dev
cd /root
cd ~/sports-frontend/sports-frontend && rm -rf node_modules package-lock.json && npm install && npm install quasar @quasar/extras
cd /root
cd ~/sports-frontend/sports-frontend && npm run dev
cd /root
pkill -f node && cd ~/sports-frontend/sports-frontend && npm run dev
node --version && npm --version
curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && apt-get install -y nodejs
node --version && npm --version
mkdir -p ~/sports-frontend && cd ~/sports-frontend && npm create vite@latest sports-frontend -- --template vue
cd /root
cd ~/sports-frontend/sports-frontend && npm install
cd /root
cd ~/sports-frontend/sports-frontend && npm install quasar @quasar/extras
cd /root
cd ~/sports-frontend/sports-frontend && npm install -D @quasar/vite-plugin sass@1.32.12
cd /root
cd ~/sports-frontend/sports-frontend && npm run dev
cd /root
cd ~/sports-frontend/sports-frontend && npm run dev
cd /root
sudo ufw status
netstat -tulpn | grep LISTEN
apt install net-tools -y && netstat -tulpn | grep LISTEN
cd ~/sports-frontend/sports-frontend && pkill -f vite && npm run dev -- --host 0.0.0.0 --port 5173
ps aux | grep vite
pkill -f vite
rm -rf node_modules/.vite
pkill -f vite
ls -l public/mock_odds.json
cd /root
sudo apt update && sudo apt install python3 python3-pip postgresql postgresql-contrib -y
sudo systemctl enable postgresql && sudo systemctl start postgresql
sudo -u postgres psql -c "CREATE DATABASE sportsdb;"
sudo -u postgres psql -c "CREATE USER sportsuser WITH ENCRYPTED PASSWORD 'sportspass';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE sportsdb TO sportsuser;"
sudo -u postgres psql -l
ps aux | grep vite
npm run dev
npm run dev -- --host 0.0.0.0 --port 5173
npm run dev
sudo apt update && sudo apt install python3 python3-pip postgresql postgresql-contrib -y
sudo systemctl enable postgresql && sudo systemctl start postgresql
sudo -u postgres psql -c "CREATE DATABASE sportsdb;" && sudo -u postgres psql -c "CREATE USER sportsuser WITH ENCRYPTED PASSWORD 'sportspass';" && sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE sportsdb TO sportsuser;"
sudo -u postgres psql -c "\l" | grep sports
cd /root/sports-frontend/sports-frontend
pip install -r requirements.txt
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
sudo apt install python3.12-venv -y && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
cd /root/sports-frontend/sports-frontend && npm install
npm run dev
cd /root/sports-frontend/sports-frontend && npm install
cd /root
cd /root/sports-frontend/sports-frontend && npm run dev
cd /root/sports-frontend/sports-frontend && npm install
cd /root/sports-frontend/sports-backend
cd /root/sports-frontend/sports-backend && pip install -r requirements.txt
cd /root/sports-frontend
ls -la /root/sports-frontend/
cd /root/sports-frontend/sports-backend
ls -la /root/sports-frontend/sports-backend/
which python
cd /root/sports-frontend
cd /root/sports-frontend && git init && git status
git config --global user.email "your.email@example.com" && git config --global user.name "Your Name"
git config --global user.email "alextrx818@gmail.com" && git config --global user.name "Alex" && git config --global init.defaultBranch main
cd /root/sports-frontend && git branch -M main && git remote add origin https://github.com/YOUR_USERNAME/sports-dashboard.git
cd /root/sports-frontend && git init && git branch -M main
cd /root/sports-frontend && git remote add origin git@github.com:alextrx818/FinalProject.git
cd /root/sports-frontend && git remote -v
cd /root/sports-frontend && git remote set-url origin git@github.com:alextrx818/FinalProject.git
cd /root/sports-frontend && git add . && git commit -m "Initial working dashboard setup" && git push -u origin main
yes
cd /root/sports-frontend && git remote -v && echo "Type 'yes' when prompted"
yes
cd /root/sports-frontend && git remote set-url origin https://github.com/alextrx818/FinalProject.git && git push -u origin main
cd /root/sports-frontend && git pull origin main
cd /root/sports-frontend && git config pull.rebase false && git pull origin main
cd /root/sports-frontend && git pull origin main --allow-unrelated-histories
cd /root/sports-frontend && git remote set-url origin https://github.com/alextrx818/FinalProject.git && git push -u origin main
cd /root/sports-frontend && git checkout -b feature/alerts && git branch
cd /root/sports-frontend && git branch -a
cd /root/sports-frontend && git branch
cd /root/sports-frontend && git add . && git commit -m "Setting up alert system structure" && git push origin feature/alerts
cd /root/sports-frontend && git checkout main && git checkout -b feature/chat && git branch
cd /root/sports-frontend && echo "LOCAL BRANCHES:" && git branch && echo -e "\nREMOTE BRANCHES (on GitHub):" && git branch -r
cd /root/sports-frontend && git push origin feature/alerts && git push origin feature/chat
cd /root/sports-frontend && echo "LOCAL BRANCHES:" && git branch && echo -e "\nREMOTE BRANCHES (on GitHub):" && git branch -r
cd /root/sports-frontend && git status && echo -e "\nBRANCH DIFFERENCES:" && git branch -v
cd /root/sports-frontend && git log --oneline
cd /root/sports-frontend && git checkout -b working-dashboard && git add . && git commit -m "Saving working dashboard state" && git push origin working-dashboard
cd /root/sports-frontend && echo "BRANCHES:" && git branch && echo -e "\nCOMMITS:" && git log --oneline
cd /root/sports-frontend && git push origin working-dashboard
cd /root/sports-frontend && echo "DETAILED BRANCHES:" && git branch -vv && echo -e "\nCURRENT BRANCH:" && git status
cd /root/sports-frontend && git config branch.working-dashboard.description "PERMANENT: Working dashboard save point" && git config branch.main.description "DEFAULT: Main production code" && git config branch.feature/chat.description "FEATURE: Chat development" && git config branch.feature/alerts.description "FEATURE: Alert system"
cd /root/sports-frontend && git tag v1.0-forever-working && git push origin v1.0-forever-working && git tag -l
cd /root/sports-frontend && git tag -l
cd /root/sports-frontend && echo "YOUR PERMANENT SAVES:" && git tag -l
cd /root/sports-frontend && echo "GIT KNOWS:" && git remote -v && echo -e "\nCURRENT BRANCH:" && git branch --show-current
cd /root/sports-frontend && echo "1. WHERE GIT SENDS CODE:" && git remote -v && echo -e "\n2. CURRENT BRANCH:" && git branch --show-current && echo -e "\n3. ALL BRANCHES:" && git branch && echo -e "\n4. PERMANENT TAGS:" && git tag -l
cd /root/sports-frontend && echo "PROJECT STRUCTURE:" && ls -R && echo -e "\nPACKAGE.JSON:" && cat sports-frontend/package.json
cd /root/sports-frontend && echo "DIGITAL OCEAN CONFIG:" && pwd && echo -e "\nGITHUB CONFIG:" && git remote -v && echo -e "\nBRANCHES:" && git branch
cd /root/sports-frontend && echo "YOUR PERMANENT SAVES:" && git tag -l
PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
pkill -f "python3 view_tennis_data.py"
pkill -f "python3 view_tennis_data.py" && PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
cd /root/sports-frontend/sports-backend
pip list | grep -E "requests|python-dotenv|psycopg2-binary|Flask|schedule"
pip install -r requirements.txt
python3 -m venv venv
source venv/bin/activate && pip install -r requirements.txt
apt-get update && apt-get install -y python3-distutils
source venv/bin/activate && pip install Flask==2.2.3 requests==2.28.2 python-dotenv==0.21.0 schedule==1.1.0
cd /root/sports-frontend/sports-frontend
rm -rf api/
cd /root/sports-frontend
git status
git add .
git commit -m "refactor: remove redundant api folder, update requirements, add backend flow doc"
git commit --amend -m "figuring out backend directory"
git tag -a v0.1.0 -m "Understanding backend structure and removing redundant frontend api"
git tag -n
git push origin working-dashboard
git push origin v0.1.0
mkdir -p sports-backend/aggregator/{tennis,soccer}/
tree -I 'node_modules|venv'
apt install tree -y
tree -I 'node_modules|venv'
mv sports-backend /root/
mv sports-frontend /root/
ls -la
ls -la sports-frontend/
cd sports-frontend && npm run dev
cd /root/sports-frontend
git tag v1.1-directories-created
git branch
git checkout -b feature/directory-structure
git add .
git commit -m "refactor: separate frontend and backend directories"
git tag v1.1-directories-created
git tag -d v1.1-directories-created && git tag v1.1-directories-created
git push origin feature/directory-structure
git push origin v1.1-directories-created
cd /root
sudo apt update && sudo apt install postgresql postgresql-contrib -y
sudo systemctl status postgresql
sudo -u postgres psql -c "CREATE DATABASE sports_odds;"
sudo -u postgres psql -c "CREATE USER amireslami WITH PASSWORD 'Lincoln95\$';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE sports_odds TO amireslami;"
psql -h localhost -U amireslami -d sports_odds -c "\l"
PGPASSWORD='Lincoln95$' psql -h localhost -U amireslami -d sports_odds -c "\l"
PGPASSWORD='Lincoln95$' psql -h localhost -U amireslami -d sports_odds -c "
CREATE TABLE tennis_odds (
    id SERIAL PRIMARY KEY,
    match_name VARCHAR(100),
    status VARCHAR(20),
    sport VARCHAR(20),
    pre_odds DECIMAL,
    live_odds DECIMAL,
    trend DECIMAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"
sudo -u postgres psql -d sports_odds -c "GRANT ALL ON SCHEMA public TO amireslami;"
PGPASSWORD='Lincoln95$' psql -h localhost -U amireslami -d sports_odds -c "
CREATE TABLE tennis_odds (
    id SERIAL PRIMARY KEY,
    match_name VARCHAR(100),
    status VARCHAR(20),
    sport VARCHAR(20),
    pre_odds DECIMAL,
    live_odds DECIMAL,
    trend DECIMAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"
PGPASSWORD='Lincoln95$' psql -h localhost -U amireslami -d sports_odds -c "
INSERT INTO tennis_odds (match_name, status, sport, pre_odds, live_odds, trend) VALUES 
('Nadal vs Federer', 'Live', 'Tennis', 1.85, 2.10, 0.25),
('Djokovic vs Alcaraz', 'Live', 'Tennis', 1.95, 1.90, -0.05);"
cd /root/sports-backend
pip install flask flask-cors psycopg2-binary
python3 -m venv venv && source venv/bin/activate && pip install flask flask-cors psycopg2-binary
python3 --version
pip3 --version
which python3
sudo apt-get install python3-flask python3-flask-cors python3-psycopg2 -y
python3 serve_api.py
rm -rf venv
python3 -m venv venv
sudo apt-get install python3.12-venv -y
python3 -m venv venv
deactivate 2>/dev/null || true; rm -rf venv
/usr/bin/python3 -m venv venv
source venv/bin/activate && pip install --upgrade pip && pip install flask==3.0.3 flask-cors==4.0.1 psycopg2-binary==2.9.9
source venv/bin/activate && python3 serve_api.py
cd sports-frontend && npm run dev
cd /root
PGPASSWORD='Lincoln95$' psql -h localhost -U amireslami -d sports_odds -c "INSERT INTO tennis_odds (match_name, status, sport, pre_odds, live_odds, trend) VALUES ('Medvedev vs Sinner', 'Live', 'Tennis', 2.00, 2.15, 0.15);"
cd /root/sports-backend/aggregator/tennis
rm rapid.py rapid_parser.py merger.py betsapi.py betsapi_parser.py
cd /root
git checkout -b feature/tennis-api-integration
cd /root && git status
cd /root/sports-frontend
ls -la
git remote -v
git checkout -b feature/tennis-api-integration && git add /root/sports-backend/aggregator/tennis/* && git commit -m "Tennis API Integration: Added dual source data flow (RapidAPI + BetsAPI)" && git tag -a v1.0.0-tennis -m "Tennis API integration complete" && git push origin feature/tennis-api-integration --tags
mkdir -p /root/sports-frontend/sports-frontend/backend/aggregator/tennis && cp -r /root/sports-backend/aggregator/tennis/* /root/sports-frontend/sports-frontend/backend/aggregator/tennis/ && cp /root/sports-backend/serve_api.py /root/sports-frontend/sports-frontend/backend/ && cd /root/sports-frontend && git checkout -b feature/tennis-api-integration && git add . && git commit -m "Tennis API Integration: Added dual source data flow (RapidAPI + BetsAPI)" && git tag -a v1.0.0-tennis -m "Tennis API integration complete" && git push origin feature/tennis-api-integration --tags
mkdir -p /root/sports-frontend/sports-frontend/backend/aggregator/tennis && cp -r /root/sports-backend/aggregator/tennis/* /root/sports-frontend/sports-frontend/backend/aggregator/tennis/ && cp /root/sports-backend/serve_api.py /root/sports-frontend/sports-frontend/backend/ && cd /root/sports-frontend && git add . && git commit -m "Tennis API Integration: Added dual source data flow (RapidAPI + BetsAPI)" && git tag -a v1.0.0-tennis -m "Tennis API integration complete" && git push origin feature/tennis-api-integration --tags
cd /root/sports-frontend && git tag -a stable-tennis-v1.0 -m "Stable tennis API integration with dual source data flow" && git push origin stable-tennis-v1.0
cd /root/sports-frontend && tree
cd /root/sports-frontend && git add -A && git commit -m "Reorganized project structure:
- /sports-frontend/backend: Backend API and tennis integration
- /sports-frontend/frontend: Vue.js dashboard
- /docs: Project documentation
" && git push origin feature/tennis-api-integration
cd /root/sports-frontend && git add README.md && git commit -m "Updated README with proper project structure" && git push origin feature/tennis-api-integration
cd /root/sports-backend && mkdir -p database serveAPI tennis soccer basketball
find /root/sports-backend -type f
rm -rf /root/sports-backend/aggregator /root/sports-backend/venv /root/sports-backend/main_bot.py /root/sports-backend/serve_api.py /root/sports-backend/requirements.txt
mkdir -p /root/sports-backend/{database,serveAPI,tennis,soccer,basketball}
mkdir -p aggregator && mv config.py aggregator/ && mv aggregator.py aggregator/ && mv database tennis soccer basketball serveAPI aggregator/
cd /root/sports-backend/aggregator && mv basketball temp_basketball && mv soccer temp_soccer && mv tennis temp_tennis && mkdir sports && mv temp_basketball sports/ && mv temp_soccer sports/ && mv temp_tennis sports/ && mv sports/temp_basketball sports/basketball && mv sports/temp_soccer sports/soccer && mv sports/temp_tennis sports/tennis
cd /root/sports-backend
cd /root/sports-backend && git status
cd /root/sports-backend && git init && git add . && git commit -m "Initial commit: Structured sports backend with database, API, and sports modules (tennis, soccer, basketball)"
cd /root/sports-backend && git tag -a v1.0.0 -m "Initial structured version with database, API, and sports modules"
cd /root/sports-backend && git tag -l -n1
cd /root/sports-backend && git remote add origin git@github.com:alextrx818/FinalProject.git && git push -u origin main && git push --tags
cd /root/sports-backend && git remote remove origin && git remote add origin https://github.com/alextrx818/FinalProject.git && git push -u origin main && git push --tags
cd /root/sports-backend && git pull origin main --allow-unrelated-histories
cd /root/sports-backend && git checkout main
cd /root/sports-backend && git checkout -b feature/structured-backend
cd /root/sports-backend && git tag v1.0-working-dashboard
cd /root/sports-backend && git push origin v1.0-working-dashboard
cd /root/sports-backend && git push -u origin feature/structured-backend
cd /root/sports-backend && echo "Branches:" && git branch -a && echo -e "\nTags:" && git tag -l
cd /root/sports-backend && git checkout main && git merge feature/structured-backend && git push origin main
cd /root/sports-backend && git pull origin main && git push origin main
cd /root/sports-backend && git push -f origin main
cd /root/sports-backend/aggregator/sports/tennis && mv rapid_inplay_events.py rapid_inplay_tennis.py
cd /root/sports-backend
python3 test_tennis.py
ls -R /root/sports-backend/
PYTHONPATH=/root/sports-backend python3 test_tennis.py
pip install python-dotenv
apt install python3-dotenv
PYTHONPATH=/root/sports-backend python3 test_tennis.py
ls -l /root/sports-backend/aggregator/sports/tennis/
PYTHONPATH=/root/sports-backend python3 test_tennis.py
ls -R /root/sports-backend/aggregator/sports/tennis/
find /root/sports-backend -name "__pycache__" -type d -exec ls -l {} \;
PYTHONPATH=/root/sports-backend python3 test_tennis.py
pip install flask
python3 -m venv venv && source venv/bin/activate && pip install flask
PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
pip install psycopg2-binary
PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
pip install python-dotenv
PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
pip install requests
PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
pkill -f "python3 view_tennis_data.py" && PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
ps aux | grep "python3 view_tennis_data.py"
pkill -f "python3 view_tennis_data.py"
pkill -f "python3 view_tennis_data.py" && PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
lsof -i :5001
PYTHONPATH=/root/sports-backend FLASK_DEBUG=1 python3 view_tennis_data.py
pkill -f "python3 view_tennis_data.py" && PYTHONPATH=/root/sports-backend python3 view_tennis_data.py
pkill -f "python3 test_tennis.py" && PYTHONPATH=/root/sports-backend python3 test_tennis.py
PYTHONPATH=/root/sports-backend python3 test_tennis.py
cd /root/sports-backend && git status
cd /root/sports-backend && git add . && git commit -m "feat: Working tennis dashboard with live data fetching and display"
cd /root/sports-backend && git checkout -b feature/tennis-dashboard && git tag v1.0-working-dashboard
cd /root/sports-backend && git tag v1.0-working-dashboard-2025-02-17
cd /root/sports-backend && git push origin feature/tennis-dashboard && git push origin v1.0-working-dashboard-2025-02-17
pip install flask
PYTHONPATH=/root/sports-backend python3 test_tennis.py
lsof -i :5000
pkill -f "python3 test_tennis.py" && PYTHONPATH=/root/sports-backend FLASK_APP=test_tennis.py FLASK_ENV=development python3 test_tennis.py
PYTHONPATH=/root/sports-backend FLASK_APP=test_tennis.py FLASK_DEBUG=1 python3 -m flask run --host=0.0.0.0 --port=5000
pkill -f "python3 test_tennis.py" && PYTHONPATH=/root/sports-backend python3 test_tennis.py
PYTHONPATH=/root/sports-backend python3 test_tennis.py
pkill -f "python3 test_tennis.py"
PYTHONPATH=/root/sports-backend python3 test_tennis.py
sudo lsof -t -i:5000 | xargs kill -9
PYTHONPATH=/root/sports-backend python3 test_tennis.py
pkill -f "python3 test_tennis.py" && PYTHONPATH=/root/sports-backend python3 test_tennis.py
cd /root/sports-backend && git tag v1.0-working-tennis-apis && git push origin v1.0-working-tennis-apis
cd /root/sports-backend && git checkout main
cd /root/sports-backend && git checkout -b feature/tennis-apis-working
cd /root/sports-backend && git tag v1.0-working-dashboard
cd /root/sports-backend && git tag -d v1.0-working-dashboard && git tag v1.0-working-dashboard && git push origin v1.0-working-dashboard
cd /root/sports-backend && git push --delete origin v1.0-working-dashboard && git tag v1.0-working-dashboard && git push origin v1.0-working-dashboard
cd /root/sports-backend && git tag -d v1.0-working-dashboard && git tag v1.0-working-dashboard && git push origin v1.0-working-dashboard
cd /root/sports-backend && git status
cd /root/sports-backend && git add . && git commit -m "feat: implemented both Rapid API and BetsAPI tennis data fetchers with prematch data" && git push origin feature/tennis-apis-working
cd /root/sports-backend && git tag -d v1.0-working-dashboard && git push --delete origin v1.0-working-dashboard && git tag v1.0-working-dashboard && git push origin v1.0-working-dashboard
cd /root/sports-backend && git status
cd /root/sports-backend && ls -la aggregator/sports/tennis/
cd /root/sports-backend && git add aggregator/sports/tennis/betsapi_prematch.py && git commit -m "feat: add betsapi_prematch.py with concurrent data fetching" && git push origin feature/tennis-apis-working
PYTHONPATH=/root/sports-backend python3 test_rapid_tennis.py
PYTHONPATH=/root/sports-backend python3 test_betsapi_prematch.py
rm /root/sports-backend/aggregator/aggregator.py
mv /root/sports-backend/aggregator/sports/tennis/tennis_odds_bot.py /root/sports-backend/aggregator/sports/tennis/tennis_odds.py
python test_tennis_odds.py
pkill -f "python3 test_tennis.py" && PYTHONPATH=/root/sports-backend python3 test_tennis.py
PYTHONPATH=/root/sports-backend python3 test_betsapi_prematch.py
cd /root/sports-backend && git add . && git commit -m "feat: implemented both Rapid API and BetsAPI tennis data fetchers" && git checkout main && git checkout -b feature/tennis-data-fetchers && git tag v1.0-working-dashboard && git push origin v1.0-working-dashboard
python3 rapid_tennis.py
rm bets_tennis.py
cd /root/sports-backend/aggregator/tennis/
python3 rapid_inplay.py
git branch --show-current && echo "---" && git status
git add . && git commit -m "Updated tennis bot with absolute imports and working fetchers. Ready for merger, parser, and database implementation."
git push origin feature/tennis-data-apis
source venv/bin/activate && cd /root/sports-backend/aggregator/sports/tennis && PYTHONPATH=/root/sports-backend python3 test_rapid_fetcher.py
cd /root/sports-backend
source venv/bin/activate && cd /root/sports-backend/aggregator/sports/tennis && PYTHONPATH=/root/sports-backend python3 rapid_tennis_fetcher.py
cd /root/sports-backend
git status
git add . && git commit -m "Added tennis bot implementation with fetchers, merger, parser, and database structure"
git checkout main
git checkout -b feature/tennis-components
git tag -l "v1.0-working-dashboard"
git push origin v1.0-working-dashboard
git branch
git checkout feature/tennis-data-apis
cd /root/sports-backend/aggregator/sports/tennis && python3 test.py
cd /root/sports-backend
git checkout feature/tennis-data-apis -- aggregator/sports/tennis/test.py
cd /root/sports-backend/aggregator/sports/tennis && python3 test.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 test.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 betsapi_prematch.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 tennis_bot.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 tennis_bot.py
cd /root/sports-backend
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.tennis_bot
python -m aggregator.sports.tennis.tennis_bot
python3 -m aggregator.sports.tennis.tennis_bot
pip3 install aiohttp
python3 -m venv venv
source venv/bin/activate && pip install aiohttp
python3 -m aggregator.sports.tennis.tennis_bot
source venv/bin/activate && pip install python-dotenv
source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.tennis_bot
cd /root/sports-backend/aggregator/sports/tennis
rm -f tennis_odds_bot.py tennis_odds.py test_rapid_fetcher.py
cd /root/sports-backend
source venv/bin/activate && cd /root/sports-backend/aggregator/sports/tennis && PYTHONPATH=/root/sports-backend python3 rapid_tennis_fetcher.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && PYTHONPATH=/root/sports-backend python3 test.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && PYTHONPATH=/root/sports-backend python3 test.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 rapid_tennis_fetcher.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 rapid_tennis_fetcher.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 test.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 rapid_tennis_fetcher.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 rapid_tennis_fetcher.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 test.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 test.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 test.py
cd /root/sports-backend
cd /root/sports-backend/aggregator/sports/tennis && python3 test.py
cd /root/sports-backend
git checkout main
git add aggregator/sports/tennis/betsapi_prematch.py && git commit -m "Updated BetsAPI prematch fetcher with hardcoded credentials and improved error handling"
git checkout main
echo "__pycache__/" >> .gitignore && git rm -r --cached "aggregator/__pycache__" && git commit -m "Remove __pycache__ files and add to gitignore"
git checkout main
git checkout -b feature/tennis-data-apis
git tag v1.0-working-dashboard
git push origin v1.0-working-dashboard
git status
cd /root/sports-backend/aggregator/sports/tennis && python3 betsapi_prematch.py
cd /root/sports-backend
echo "*.log" >> .gitignore
cd /root/sports-backend/aggregator/sports/tennis && python3 tennis_bot.py
cd /root/sports-backend
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.tennis_bot
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
import json
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher

async def get_match_data():
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    # Get first match from each
    if bets_data:
        print('\nBetsAPI Data (First Match):')
        print(json.dumps(bets_data[0], indent=2))
    
    if rapid_data:
        print('\nRapidAPI Data (First Match):')
        print(json.dumps(rapid_data[0], indent=2))

asyncio.run(get_match_data())
"
cd /root/sports-backend && source venv/bin/activate && pip install rapidfuzz && python3 -m pytest aggregator/sports/tennis/test_merger.py -v
cd /root/sports-backend && source venv/bin/activate && pip install pytest && python3 -m pytest aggregator/sports/tennis/test_merger.py -v
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m unittest aggregator/sports/tennis/test_merger.py -v
cd /root/sports-backend && source venv/bin/activate && pip install rapidfuzz
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m unittest aggregator/sports/tennis/test_merger.py -v
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

async def show_merged_match():
    # Get data from both APIs
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    merger = TennisMerger()
    
    print('Fetching from both APIs...\n')
    
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    # Merge the data
    merged = merger.merge(bets_data, rapid_data)
    
    if merged:
        # Show one matched event in detail
        match = next((m for m in merged if m['betsapi_data'] and m['rapid_data']), None)
        if match:
            print('Example of Merged Match Data:')
            print('\nBetsAPI Data:')
            print(f'Home: {match['betsapi_data']['players']['home']}')
            print(f'Away: {match['betsapi_data']['players']['away']}')
            print(f'Tournament: {match['betsapi_data'].get('tournament', 'N/A')}')
            
            print('\nRapidAPI Data:')
            event_data = match['rapid_data']['raw_event_data']
            print(f'Home: {event_data['home_player']}')
            print(f'Away: {event_data['away_player']}')
            print(f'Score: {event_data.get('score', 'N/A')}')
            
            print('\nMerged Result:')
            print(f'Home Player: {match['home_player']}')
            print(f'Away Player: {match['away_player']}')
    else:
        print('No live matches found with data from both APIs')

asyncio.run(show_merged_match())
"
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

async def show_merged_match():
    # Get data from both APIs
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    merger = TennisMerger()
    
    print('Fetching from both APIs...\n')
    
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    print(f'Found {len(bets_data)} matches from BetsAPI')
    print(f'Found {len(rapid_data)} matches from RapidAPI')
    
    # Show raw data from both APIs for one match
    if rapid_data:
        print('\nExample RapidAPI Match:')
        rd = rapid_data[0]
        event_data = rd.get('raw_event_data', {})
        print(f'Home: {event_data.get('home_player')}')
        print(f'Away: {event_data.get('away_player')}')
        print(f'Score: {event_data.get('score')}')
    
    if bets_data:
        print('\nExample BetsAPI Match:')
        bd = bets_data[0]
        print(f'Raw data: {bd}')

asyncio.run(show_merged_match())
"
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher

async def show_live_match():
    rapid_fetcher = RapidInplayOddsFetcher()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    if rapid_data:
        match = rapid_data[0]
        print('\nExample Live Tennis Match:')
        print(f'Raw Event Data: {match.get('raw_event_data')}')
        print(f'\nRaw Odds Data: {match.get('raw_odds_data', {}).keys()}')

asyncio.run(show_live_match())
"
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

async def test_merger():
    # Initialize components
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    merger = TennisMerger()
    
    # Get data from both sources
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    print(f'\nFound {len(bets_data)} matches from BetsAPI')
    print(f'Found {len(rapid_data)} matches from RapidAPI')
    
    # Use the merger to combine the data
    merged_data = merger.merge(bets_data, rapid_data)
    print(f'\nMerger produced {len(merged_data)} combined records')
    
    # Show an example of a merged match
    if merged_data:
        match = merged_data[0]
        print('\nExample of Merged Match:')
        print(f'Home Player: {match['home_player']}')
        print(f'Away Player: {match['away_player']}')
        print('\nBetsAPI Data Available:', 'Yes' if match['betsapi_data'] else 'No')
        print('RapidAPI Data Available:', 'Yes' if match['rapid_data'] else 'No')
        
        if match['rapid_data']:
            event = match['rapid_data']['raw_event_data']
            print(f'\nLive Score: {event.get('sets')} (sets), {event.get('score')} (current game)')

asyncio.run(test_merger())
"
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

async def test_merger():
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    merger = TennisMerger()
    
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    # Show raw data before merging
    print('\nRapidAPI first match:')
    if rapid_data:
        rd = rapid_data[0]
        event = rd.get('raw_event_data', {})
        print(f'Home: {event.get('team1')}')
        print(f'Away: {event.get('team2')}')
    
    print('\nBetsAPI first match:')
    if bets_data:
        bd = bets_data[0]
        print(f'Raw data: {bd}')
    
    # Now merge and show result
    merged_data = merger.merge(bets_data, rapid_data)
    print(f'\nMerger combined {len(merged_data)} records')
    
    if merged_data:
        match = merged_data[0]
        print('\nMerged Result:')
        print(f'Home: {match.get('home_player')}')
        print(f'Away: {match.get('away_player')}')
        if match.get('rapid_data'):
            event = match['rapid_data'].get('raw_event_data', {})
            print(f'Score: {event.get('sets')} (sets)')
        if match.get('betsapi_data'):
            print(f'Tournament: {match['betsapi_data'].get('tournament')}')

asyncio.run(test_merger())
"
which python3 && which pip3 && python3 --version && pip3 --version
source venv/bin/activate && which python && which pip && python --version && pip --version
source venv/bin/activate && python3 -c "import aiohttp; print(f'aiohttp version: {aiohttp.__version__}')"
source venv/bin/activate && python -m pip install --upgrade --force-reinstall aiohttp
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.tennis_bot
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_bot
cd /root/sports-backend && python3 -m aggregator.sports.tennis.tennis_bot
cd /root/sports-backend && pip3 install -r requirements.txt
cd /root/sports-backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
cd /root/sports-backend && source venv/bin/activate && pip install aiohttp
cd /root/sports-backend && source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot
git push -u origin tennis_merger_backup
git checkout -b tennis_merger_fixes
git push -u origin tennis_merger_fixes
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch

async def show_betsapi_data():
    fetcher = BetsapiPrematch()
    data = await fetcher.get_tennis_data()
    if data and len(data) > 0:
        print('\nFirst match data structure:')
        match = data[0]
        print('Players structure:')
        print(f'Full match data: {match}')
        if 'players' in match:
            print(f'\nPlayers dict: {match['players']}')
        if 'home' in match:
            print(f'\nHome player structure: {match['home']}')
        if 'away' in match:
            print(f'\nAway player structure: {match['away']}')

asyncio.run(show_betsapi_data())
"
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher

async def show_data_structures():
    # Get BetsAPI data
    bets_fetcher = BetsapiPrematch()
    bets_data = await bets_fetcher.get_tennis_data()
    
    print('\nBetsAPI Data Structure:')
    if bets_data and len(bets_data) > 0:
        match = bets_data[0]
        print(f'Full match structure: {match}')
    
    # Get RapidAPI data
    rapid_fetcher = RapidInplayOddsFetcher()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    print('\nRapidAPI Data Structure:')
    if rapid_data and len(rapid_data) > 0:
        match = rapid_data[0]
        print(f'raw_event_data: {match.get('raw_event_data')}')

asyncio.run(show_data_structures())
"
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "
import asyncio
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

async def test_merger():
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    merger = TennisMerger()
    
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    print('\nMerging data...')
    merged_data = merger.merge(bets_data, rapid_data)
    print(f'Merged {len(merged_data)} records')
    
    if merged_data:
        print('\nFirst merged record:')
        match = merged_data[0]
        print(f'Home player: {match.get('home_player')}')
        print(f'Away player: {match.get('away_player')}')

asyncio.run(test_merger())
"
cd /root/sports-backend && git add . && git commit -m "Fixed tennis merger to use team1/team2 fields from RapidAPI data" && git push origin tennis_merger_fixes && git tag -a v1.0.0-tennis-merger -m "Tennis merger with fixed player name extraction" && git push origin v1.0.0-tennis-merger
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 dump_raw_data.py
ls -l merged_data.json
pwd && ls -l merged_data.json
cd /root/sports-backend && source venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m pytest aggregator/sports/tennis/test_merger.py -v
cd /root/sports-backend && git add . && git commit -m "Save current state of tennis merger project"
cd /root/sports-backend && git remote -v
cd /root/sports-backend && git push origin tennis_merger_fixes
cd /root/sports-backend && git branch -v
cd /root/sports-backend && git checkout -b tennis_merger_backup && git add . && git commit -m "Saving current state of tennis merger implementation" && git remote add origin git@github.com:alextrx818/FinalProject.git && git push -u origin tennis_merger_backup
cd /root/sports-backend
git status
