# Assignment 8 – Streamlit (Basic App Building)

## 📌 Project Information

- **Assignment Name:** Assignment 8 – Streamlit (Basic App Building)
- **Author Name:** Tanu Patel
- **Programming Language:** Python
- **Framework:** Streamlit

---

## 1. Introduction

This project contains four beginner-friendly Streamlit applications developed using Python.

The main objective of this assignment is to understand how to create simple and interactive web applications using Streamlit components such as text inputs, number inputs, buttons, sliders, select boxes, sidebars, and charts.

## 2. Objectives

- To understand the basics of Streamlit.
- To create interactive applications using Python.
- To accept user input and display output.
- To perform simple mathematical calculations.
- To use different Streamlit components.
- To create a simple dashboard with a bar chart.

## 3. Technologies Used

- **Python:** Used for application development.
- **Streamlit:** Used to create interactive web applications.
- **VS Code:** Used as the code editor.

## 4. Project Structure

The project contains the following files:

```text
GenAI-Task8-Tanu/
│
├── app_basic.py
├── app_discount.py
├── app_product_form.py
├── app_dashboard.py
│
└── README.md
```

## 5. Tasks Description

### Task 1: Basic Streamlit App

**File Name:** `app_basic.py`

**Description:**

This application displays a welcome title and accepts the user's name through a text input field.

When the user clicks the "Greet Me" button, the application displays a personalised greeting message.

**Streamlit Components Used:**

- `st.title()` – Displays the application title.
- `st.text_input()` – Accepts the user's name.
- `st.button()` – Creates a clickable button.
- `st.write()` – Displays the greeting message.

### Task 2: Price Calculator

**File Name:** `app_discount.py`

**Description:**

This application calculates the final product price after applying a discount percentage.

The user enters the original product price and selects a discount percentage using a slider.

After clicking the calculate button, the application displays the discounted price.

**Streamlit Components Used:**

- `st.number_input()` – Accepts the product price.
- `st.slider()` – Selects the discount percentage.
- `st.button()` – Calculates the discounted price.
- `st.success()` – Displays the final result.
- `st.table()` – Displays the before-and-after price comparison (optional).

### Task 3: Product Form

**File Name:** `app_product_form.py`

**Description:**

This application creates a simple product entry form using Streamlit's sidebar.

The user enters the product name, selects a category, and enters the product price.

After clicking the "Add Product" button, the application displays a success message and the entered product details.

**Streamlit Components Used:**

- `st.sidebar.text_input()` – Accepts the product name.
- `st.sidebar.selectbox()` – Allows category selection.
- `st.sidebar.number_input()` – Accepts the product price.
- `st.sidebar.button()` – Adds the product.
- `st.success()` – Displays a success message.
- `st.write()` – Displays product information.

### Task 4: Mini Dashboard

**File Name:** `app_dashboard.py`

**Description:**

This application creates a simple sales dashboard using Streamlit.

It displays a title and description, provides a select box to choose a month, and shows the selected month's sales using a metric or text output.

It also displays a bar chart representing the monthly sales data.

**Streamlit Components Used:**

- `st.title()` – Displays the dashboard title.
- `st.write()` – Displays the description and sales information.
- `st.selectbox()` – Allows the user to select a month.
- `st.metric()` – Displays the selected month's sales.
- `st.bar_chart()` – Displays the monthly sales bar chart.

## 6. Installation and Setup

Follow these steps to run the project.

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version using:

```bash
python --version
```

### Step 2: Install Streamlit

Open the VS Code terminal and execute:

```bash
python -m pip install streamlit
```

### Step 3: Open the Project Folder

Open the project folder in Visual Studio Code.

Navigate to the project directory using:

```bash
cd path_to_project_folder
```

### Step 4: Run the Applications

Execute the following commands in the VS Code terminal.

**Task 1:**

```bash
python -m streamlit run app_basic.py
```

**Task 2:**

```bash
python -m streamlit run app_discount.py
```

**Task 3:**

```bash
python -m streamlit run app_product_form.py
```

**Task 4:**

```bash
python -m streamlit run app_dashboard.py
```

### Step 5: View the Application

After executing the command, Streamlit starts a local server and displays a URL in the terminal.

Open the displayed URL in your web browser to use the application.

Usually, the local URL is:

```text
http://localhost:8501
```

## 7. Important Note

If the command `streamlit run app.py` is not recognised in the terminal, use:

```bash
python -m streamlit run app.py
```

This runs Streamlit through the Python interpreter and can work even when the Streamlit command is not available directly in the system PATH.

## 8. Learning Outcomes

After completing this assignment, I learned:

- How to create basic Streamlit applications.
- How to accept user input using Streamlit.
- How to use buttons and sliders.
- How to create a sidebar-based product form.
- How to perform calculations and display results.
- How to create a simple dashboard.
- How to display data using Streamlit charts.

## 9. Conclusion

This assignment helped me understand the fundamentals of Streamlit and its different components.

By completing all four tasks, I gained practical knowledge of building simple, interactive web applications using Python and Streamlit.
