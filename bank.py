import streamlit as st

# -------------------------------
# BANK VERSION 1
# -------------------------------

class Bank_v1:

    bank_name = "SBI"
    bank_roi = 6
    bank_ifsc = 1245
    bank_address = "KR Puram"

    def __init__(self, n, ac, b, ad):
        self.name = n
        self.account = ac
        self.balance = b
        self.address = ad

    def customer_details(self):

        st.write(f"Customer Name : {self.name}")
        st.write(f"Customer Account : {self.account}")
        st.write(f"Customer Balance : ₹{self.balance}")
        st.write(f"Customer Address : {self.address}")

    @staticmethod
    def get_int_value():

        value = st.number_input(
            "Enter Amount",
            min_value=0,
            step=100
        )

        return value

    def withdraw(self):

        amount = self.get_int_value()

        if amount <= self.balance:

            self.balance -= amount

            st.success("Withdraw Successful")

        else:

            st.error("Insufficient Balance")

    def deposit(self):

        amount = self.get_int_value()

        if amount > 0:

            self.balance += amount

            st.success("Deposit Successful")

        else:

            st.error("Amount should be greater than 0")


# -------------------------------
# BANK VERSION 2
# -------------------------------

class Bank_v2(Bank_v1):

    bank_address = "Bangalore"
    bank_mobile = 8501012250

    @classmethod
    def bank_details(cls):

        st.subheader("Bank Details")

        st.write(f"Bank Name : {cls.bank_name}")
        st.write(f"Bank ROI : {cls.bank_roi}")
        st.write(f"Bank IFSC : {cls.bank_ifsc}")
        st.write(f"Bank Address : {cls.bank_address}")
        st.write(f"Bank Mobile : {cls.bank_mobile}")

    @classmethod
    def change_roi(cls):

        newroi = st.number_input(
            "Enter New ROI",
            min_value=0.0,
            step=0.5
        )

        if st.button("Update ROI"):

            cls.bank_roi = newroi

            st.success(f"ROI Changed to {newroi}")


# -------------------------------
# MULTIPLE USERS DATABASE
# -------------------------------

if "users" not in st.session_state:

    st.session_state.users = {

        "Sagar": Bank_v2(
            "Sagar",
            675432,
            10000,
            "Bangalore"
        ),

        "Rahul": Bank_v2(
            "Rahul",
            987654,
            15000,
            "Hyderabad"
        ),

        "Priya": Bank_v2(
            "Priya",
            456789,
            20000,
            "Chennai"
        )
    }


# -------------------------------
# STREAMLIT UI
# -------------------------------

st.title("🏦 Bank Management System")

st.sidebar.header("Customers")

selected_user = st.sidebar.radio(
    "Select Customer",
    list(st.session_state.users.keys())
)

customer = st.session_state.users[selected_user]

# -------------------------------
# CUSTOMER DETAILS
# -------------------------------

st.subheader("Customer Details")

customer.customer_details()

st.markdown("---")

# -------------------------------
# BANK DETAILS
# -------------------------------

customer.bank_details()

st.markdown("---")

# -------------------------------
# DEPOSIT SECTION
# -------------------------------

st.subheader("Deposit Money")

deposit_amount = st.number_input(
    "Deposit Amount",
    min_value=0,
    step=100,
    key="deposit"
)

if st.button("Deposit"):

    if deposit_amount > 0:

        customer.balance += deposit_amount

        st.success(f"₹{deposit_amount} Deposited Successfully")

    else:

        st.error("Enter Valid Amount")


# -------------------------------
# WITHDRAW SECTION
# -------------------------------

st.subheader("Withdraw Money")

withdraw_amount = st.number_input(
    "Withdraw Amount",
    min_value=0,
    step=100,
    key="withdraw"
)

if st.button("Withdraw"):

    if withdraw_amount <= customer.balance:

        customer.balance -= withdraw_amount

        st.success(f"₹{withdraw_amount} Withdrawn Successfully")

    else:

        st.error("Insufficient Balance")


# -------------------------------
# UPDATED BALANCE
# -------------------------------

st.subheader("Updated Balance")

st.info(f"Current Balance : ₹{customer.balance}")

st.markdown("---")

# -------------------------------
# CHANGE ROI
# -------------------------------

st.subheader("Change ROI")

customer.change_roi()

st.markdown("---")

# -------------------------------
# CREATE NEW USER
# -------------------------------

st.subheader("Create New Customer")

new_name = st.text_input("Enter Name")

new_account = st.number_input(
    "Enter Account Number",
    min_value=100000,
    step=1
)

new_balance = st.number_input(
    "Enter Opening Balance",
    min_value=0,
    step=100
)

new_address = st.text_input("Enter Address")

if st.button("Create Customer"):

    if new_name not in st.session_state.users:

        st.session_state.users[new_name] = Bank_v2(
            new_name,
            new_account,
            new_balance,
            new_address
        )

        st.success(f"{new_name} Created Successfully")

    else:

        st.error("Customer Already Exists")
