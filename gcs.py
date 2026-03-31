"""
Glasgow Coma Scale (GCS) Module

Provides:
- Input validation
- GCS calculation
- Clinical interpretation
"""


# -------------------------
# Validation
# -------------------------

def validate_score(value: int, min_val: int, max_val: int, name: str) -> int:
    """
    Validate that a score is an integer within a specific range.

    Args:
        value (int): Input score
        min_val (int): Minimum allowed value
        max_val (int): Maximum allowed value
        name (str): Name of parameter (E, V, M)

    Returns:
        int: Validated score

    Raises:
        TypeError: If not an integer
        ValueError: If out of range
    """
    if not isinstance(value, int):
        raise TypeError(f"{name} score must be an integer.")

    if value < min_val or value > max_val:
        raise ValueError(f"{name} score must be between {min_val} and {max_val}.")

    return value


# -------------------------
# Calculation
# -------------------------

def calculate_gcs(eye: int, verbal: int, motor: int) -> int:
    """
    Calculate total GCS score.

    Args:
        eye (int): Eye opening score (1–4)
        verbal (int): Verbal response score (1–5)
        motor (int): Motor response score (1–6)

    Returns:
        int: Total GCS score
    """

    # Validate inputs
    eye = validate_score(eye, 1, 4, "Eye")
    verbal = validate_score(verbal, 1, 5, "Verbal")
    motor = validate_score(motor, 1, 6, "Motor")

    return eye + verbal + motor


# -------------------------
# Interpretation
# -------------------------

def interpret_gcs(score: int) -> dict:
    """
    Interpret GCS score into clinical category and suggestion.

    Args:
        score (int): Total GCS score

    Returns:
        dict: {
            "category": str,
            "suggestion": str
        }
    """

    if not isinstance(score, int):
        raise TypeError("GCS score must be an integer.")

    if score < 3 or score > 15:
        raise ValueError("GCS score must be between 3 and 15.")

    if score <= 8:
        return {
            "category": "Severe Brain Injury",
            "suggestion": "URGENT: Secure airway (consider intubation) and ICU management."
        }

    elif 9 <= score <= 12:
        return {
            "category": "Moderate Brain Injury",
            "suggestion": "Close monitoring and urgent CT brain recommended."
        }

    else:  # 13–15
        return {
            "category": "Mild Brain Injury",
            "suggestion": "Observation and reassessment. Monitor for deterioration."
        }


# -------------------------
# Helper (Optional but useful)
# -------------------------

def format_gcs_output(eye: int, verbal: int, motor: int) -> dict:
    """
    Full pipeline: calculate + interpret + format output.

    Returns:
        dict: structured result for frontend
    """

    score = calculate_gcs(eye, verbal, motor)
    interpretation = interpret_gcs(score)

    return {
        "score": score,
        "breakdown": f"E{eye} V{verbal} M{motor}",
        "category": interpretation["category"],
        "suggestion": interpretation["suggestion"]
    }