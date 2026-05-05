def add_employee_features(df):
    df['Employee'] = 1
    df['EmployeeID'] = range(1, len(df) + 1)
    return df