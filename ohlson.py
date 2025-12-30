import math

def calculate_o_score(fin):
    TA = fin["total_assets"]
    TL = fin["total_liabilities"]
    CA = fin["current_assets"]
    CL = fin["current_liabilities"]
    NI = fin["net_income"]
    WC = CA - CL

    if TA == 0:
        return 0, 0

    X1 = math.log(TA)
    X2 = TL / TA
    X3 = WC / TA
    X4 = CL / CA if CA > 0 else 0
    X5 = 1 if NI < 0 else 0
    X6 = NI / TA

    o_score = (
        -1.32
        - 0.407 * X1
        + 6.03 * X2
        - 1.43 * X3
        + 0.076 * X4
        - 1.72 * X5
        - 2.37 * X6
    )

    p_bankruptcy = math.exp(o_score) / (1 + math.exp(o_score))

    return o_score, p_bankruptcy
