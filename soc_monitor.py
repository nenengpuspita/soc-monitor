# PORTOFOLIO 2 (SOC MONITOR) WITH ALERT

# IMPORT

import os
import json
from datetime import datetime, UTC
import uuid

# DEFAULT DATA

total_summary = {

         "INFO" : 0,
         "WARN" : 0,
         "ERROR": 0,
         "BRUTEFORCE ATTEMPT" : 0

}


# FUNCTION

def security_parse(lines):

	summary = {

	     "INFO" : 0,
	     "WARN" : 0,
	     "ERROR": 0,
	     "BRUTEFORCE ATTEMPT" : 0

	}

	for each_lines in lines:
		only_status = each_lines.split()[0]

		if only_status in summary:
			summary[only_status] += 1

	return summary


def detect_bruteforce(lines):
	total_bruteforce = 0

	for each_lines in lines:

		if "failed password" in each_lines:
			total_bruteforce += 1

	return total_bruteforce


def merge_summary(total, summary_per_file):

	for key in summary_per_file:
		total[key] += summary_per_file[key] 

	return total


def decide_security_status(result_mergesummary):
	
	if total_summary["ERROR"] >= 5 or total_summary["BRUTEFORCE ATTEMPT"] >= 5:
		return "CRITICAL"

	elif total_summary["ERROR"] >= 2 or total_summary["WARN"] >= 3:
		return "WARNING"

	return "NORMAL"


def alert_level(result_mergesummary):

	if result_mergesummary["STATUS SYSTEM"] == "CRITICAL":
		return "HIGH"

	elif result_mergesummary["STATUS SYSTEM"] == "WARNING":
		return "MEDIUM"

	return None

def decide_alert_reason(result_mergesummary):

	if result_mergesummary["ALERT"] == "HIGH":
                return "high error or brute force activity detected"

	elif result_mergesummary["ALERT"] == "MEDIUM":
                return "moderate error rate and elevated warning detected"

	return None


def get_timestamp():
	return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def generate_alert_id():
	return str(uuid.uuid4())


def decide_alert(result_mergesummary):
	
	if result_mergesummary["ALERT"] is None:
		return None

	alert = {

	    "alert_level" : result_mergesummary["ALERT"],
	    "reason" : decide_alert_reason(result_mergesummary),
	    "timestamp" : get_timestamp(),
	    "alert_id" : generate_alert_id(),
	    "details" : {
		
		"ERROR" : result_mergesummary["ERROR"],
		"BRUTEFORCE ATTEMPT" : result_mergesummary["BRUTEFORCE ATTEMPT"]

	    }

	}

	
	return alert



# MAIN FLOW

files = os.listdir("security_logs")

for filename in files:
	with open("security_logs/" + filename) as read_file:
		lines = read_file.readlines()
		summary = security_parse(lines)
		summary["BRUTEFORCE ATTEMPT"] = detect_bruteforce(lines)

		result_mergesummary = merge_summary(total_summary, summary)
		
# CALL RESULT GLOBAL SUMMARY
result_mergesummary["STATUS SYSTEM"] = decide_security_status(result_mergesummary)
result_mergesummary["ALERT"] = alert_level(result_mergesummary)

# CALL ALERT

result_alert = decide_alert(result_mergesummary)


# REPORT / OUTPUT

# REPORT SECURITY

folder_report_name = "reports"
file_name_in_folder = "security_reports.json"

file_report_path = os.path.join(folder_report_name, file_name_in_folder)

with open(file_report_path, "w") as file_report:
	json.dump(result_mergesummary, file_report, indent=4)


# REPORT ALERT

folder_alert_name = "alerts"
file_alert_name = "alerts.json"

file_alert_path = os.path.join(folder_alert_name, file_alert_name)

if result_alert is not None:
	with open(file_alert_path, "w") as alert_file:
		json.dump(result_alert, alert_file, indent=4)
