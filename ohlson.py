import math

def calculate_o_score(fin):

    TA = fin["total_assets"]
    TL = fin["total_liabilities"]
    CA = fin["current_assets"]
    CL = fin["current_liabilities"]
    NI = fin["net_income"]
    CFO = fin["cfo"]

    X = -1.32 \
        - 0.407 * math.log(TA) \
        + 6.03 * (TL / TA) \
        - 1.43 * ((CA - CL) / TA) \
        + 0.076 * (CL / CA) \
        - 1.72 * (NI / TA) \
        - 2.37 * (CFO / TL)

    return X
