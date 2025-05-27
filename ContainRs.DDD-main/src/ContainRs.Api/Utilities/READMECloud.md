# ☁️ How to Create a Virtual Machine in Azure

This guide walks you through the steps to create a Virtual Machine (VM) in Microsoft Azure using the Azure Portal.

---

## 🧰 Prerequisites

* An active [Azure account](https://portal.azure.com)
* Required permissions to create resources (Contributor role or higher)

---

## 𞪟 Step-by-Step: Create a VM in Azure Portal

### 1. **Log into Azure Portal**

Go to: [https://portal.azure.com](https://portal.azure.com)

---

### 2. **Search for Virtual Machines**

* In the top search bar, type `Virtual Machines`
* Click on **"Virtual Machines"** in the search results

---

### 3. **Create a New VM**

* Click **`+ Create`** > **`Azure virtual machine`**

---

### 4. **Configure Basic Settings**

| Field                    | Description                                    |
| ------------------------ | ---------------------------------------------- |
| **Subscription**         | Choose your Azure subscription                 |
| **Resource group**       | Select an existing one or click `Create new`   |
| **Virtual machine name** | Set a unique name for your VM                  |
| **Region**               | Choose your preferred region (e.g., East US)   |
| **Image**                | Choose the OS (e.g., Ubuntu 22.04, Windows 11) |
| **Size**                 | Click `Change size` to select VM specs         |
| **Authentication type**  | Password or SSH public key                     |
| **Username**             | Admin username for VM access                   |
| **Password / SSH key**   | Depending on auth type                         |

---

### 5. **Configure Disks (Optional)**

* Choose OS disk type (Standard SSD, Premium SSD, etc.)
* Add data disks if needed

---

### 6. **Configure Networking**

* Azure will create a Virtual Network and Subnet automatically
* Make sure `Public IP` is enabled if you want internet access
* Set `Inbound port rules`: allow SSH (port 22) or RDP (port 3389)

---

### 7. **Management, Monitoring, and Tags (Optional)**

* Enable or disable **Auto-shutdown**
* Enable **Boot diagnostics** if needed
* Add tags for better resource management

---

### 8. **Review + Create**

* Click **`Review + create`**
* Wait for validation to pass
* Click **`Create`** to deploy the VM

---

## 💝 Access Your Virtual Machine

### ✅ For Linux (SSH):

```bash
ssh username@<public-ip>
```

### ✅ For Windows (RDP):

* Use Remote Desktop Connection
* Enter the public IP
* Login with the admin credentials you set

---

## 🧹 Cleanup Resources (Optional)

To avoid charges, delete the VM and associated resources:

* Go to **Resource Groups**
* Select the group you created
* Click **`Delete resource group`**

---

## 📌 Notes

* VM pricing depends on size, OS, disk, and uptime.
* Make sure to secure your VM (e.g., disable public IP if not needed).
* Consider using **Azure Bastion** for safer RDP/SSH access.

---

## Creating Instance in the Cloud 
[Link Microsoft Learn](https://learn.microsoft.com/pt-br/azure/azure-sql/managed-instance/instance-create-quickstart?view=azuresql&tabs=azure-portal)