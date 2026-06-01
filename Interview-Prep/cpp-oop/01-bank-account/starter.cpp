// BankAccount — fill in the TODOs. Build:
//   g++ -std=c++17 -Wall -Wextra -g starter.cpp -o starter && ./starter
#include <iostream>
#include <stdexcept>
#include <string>

class BankAccount {
public:
    // TODO: constructor(s). Should it be explicit?
    // TODO: deposit(double amount)
    // TODO: withdraw(double amount)
    // TODO: double balance() const
    // TODO: const std::string& owner() const
    // TODO: int transactionCount() const

private:
    // TODO: members (owner name, balance, transaction count)
};

int main() {
    BankAccount acct{"Joseph", 100.0};
    acct.deposit(50.0);
    acct.withdraw(30.0);
    std::cout << acct.owner() << " balance: " << acct.balance()
              << " (" << acct.transactionCount() << " txns)\n";

    try {
        acct.withdraw(1000.0);  // should throw (overdraft)
    } catch (const std::exception& e) {
        std::cout << "Rejected: " << e.what() << "\n";
    }
    return 0;
}
