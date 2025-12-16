import math

def calculate_o_score(
    total_assets,
    total_liabilities,
    working_capital,
    current_assets,
    current_liabilities,
    net_income,
    prev_net_income
):
    X = 1 if total_liabilities > total_assets else 0
    Y = 1 if (net_income < 0 and prev_net_income < 0) else 0
    Z = (net_income - prev_net_income) / (abs(net_income) + abs(prev_net_income) + 1)

    o_score = (
        -1.32
        - 0.407 * math.log(total_assets)
        + 6.03 * (total_liabilities / total_assets)
        - 1.43 * (working_capital / total_assets)
        + 0.076 * (current_liabilities / current_assets)
        - 1.72 * X
        - 2.37 * (net_income / total_assets)
        - 1.83 * Y
        + 0.285 * Z
    )

    return round(o_score, 2)
