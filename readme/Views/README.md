## 🧭 Menu Structure (`menu.xml`)

The `menu.xml` file defines the **navigation menus** visible in the Odoo backend. These menus are essential for allowing users to access the views of your custom models.

### 📋 Menu Item Definition

The `<menuitem>` tag defines a menu item. You must give it:

- **`id`** – unique identifier in XML
- **`name`** – the label shown to the user  
- **`parent`** – if it's a submenu, this defines its parent menu
- **`action`** – connects to a window action to show a model's view (form/list)
- **`sequence`** – controls the order in the sidebar

### ✅ Menus Defined

1. **Top-Level Menu**
   - **Hospital**: Main category for all healthcare-related operations.

2. **Submenus**
   - **Patients**: Opens the patient list and form views.
   - **Appointments**: Opens appointment views (calendar, list, form).
   - **Doctors**: Manages doctor profiles.

### 🧩 Dependencies

Each submenu is linked to an `ir.actions.act_window` record defined in their respective view files (`*_view.xml`), which open the model's views (tree, form, etc.).

### 🧾 Example Menu Code

```xml
<odoo>
  <!-- Top-level menu (no parent) -->
  <menuitem id="hospital_main_menu" 
            name="Hospital" 
            sequence="1"/>

  <!-- Submenu with all required attributes -->
  <menuitem id="hospital_patient_menu" 
            name="Patients"
            parent="hospital_main_menu"
            action="action_patient"
            sequence="1" />

  <menuitem id="hospital_appointment_menu" 
            name="Appointments"
            parent="hospital_main_menu"
            action="action_appointment"
            sequence="2" />

  <menuitem id="hospital_doctor_menu" 
            name="Doctors"
            parent="hospital_main_menu"
            action="action_doctor"
            sequence="3" />
</odoo>
```