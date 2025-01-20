from datetime import datetime
import pytz

def checkTime():
    """Check the actual time where you are
    
        Args:
        None

        Returns:
            Current time where Lucy is hosted.
    """
    print("Checking current time!")
    spain_timezone = pytz.timezone("Europe/Madrid")
    spain_time = datetime.now(spain_timezone)
    return (f"Current time in Spain: {spain_time.strftime('%Y-%m-%d %H:%M:%S')}")
