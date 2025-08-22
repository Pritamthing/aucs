## Getting Started

First, to run the app in a Docker container

```bash
docker --version

```
If Docker is running on your machine, you are good to go

##Activate the env, first navigate to the project folder
### Windows 
```CMD
venv\Scripts\activate
```
##Linux or Mac
```CMD
source venv/bin/activate
```

Once the virtual Env is activated, run the Docker Compose command to up all containers in detached mode
```bash
 docker compose up -d
```

### Running front-end
 Clone the front-end repo and run the app as mentioned in README file

##Default users and cleanup logs
1. Added 10 users by default and 1 Cleanup Report logs 
 ##Testing functionality
 1. Open the front-end with url ```http://localhost:3000/dashboard```
 2. Now, check the dashboard table with single record
 3. Click or Trigger on ```Cleanup Inactive Users```
 4. See the log reports in the table 
 5. The Celery job scheduler is scheduled to run every 5 minutes using crontab exp, which is configured in the settings.py
    

