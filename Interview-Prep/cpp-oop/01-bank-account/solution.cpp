// BankAccount — reference solution.
//   g++ -std=c++17 -Wall -Wextra -g solution.cpp -o solution && ./solution
#include <iostream>
#include <stdexcept>
#include <string>

class BankAccount {
public:
    // explicit: prevents accidental BankAccount a = "name"; conversions.
    explicit BankAccount(std::string owner, double startingBalance = 0.0)
        : owner_(std::move(owner)), balance_(startingBalance) {
        if (startingBalance < 0.0)
            throw std::invalid_argument("starting balance cannot be negative");
    }

    void deposit(double amount) {
        requirePositive(amount);
        balance_ += amount;
        ++txnCount_;
    }

    void withdraw(double amount) {
        requirePositive(amount);
        if (amount > balance_)
            throw std::runtime_error("insufficient funds");
        balance_ -= amount;
        ++txnCount_;
    }

    // const: this method promises not to mutate the object, so it can be
    // called on a `const BankAccount&`.
    double balance() const { return balance_; }
    const std::string& owner() const { return owner_; }
    int transactionCount() const { return txnCount_; }

private:
    static void requirePositive(double amount) {
        if (amount <= 0.0)
            throw std::invalid_argument("amount must be positive");
    }

    std::string owner_;
    double balance_ = 0.0;   // private: only mutated through validated methods
    int txnCount_ = 0;
};

int main() {
    BankAccount acct{"Joseph", 100.0};
    acct.deposit(50.0);
    acct.withdraw(30.0);
    std::cout << acct.owner() << " balance: " << acct.balance()
              << " (" << acct.transactionCount() << " txns)\n";  // 120, 2 txns

    try {
        acct.withdraw(1000.0);
    } catch (const std::exception& e) {
        std::cout << "Rejected: " << e.what() << "\n";
    }
    return 0;
}

// Notes:
// - balance_ is private so the only path to change it runs the invariant
//   checks. A public balance_ would let callers set it to -1 directly.
// - For real money, prefer integer cents over double to avoid 0.1+0.2!=0.3
//   floating-point rounding. double is used here for brevity.
