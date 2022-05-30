import json
import unittest

# the code should:
# accept as an input 2 legs of the SFT as a JSON file
# return the K-TCD for that transaction

# Open the json data in read mode; you will need to alter line 8 with the data file you would like to use.
with open("data.json", "r") as read_file:
    dataset = json.load(read_file)


# This function encapsulates the calculation of K-TCD by passing in the dataset.
def calculate_ktcd(data):
    # split the data into the cash and asset leg of the SFT
    if data["data"][0]["movement"] == "cash":
        cash_leg = data["data"][0]
        asset_leg = data["data"][1]
    elif data["data"][0]["movement"] == "asset":
        cash_leg = data["data"][1]
        asset_leg = data["data"][0]
    else:
        raise Exception("data not valid")  # do not run the function if the SFT is not a cash and asset reverse repo

    # Now we will start calculating each piece of the K-TCD equation

    # alpha is given
    alpha = 1.2

    # Exposure Value Calculation:
    # first we will calculate Replacement Cost and Collateral

    # Replacement cost should be positive since the investment firm is lending money in a reverse repo
    replacementcost = -cash_leg["balance"]
    # print(replacementcost)  # test; should be 1500

    # Collateral is equal to the current market value of the asset
    # Adjust for potential currency mismatches (see Article 30(3))
    if cash_leg["currency_code"] == asset_leg["currency_code"]:
        currency_adjustment = 1
    else:
        currency_adjustment = 0.08
    # print(currency_adjustment)  # test; should be 1

    collateral = asset_leg["mtm_dirty"] * currency_adjustment
    # print(collateral)  # test; should be 1400

    # Now we can calculate exposure value
    exposure = max(0, replacementcost - collateral)
    # print(exposure)  # test; should be 100

    # Calculate risk factor which is determined by counterparty type:

    # first isolate counterparty type
    counterparty = asset_leg["issuer"]["type"]
    # print(counterparty)  # test; should return central_govt

    # determine risk factor based on counterparty types from Table 2 in Article 26
    if "central" or "regional" in counterparty:
        riskfactor = .016
    elif "credit" or "investment" in counterparty:
        riskfactor = .016
    else:
        riskfactor = .08

    # print(str(riskFactor * 100) + "%")  # test; should be 1.6%

    # Credit Value Adjustment (cva) is equal to the market value times 1 since we are working with an SFT
    # (see Article 32 point d)
    cva = 1 * asset_leg["mtm_dirty"]

    # Now we can calculate the K-TCD! Exciting :)
    ktcd = alpha * exposure * riskfactor * cva
    print(ktcd)  # should be 2688.0
    return ktcd


calculate_ktcd(dataset)
