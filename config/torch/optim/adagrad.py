# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# SPDX-License-Identifier: MIT
#
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any


@dataclass
class AdagradConf:
    """For more details on parameteres please refer to the original documentation:
    https://pytorch.org/docs/stable/optim.html#torch.optim.Adagrad
    """
    _target_: str = "torch.optim.adagrad.Adagrad"
    params: Any = MISSING
    lr: Any = 0.01
    lr_decay: Any = 0
    weight_decay: Any = 0
    initial_accumulator_value: Any = 0
    eps: Any = 1e-10
