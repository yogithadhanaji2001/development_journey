# bank(bank_name,person_name,account_number,balance) depost(amount) withdraw(amount) bal_enq()

class bank:

    def set_customer_details(self,person_name,acc_no,bal):

        self.bank_name="SBI"

        self.person_name=person_name

        self.acc_no=acc_no

        self.bal=bal

    def bal_enq(self):

        print(f"{self.bank_name} customer your acc {self.acc_no} avl balance is {self.bal}")

          

