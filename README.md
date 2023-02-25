# Dependency Injection

* Write a minimal MVC-"App"
  * (over-engineered "Hello \<Name\>")
    * Model: stores the name
    * View: Displays/ask for the name
    * Controller: the glue between Model/View
  * Add a configuration object
  * Add a logger object

--

* Set up dependency injection
  * Manually
  * Use a DI-Framework
  * Write a mini DI-Injector

---

## Run project

### 1. Clone the project and open the folder

```
git clone https://github.com/cammarb/my-portfolio.git && cd my-portfolio
```

### 2. Create virtual enviroment

#### Linux/MacOS

```
python3 -m venv venv
```

#### Windows - Powershell

```
py -3 -m venv venv
```

### 3. Activate virtual enviroment

#### Linux/MacOS

```
. venv/bin/activate
```

#### Windows - Powershell

```
venv\Scripts\activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Run it

#### Linux/MacOS

```
python3 run.py
```

#### Windows - Powershell

```
py run.py
```
