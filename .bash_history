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
cd /root/sports-backend && pkill -f "python3 view_merged_data.py" || true
cd /root
cd /root/sports-backend && python3 -m json.tool mergedDump.json | less
curl http://165.227.123.99:8080
cd /root/sports-backend && pkill -f "python3 view_merged_data.py" || true
echo "mergedDump.json" >> /root/sports-backend/.gitignore
cd /root
cd /root/sports-backend && git rm --cached mergedDump.json || true
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && head -n 5 mergedDump.json
cd /root
cd /root/sports-backend && echo "First run timestamp:" && head -n 2 mergedDump.json && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump && echo "Second run timestamp:" && head -n 2 mergedDump.json
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && echo "Previous timestamp:" && head -n 2 mergedDump.json && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump && echo "New timestamp:" && head -n 2 mergedDump.json
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump && head -n 20 mergedDump.json
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump && head -n 30 mergedDump.json
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump && head -n 40 mergedDump.json
cd /root
cd /root/sports-backend && cat mergedDump.json | grep -A 50 '"FI": "170091742"'
cd /root
cd /root/sports-backend && cat mergedDump.json | grep -A 100 '"main": {' | grep -A 50 '170091742'
cd /root
cd /root/sports-backend && git status
cd /root
cd /root/sports-backend && git add . && git commit -m "Enhanced tennis merger with consistent player names across all data structures" && git push origin feature/tennis-merger-est-restore
cd /root
cd /root/sports-backend && git tag -a v1.0.0-tennis-merger-20250219 -m "Tennis merger with consistent player names across all data structures" && git push origin v1.0.0-tennis-merger-20250219
cd /root
cd /root/sports-backend && git status
cd /root
cd /root/sports-backend && git tag -a v1.0.0-tennis-merger-20250219-1751 -m "Tennis merger with consistent player names - final version" && git push origin v1.0.0-tennis-merger-20250219-1751
cd /root
cd /root/sports-backend && git tag -l
cd /root
cd /root/sports-backend/aggregator/sports/tennis && chmod +x dump_data.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/dump_data.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/dump_data.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/dump_data.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/dump_data.py
cd /root
cd /root/sports-backend && git status
cd /root
cd /root/sports-backend && git add aggregator/sports/tennis/dump_data.py && git commit -m "Added dump_data.py script for dumping merged tennis data with timestamps" && git push origin feature/tennis-merger-est-restore
cd /root
cd /root/sports-backend && git tag -a v1.0.0-tennis-merger-20250219-1844 -m "Added dump_data.py script for data analysis" && git push origin v1.0.0-tennis-merger-20250219-1844
tail -n 1000 /root/sports-backend/aggregator/sports/tennis/betsapi_prematch.log | grep -A 20 "Raw event data"
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -c "from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch; import asyncio; fetcher = BetsapiPrematch(); async def test(): async with fetcher.get_session() as session: data = await fetcher.fetch_prematch_data(session); print('Sample events:', data[:2] if data else 'No data'); asyncio.run(test())"
cd /root
source /root/venv/bin/activate && python3 /root/view_betsapi_data.py
tree /root/sports-backend/aggregator/sports/tennis
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_merge_dump
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_tennis_bot
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_orchestrator
cd /root
ls -l /root/sports-backend/mergedDump.json
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_orchestrator
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_orchestrator
cd /root
ls -l /root/sports-backend/mergedDump.json
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_orchestrator
cd /root
head -n 5 /root/sports-backend/mergedDump.json
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_orchestrator
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_orchestrator
cd /root
head -n 10 /root/sports-backend/mergedDump.json
cd /root/sports-backend && source /root/venv/bin/activate && pip install pytz
cd /root
cd /root/sports-backend && source /root/venv/bin/activate && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.test_orchestrator
cd /root
head -n 5 /root/sports-backend/mergedDump.json
cd /root/sports-backend && git status
cd /root
cd /root/sports-backend && git remote -v
cd /root
cd /root/sports-backend && git checkout -b feature/tennis-merger-update
cd /root
cd /root/sports-backend && git add aggregator/sports/tennis/test_orchestrator.py aggregator/sports/tennis/tennis_merger.py
cd /root
cd /root/sports-backend && git commit -m "Update tennis merger to prioritize RapidAPI player names and add EST timezone"
cd /root
cd /root/sports-backend && git push -u origin feature/tennis-merger-update
cd /root
ssh-keygen -t ed25519 -C "alextrx818@github" -f /root/.ssh/github_ed25519 -N ""
cat /root/.ssh/github_ed25519.pub
cd /root/sports-backend && git tag -a v1.0.0 -m "Tennis Merger with RapidAPI player names and EST timezone" && git push origin v1.0.0 && git push origin feature/tennis-merger-update
cd /root
cd /root/sports-backend && ssh -T git@github.com
cd /root
cd /root/sports-backend && git push origin main && git tag -a v1.0.0 -m "Tennis Merger with RapidAPI player names and EST timezone" && git push origin v1.0.0
cd /root
cd /root/sports-backend && git remote set-url origin https://github.com/alextrx818/FinalProject.git
cd /root
cd /root/sports-backend && git push origin main && git tag -a v1.0.0 -m "Tennis Merger with RapidAPI player names and EST timezone" && git push origin v1.0.0
cd /root
cd /root/sports-backend && git push -f origin main && git tag -a v1.0.0 -m "Tennis Merger with RapidAPI player names and EST timezone" && git push -f origin v1.0.0
cd /root
cd /root/sports-backend && git checkout -b feature/tennis-merger-est && git tag v1.0-working-dashboard && git push origin v1.0-working-dashboard
cd /root
cd /root/sports-backend && git tag -d v1.0-working-dashboard && git tag v1.0-working-dashboard && git push origin v1.0-working-dashboard
cd /root
cd /root/sports-backend && git push -f origin v1.0-working-dashboard
cd /root
cd /root/sports-backend && git add .
cd /root
cd /root/sports-backend && git commit -m "Update tennis merger with EST timezone"
cd /root
cd /root/sports-backend && git push
cd /root
cd /root/sports-backend && git push --set-upstream origin feature/tennis-merger-est
cd /root
cd /root/sports-backend && echo "mergedDump.json" >> .gitignore && echo "raw_merger_dumps/" >> .gitignore && git rm -r --cached mergedDump.json raw_merger_dumps/ && git commit -m "Remove large data files" && git push --set-upstream origin feature/tennis-merger-est
cd /root
cd /root/sports-backend && du -h mergedDump.json raw_merger_dumps/* test_merge_dump.py
cd /root
cd /root/sports-backend && find . -type f -size +500k -exec du -h {} \;
cd /root
cd /root/sports-backend && echo -e "\n# Generated data files\nmergedDump.json\nraw_merger_dumps/\n*.log" >> .gitignore && git rm -r --cached mergedDump.json raw_merger_dumps/ tennis_bot.log && git commit -m "Remove data files from git tracking" && git push --set-upstream origin feature/tennis-merger-est
cd /root
cd /root/sports-backend && git reset HEAD mergedDump.json raw_merger_dumps/ tennis_bot.log && echo -e "\n# Generated data files\nmergedDump.json\nraw_merger_dumps/\n*.log" >> .gitignore && git add .gitignore && git commit -m "Update gitignore to exclude data files" && git push --set-upstream origin feature/tennis-merger-est
cd /root
cd /root/sports-backend && git reset && git add aggregator/sports/tennis/test_orchestrator.py aggregator/sports/tennis/tennis_merger.py && git commit -m "Update tennis merger with EST timezone" && git push --set-upstream origin feature/tennis-merger-est
cd /root
cd /root/sports-backend && git checkout -b feature/tennis-merger-est-clean && git add aggregator/sports/tennis/test_orchestrator.py aggregator/sports/tennis/tennis_merger.py && git commit -m "Update tennis merger with EST timezone" && git push --set-upstream origin feature/tennis-merger-est-clean
cd /root
cd /root/sports-backend/aggregator/sports/tennis && git add test_orchestrator.py tennis_merger.py && git commit -m "Update tennis merger with EST timezone" && git push --set-upstream origin feature/tennis-merger-est-clean
cd /root
cd /root/sports-backend && git clean -fd && git add aggregator/sports/tennis/test_orchestrator.py aggregator/sports/tennis/tennis_merger.py && git commit -m "Update tennis merger with EST timezone" && git push --set-upstream origin feature/tennis-merger-est-clean
cd /root
cd /root/sports-backend && git add .gitignore aggregator/sports/tennis/test_orchestrator.py aggregator/sports/tennis/tennis_merger.py && git commit -m "Update tennis merger with EST timezone and improve .gitignore" && git push --set-upstream origin feature/tennis-merger-est-clean
cd /root
cd /root/sports-backend && git checkout -b feature/tennis-merger-est-v2 && git add .gitignore aggregator/sports/tennis/test_orchestrator.py aggregator/sports/tennis/tennis_merger.py && git commit -m "Update tennis merger with EST timezone and improve .gitignore" && git remote -v
cd /root
cd /root/sports-backend && git status -u .
cd /root
cd /root/sports-backend && git diff aggregator/sports/tennis/test_orchestrator.py
cd /root
cd /root/sports-backend && git log -n 3
cd /root
cd /root/sports-backend && git remote -v
cd /root
cd /root/sports-backend && git push --set-upstream origin feature/tennis-merger-est-v2
cd /root
cd /root/sports-backend && git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sort -nr -k3 | head -n 10
cd /root
cd /root/sports-backend && git reset --hard HEAD && git clean -fd
cd /root
cd /root && curl -Lo bfg.jar https://repo1.maven.org/maven2/com/madgag/bfg/1.14.0/bfg-1.14.0.jar
cd /root && java -jar bfg.jar --strip-blobs-bigger-than 10M sports-backend/.git
apt-get update && apt-get install -y default-jre
cd /root && java -jar bfg.jar --strip-blobs-bigger-than 10M sports-backend/.git
cd /root && rm -rf sports-backend && git clone --mirror https://github.com/alextrx818/FinalProject.git sports-backend.git
cd /root && java -jar bfg.jar --strip-blobs-bigger-than 10M sports-backend.git
cd /root && rm -rf sports-backend && git clone https://github.com/alextrx818/FinalProject.git sports-backend
cd /root/sports-backend && find . -type f -size +10M
cd /root
cd /root/sports-backend && git checkout -b feature/tennis-merger-est-v3 && git add .gitignore aggregator/sports/tennis/test_orchestrator.py aggregator/sports/tennis/tennis_merger.py && git commit -m "Update tennis merger with EST timezone and improve .gitignore" && git push --set-upstream origin feature/tennis-merger-est-v3
cd /root
cd /root/sports-backend && git add .gitignore aggregator/sports/tennis/test_orchestrator.py aggregator/sports/tennis/tennis_merger.py && git commit -m "Update tennis merger with EST timezone and improve .gitignore" && git push --set-upstream origin feature/tennis-merger-est-v3
cd /root
cd /root/sports-backend && ls -la
cd /root
cd /root/sports-backend/aggregator/sports/tennis && ls -la
cd /root
cd /root && ls -la sports-backend*/aggregator/sports/tennis/
cd /root/sports-backend && git checkout -- .
cd /root
cd /root/sports-backend/aggregator/sports/tennis && ls -la
cd /root
cd /root/sports-backend && git branch
cd /root
cd /root/sports-backend && git checkout feature/tennis-merger-est && git status
cd /root
cd /root && ls -la
cd /root && mv sports-backend sports-backend-new && mv sports-backend.git sports-backend-git && cd /root/sports-backend-new && git status
cd /root
cd /root/sports-backend-new/aggregator/sports/tennis && ls -la
cd /root
cd /root && ls -la
cd /root && ls -la /root/sports-backend/aggregator/sports/tennis/
cd /root && mv sports-backend-new sports-backend && ls -la /root/sports-backend/aggregator/sports/tennis/
cd /root/sports-backend && git checkout feature/tennis-merger-est
cd /root
cd /root/sports-backend && git branch -a
cd /root
cd /root/sports-backend && git checkout tennis_merger_backup
cd /root
cd /root/sports-backend && rm .gitignore && git checkout origin/tennis_merger_backup && ls -la aggregator/sports/tennis/
cd /root
cd /root/sports-backend && git checkout -b feature/tennis-merger-est-restore && ls -la aggregator/sports/tennis/
cd /root
cd /root/sports-backend/aggregator/sports/tennis && python3 test_merger.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_merger.py
cd /root
cd /root/sports-backend && ls -la aggregator/sports/tennis/test_orchestrator.py
cd /root
cd /root/sports-backend && ls -la aggregator/sports/tennis/test*
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_orchestrator.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_orchestrator.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/tennis_bot.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/tennis_bot.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_merger.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_merger.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_merger.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_orchestrator.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_orchestrator.py
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 aggregator/sports/tennis/test_orchestrator.py
cd /root
head -n 50 mergedDump.json
cd /root/sports-backend && head -n 50 mergedDump.json
cd /root
cd /root/sports-backend && cat mergedDump.json
cd /root
cd /root/sports-backend && pip install flask && python3 view_merged_data.py
cd /root
cd /root/sports-backend && python3 view_merged_data.py
cd /root
cd /root/sports-backend && python3 view_merged_data.py
/bin/python3 /root/.windsurf-server/extensions/ms-python.python-2025.0.0-universal/python_files/printEnvVariablesToFile.py /root/.windsurf-server/extensions/ms-python.python-2025.0.0-universal/python_files/deactivate/bash/envVars.txt
cd /root/sports-backend && python3 -m aggregator.sports.tennis.tennis_bot
cd /root
pip install aiohttp rapidfuzz
apt-get update && apt-get install -y python3-venv
python3 -m venv venv && source venv/bin/activate && pip install -r /root/sports-backend/requirements.txt aiohttp rapidfuzz
source venv/bin/activate && cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 -m aggregator.sports.tennis.tennis_bot
python3 -m aggregator.sports.tennis.dump_data
python3 -m aggregator.sports.tennis.test_merge_dump
pip install pytz
apt-get update && apt-get install -y python3-pytz
ls -la /root/sports-backend/
source venv/bin/activate && python3 -m aggregator.sports.tennis.test_merge_dump
source venv/bin/activate && pip install pytz
source venv/bin/activate && python3 -m aggregator.sports.tennis.test_merge_dump
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | head -n 100
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | grep -A 5 "rapid_data" | head -n 20
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/Nicolas Jarry/p' | grep "name" | sort | uniq
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | awk '/Francisco Comesana/{p=1}/"rapid_data"/{if(p)p=0}/name":/{ if(p) print}' | sort | uniq
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | awk '/Francisco Comesana/{p=1}/rapid_data/{p=0} /raw_prematch_data/{print "PREMATCH:"; pm=1} /inplay_event/{print "LIVE:"; pm=0} /"name":/{if(p) print (pm?"PREMATCH: ":"LIVE: ") $0}' | sort | uniq
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | grep -A 1 '"id": ".*"' | grep 'name' | sort | uniq
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | grep -A 1 'sp.*:.*{' | grep 'name' | sort | uniq
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep '"name"' | sort | uniq
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep -A 10 "inplay_event"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep -A 20 "rapid_data"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep -B2 -A2 "inplay"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep -B2 -A2 "sp"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep -B1 -A3 "updated_at.*1739" | grep "name\|updated_at" | sort
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep -B5 -A1 "updated_at.*173999" | grep "name"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep -A 5 "time_status.*1"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep -A 3 "sp.*{" | grep "name\|id"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/rapid_data/p' | grep "FI"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/marketFI.*170108473/,/rapid_data/p' | grep "name"
source venv/bin/activate && cat mergedDump.json | python3 -m json.tool | sed -n '/Francisco Comesana/,/Carol Zhao/p' | grep -B2 "name.*:"
source venv/bin/activate && pip install google-auth-oauthlib google-auth google-api-python-client
source venv/bin/activate && pip install pandas openpyxl
source venv/bin/activate && python json_to_excel.py
source venv/bin/activate && head -n 20 mergedDump.json
source venv/bin/activate && python format_odds.py > tennis_odds.txt
head -n 10 tennis_odds.txt
source venv/bin/activate && python format_table.py
head -n 10 tennis_odds_table.md
source venv/bin/activate && python format_csv.py && cat tennis_odds.csv
source venv/bin/activate && python format_csv.py && head -n 10 tennis_odds.csv
source venv/bin/activate && python3 -c "import json; f = open('mergedDump.json'); data = json.load(f); print(json.dumps(data['data'][0]['betsapi_data']['odds'][0], indent=2))"
source venv/bin/activate && python3 -c "import json; f = open('mergedDump.json'); data = json.load(f); print(json.dumps(list(data['data'][0].keys()), indent=2))"
source venv/bin/activate && python format_csv.py && head -n 10 tennis_odds.csv
source venv/bin/activate && python3 -c "import json; f = open('mergedDump.json'); data = json.load(f); print(json.dumps(data['data'][0]['rapid_data'].keys(), indent=2))"
source venv/bin/activate && python3 -c "import json; f = open('mergedDump.json'); data = json.load(f); print(list(data['data'][0]['rapid_data'].keys()))"
source venv/bin/activate && python format_csv.py && cat tennis_odds.csv
cat temp_data.json | python format_csv.py && cat tennis_odds.csv
pip install tabulate
cat temp_data.json | python format_table.py
pip install pandas openpyxl
cat temp_data.json | python json_to_excel.py
ls -l tennis_odds.xlsx
python3 -c "import pandas as pd; print(pd.read_excel('tennis_odds.xlsx'))"
mkdir -p ~/output
rm json_to_table.py
cat paste_json_here.txt | python json_to_table.py
mkdir -p json_tools && mv json_to_table.py paste_json_here.txt json_tools/
pip install deepdiff
cd json_tools && cat paste_json_here.txt | python json_to_table.py
cd /root/sports-backend
cat json_tools/paste_json_here.txt | python json_tools/json_to_table.py
cat json_tools/paste_json_here.txt | tr -d '\n' | python json_tools/json_to_table.py
cat -A json_tools/paste_json_here.txt | head -n 1
sed '1d' json_tools/paste_json_here.txt | python json_tools/json_to_table.py
(sed '1d' json_tools/paste_json_here.txt; echo "1") | python json_tools/json_to_table.py
cat json_tools/paste_json_here.txt | python3 -c "import sys, json; print(json.dumps(json.load(sys.stdin)))" | python json_tools/json_to_table.py
echo '{"sport":"tennis","score":"1:0","sets":"6:4,0:0","serve":"team2","game":"0:0","liga":"ATP Rio De Janeiro","eventId":"6V170101074C13A_1_1","eventName":"Sebastian Baez - Mariano Navone","team1":"Sebastian Baez","team2":"Mariano Navone","marketFI":"170108501","evLink":"https://www.bet365.com/#/IP/EV151151151045C13","markets":[{"fi":"170108501","na":"Sebastian Baez","id":"161142517","it":"6VP170108501-0161142517_1_1","od":"8/13","or":"0","su":"0","zw":"170108501-161142517","group":"Set 2 Winner","coef":1.615}]}' > temp.json && cat temp.json | python json_tools/json_to_table.py
(echo '{"sport":"tennis","score":"1:0","sets":"6:4,0:0","serve":"team2","game":"0:0","liga":"ATP Rio De Janeiro","eventId":"6V170101074C13A_1_1","eventName":"Sebastian Baez - Mariano Navone","team1":"Sebastian Baez","team2":"Mariano Navone","marketFI":"170108501","evLink":"https://www.bet365.com/#/IP/EV151151151045C13","markets":[{"fi":"170108501","na":"Sebastian Baez","id":"161142517","it":"6VP170108501-0161142517_1_1","od":"8/13","or":"0","su":"0","zw":"170108501-161142517","group":"Set 2 Winner","coef":1.615}]}'; echo "1") | python json_tools/json_to_table.py
python3 -c "import json; print(json.dumps(json.loads('''$(cat json_tools/paste_json_here.txt | tail -n +2)''')))" > temp.json && (cat temp.json; echo "1") | python json_tools/json_to_table.py
cd json_tools && python json_to_table.py
cd /root/sports-backend
cd json_tools && python json_to_table.py
cd /root/sports-backend
cd json_tools && python json_to_table.py
cd /root/sports-backend
git status
git add json_tools/
git commit -m "Update json_to_table.py to read from paste_json_here.txt file directly"
git push origin feature/tennis-merger-est-restore
git tag -a v1.0.0-json-tools -m "First stable version of JSON tools with file-based input"
git push origin v1.0.0-json-tools
PYTHONPATH=/root/sports-backend python -m aggregator.sports.tennis.test_orchestrator
PYTHONPATH=/root/sports-backend python -i aggregator/sports/tennis/test_orchestrator.py
PYTHONPATH=/root/sports-backend python -m aggregator.sports.tennis.tennis_bot
python tennis_bot.py
cd /root/sports-backend
PYTHONPATH=/root/sports-backend python -m aggregator.sports.tennis.tennis_bot
ps aux | grep python
PYTHONPATH=/root/sports-backend python -m aggregator.sports.tennis.tennis_bot
head -n 20 mergedDump.json
PYTHONPATH=/root/sports-backend python -m aggregator.sports.tennis.test_merger
ps aux | grep python
kill 482364 611469 611873
PYTHONPATH=/root/sports-backend python -m aggregator.sports.tennis.tennis_bot
[200~sudo -u postgres psql
~sudo -u postgres psql
sudo -u postgres psql
[200~CREATE DATABASE tennis_db;
\c tennis_db
~CREATE DATABASE tennis_db;
\c tennis_db
CREATE DATABASE tennis_db;
\c tennis_db
sudo -u postgres psql
ALTER ROLE amireslami WITH PASSWORD 'LIncoln95amir';
sudo -u postgres psql
[200~psql --username=amireslami --dbname=tennis_db
psql --username=amireslami --dbname=tennis_db
/etc/postgresql/16/main/pg_hba.conf
sudo nano /etc/postgresql/16/main/pg_hba.conf
sudo systemctl reload postgresql
psql --username=amireslami --dbname=tennis_db
psql -V
systemctl status postgresql
psql -l
sudo -u postgres psql -c "CREATE DATABASE tennis_db;"
sudo -u postgres psql -d tennis_db -c "CREATE TABLE tennis_matches (match_id VARCHAR(50) PRIMARY KEY, raw_data JSONB NOT NULL, inserted_at TIMESTAMP DEFAULT NOW());"
sudo -u postgres psql -d tennis_db -c "\d tennis_matches"
sudo -u postgres psql -c "SHOW data_directory;"
tree /root/sports-backend/aggregator/sports/tennis
mkdir -p /root/sports-backend/aggregator/databases/tennis
rm -rf /root/sports-backend/aggregator/databases
tree /root/sports-backend/aggregator/sports/tennis
PYTHONPATH=/root/sports-backend python3 -c "from aggregator.sports.tennis.tennis_database import TennisDatabase; db = TennisDatabase()"
sudo -u postgres psql -c "CREATE USER amireslami WITH PASSWORD 'LIncoln95amir';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE tennis_db TO amireslami;"
PYTHONPATH=/root/sports-backend python3 -c "from aggregator.sports.tennis.tennis_database import TennisDatabase; db = TennisDatabase()"
sudo -u postgres psql -d tennis_db -c "GRANT ALL ON SCHEMA public TO amireslami;"
PYTHONPATH=/root/sports-backend python3 -c "from aggregator.sports.tennis.tennis_database import TennisDatabase; db = TennisDatabase()"
sudo -u postgres psql -c "SHOW hba_file;"
sudo cat /etc/postgresql/16/main/pg_hba.conf
sudo sed -i 's/scram-sha-256/md5/g' /etc/postgresql/16/main/pg_hba.conf && sudo systemctl restart postgresql
PYTHONPATH=/root/sports-backend python3 -c "from aggregator.sports.tennis.tennis_database import TennisDatabase; db = TennisDatabase()"
sudo -u postgres psql -c "ALTER USER amireslami WITH PASSWORD 'LIncoln95amir';"
PYTHONPATH=/root/sports-backend python3 -c "from aggregator.sports.tennis.tennis_database import TennisDatabase; db = TennisDatabase()"
sudo -u postgres createdb tennis_db
PGPASSWORD='LIncoln95amir' psql -U amireslami -d tennis_db -h localhost
source venv/bin/activate
python /root/sports-backend/aggregator/sports/tennis/tennis_database.py
root@ubuntu-s-4vcpu-16gb-amd-nyc3-01:~#
PGPASSWORD='LIncoln95amir' psql -U amireslami -d tennis_db -h localhost
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_bot
cd /root
cd /root/sports-backend && python3 -m aggregator.sports.tennis.tennis_bot
which python3 && python3 -c "import sys; print(sys.path)"
ls -la /root/sports-backend/venv/bin/activate 2>/dev/null || ls -la /root/venv/bin/activate 2>/dev/null || ls -la /root/.venv/bin/activate 2>/dev/null || echo "No venv found in common locations"
cd /root
source /root/sports-backend/venv/bin/activate && cd /root/sports-backend && python3 -m aggregator.sports.tennis.tennis_bot
cd /root
sudo service postgresql status
source /root/sports-backend/venv/bin/activate && cd /root/sports-backend && python3 view_tennis_data.py
cd /root
pkill -f "python3 -m aggregator.sports.tennis.tennis_bot" && cd /root/sports-backend && source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot
pkill -f "python3 view_tennis_data.py"
git status
git remote add origin git@github.com:alextrx818/FinalProject.git
git add aggregator/sports/tennis/tennis_bot.py aggregator/sports/tennis/tennis_database.py aggregator/sports/tennis/tennis_merger.py requirements.txt
git commit -m "Updated tennis database implementation with proper table creation and indexes"
git push origin feature/tennis-merger-est-restore
git status
git add aggregator/sports/tennis/models.py
git commit -m "Added tennis database models with table and index definitions"
git push origin feature/tennis-merger-est-restore
git status
git log -n 2
source venv/bin/activate && pip install fastapi uvicorn
curl http://localhost:8000/merged_data
cd /root
source venv/bin/activate && cd /root/sports-backend && python3 server.py
source venv/bin/activate && pip install fastapi uvicorn
cd /root
source venv/bin/activate && cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 server.py
pip install fastapi "uvicorn[standard]" --break-system-packages
cd /root
cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 server.py
cd /root
pkill -f "python3 server.py" && cd /root/sports-backend && PYTHONPATH=/root/sports-backend python3 server.py
pkill -f "python3 server.py" && source venv/bin/activate && python3 server.py
source venv/bin/activate && python3 server.py
cd /root/sports-frontend/sports-frontend && npm install axios
cd /root
cd /root/sports-frontend/sports-frontend && npm install axios --legacy-peer-deps
cd /root
cd /root/sports-frontend/sports-frontend && npm install && npm install axios
cd /root/sports-backend
pkill -f "python server.py" && python server.py
cd /root/sports-frontend/sports-frontend
npm install axios --save
npm install axios --save --legacy-peer-deps
cd /root/sports-backend
python3 -m aggregator.sports.tennis.tennis_bot
pip install pytz
python3 -m venv venv && source venv/bin/activate && pip install pytz
source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot
cd /root/sports-backend && source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot
cd /root
pip install fastapi uvicorn
cd /root/sports-backend
python server.py
pkill -f "python3 server.py" && python3 server.py
cd /root/sports-frontend/sports-frontend
npm run dev
/bin/python3 /root/.windsurf-server/extensions/ms-python.python-2025.0.0-universal/python_files/printEnvVariablesToFile.py /root/.windsurf-server/extensions/ms-python.python-2025.0.0-universal/python_files/deactivate/bash/envVars.txt
pkill -f tennis_bot.py
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_bot
pkill -f tennis_bot.py
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_bot
cd /root/sports-backend && python print_sample_data.py
head -n 50 sample_tennis_data.json
tail -n 50 sample_tennis_data.json
cd /root/sports-backend && python print_sample_data.py
head -n 50 merged_match_data.json
tail -n 50 merged_match_data.json
cd /root/sports-backend && python print_sample_data.py
head -n 50 merged_matches_data.json
tail -n 50 merged_matches_data.json
cat merged_matches_data.json
cd /root/sports-backend && python print_sample_data.py
cat merged_matches_data.json
cd /root/sports-backend && python print_sample_data.py
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_database
pip install asyncpg
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_database
psql -U amireslami -d tennis_db -c "\dt"
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_database
systemctl status postgresql
psql -U postgres -l
sudo -u postgres psql -l
sudo -u postgres psql -d tennis_db -c "\dt"
sudo -u postgres psql -d tennis_db -c "GRANT ALL PRIVILEGES ON TABLE tennis_matches TO amireslami;"
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_database
sudo -u postgres psql -d tennis_db -c "ALTER TABLE tennis_matches OWNER TO amireslami;"
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_database
cd /root/sports-backend && git status
cd /root/sports-backend && git add aggregator/sports/tennis/tennis_bot.py aggregator/sports/tennis/tennis_database.py
cd /root/sports-backend && git commit -m "Updated tennis database implementation with asyncpg and added merged data storage"
cd /root/sports-backend && git push origin feature/tennis-merger-est-restore
sudo apt update
sudo apt upgrade -y
sudo systemctl status pgadmin4
sudo reboot
cd /root/sports-backend && python -m aggregator.sports.tennis.tennis_bot
uname -r
sudo systemctl status postgresql
sudo -u postgres psql
sudo apt update
sudo apt install pgadmin4
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu $(lsb_release -cs) pgadmin4" > /etc/apt/sources.list.d/pgadmin4.list'
sudo apt update
lsb_release -cs
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu focal pgadmin4" > /etc/apt/sources.list.d/pgadmin4.list'
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
curl -o /etc/apt/trusted.gpg.d/pgadmin.gpg https://www.pgadmin.org/static/packages_pgadmin_org.pub
sudo apt update
sudo rm /etc/apt/sources.list.d/pgadmin4.list
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu bionic pgadmin4" > /etc/apt/sources.list.d/pgadmin4.list'
curl -o /etc/apt/trusted.gpg.d/pgadmin.gpg https://www.pgadmin.org/static/packages_pgadmin_org.pub
sudo apt update
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
sudo rm /etc/apt/sources.list.d/pgadmin4.list
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu jammy pgadmin4" > /etc/apt/sources.list.d/pgadmin4.list'
curl -o /etc/apt/trusted.gpg.d/pgadmin.gpg https://www.pgadmin.org/static/packages_pgadmin_org.pub
sudo apt update
sudo rm /etc/apt/sources.list.d/pgadmin4.list
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu focal pgadmin4" > /etc/apt/sources.list.d/pgadmin4.list'
sudo apt update
sudo rm /etc/apt/sources.list.d/pgadmin4.list
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu focal-pgdg main" > /etc/apt/sources.list.d/pgadmin4.list'
curl -o /etc/apt/trusted.gpg.d/pgadmin.gpg https://www.pgadmin.org/static/packages_pgadmin_org.pub
sudo apt update
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt focal-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo rm /etc/apt/trusted.gpg.d/pgadmin.gpg
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/pgadmin.gpg > /dev/null
sudo apt update
sudo rm /etc/apt/sources.list.d/pgadmin4.list
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt focal-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/pgdg.gpg > /dev/null
sudo apt update
sudo apt install pgadmin4
deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu focal-pgdg InRelease
sudo nano /etc/apt/sources.list.d/pgadmin4.list
sudo apt update
deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/ubuntu focal pgadmin4 main
ls /etc/apt/sources.list.d/
sudo nano /etc/apt/sources.list.d/pgadmin4.list
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
sudo apt update
sudo apt install libgmp3-dev libpq-dev
sudo rm /etc/apt/sources.list.d/pgadmin4.list
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
echo "deb https://ftp.pgadmin.org/pub/pgadmin4/apt/ubuntu focal pgadmin4" | sudo tee /etc/apt/sources.list.d/pgadmin4.list
sudo apt update
date
sudo apt-get install --reinstall ca-certificates
sudo update-ca-certificates
sudo nano /etc/apt/sources.list.d/pgadmin4.list
sudo apt update
sudo rm /etc/apt/sources.list.d/pgadmin4.list
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
echo "deb https://ftp.pgadmin.org/pub/pgadmin4/apt/ubuntu jammy pgadmin4" | sudo tee /etc/apt/sources.list.d/pgadmin4.list
sudo apt update
id username
id your_actual_username
whoami
adduser newusername
adduser amireslami
usermod -aG sudo amireslami
ufw app list
ufw allow OpenSSH
ufw enable
ufw status
ssh%20amireslami@165.227.123.99
http://ssh%20amireslami@165.227.123.99/
$ ssh amireslami@165.227.123.99
ssh amireslami@165.227.123.99
mkdir -p /root/CascadeProjects/flask_test
sudo apt update
sudo apt install nginx
sudo command_to_run
ssh amireslami@165.227.123.99
cd /root/sports-backend && git checkout -b Created_Database
cd /root/sports-backend && git status
cd /root/sports-backend && git add aggregator/sports/tennis/tennis_bot.py aggregator/sports/tennis/tennis_database.py .gitignore
cd /root/sports-backend && git commit -m "Database Implementation Complete: Added database storage functionality for tennis matches"
cd /root/sports-backend && git tag -a v1.0.0-database -m "Database implementation milestone: Tennis match data storage complete"
cd /root/sports-backend && git push origin Created_Database && git push origin v1.0.0-database
cd /root/sports-backend && python3 -m aggregator.sports.tennis.tennis_bot
pwd
hostname -I
ps aux | grep test_flask_app.py
curl -I http://livesportsalerts.io:8000
dig livesportsalerts.io
ps aux | grep test_flask_app.py
curl http://165.227.123.99:8000
curl http://livesportsalerts.io:8000
curl http://livesportsalerts.io
sudo netstat -tulpn | grep :80
curl -I http://livesportsalerts.io:8000
curl -I http://livesportsalerts.io
sudo ufw status
ls -la /etc/nginx/sites-enabled/
cat /etc/nginx/sites-available/your_domain
cat /etc/nginx/sites-available/165.227.123.99
cat /etc/nginx/sites-available/livesportsalerts.io
sudo bash -c 'cat > /etc/nginx/sites-available/livesportsalerts.io << EOL
server {
    listen 80;
    listen [::]:80;

    server_name livesportsalerts.io www.livesportsalerts.io;
        
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOL'
sudo ln -sf /etc/nginx/sites-available/livesportsalerts.io /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/165.227.123.99 /etc/nginx/sites-enabled/your_domain
sudo nginx -t
sudo systemctl restart nginx
curl http://livesportsalerts.io
certbot --version
sudo apt update && sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d livesportsalerts.io -d www.livesportsalerts.io
curl -I http://livesportsalerts.io
curl -I https://livesportsalerts.io
sudo netstat -tulpn | grep 'nginx\|:80\|:443'
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list'
sudo apt update && sudo apt install -y pgadmin4-web
sudo /usr/pgadmin4/bin/setup-web.sh
y
sudo bash -c 'cat > /etc/nginx/sites-available/pgadmin.livesportsalerts.io << EOL
server {
    listen 80;
    listen [::]:80;
    server_name pgadmin.livesportsalerts.io;

    location / {
        proxy_pass http://127.0.0.1:5050;
        proxy_set_header X-Script-Name /pgadmin4;
        proxy_set_header X-Scheme \$scheme;
        proxy_set_header Host \$host;
        proxy_redirect off;
    }
}
EOL'
sudo ln -sf /etc/nginx/sites-available/pgadmin.livesportsalerts.io /etc/nginx/sites-enabled/ && sudo nginx -t
sudo bash -c 'cat > /etc/systemd/system/pgadmin4.service << EOL
[Unit]
Description=pgAdmin4 service
After=network.target

[Service]
User=www-data
Group=www-data
Environment="PATH=/usr/pgadmin4/venv/bin:\$PATH"
ExecStart=/usr/pgadmin4/venv/bin/gunicorn --bind 127.0.0.1:5050 --workers=1 --threads=25 --chdir /usr/pgadmin4/web/ pgAdmin4:app

[Install]
WantedBy=multi-user.target
EOL'
sudo apt install -y gunicorn && sudo systemctl daemon-reload && sudo systemctl enable pgadmin4 && sudo systemctl start pgadmin4
sudo certbot --nginx -d pgadmin.livesportsalerts.io
dig pgadmin.livesportsalerts.io
sudo systemctl status pgadmin4
dig pgadmin.livesportsalerts.io
sudo certbot --nginx -d pgadmin.livesportsalerts.io
sudo systemctl status pgadmin4
sudo /usr/pgadmin4/bin/setup-web.sh --yes
sudo bash -c 'cat > /etc/systemd/system/pgadmin4.service << EOL
[Unit]
Description=pgAdmin4 service
After=network.target

[Service]
User=www-data
Group=www-data
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
ExecStart=/usr/local/bin/gunicorn --bind 127.0.0.1:5050 --workers=1 --threads=25 --chdir /usr/share/pgadmin4/web pgAdmin4:app

[Install]
WantedBy=multi-user.target
EOL'
sudo systemctl daemon-reload && sudo systemctl restart pgadmin4 && sudo systemctl status pgadmin4
which gunicorn
sudo apt install -y python3-gunicorn && which gunicorn
ls -la /usr/share/pgadmin4/web/
find / -name pgadmin4 2>/dev/null
sudo apt remove -y pgadmin4-web && sudo pip3 install pgadmin4
sudo apt install -y python3-venv && python3 -m venv /opt/pgadmin4 && source /opt/pgadmin4/bin/activate && pip install pgadmin4
sudo bash -c 'cat > /etc/systemd/system/pgadmin4.service << EOL
[Unit]
Description=pgAdmin4 service
After=network.target

[Service]
User=www-data
Group=www-data
Environment="PATH=/opt/pgadmin4/bin:/usr/local/bin:/usr/bin:/bin"
ExecStart=/opt/pgadmin4/bin/gunicorn --bind 127.0.0.1:5050 --workers=1 --threads=25 pgAdmin4:app
WorkingDirectory=/opt/pgadmin4/lib/python3.12/site-packages/pgadmin4

[Install]
WantedBy=multi-user.target
EOL'
sudo mkdir -p /var/lib/pgadmin && sudo chown -R www-data:www-data /var/lib/pgadmin && sudo -u www-data python3 /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4/setup.py
sudo mkdir -p /var/lib/pgadmin && sudo chown -R www-data:www-data /var/lib/pgadmin && sudo mkdir -p /var/log/pgadmin && sudo chown -R www-data:www-data /var/log/pgadmin && sudo -u www-data /opt/pgadmin4/bin/python3 -c "from pgadmin4.config import SQLITE_PATH; from pgadmin4.setup import db_upgrade; db_upgrade(SQLITE_PATH)"
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg && sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list' && sudo apt update && sudo apt install -y pgadmin4-web
sudo /usr/pgadmin4/bin/setup-web.sh --yes
sudo systemctl stop apache2 && sudo systemctl disable apache2
sudo bash -c 'cat > /etc/systemd/system/pgadmin4.service << EOL
[Unit]
Description=pgAdmin4 service
After=network.target

[Service]
User=www-data
Group=www-data
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
ExecStart=/usr/bin/python3 /usr/pgadmin4/web/pgAdmin4.py
WorkingDirectory=/usr/pgadmin4/web

[Install]
WantedBy=multi-user.target
EOL'
sudo systemctl daemon-reload && sudo systemctl enable pgadmin4 && sudo systemctl start pgadmin4 && sudo systemctl status pgadmin4 && sudo nginx -t && sudo systemctl reload nginx
sudo netstat -tlpn | grep 5050
sudo journalctl -u pgadmin4 -n 50
sudo apt install -y python3-flask-socketio python3-flask python3-werkzeug python3-sqlalchemy python3-flask-sqlalchemy python3-flask-migrate && sudo -H pip3 install flask-socketio
sudo bash -c 'cat > /etc/pgadmin4/config_system.py << EOL
import os

DATA_DIR = os.path.realpath(os.path.expanduser(u"/var/lib/pgadmin"))
LOG_FILE = os.path.join(DATA_DIR, "pgadmin4.log")
SQLITE_PATH = os.path.join(DATA_DIR, "pgadmin4.db")
SESSION_DB_PATH = os.path.join(DATA_DIR, "sessions")
STORAGE_DIR = os.path.join(DATA_DIR, "storage")
SERVER_MODE = True
EOL'
sudo apt remove -y --purge pgadmin4* && sudo rm -rf /var/lib/pgadmin /var/log/pgadmin /etc/pgadmin4 /usr/pgadmin4 && sudo apt update && sudo apt install -y postgresql-16 pgadmin4-web
sudo docker pull dpage/pgadmin4 && sudo docker run -d -p 5050:80 --name pgadmin4 -e "PGADMIN_DEFAULT_EMAIL=admin@admin.com" -e "PGADMIN_DEFAULT_PASSWORD=admin" dpage/pgadmin4
curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
sudo docker pull dpage/pgadmin4 && sudo docker run -d -p 5050:80 --name pgadmin4 -e "PGADMIN_DEFAULT_EMAIL=admin@admin.com" -e "PGADMIN_DEFAULT_PASSWORD=admin" dpage/pgadmin4
sudo systemctl stop pgadmin4 || true && sudo systemctl disable pgadmin4 || true && sudo nginx -t && sudo systemctl reload nginx && sudo docker ps | grep pgadmin4
sudo docker stop pgadmin4 && sudo docker rm pgadmin4
sudo mkdir -p /var/lib/pgadmin4/{sessions,storage} /var/log/pgadmin4 && sudo apt install -y libgmp3-dev libpq-dev python3-venv
python3 -m venv /opt/pgadmin4 && source /opt/pgadmin4/bin/activate && pip install pgadmin4 gunicorn
sudo mkdir -p /etc/pgadmin4 && sudo bash -c 'cat > /etc/pgadmin4/config_system.py << EOL
import os

DATA_DIR = os.path.realpath(os.path.expanduser(u"/var/lib/pgadmin4"))
LOG_FILE = os.path.join(DATA_DIR, "pgadmin4.log")
SQLITE_PATH = os.path.join(DATA_DIR, "pgadmin4.db")
SESSION_DB_PATH = os.path.join(DATA_DIR, "sessions")
STORAGE_DIR = os.path.join(DATA_DIR, "storage")
SERVER_MODE = True
EOL'
sudo bash -c 'cat > /etc/systemd/system/pgadmin4.service << EOL
[Unit]
Description=pgAdmin4 service
After=network.target

[Service]
User=www-data
Group=www-data
Environment="PATH=/opt/pgadmin4/bin:/usr/local/bin:/usr/bin:/bin"
ExecStart=/opt/pgadmin4/bin/gunicorn --bind unix:/tmp/pgadmin4.sock --workers=1 --threads=25 pgAdmin4:app
WorkingDirectory=/opt/pgadmin4/lib/python3.12/site-packages/pgadmin4

[Install]
WantedBy=multi-user.target
EOL'
sudo chown -R www-data:www-data /var/lib/pgadmin4 /var/log/pgadmin4 /opt/pgadmin4 && sudo chmod 775 /var/lib/pgadmin4 /var/log/pgadmin4
sudo systemctl daemon-reload && sudo systemctl enable pgadmin4 && sudo systemctl start pgadmin4 && sudo systemctl status pgadmin4 && sudo nginx -t && sudo systemctl reload nginx
cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py
cd /root
cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py --help
cd /root
cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py setup-db && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py add-user --username admin@admin.com --password admin
cd /root
sudo mkdir -p /var/lib/pgadmin && sudo chown -R www-data:www-data /var/lib/pgadmin && cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py setup-db && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py add-user --username admin@admin.com --password admin
cd /root
sudo mkdir -p /var/lib/pgadmin /var/log/pgadmin && sudo chown -R www-data:www-data /var/lib/pgadmin /var/log/pgadmin && cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py setup-db && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py add-user --username admin@admin.com --password admin
cd /root
cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py add-user admin@admin.com admin
cd /root
cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py add-user amireslami@gmail.com admin123
cd /root
cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py update-user amireslami@gmail.com --role admin
cd /root
cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py update-user --help
cd /root
cd /opt/pgadmin4/lib/python3.12/site-packages/pgadmin4 && sudo -u www-data /opt/pgadmin4/bin/python3 setup.py update-user amireslami@gmail.com --admin --active
cd /root
sudo systemctl restart pgadmin4 && sudo systemctl status pgadmin4
sudo ufw status
sudo ufw allow 'Nginx Full' && sudo ufw allow ssh && sudo ufw status
sudo adduser amireslami && sudo usermod -aG sudo amireslami
sudo systemctl status nginx
sudo tail -f /var/log/pgadmin/pgadmin4.log
sudo -u postgres psql -c "SELECT datname, pg_size_pretty(pg_database_size(datname)) as size FROM pg_database;"
chmod +x /root/db_maintenance.sh && sudo bash -c 'echo "0 0 * * 0 root /root/db_maintenance.sh > /var/log/db_maintenance.log 2>&1" > /etc/cron.d/db_maintenance'
sudo -u postgres psql -c "ALTER SYSTEM SET maintenance_work_mem = '128MB';" && sudo -u postgres psql -c "ALTER SYSTEM SET autovacuum_vacuum_scale_factor = '0.1';" && sudo -u postgres psql -c "ALTER SYSTEM SET autovacuum_analyze_scale_factor = '0.05';" && sudo systemctl restart postgresql
sudo -u postgres psql -d tennis_db -c "\dt"
sudo -u postgres psql -c "\du"
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres123';"
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'LIncoln95amir';"
cd /root/sports-backend/aggregator/sports/tennis
cd /root/sports-backend/aggregator/sports/tennis && python3 tennis_bot.py
cd /root/sports-backend
cd /root/sports-backend && python3 -m aggregator.sports.tennis.tennis_bot
pip3 install aiohttp
pip3 install asyncpg pytz
cd /root/sports-backend && python3 -m aggregator.sports.tennis.tennis_bot
pip3 install rapidfuzz
cd /root/sports-backend && python3 -m aggregator.sports.tennis.tennis_bot
ls -la /var/www/livesportsalerts.io/static/
sudo mkdir -p /var/www/livesportsalerts.io/static/
sudo mkdir -p /var/www/livesportsalerts.io/media/
sudo chown -R www-data:www-data /var/www/livesportsalerts.io/static/
sudo chown -R www-data:www-data /var/www/livesportsalerts.io/media/
sudo chmod -R 755 /var/www/livesportsalerts.io/static/
sudo chmod -R 755 /var/www/livesportsalerts.io/media/
python3 test_flask_app.py
/bin/python3 /root/.windsurf-server/extensions/ms-python.python-2025.0.0-universal/python_files/printEnvVariablesToFile.py /root/.windsurf-server/extensions/ms-python.python-2025.0.0-universal/python_files/deactivate/bash/envVars.txt
lsof -i :8765
pkill -9 python
cat /etc/nginx/sites-enabled/*
lsof -i :8000
lsof -i :8765
ls -l /var/www/html/
cd /root/sports-frontend/sports-frontend
cd /root/sports-frontend/sports-frontend && npm run build
cd /root
rm -rf /var/www/html/* && cp -r /root/sports-frontend/sports-frontend/dist/* /var/www/html/
cat > /etc/nginx/sites-enabled/livesportsalerts << 'EOL'
server {
    server_name livesportsalerts.io www.livesportsalerts.io;
        
    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /ws {
        proxy_pass http://127.0.0.1:8765;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    listen [::]:443 ssl ipv6only=on;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/livesportsalerts.io/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/livesportsalerts.io/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
}

server {
    if ($host = www.livesportsalerts.io) {
        return 301 https://$host$request_uri;
    }

    if ($host = livesportsalerts.io) {
        return 301 https://$host$request_uri;
    }

    listen 80;
    listen [::]:80;
    server_name livesportsalerts.io www.livesportsalerts.io;
    return 404;
}
EOL

nginx -t && systemctl restart nginx
mv /etc/nginx/sites-enabled/livesportsalerts.io /etc/nginx/sites-enabled/livesportsalerts.io.bak && cat > /etc/nginx/sites-enabled/livesportsalerts << 'EOL'
server {
    server_name livesportsalerts.io www.livesportsalerts.io;
        
    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /ws {
        proxy_pass http://127.0.0.1:8765;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    listen [::]:443 ssl ipv6only=on;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/livesportsalerts.io/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/livesportsalerts.io/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
}
EOL

nginx -t && systemctl restart nginx
rm /etc/nginx/sites-enabled/* && cat > /etc/nginx/sites-enabled/livesportsalerts << 'EOL'
server {
    server_name livesportsalerts.io www.livesportsalerts.io;
        
    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /ws {
        proxy_pass http://127.0.0.1:8765;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    listen [::]:443 ssl ipv6only=on;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/livesportsalerts.io/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/livesportsalerts.io/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
}

server {
    listen 80;
    listen [::]:80;
    server_name livesportsalerts.io www.livesportsalerts.io;
    return 301 https://$server_name$request_uri;
}
EOL

nginx -t && systemctl restart nginx
cd /root/sports-backend
pkill -9 -f tennis_bot.py && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root
ps aux | grep tennis_bot
pkill -9 -f tennis_bot.py
cd /root/sports-backend
cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
pkill -9 -f tennis_bot.py
cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
pkill -f tennis_bot.py
cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
pkill -f tennis_bot.py
cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root/sports-frontend/sports-frontend && npm run serve
cd /root/sports-frontend/sports-frontend && npm run dev
source venv/bin/activate && pip install websockets
cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot
cd /root
lsof -i :8765
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root
lsof -i :8765
cd /root/sports-frontend/sports-frontend
cd /root/sports-frontend/sports-frontend && npm run build && rm -rf /var/www/html/* && cp -r dist/* /var/www/html/
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root/sports-frontend/sports-frontend
cd /root/sports-frontend/sports-frontend && npm run build && rm -rf /var/www/html/* && cp -r dist/* /var/www/html/
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
pkill -f "python3 -m aggregator.sports.tennis.tennis_bot"
less tennis_bot.log
python -m aggregator.sports.tennis.tennis_bot
python3 -m aggregator.sports.tennis.tennis_bot
pip3 install aiohttp fastapi uvicorn
python3 -m venv venv
source venv/bin/activate && pip install -r requirements.txt aiohttp fastapi uvicorn
source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot
source venv/bin/activate && pip install asyncpg
source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot
source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot > tennis_bot.log 2>&1 &
source venv/bin/activate && python3 -m aggregator.sports.tennis.tennis_bot | tee tennis_bot.log
cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root/sports-frontend/sports-frontend
cd /root/sports-frontend/sports-frontend && npm run build && rm -rf /var/www/html/* && cp -r dist/* /var/www/html/
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root/sports-frontend/sports-frontend && npm run build && rm -rf /var/www/html/* && cp -r dist/* /var/www/html/
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root
tail -n 50 /var/log/nginx/error.log
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root/sports-backend && source venv/bin/activate && python -c "import asyncio; from websocket_server import main; asyncio.run(main())"
cd /root
lsof -i :8765
ps aux | grep tennis_bot
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root
lsof -i :8765
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cat > /etc/nginx/sites-available/default << 'EOL'
server {
    listen 80;
    listen [::]:80;
    server_name livesportsalerts.io;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name livesportsalerts.io;

    ssl_certificate /etc/letsencrypt/live/livesportsalerts.io/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/livesportsalerts.io/privkey.pem;

    location / {
        root /var/www/html;
        try_files $uri $uri/ /index.html;
    }

    location /ws {
        proxy_pass http://localhost:8765;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOL

nginx -t && systemctl reload nginx
cd /root/sports-frontend/sports-frontend
cd /root/sports-frontend/sports-frontend && npm run build && rm -rf /var/www/html/* && cp -r dist/* /var/www/html/
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
cd /root
cat /etc/nginx/sites-enabled/default
ls -la /etc/nginx/conf.d/
nginx -t && systemctl restart nginx
find /etc/nginx -type f -exec grep -l "livesportsalerts.io" {} \;
cat /etc/nginx/sites-enabled/livesportsalerts
cd /root/sports-frontend/sports-frontend && npm run build && cp -r dist/* /var/www/html/
cd /root
cd /root/sports-frontend/sports-frontend && npm run build && cp -r dist/* /var/www/html/
cd /root/sports-backend
pkill -9 python && cd /root/sports-backend && source venv/bin/activate && python -m aggregator.sports.tennis.tennis_bot
