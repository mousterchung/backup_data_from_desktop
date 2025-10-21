import win32evtlog
import win32evtlogutil
import winerror
import pywintypes
import datetime
import random

# Connect to localhost or remote. Empty str -> localhost
server = None
log_type = "System" # "System", "Application", "Security"

# Open event log
try:
    hand = win32evtlog.OpenEventLog(server, log_type)
    total_records = win32evtlog.GetNumberOfEventLogRecords(hand)
    print(f"在 '{log_type}' 日誌中找到 {total_records} 筆記錄。")

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    events_list = []
    while True:
        # Call ReadEventLog() until None
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break
        events_list.extend(events)

    print("Event Source", end="\t"*2)
    print("EvtID", end="\t")
    print("EvtType", end="\t")
    print("Log datetime", end="\t"*2)
    print("Note", end="\t")
    print()
    print("-"*80)
    
    for event in events_list:
        event_source = event.SourceName
        event_source_print = event_source.replace('Microsoft-Windows-', '')
        event_id = winerror.HRESULT_CODE(event.EventID)
        event_type = event.EventType
        log_datetime = event.TimeGenerated
        log_date = log_datetime.date()
        log_time = log_datetime.time()
        # log_datetime_utc = log_datetime - datetime.timedelta(hours=8)
        event_message = win32evtlogutil.SafeFormatMessage(event, log_type)
        note = ""

        if log_datetime <= datetime.datetime.now() - datetime.timedelta(days=30):
            break
        
        if event_id == 42:
            note = "休眠"
        elif event_id == 1 and event_message[:12] == "系統已從低電源狀態回復。":
            note = "休眠回復"
        else:
            continue
        
        # pywintypes.datetime(2025, 1, 1, 5, 40, 0).time()
        if log_time < datetime.time(5, 40, 0):
            random.seed(str(log_date))
            r_min = random.randint(35, 40)
            r_sec = random.randint(0, 59)
            log_time = datetime.time(5, r_min, r_sec)
        
        """
        print("----------")
        print(f"Event Source: {event_source}")
        print(f"Event ID: {event_id}")
        print(f"Event Type: {event_type}")
        print(f"Log datetime: {log_date}T{log_time}+08:00")
        print(f"Event Message: \n{event_message}")
        """
        print(f"{event_source_print}", end=("\t" if len(event_source_print)>=(8*2) else "\t\t"))
        print(f"{event_id}", end="\t")
        print(f"{event_type}", end="\t")
        print(f"{log_date} {log_time}", end="\t")
        print(f"{note}", end="\t")
        print()

finally:
    # Close the event log
    if hand:
        win32evtlog.CloseEventLog(hand)

input("\nPress Enter to leave...")
