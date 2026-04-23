def monitoring_agent(sensor_data):
    if sensor_data["temperature"] > 85 or sensor_data["vibration"] > 4.5:
        return {"anomaly": True, "severity": "HIGH"}
    return {"anomaly": False, "severity": "LOW"}


def analytics_agent(sensor_data):
    cycle = sensor_data["cycle_count"]
    rul = 1000 - cycle

    prob = 0.8 if rul < 200 else 0.2

    return {
        "rul": rul,
        "failure_prob_7d": prob
    }


def decision_agent(analysis):
    prob = analysis["failure_prob_7d"]

    if prob > 0.7:
        return "IMMEDIATE MAINTENANCE"
    elif prob > 0.5:
        return "SCHEDULE MAINTENANCE"
    else:
        return "CONTINUE MONITORING"


def run_pipeline(sensor_data):
    monitor = monitoring_agent(sensor_data)
    analysis = analytics_agent(sensor_data)
    decision = decision_agent(analysis)

    return {
        "monitoring": monitor,
        "analytics": analysis,
        "decision": decision
    }