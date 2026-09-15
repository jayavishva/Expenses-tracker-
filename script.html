const form = document.getElementById("expenseForm");
const itemInput = document.getElementById("item");
const amountInput = document.getElementById("amount");
const totalElement = document.getElementById("total");
const expenseList = document.getElementById("expenseList");
const message = document.getElementById("message");
const refreshBtn = document.getElementById("refreshBtn");

function formatCurrency(amount) {
    return new Intl.NumberFormat("en-IN", {
        style: "currency",
        currency: "INR"
    }).format(amount);
}

async function loadExpenses() {
    try {
        const response = await fetch("/api/expenses");
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Could not load expenses");
        }

        totalElement.textContent = formatCurrency(data.total);

        if (data.expenses.length === 0) {
            expenseList.innerHTML = '<p class="empty">No expenses added yet.</p>';
            return;
        }

        expenseList.innerHTML = data.expenses.map(expense => `
            <div class="expense-row">
                <div class="expense-info">
                    <span class="expense-item">${escapeHtml(expense.item)}</span>
                    <span class="expense-amount">${formatCurrency(expense.amount)}</span>
                </div>
                <button class="delete-btn" onclick="deleteExpense(${expense.id})">
                    Delete
                </button>
            </div>
        `).join("");
    } catch (error) {
        expenseList.innerHTML = `<p class="empty">${error.message}</p>`;
    }
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const item = itemInput.value.trim();
    const amount = amountInput.value;

    try {
        const response = await fetch("/api/expenses", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ item, amount })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Failed to add expense");
        }

        message.textContent = data.message;
        form.reset();
        await loadExpenses();
    } catch (error) {
        message.textContent = error.message;
    }
});

async function deleteExpense(id) {
    if (!confirm("Delete this expense?")) {
        return;
    }

    try {
        const response = await fetch(`/api/expenses/${id}`, {
            method: "DELETE"
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Failed to delete expense");
        }

        await loadExpenses();
    } catch (error) {
        message.textContent = error.message;
    }
}

function escapeHtml(value) {
    const div = document.createElement("div");
    div.textContent = value;
    return div.innerHTML;
}

refreshBtn.addEventListener("click", loadExpenses);

loadExpenses();
