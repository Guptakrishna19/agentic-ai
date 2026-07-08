// Fetch and parse the local .env file
async function loadEnv() {
    try {
        const response = await fetch('.env');
        if (!response.ok) return;

        const text = await response.text();
        const lines = text.split('\n');
        for (const line of lines) {
            // Skip comments and empty lines
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

async function loadEmployees() {
    try {
        const response = await fetch(`${API_URL}/employees`);
        const employees = await response.json();

        const tableBody = document.getElementById("employeeTable");
        tableBody.innerHTML = "";

        employees.forEach(employee => {
            const row = `
                <tr>
                    <td>${employee.ID}</td>
                    <td>${employee.NAME}</td>
                    <td>${employee.department_id}</td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });

    } catch (error) {
        console.error("Error loading employees:", error);
    }
}

document.getElementById("employeeForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const departmentId = parseInt(document.getElementById("department").value, 10);

    try {
        await fetch(`${API_URL}/employees`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                department_id: departmentId,
                salary: 0.0
            })
        });

        document.getElementById("employeeForm").reset();
        loadEmployees();

    } catch (error) {
        console.error("Error adding employee:", error);
    }
});

// Initialize the application after loading env configuration
async function init() {
    await loadEnv();
    loadEmployees();
}

init();