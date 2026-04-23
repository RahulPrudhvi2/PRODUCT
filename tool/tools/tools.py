def detect_anomaly(sensor_data):
    if sensor_data["temperature"] > 85 or sensor_data["vibration"] > 4.5:
        return {"anomaly": True, "score": 0.8}
    return {"anomaly": False, "score": 0.2}


def predict_rul(cycle_count):
    rul = 1000 - cycle_count
    return {
        "rul": rul,
        "failure_prob_7d": 0.8 if rul < 200 else 0.2
    }


def decide_action(prob):
    if prob > 0.7:
        return "IMMEDIATE MAINTENANCE"
    elif prob > 0.5:
        return "SCHEDULE MAINTENANCE"
    else:
        return "CONTINUE MONITORING"