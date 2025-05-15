from application_tracker import log_application
from tracker.status_updater import update_status

def main():
    while True:
        print("\n--- Resume Application Tracker ---")
        print("1. Log New Application")
        print("2. Update Application Status")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            company = input("Enter company name: ")
            role = input("Enter role applied for: ")
            status = input("Enter current status (e.g., Applied, Interviewed, Offered): ")
            log_application(company, role, status)
            print("Application logged.")

        elif choice == "2":
            company = input("Enter company name to update: ")
            new_status = input("Enter new status: ")
            update_status(company, new_status)
            print("Status updated.")

        elif choice == "3":
            print("Exiting tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
