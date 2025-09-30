# Vendor Onboarding API

A simple Django REST Framework project that handles user signup/login and vendor onboarding.  
Users can register, log in, and submit vendor details (including documents).  
Authenticated users can fetch all vendors or a single vendor.

---

## Features
- User signup (full name + email)
- Simple session-based login
- Vendor onboarding with:
  - Address
  - Type of service
  - Years in business
  - Phone number
  - CAC certificate (image)
  - Verified ID (image)
  - Proof of address (image)
- Fetch all vendors (authenticated)
- Fetch a single vendor (authenticated)

---

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite3
