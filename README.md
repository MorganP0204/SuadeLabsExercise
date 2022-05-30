# **K-TCD CALCULATOR**

### **How to Run the Code:**

Please alter the text in line 8 with the correct json data file you would like to use to calculate K-TCD.
After that, simply run the python file "KtcdCalculator.py".


### What is the code actually doing?
K-TCD captures the risk to an investment firm by counterparties to repo transactions in this case by multiplying the 
value of the exposures, based on replacement costs and an add-on for potential risk exposure, by risk factors based on 
regulations, accounting for the mitigating effects of effective netting and the exchange of collateral

In order to further align the treatment of counterparty credit risk with Regulation (EU) No 575/2013, a fixed multiplier
of 1.2 and a multiplier for credit valuation adjustment (CVA) to reflect the current market value of the credit risk of 
the counterparty to the investment firm in specific transactions should also be added. (alpha and CVA)

Reverse repurchase agreements (RRPs) are the buyer end of a repurchase agreement. (counterparty

## **Equation for K-TCD**:

own funds requirement = alpha * EV * RF * CVA

where:

- alpha is given as 1.2

- EV: exposure value = max(0, RC + PFE - C)
  - RC: replacement cost
    - for repurchase transactions it is the amount of cash
lent or borrowed; cash lent by the investment firm is to be treated
as a positive amount and cash borrowed by the investment firm is to be 
treated as a negative amount
  - PFE: potential future exposure (only applicable to derivative contracts)
  - C: Collateral 
    - sum of the CMV (current market value: found in the "mtm_dirty" variable) of the security (asset) leg and 
the net amount of collateral posted or received by the investment firm
(For securities financing transactions, where both legs of the transaction are securities, collateral is determined by the CMV of the security borrowed by the investment firm)

- RF: Risk Factor defined by counterparty type
corresponds to the "customer variable"
- CVA: Credit Valuation Adjustment (either 1 or 1.5 depending on type of transaction)











