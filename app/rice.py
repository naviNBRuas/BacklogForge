def calculate_rice(reach, impact, confidence, effort):
    if effort == 0:
        raise ValueError("effort must be greater than zero")
    return (reach * impact * confidence) / effort
