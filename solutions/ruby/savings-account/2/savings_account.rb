module SavingsAccount
  def self.interest_rate(balance)
    return 3.213 if balance < 0
    return 0.500 if balance < 1_000
    return 1.621 if balance < 5_000
    return 2.475
  end

  def self.annual_balance_update(balance)
    balance * (1 + interest_rate(balance) / 100.0)
  end

  def self.years_before_desired_balance(current_balance, desired_balance)
    years = 0
    while current_balance < desired_balance
      current_balance = annual_balance_update(current_balance)
      years += 1
    end
    years
  end

end
