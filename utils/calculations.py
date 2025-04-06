def calculate_amount_after_fee(amount, withdrawal_fee_percentage, withdrawal_fee_fixed):
    fee = amount * (withdrawal_fee_percentage / 100) + withdrawal_fee_fixed
    return amount - fee
