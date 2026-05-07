from apscheduler.schedulers.background import BackgroundScheduler

# Create Scheduler
scheduler = BackgroundScheduler()

# Start Scheduler
def start_scheduler():
    scheduler.start()