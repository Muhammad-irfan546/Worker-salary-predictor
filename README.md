# Salary Predictor

A Streamlit app that loads a trained Linear Regression model and predicts
salary from years of experience.

## Files

- `app.py` — the Streamlit app
- `salary_model.pkl` — the trained model
- `requirements.txt` — pinned dependencies
- `.python-version` — pins Python to 3.12 (needed so scikit-learn 1.6.1
  installs from a ready-made package instead of a very slow from-source build)

## Step 1 — Create the repo and upload the normal files

1. Go to https://github.com/Muhammad-irfan546
2. Click **New repository** → name it (e.g. `salary-predictor-app`) → Create
3. Click **Add file → Upload files**
4. Drag in `app.py`, `salary_model.pkl`, and `requirements.txt`
5. Click **Commit changes**

## Step 2 — Add .python-version (can't be uploaded as a file)

File pickers hide dotfiles, so add it directly on GitHub instead:

1. In your repo, click **Add file → Create new file**
2. Name it exactly: `.python-version`
3. In the content box, type: `3.12`
4. Click **Commit changes**

## Step 3 — Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click **New app**
4. Select your repo, branch `main`, main file path `app.py`
5. Click **Deploy**

## Note

The model doesn't store its original feature name, so the app labels the
input "Years of Experience" based on the filename and the dataset's
typical shape. If that's not the right feature, just say so and the
label (and units) can be updated.
