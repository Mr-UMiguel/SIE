from prefect.utilities.notifications import gmail_notifier
from prefect import Task, Flow

def state_handler(obj, old_state, new_state):
    msg = "".join(f"""
    Calling my custom state handler on {obj}:\n{old_state} to {new_state}
    """)
    pass
