import os
import os.path
import logging
import random
import subprocess
import shlex
import gzip
import re
import functools
from glob import glob
import time
import imp
import sys
import json
from steamroller import Environment
# workaround needed to fix bug with SCons and the pickle module
#del sys.modules['pickle']
#sys.modules['pickle'] = imp.load_module('pickle', *imp.find_module('pickle'))
#import pickle

vars = Variables("custom.py")

vars.AddVariables(
    ("TEST_IMAGE_PATH", "", "data"),
    (
        "LAYOUT_MODELS",
        "",
        {
            "publaynet" : {
                "url" : "lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config"
            },
            "newspapernavigator" : {
                "url" : "lp://NewspaperNavigator/faster_rcnn_R_50_FPN_3x/config"
            },
            "tablebank" : {
                "url" : "lp://TableBank/faster_rcnn_R_101_FPN_3x/config"
            },
            "hjr_cnn" : {
                "url" : "lp://HJDataset/mask_rcnn_R_50_FPN_3x/config",
            },
            "hjr_retina" : {
                "url" : "lp://HJDataset/retinanet_R_50_FPN_3x/config",
            },
            "mfd" : {
                "url" : "lp://MFD/faster_rcnn_R_50_FPN_3x/config",
            },
            "primalayout" : {
                "url" : "lp://PrimaLayout/mask_rcnn_R_50_FPN_3x/config"
            },                        
        }
    )
)

env = Environment(
    variables=vars,
    ENV=os.environ,
    tools=[],
    BUILDERS={
        "PerformLayoutAndOCR" : Builder(
            action="python scripts/perform_layout_and_ocr.py --image_file ${SOURCES[0]} --layout_model_url ${LAYOUT_MODEL_URL} --ocr_model_url ${OCR_MODEL_URL} --layout_output ${TARGETS[0]} --ocr_output ${TARGETS[1]}"
        )
    }
)

env.Decider("timestamp-newer")

for layout_model_name, layout_model_conf in env["LAYOUT_MODELS"].items():
    for fname in env.Glob("{}/*".format(env["TEST_IMAGE_PATH"])):
        target_image_fname = "work/{1}_{0}{2}".format(layout_model_name, *os.path.splitext(os.path.basename(fname.rstr())))
        target_text_fname = "work/{1}_{0}.txt".format(layout_model_name, *os.path.splitext(os.path.basename(fname.rstr())))
        res = env.PerformLayoutAndOCR(
            [target_image_fname, target_text_fname],
            fname,
            LAYOUT_MODEL_URL=layout_model_conf["url"],
            LAYOUT_MODEL_NAME=layout_model_name,
            OCR_MODEL_URL="None"
        )

