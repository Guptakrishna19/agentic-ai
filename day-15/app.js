
let employees = [];
let departments = [];

// Fetch and parse the local .env file
async function loadEnv() {
    try {
        // Fallback default is window.location.origin if hosted via FastAPI uvicorn
        API_URL = window.location.origin;

        const response = await fetch('.env');
        if (!response.ok) return;

        const text = await response.text();
        const lines = text.split('\n');
        for (const line of lines) {
            if (line.trim().startsWith('#') || !line.includes('=')) continue;

            const parts = line.split('=');
            const key = parts[0].trim();
            const value = parts.slice(1).join('=').trim();

            if (key === 'API_URL') {
                API_URL = value;
            }
        }
    } catch (error) {
        console.warn("Could not load .env file, using default API_URL:", error);
    }
}

// Toast notification helper
function showToast(message, type = "success") {
    const container = document.getElementById("toastContainer");
    const toast = document.createElement("div");
    toast.className = `toast toast-${type}`;

    let icon = "ℹ️";
    if (type === "success") icon = "✅";
    if (type === "error") icon = "❌";

    toast.innerHTML = `
        <span>${icon}</span>
        <span>${message}</span>
    `;

    container.appendChild(toast);

    // Auto-remove toast after 4 seconds
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(120%)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

// Populate department dropdowns
function populateDepartmentDropdowns() {
    const mainSelect = document.getElementById("department");
    const editSelect = document.getElementById("editDepartment");

    // Keep the default placeholder option for the main form
    mainSelect.innerHTML = `<option value="" disabled selected>Select Department</option>`;
    editSelect.innerHTML = "";

    departments.forEach(dept => {
        const optHtml = `<option value="${dept.department_id}">${dept.department_name}</option>`;
        mainSelect.innerHTML += optHtml;
        editSelect.innerHTML += optHtml;
    });
}

// Fetch departments list
async function loadDepartments() {
    try {
        const response = await fetch(`${API_URL}/departments`);
        if (!response.ok) throw new Error("Failed to fetch departments");
        departments = await response.json();
        populateDepartmentDropdowns();
    } catch (error) {
        console.error("Error loading departments:", error);
        showToast("Error loading departments. Please check if the backend is running.", "error");
    }
}

// Render employees list based on search query
function renderEmployees(filterText = "") {
    const tableBody = document.getElementById("employeeTable");
    const noDataMessage = document.getElementById("noDataMessage");
    tableBody.innerHTML = "";

    const query = filterText.toLowerCase().trim();

    const filtered = employees.filter(emp => {
        const name = (emp.NAME || "").toLowerCase();
        const dept = getDepartmentName(emp.department_id).toLowerCase();
        return name.includes(query) || dept.includes(query) || String(emp.ID).includes(query);
    });

    if (filtered.length === 0) {
        noDataMessage.classList.remove("hidden");
    } else {
        noDataMessage.classList.add("hidden");
    }

    filtered.forEach(employee => {
        const deptName = getDepartmentName(employee.department_id);
        const salaryFormatted = new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR',
            maximumFractionDigits: 0
        }).format(employee.SALARY || 0);

        const row = `
            <tr>
                <td>${employee.ID}</td>
                <td><strong>${employee.NAME}</strong></td>
                <td><span class="badge">${deptName}</span></td>
                <td>${salaryFormatted}</td>
                <td class="actions-col">
                    <button class="btn-edit" onclick="openEditModal(${employee.ID})">Edit</button>
                    <button class="btn-danger" onclick="deleteEmployee(${employee.ID})">Delete</button>
                </td>
            </tr>
        `;
        tableBody.innerHTML += row;
    });

    updateMetrics(filtered);
}

// Get department name by ID
function getDepartmentName(id) {
    const dept = departments.find(d => d.department_id === id);
    return dept ? dept.department_name : `Dept ${id}`;
}

// Calculate and update metrics
function updateMetrics(list) {
    const totalCountSpan = document.getElementById("totalEmployeesCount");
    const avgSalarySpan = document.getElementById("avgSalaryCount");

    totalCountSpan.textContent = list.length;

    if (list.length === 0) {
        avgSalarySpan.textContent = "₹0";
        return;
    }

    const totalSalary = list.reduce((sum, emp) => sum + (emp.SALARY || 0), 0);
    const avgSalary = totalSalary / list.length;

    avgSalarySpan.textContent = new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        maximumFractionDigits: 0
    }).format(avgSalary);
}

// Fetch all employees
async function loadEmployees() {
    try {
        const response = await fetch(`${API_URL}/employees`);
        if (!response.ok) throw new Error("Failed to fetch employees");
        employees = await response.json();
        renderEmployees(document.getElementById("searchBar").value);
    } catch (error) {
        console.error("Error loading employees:", error);
        showToast("Error loading employee directory.", "error");
    }
}

// Handle Add Employee Form Submission
document.getElementById("employeeForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const nameInput = document.getElementById("name");
    const deptInput = document.getElementById("department");
    const salaryInput = document.getElementById("salary");

    const name = nameInput.value.trim();
    const departmentId = parseInt(deptInput.value, 10);
    const salary = parseFloat(salaryInput.value);

    if (!name || isNaN(departmentId) || isNaN(salary)) {
        showToast("Please fill in all inputs correctly.", "error");
        return;
    }

    try {
        const response = await fetch(`${API_URL}/employees`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                department_id: departmentId,
                salary: salary
            })
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.detail || "Failed to create employee");
        }

        showToast("Employee added successfully!");
        document.getElementById("employeeForm").reset();
        loadEmployees();

    } catch (error) {
        console.error("Error adding employee:", error);
        showToast(`Failed to add employee: ${error.message}`, "error");
    }
});

// Delete employee
async function deleteEmployee(id) {
    if (!confirm(`Are you sure you want to delete employee #${id}?`)) {
        return;
    }

    try {
        const response = await fetch(`${API_URL}/employees/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.detail || "Failed to delete employee");
        }

        showToast("Employee deleted successfully!");
        loadEmployees();
    } catch (error) {
        console.error("Error deleting employee:", error);
        showToast(`Failed to delete employee: ${error.message}`, "error");
    }
}

// Open Edit Modal
function openEditModal(id) {
    const employee = employees.find(emp => emp.ID === id);
    if (!employee) return;

    document.getElementById("editEmployeeId").value = employee.ID;
    document.getElementById("editName").value = employee.NAME || "";
    document.getElementById("editDepartment").value = employee.department_id || "";
    document.getElementById("editSalary").value = employee.SALARY || 0;

    document.getElementById("editModal").classList.remove("hidden");
}

// Close Edit Modal
function closeEditModal() {
    document.getElementById("editModal").classList.add("hidden");
    document.getElementById("editForm").reset();
}

// Cancel and Close buttons
document.getElementById("closeModalBtn").addEventListener("click", closeEditModal);
document.getElementById("cancelModalBtn").addEventListener("click", closeEditModal);

// Close modal if clicked outside
document.getElementById("editModal").addEventListener("click", (e) => {
    if (e.target.id === "editModal") {
        closeEditModal();
    }
});

// Edit Form Submit
document.getElementById("editForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const id = parseInt(document.getElementById("editEmployeeId").value, 10);
    const name = document.getElementById("editName").value.trim();
    const departmentId = parseInt(document.getElementById("editDepartment").value, 10);
    const salary = parseFloat(document.getElementById("editSalary").value);

    if (isNaN(id) || !name || isNaN(departmentId) || isNaN(salary)) {
        showToast("Please fill in all inputs correctly.", "error");
        return;
    }

    try {
        const response = await fetch(`${API_URL}/employees/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                department_id: departmentId,
                salary: salary
            })
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.detail || "Failed to update employee");
        }

        showToast("Employee details updated!");
        closeEditModal();
        loadEmployees();
    } catch (error) {
        console.error("Error updating employee:", error);
        showToast(`Failed to update: ${error.message}`, "error");
    }
});

// Setup Live Search filtering
document.getElementById("searchBar").addEventListener("input", (e) => {
    renderEmployees(e.target.value);
});

// Initialize
async function init() {
    await loadEnv();
    await loadDepartments(); // load departments list first
    await loadEmployees();   // then load and map employees
}

init();