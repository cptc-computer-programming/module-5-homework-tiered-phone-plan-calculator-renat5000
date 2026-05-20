# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3



# The program prompts the user for data usage, monthly plan cost, and whether they are a premium user.
data_usage_gb = float(input("Enter the data usage in GB: "))
monthly_plan = int(input("Enter the monthly plan cost: "))
premium_user_input = input("Is the user a premium user? (yes/no): ").strip().lower()
is_premium_user = premium_user_input == "yes"
5
# proccessing monthly bill 
total_bill = monthly_plan   
if data_usage_gb > TIER_1_DATA_LIMIT_GB:
    if data_usage_gb <= TIER_2_DATA_LIMIT_GB:
        overage_gb = data_usage_gb - TIER_1_DATA_LIMIT_GB
        if is_premium_user:
            total_bill += overage_gb * PREMIUM_USER_OVERAGE_RATE_TIER_2
        else:
            total_bill += overage_gb * REGULAR_USER_OVERAGE_RATE_TIER_2
    else:
        overage_gb_tier_2 = TIER_2_DATA_LIMIT_GB - TIER_1_DATA_LIMIT_GB
        overage_gb_tier_3 = data_usage_gb - TIER_2_DATA_LIMIT_GB
        if is_premium_user:
            total_bill += overage_gb_tier_2 * PREMIUM_USER_OVERAGE_RATE_TIER_2
            total_bill += overage_gb_tier_3 * PREMIUM_USER_OVERAGE_RATE_TIER_3
        else:
            total_bill += overage_gb_tier_2 * REGULAR_USER_OVERAGE_RATE_TIER_2
            total_bill += overage_gb_tier_3 * REGULAR_USER_OVERAGE_RATE_TIER_3

          
        # output
print(f"Your total bill is: ${total_bill:.2f}") 
print("----------------------------------------")
print("Thank you for using The Moon Data Central!") 