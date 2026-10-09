import spaces
import gradio as gr
import numpy as np
from model_loader import model

def on_click(hours: float | None, att: float | None, assgn: float | None, exam: float | None) -> str | None:
  """Handles the UI click event, validating inputs before generating a performance prediction.

    Parameters
    ----------
    hours : float or None
        Number of study hours.
    att : float or None
        Attendance percentage or score.
    assgn : float or None
        Assignment score.
    exam : float or None
        Exam score.

    Returns
    -------
    str or None
        A formatted prediction string ('PASS' or 'FAIL') if all inputs are provided,
        or None if validation fails (a Gradio info notification is displayed).
  """
  inputs = np.asarray([[hours, att, assgn, exam]])
  if (None in inputs):
    gr.Info('Please fill all student details', duration=4)
    return
  else:
    return predict(model, inputs)

@spaces.GPU # required for HF Spaces ZeroGPU 
def predict(model: sklearn.model_selection.GridSearchCV, inputs: np.ndarray) -> str:
  """Executes the trained model to predict whether a student will pass or fail.

    Parameters
    ----------
    model : sklearn.model_selection.GridSearchCV
        A fitted scikit-learn estimator or GridSearchCV object used for inference.
    inputs : np.ndarray
        A 2D NumPy array of shape (1, 4) containing numerical feature values.

    Returns
    -------
    str
        A formatted string stating whether the student is likely to PASS or FAIL.
  """
  # make prediction
  pred = 'PASS' if model.predict(inputs).item() == 1 else 'FAIL'
  # return statement with prediction
  return f'The student is likely to {pred}'
# custom CSS
custom_css = """
  #txt {
    text-align: center;
  }

  #prediction textarea {
    font-weight: bold !important;
    font-size: 15px !important;
  }

  #submit_btn {
    font-weight: normal !important;
    color: #000000 !important;
  }

  #clear_btn {
    font-weight: normal !important;
  }
"""

with gr.Blocks() as demo:
  # header
  gr.Markdown(
      """
      ## Predict Student Performance
      > _Enter student details to predict **PASS** or **FAIL**_
      """,
      elem_id='txt'
  )

  # inputs
  with gr.Row():
    hours = gr.Number(label='Hours Studied', minimum=0, maximum=10)
    att = gr.Number(label='Attendance (%)', minimum=0, maximum=100)
    assgn = gr.Number(label='Assignments Submitted', minimum=0, maximum=10)
    exam = gr.Number(label='Previous Exam Score (%)', minimum=0, maximum=100)

  # prediction
  pred_mssg = gr.Textbox(label='Prediction:', elem_id='prediction')

  # buttons
  with gr.Row():
    with gr.Row(scale=1):
        submit = gr.Button('✔️ Submit', variant='primary', size='md', elem_id='submit_btn')
        gr.ClearButton([hours, att, assgn, exam, pred_mssg], value='🗑️ Clear', size='md', elem_id='clear_btn')

    with gr.Column(scale=1):
      pass

  # footer
  gr.Markdown(
      """
      _Find GitHub repository and documentation linked [here](https://github.com/Martinmbiro/student-knn-task)_<br>
      """,
      elem_id='txt'
  )

  submit.click(
      fn=predict,
      inputs=[hours, att, assgn, exam],
      outputs=pred_mssg
  )


demo.queue().launch(css=custom_css)
