def validate_case(case):
    required = {"case_id", "note", "reference_label", "synthetic"}
    return required.issubset(case) and case["synthetic"] is True and isinstance(case["note"], str)
