# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3


# Your code goes here:

data_usage_gb = float(input("Enter the data usage in GB: "))
monthly_plan = int(input("Enter the monthly plan cost: "))
premium_user_input = input("Is the user a premium user? (yes/no): ").strip().lower()
is_premium_user = premium_user_input == "yes"
total_bill = monthly_plan

