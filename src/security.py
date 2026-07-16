def reject_patient_identifiers(record):
    forbidden={"patient_name","dob","medical_record_number","email","phone"}
    return not bool(forbidden.intersection(record))
