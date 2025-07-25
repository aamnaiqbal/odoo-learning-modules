## 🔐 Security: `ir.model.access.csv`

The `security/ir.model.access.csv` file is essential for controlling user access to your module's models. Without it, Odoo will restrict users from interacting with your data, even if the UI is properly set up.

---

## 🧾 What Is It?

This file defines **access control rules** at the **model level** for different user groups. It determines whether a user can:

- 🔍 **Read** records
- ✍️ **Write** (edit) records
- ➕ **Create** new records
- 🗑️ **Delete** records

---

## 🧩 File Location

patient_appointment_system/
├── security/
│ └── ir.model.access.csv


---

## 📊 File Format

Each line in the CSV defines an access rule using the following columns:

| Column         | Description |
|----------------|-------------|
| `id`           | Unique ID for the rule |
| `name`         | Name shown in the system |
| `model_id:id`  | Technical model name prefixed by `model_` |
| `group_id:id`  | Group this rule applies to (can be empty for public access) |
| `perm_read`    | 1 if allowed to read records |
| `perm_write`   | 1 if allowed to write (edit) records |
| `perm_create`  | 1 if allowed to create records |
| `perm_unlink`  | 1 if allowed to delete records |

---

## ✅ Example: Patient Appointment System

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_hospital_patient_user,Hospital Patient,model_hospital_patient,base.group_user,1,1,1,1
access_hospital_appointment_user,Hospital Appointment,model_hospital_appointment,base.group_user,1,1,1,1
access_hospital_doctor_user,Hospital Doctor,model_hospital_doctor,base.group_user,1,1,1,1
```

---

## 👥 User Groups
- Odoo provides default user groups such as:
- base.group_user → Internal Users (default employees)
- base.group_system → System Administrators
- You can also create custom groups in security/security.xml if needed.