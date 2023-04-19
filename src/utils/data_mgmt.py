import logging
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET
import re
import joblib
import numpy as np
import scipy.sparse as sparse


def process_posts(fd_in, fd_out_train, fd_out_test, target_tag, split):
    line_num = 1
    column_names = "pid\tlabel\ttext\n"
    fd_out_train.write(column_names)
    fd_out_test.write(column_names)
    for line in tqdm(fd_in):
        try:
            # random.random() will generate random number between 0 and 1, so if number is greater than 0.3 then store the line in fd_out_train otherwise in fd_out_test 
            fd_out = fd_out_train if random.random() > split else fd_out_test 

            attr = ET.fromstring(line).attrib # it will take the line and read the attributes

            pid = attr.get('Id',"") # attr.get will take out the label, title,body from the xml file
            label = 1 if target_tag in attr.get('Tags',"") else 0 # if python is present then 1 if not then 0
            title = re.sub(r"\s+", " ", attr.get('Title',"")).strip() # this removes the extra spaces between the text
            body = re.sub(r"\s+", " ", attr.get('Body',"")).strip() # this removes the extra spaces between the text
            text = f"{title} {body}" # title + " " + body

            fd_out.write(f"{pid}\t{label}\t{text}\n")
            line_num += 1
        except Exception as e:
            msg = f"skipping the broken line {line_num}: {e}\n"
            logging.exception(msg)


def save_matrix(df, text_matrix, out_path):
    pid_matrix = sparse.csr_matrix(df.pid.astype(np.int64)).T # sparse.csr_matrix what it will do if there are lots of zeroes then it will only stores the position of the value only - see csr_expts.py
    label_matrix = sparse.csr_matrix(df.label.astype(np.int64)).T

    result = sparse.hstack([pid_matrix, label_matrix, text_matrix],format="csr")

    msg = f"The output matrix saved at {out_path} of shape: {result.shape}"
    logging.info(msg)
    joblib.dump(result, out_path)