**Prerequisite**

Python should be install, validate by running below command on your terminal

# Creating Virtual Environment

**Create virtual environment using below command on root of your project**

`python3 -m venv [name_of_your_virtual_environment]`

eg. `python3 -m venv venv_sl`

> Prefixing virtual environemnt name with venv will exclude to checkin

**Activate virtual envirnmnet using below commnds or root location of your project**

`source [name_of_your_virtual_environment]/bin/activate`

eg. `source venv_sl/bin/activate`

> Now you command line prompt will start with virtual envirnmnet name in bracket and pip commnd will be available for you

# Creating Dependency file

Create **requirements.txt** in root folder of project

Mention all the libraries required for your project

e.g.

```makefile
streamlit
matplotlib
seaborn==0.11.1
setuptools
numpy
pandas
pandasql
```

Now run below command to download all the depdendencies mention in requirements.txt file

`pip install -r requirements.txt`

> Make sure you are running all the command on virtual environment

once all the download is complete, run test code, crete **test.py** file in root of the project and copy below content

```python
import numpy as np
print ("Hello Numpy")
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
```

Now run folowing command on virtual environment promt

`python3 test.py`

Above commnd should run successfully

# Using Juyter Notebook in VS Code

Install plugin "Jupyter" from microsft

Once Jupyter plugin is installed, create  "test.ipynb" and copy below content in file.

```python
import numpy as np
print ("Hello Numpy")
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
```

File will be open opened using jupyter notebook extension

Run above code Jupyter notebook, but now notebook will ask you to select the environment, so from the above dropdown select virtual environment you created.
